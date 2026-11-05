"""Teaching-only Northstar request scheduler. No real dispatch or vehicle control.

This deliberately small model exposes assumptions and audit trails. Standard library only.
"""
from __future__ import annotations
import csv
import hashlib
import heapq
import json
import math
import random
from dataclasses import dataclass, asdict, replace
from pathlib import Path


@dataclass(frozen=True)
class Request:
    request_id: str
    arrival_min: float
    origin: str
    destination: str
    passengers: int
    delivery_key: str

    @classmethod
    def from_row(cls, row):
        req = cls(str(row['request_id']).strip(), float(row['arrival_min']),
                  str(row['origin']).strip(), str(row['destination']).strip(),
                  int(row['passengers']), str(row['delivery_key']).strip())
        if not req.request_id or not req.delivery_key or not req.origin or not req.destination:
            raise ValueError('empty required field')
        if not math.isfinite(req.arrival_min) or req.arrival_min < 0:
            raise ValueError('arrival must be finite and nonnegative')
        if req.passengers != 1:
            raise ValueError('teaching dispatcher supports one passenger per request')
        if req.origin == req.destination:
            raise ValueError('origin and destination must differ')
        return req


@dataclass(frozen=True)
class Config:
    vehicles: int = 2
    trip_min: float = 12.0
    end_min: float = 80.0
    target_served: float = 0.95
    target_p90_wait_min: float = 20.0

    def __post_init__(self):
        if not isinstance(self.vehicles, int) or self.vehicles < 1:
            raise ValueError('vehicles must be a positive integer')
        if self.trip_min <= 0 or not math.isfinite(self.trip_min):
            raise ValueError('trip_min must be finite and positive')
        if self.end_min <= 0 or not math.isfinite(self.end_min):
            raise ValueError('end_min must be finite and positive')
        if not 0 <= self.target_served <= 1 or self.target_p90_wait_min < 0:
            raise ValueError('invalid targets')


def load_requests(path):
    with open(path, newline='', encoding='utf-8') as f:
        return [Request.from_row(row) for row in csv.DictReader(f)]


def deduplicate(events):
    """Idempotency: exact repeated payload accepted once; conflicting reuse rejected."""
    unique = {}
    delivery_keys = {}
    duplicates = 0
    for req in events:
        if req.delivery_key in delivery_keys and delivery_keys[req.delivery_key] != req.request_id:
            raise ValueError('delivery key reused for a different request')
        delivery_keys[req.delivery_key] = req.request_id
        if req.request_id in unique:
            if unique[req.request_id] != req:
                raise ValueError('request identifier reused with a different payload')
            duplicates += 1
        else:
            unique[req.request_id] = req
    return sorted(unique.values(), key=lambda r: (r.arrival_min, r.request_id)), duplicates


def nearest_rank(values, percentile):
    if not values:
        return None
    if not 0 < percentile <= 1:
        raise ValueError('percentile outside (0,1]')
    s = sorted(values)
    return s[math.ceil(percentile * len(s))-1]


def dispatch(events, config: Config):
    reqs, duplicates = deduplicate(events)
    fleet = [(0.0, f'V{i+1:02d}') for i in range(config.vehicles)]
    heapq.heapify(fleet)
    assignments = []
    audit = []
    for req in reqs:
        free_at, vid = heapq.heappop(fleet)
        start = max(req.arrival_min, free_at)
        finish = start + config.trip_min
        # Finish must occur at or before end of teaching horizon.
        accepted = finish <= config.end_min + 1e-9
        entry = dict(request_id=req.request_id, origin=req.origin,
                     destination=req.destination, vehicle=vid if accepted else '',
                     arrival_min=req.arrival_min,
                     start_min=start if accepted else None,
                     finish_min=finish if accepted else None,
                     wait_min=round(start - req.arrival_min, 6) if accepted else None,
                     status='completed' if accepted else 'unserved_capacity')
        assignments.append(entry)
        audit.append(f"{req.request_id}:{entry['status']}:{entry['vehicle']}:{entry['start_min']}")
        heapq.heappush(fleet, (finish if accepted else free_at, vid))
    waits = [a['wait_min'] for a in assignments if a['status']=='completed']
    served = len(waits)
    served_fraction = served/len(reqs) if reqs else 1.0
    p90 = nearest_rank(waits, .90)
    # A stated acceptance condition is not an estimate of real-world reliability.
    meets = (bool(reqs) and served_fraction >= config.target_served and
             p90 is not None and p90 <= config.target_p90_wait_min)
    return dict(config=asdict(config), input_events=len(events), unique_requests=len(reqs),
                duplicates_ignored=duplicates, served=served,
                unserved=len(reqs)-served, served_fraction=round(served_fraction,6),
                p90_wait_min=p90, max_wait_min=max(waits) if waits else None,
                demonstration_pass=meets, assignments=assignments,
                audit_sha256=hashlib.sha256('\n'.join(audit).encode()).hexdigest())


def synthetic_replications(config: Config, count=200, seed=20261101, requests=12, mean_gap=4.0):
    """Independent synthetic arrival streams. Illustrates model sensitivity, not field validation."""
    if count < 2 or requests < 1 or mean_gap <= 0:
        raise ValueError('invalid simulation parameters')
    rng = random.Random(seed)
    outcomes = []
    for run in range(count):
        clock = 0.0
        events = []
        for j in range(requests):
            clock += rng.expovariate(1.0/mean_gap)
            events.append(Request(f'S{run:03d}-{j:03d}', clock, 'A', 'B', 1, f'k{run}-{j}'))
        report = dispatch(events, config)
        outcomes.append((report['served_fraction'], report['demonstration_pass']))
    fractions = [a for a,b in outcomes]
    mean = sum(fractions)/count
    sd = math.sqrt(sum((x-mean)**2 for x in fractions)/(count-1))
    margin = 1.96*sd/math.sqrt(count)  # normal approximation for mean across replications
    return dict(replications=count, seed=seed, mean_gap_min=mean_gap,
                mean_served_fraction=round(mean,6),
                approximate_95pct_interval_for_replication_mean=[round(mean-margin,6), round(mean+margin,6)],
                fraction_of_replications_meeting_demonstration_targets=round(sum(b for a,b in outcomes)/count,6),
                caveat='Monte Carlo precision only; does not account for model error or prove field performance')
