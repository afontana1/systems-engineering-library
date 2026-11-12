"""NS-T4.1: cross-concept evidence checks (synthetic classroom data).

The outputs are SCREENING calculations, not certification, field validation, or authorization.
Only Python's standard library is required.
"""
from __future__ import annotations
import json
import math
import statistics
from pathlib import Path

DEFAULT = Path(__file__).resolve().parents[1] / 'labs' / 't1-case.json'


def valid_probability(value, name):
    if isinstance(value, bool) or not isinstance(value, (float, int)) or not math.isfinite(value) or not 0 <= value <= 1:
        raise ValueError(f'{name} must be a finite probability in [0,1]')
    return float(value)


def zero_failure_upper(n: int, confidence: float = 0.95) -> float:
    if type(n) is not int or n < 1:
        raise ValueError('n must be a positive integer')
    c = valid_probability(confidence, 'confidence')
    if c <= 0 or c >= 1:
        raise ValueError('confidence must be strictly between 0 and 1')
    return -math.expm1(math.log1p(-c) / n)


def euler_recovery(k: float, dt: float, horizon: float = 1.0) -> dict:
    for name, v in [('gain', k), ('step', dt), ('horizon', horizon)]:
        if isinstance(v, bool) or not isinstance(v, (int, float)) or not math.isfinite(v):
            raise ValueError(name + ' must be a finite number')
    if k <= 0 or dt <= 0 or horizon <= 0 or not math.isclose(horizon/dt, round(horizon/dt), abs_tol=1e-10):
        raise ValueError('positive gain, step, and an integer number of steps required')
    steps = round(horizon/dt)
    factor = 1-k*dt
    return {'factor': factor, 'stable': abs(factor) < 1, 'nonnegative': factor >= 0,
            'estimate': factor**steps, 'exact': math.exp(-k*horizon)}


def audit(data: dict) -> dict:
    if not isinstance(data, dict):
        raise ValueError('object required')
    limit = data['latency_limit_s']; guard = data['clock_uncertainty_s']
    if any(type(v) not in (float,int) or not math.isfinite(v) for v in (limit,guard)) or limit <= 0 or guard < 0:
        raise ValueError('invalid timing rule')
    requests = data['requests']
    if not isinstance(requests,list) or not requests:
        raise ValueError('nonempty requests list required')
    ids = [r['id'] for r in requests]
    if len(ids)!=len(set(ids)) or any(not isinstance(i,str) or not i for i in ids):
        raise ValueError('request identifiers must be unique and nonempty')
    statuses = {'served', 'rejected', 'pending'}
    if any(r['status'] not in statuses or type(r['accessible']) is not bool for r in requests):
        raise ValueError('status or accessibility flag invalid')
    for r in requests:
        d=r.get('latency_s')
        if r['status']=='served':
            if type(d) not in (float,int) or not math.isfinite(d) or d < 0: raise ValueError('invalid served latency')
        elif d is not None:
            raise ValueError('unserved request cannot have a completion latency')
    counts = {s:sum(r['status']==s for r in requests) for s in sorted(statuses)}
    assert len(requests) == sum(counts.values())
    timely = lambda r, guard: r['status']=='served' and r['latency_s'] + guard <= limit + 1e-12
    nom = sum(timely(r,0) for r in requests)
    safe = sum(timely(r,guard) for r in requests)
    accessible = [r for r in requests if r['accessible']]
    ac_safe = sum(timely(r,guard) for r in accessible)
    if not accessible: raise ValueError('accessible denominator absent')
    r = valid_probability(data['channel_reliability'], 'channel_reliability')
    c = valid_probability(data['common_cause_probability'], 'common_cause_probability')
    independent_parallel = 1-(1-r)**2
    joint = (1-c)*independent_parallel  # Conditional independence only if common cause absent.
    candidates = []
    for x in (1,2,3):
        nominal = x*data['nominal_capacity_per_vehicle']
        stressed = x*data['stressed_capacity_per_vehicle']
        energy = x*data['energy_kwh_per_hour_per_vehicle']
        candidates.append({'vehicles':x,'nominal_capacity_per_hour':nominal,
                           'stress_capacity_per_hour':stressed, 'energy_kwh_per_hour':energy,
                           'nominal_feasible':nominal>=data['required_service_per_hour'] and energy<=data['energy_cap_kwh_per_hour'],
                           'robust_feasible':stressed>=data['required_service_per_hour'] and energy<=data['energy_cap_kwh_per_hour']})
    evidence = data['evidence']
    if not isinstance(evidence, list) or not evidence or len({e['requirement'] for e in evidence}) != len(evidence):
        raise ValueError('evidence paths must be unique')
    actionable = sum(e['revision']==data['expected_revision'] and e['status']=='verified' and e['intended_use']==data['intended_use'] for e in evidence)
    prior = data['paired_baseline_wait_min']; new = data['paired_candidate_wait_min']
    if not prior or len(prior)!=len(new) or len(prior)<2 or any(type(v) not in (int,float) or not math.isfinite(v) for v in prior+new):
        raise ValueError('paired streams invalid')
    differences=[b-a for a,b in zip(prior,new)]
    pvfactor=sum(1/1.05**t for t in (1,2,3))
    finance = {'A_pv':1000+200*pvfactor,'B_pv':1200+110*pvfactor,'required_saving_per_year':200/pvfactor}
    outputs = {'request_accounting':{'arrivals':len(requests),**counts},
               'timely_nominal':nom,'timely_guarded':safe,
               'timely_guarded_all_fraction':safe/len(requests),
               'accessible_guarded':ac_safe,'accessible_count':len(accessible),
               'accessible_guarded_fraction':ac_safe/len(accessible),
               'zero_failure_upper_95_300':zero_failure_upper(300),
               'mm1':{'rho':.8,'mean_in_system_min':30.0,'mean_wait_queue_min':24.0,'L':4.0,'Lq':3.2},
               'euler':{'coarse':euler_recovery(.7,1),'refined':euler_recovery(.7,.25),
                        'unstable_factor':1-.7*3},
               'reliability':{'independent_parallel':independent_parallel,'common_cause_adjusted':joint},
               'candidates':candidates,
               'actionable_evidence':actionable,'evidence_total':len(evidence),
               'paired_effect_min':statistics.mean(differences),
               'paired_se_min':statistics.stdev(differences)/math.sqrt(len(differences)),
               'finance':finance}
    outputs['authorization'] = {'required_permissions':data['required_permissions'],
             'granted_permissions':data['granted_permissions'],
             'all_granted':set(data['required_permissions']).issubset(data['granted_permissions'])}
    outputs['deployment_screen'] = {'passes': bool(
        outputs['timely_guarded_all_fraction'] >= .9 and outputs['accessible_guarded_fraction'] >= .85 and
        joint >= .98 and any(d['robust_feasible'] for d in candidates) and
        actionable==len(evidence) and outputs['authorization']['all_granted']),
        'scope':'synthetic classroom screening only; passing does not authorize deployment'}
    return outputs


def main() -> None:
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument('--input',default=str(DEFAULT))
    parser.add_argument('--output')
    args=parser.parse_args()
    out=audit(json.loads(Path(args.input).read_text(encoding='utf-8')))
    result=json.dumps(out,sort_keys=True,indent=2)+'\n'
    if args.output: Path(args.output).write_text(result,encoding='utf-8')
    else: print(result,end='')

if __name__=='__main__':main()
