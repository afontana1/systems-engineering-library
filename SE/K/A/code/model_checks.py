"""Transparent educational models for the architecture & assurance sequence.

Not SysML conformance tooling; not safety or reliability certification.
Runs without third-party Python dependencies.
"""
from __future__ import annotations
import json
import math
from pathlib import Path

NODE_TYPES = {'Need','Requirement','Function','Component','Interface','Test','Evidence'}
EDGE_TYPES = {
    'refines': ('Requirement', 'Need'),
    'allocatedTo': ('Requirement', 'Component'),
    'realizes': ('Component', 'Function'),
    'verifiedBy': ('Requirement', 'Test'),
    'produces': ('Test', 'Evidence'),
    'dependsOn': ('Component', 'Component'),
}


def validate_model(model):
    """Return structural validation defects, not semantic adequacy verdicts."""
    nodes = model.get('nodes', [])
    idx = {x['id']: x for x in nodes}
    problems = []
    if len(idx) != len(nodes):
        problems.append('duplicate-node-id')
    for item in nodes:
        if item.get('type') not in NODE_TYPES:
            problems.append(f"unknown-node-type:{item['id']}")
    for e in model.get('edges', []):
        src, dst, rel = e['source'], e['target'], e['type']
        if src not in idx or dst not in idx:
            problems.append(f'broken-edge:{src}:{dst}')
        elif rel not in EDGE_TYPES:
            problems.append(f'unknown-edge:{rel}')
        elif (idx[src]['type'], idx[dst]['type']) != EDGE_TYPES[rel]:
            problems.append(f'type-violation:{src}:{rel}:{dst}')
    for item in nodes:
        if item['type'] == 'Requirement' and item.get('criticality') == 'high':
            outgoing = {(e['type'], e['target']) for e in model.get('edges', []) if e['source']==item['id']}
            if not any(r=='allocatedTo' and dst in idx and idx[dst]['type']=='Component' for r,dst in outgoing):
                problems.append(f'missing-allocation:{item["id"]}')
            if not any(r=='verifiedBy' and dst in idx and idx[dst]['type']=='Test' for r,dst in outgoing):
                problems.append(f'missing-test:{item["id"]}')
    return sorted(set(problems))


def energy_margin(battery_kwh, distance_km, intensity_kwh_km, overhead_kwh, reserve_kwh):
    values = (battery_kwh,distance_km,intensity_kwh_km,overhead_kwh,reserve_kwh)
    if any(x < 0 or not math.isfinite(x) for x in values):
        raise ValueError('nonnegative finite inputs required')
    return battery_kwh - distance_km*intensity_kwh_km - overhead_kwh - reserve_kwh


def route_status_ok(status, measured_at, now, max_age):
    if max_age < 0: raise ValueError('max_age must be nonnegative')
    return status == 'OPEN' and 0 <= (now-measured_at) <= max_age


class ReservationBook:
    """Single-process atomic teaching abstraction, not distributed transaction code."""
    def __init__(self, vehicles):
        self.vehicles=set(vehicles)
        self.by_key={}
        self.busy={}

    def reserve(self, key, payload, vehicle):
        if key in self.by_key:
            original_payload, result = self.by_key[key]
            if original_payload != payload: raise ValueError('idempotency key conflict')
            return result
        if vehicle not in self.vehicles: raise ValueError('unknown vehicle')
        if vehicle in self.busy: return 'REJECTED:vehicle-unavailable'
        self.busy[vehicle] = key
        result=f'ASSIGNED:{vehicle}'
        self.by_key[key]=(payload,result)
        return result


def series_reliability(reliabilities):
    if any(not 0 <= r <= 1 for r in reliabilities): raise ValueError('probabilities must be [0,1]')
    return math.prod(reliabilities)


def parallel_with_common_cause(channel_reliability, common_cause_probability):
    if not 0 <= channel_reliability <= 1 or not 0 <= common_cause_probability <= 1:
        raise ValueError('probabilities must be [0,1]')
    return (1-common_cause_probability)*(1-(1-channel_reliability)**2)


def zero_failure_upper(n, confidence=.95):
    if not isinstance(n,int) or n<1 or not 0<confidence<1:
        raise ValueError('n positive integer and confidence in (0,1)')
    return 1-(1-confidence)**(1/n)


def min_trials_for_upper(target, confidence=.95):
    if not 0<target<1 or not 0<confidence<1:raise ValueError('invalid target or confidence')
    return math.ceil(math.log(1-confidence)/math.log(1-target))


def check_evidence(rows, revision):
    """Find absent, wrong-revision, or non-passing evidence. Never infers semantic sufficiency."""
    findings=[]
    for e in rows:
        if not e.get('test_id') or not e.get('evidence_id'):
            findings.append((e.get('requirement','?'),'missing-evidence-reference'))
        elif e.get('revision') != revision:
            findings.append((e.get('requirement','?'),'stale-revision'))
        elif e.get('status') != 'PASS':
            findings.append((e.get('requirement','?'),'nonpass'))
    return findings


def load_model(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))

if __name__ == '__main__':
    here=Path(__file__).resolve().parents[1]
    m=load_model(here/'data/model.json')
    print('Model defects:',validate_model(m))
    print('Nominal energy margin:',energy_margin(24,24,.62,1.8,4))
    print('Shared-cause reliability:',parallel_with_common_cause(.95,.03))
    print('Zero-failure 95% upper bound, n=30:',zero_failure_upper(30))
