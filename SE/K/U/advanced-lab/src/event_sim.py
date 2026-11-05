"""Deterministic-seed event scheduling and explicitly injected synthetic faults.

No real transportation behavior, human response, safety certification, or field prediction.
The scheduler intentionally uses a simplified central reservation queue.
"""
from __future__ import annotations
import csv
import hashlib
import json
import math
import random
from dataclasses import dataclass, asdict
from pathlib import Path

@dataclass(frozen=True)
class Request:
    request_id: str
    minute: float
    origin: str
    destination: str
    delivery_key: str

@dataclass(frozen=True)
class Scenario:
    id: str
    vehicles: int = 2
    trip_min: float = 12.0
    horizon_min: float = 80.0
    comm_delay_min: float = 0.0
    drop_probability: float = 0.0
    outage_vehicle: int = 0  # 1-based, 0 = none
    outage_start: float = 0.0
    outage_end: float = 0.0
    telemetry_block_start: float = 0.0
    telemetry_block_end: float = 0.0
    seed: int = 1
    def __post_init__(self):
        if not isinstance(self.vehicles, int) or self.vehicles < 1:
            raise ValueError('vehicles must be positive integer')
        if self.trip_min <= 0 or self.horizon_min <= 0 or self.comm_delay_min < 0:
            raise ValueError('invalid times')
        if not all(math.isfinite(x) for x in (self.trip_min,self.horizon_min,self.comm_delay_min,self.outage_start,self.outage_end,self.telemetry_block_start,self.telemetry_block_end)):
            raise ValueError('times must be finite')
        if not 0 <= self.drop_probability <= 1:
            raise ValueError('drop_probability outside 0-1')
        if self.outage_vehicle < 0 or self.outage_vehicle > self.vehicles:
            raise ValueError('invalid outage vehicle')
        if self.outage_end < self.outage_start or self.telemetry_block_end < self.telemetry_block_start:
            raise ValueError('fault interval inverted')


def load_events(path):
    with Path(path).open(newline='', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    result = []
    for r in rows:
        tm = float(r['arrival_min'])
        if not math.isfinite(tm) or tm < 0 or not r['request_id'].strip() or not r['delivery_key'].strip():
            raise ValueError('malformed request')
        if int(r['passengers']) != 1 or not r['origin'] or not r['destination'] or r['origin'] == r['destination']:
            raise ValueError('unsupported request')
        result.append(Request(r['request_id'], tm, r['origin'], r['destination'], r['delivery_key']))
    return result


def _blocked(start, duration, blocks):
    """Earliest service window not overlapping any blocked intervals."""
    while True:
        changed = False
        for a, b in blocks:
            if a < b and start < b and start + duration > a:
                start = b
                changed = True
                break
        if not changed:
            return start


def simulate(events, spec: Scenario):
    rng = random.Random(spec.seed)
    dedup = {}
    keys = {}
    duplicates = 0
    rejections = 0
    for r in events:
        if r.delivery_key in keys and keys[r.delivery_key] != r.request_id:
            rejections += 1
            continue
        keys[r.delivery_key] = r.request_id
        if r.request_id in dedup:
            if dedup[r.request_id] != r:
                rejections += 1
            else:
                duplicates += 1
        else:
            dedup[r.request_id] = r
    unique = sorted(dedup.values(), key=lambda r: (r.minute,r.request_id))
    dropped = []
    received = []
    for req in unique:
        if rng.random() < spec.drop_probability:
            dropped.append(req)
        else:
            # Constant delay: controlled experiment. Not a physical network model.
            received.append((req.minute + spec.comm_delay_min,req))
    received.sort(key=lambda x:(x[0],x[1].request_id))
    ready = {i:0.0 for i in range(1,spec.vehicles+1)}
    records = []
    for when,req in received:
        choices = []
        for vehicle,available in ready.items():
            blocks=[]
            if vehicle == spec.outage_vehicle:
                blocks.append((spec.outage_start,spec.outage_end))
            blocks.append((spec.telemetry_block_start,spec.telemetry_block_end))
            start = _blocked(max(when,available),spec.trip_min,blocks)
            choices.append((start,vehicle))
        start,vehicle = min(choices)
        done = start + spec.trip_min
        completed = done <= spec.horizon_min + 1e-9
        if completed:
            ready[vehicle]=done
        records.append(dict(request_id=req.request_id,arrival_min=req.minute,received_min=when,
                            vehicle=f'V{vehicle:02d}' if completed else None,
                            start_min=start if completed else None,
                            finish_min=done if completed else None,
                            wait_min=round(start-req.minute,6) if completed else None,
                            status='completed' if completed else 'unserved_capacity'))
    for req in dropped:
        records.append(dict(request_id=req.request_id,arrival_min=req.minute,received_min=None,
                            vehicle=None,start_min=None,finish_min=None,wait_min=None,status='unobserved_message_loss'))
    records.sort(key=lambda x:(x['arrival_min'],x['request_id']))
    served = [r for r in records if r['status']=='completed']
    waits = sorted(r['wait_min'] for r in served)
    p90 = waits[math.ceil(.90*len(waits))-1] if waits else None
    total = len(unique)
    service_fraction = len(served)/total if total else 1.0
    nonoverlap = check_nonoverlap(records)
    ledger = json.dumps(records,sort_keys=True,separators=(',',':'))
    return dict(scenario=asdict(spec),input_events=len(events),unique_requests=total,
                duplicates_ignored=duplicates,rejected_conflicts=rejections,
                completed=len(served),lost_messages=len(dropped),unserved_capacity=total-len(served)-len(dropped),
                completion_fraction=round(service_fraction,6),p90_wait_min=p90,
                vehicle_nonoverlap=nonoverlap,records=records,
                evidence_sha256=hashlib.sha256(ledger.encode('utf-8')).hexdigest(),
                caveat='Teaching simulation: omission of geography, accessibility, real faults and human operations prevents field claims')


def check_nonoverlap(records):
    vehicles = {}
    for r in records:
        if r['status']=='completed':
            vehicles.setdefault(r['vehicle'],[]).append((r['start_min'],r['finish_min']))
    return all(b[0] >= a[1]-1e-9 for intervals in vehicles.values()
               for a,b in zip(sorted(intervals),sorted(intervals)[1:]))


def synthetic_demand(seed, n, mean_gap=4.0):
    if n < 1 or mean_gap <= 0: raise ValueError('invalid synthetic parameters')
    rng=random.Random(seed)
    t=0.0
    out=[]
    for k in range(n):
        t+=rng.expovariate(1/mean_gap)
        out.append(Request(f'D{seed:04d}-{k:03d}',t,'A','B',f'delivery-{seed}-{k}'))
    return out


def paired_experiment(base:Scenario, fault:Scenario, replications=100, n=12, mean_gap=4.0, seed=911):
    """Paired common-demand-stream comparison. CI reflects sampling variability only."""
    if replications < 3: raise ValueError('need >=3 independent demand streams')
    differences=[]
    base_rates=[];fault_rates=[]
    for i in range(replications):
        requests=synthetic_demand(seed+i,n,mean_gap)
        a=simulate(requests,base)
        b=simulate(requests,fault)
        base_rates.append(a['completion_fraction']);fault_rates.append(b['completion_fraction'])
        differences.append(b['completion_fraction']-a['completion_fraction'])
    mu=sum(differences)/replications
    sd=math.sqrt(sum((d-mu)**2 for d in differences)/(replications-1))
    halfwidth=1.96*sd/math.sqrt(replications)
    return dict(replications=replications,independent_arrival_streams=replications,
                seed=seed,mean_gap_min=mean_gap,n=n,
                mean_baseline=round(sum(base_rates)/replications,6),
                mean_faulted=round(sum(fault_rates)/replications,6),
                paired_mean_difference=round(mu,6),
                approximate_normal_95pct_interval=[round(mu-halfwidth,6),round(mu+halfwidth,6)],
                caveat='Normal approximation for Monte Carlo precision of a synthetic model, NOT confidence in field effects or validity')
