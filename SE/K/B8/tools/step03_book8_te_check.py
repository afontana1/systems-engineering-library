#!/usr/bin/env python3
"""Educational NS-TE8.1 evidence audit (Python stdlib only).

All inputs are invented. The program calculates sample confidence limits and
checks referential integrity, applicability and missing requirements. It does
NOT qualify a product or validate a field operating distribution.
"""
from __future__ import annotations
import csv, json, math
from pathlib import Path

CASE=Path(__file__).resolve().parents[1]/'case'
INHERITED=CASE.parent.parent/'B7/case/model-baseline.json'


def rows(filename):
    with (CASE/filename).open(encoding='utf8',newline='') as f:
        return list(csv.DictReader(f))


def zero_failure_upper(n:int, alpha:float=0.05)->float:
    if not isinstance(n,int) or n<1 or not 0<alpha<1:
        raise ValueError('n must be positive integer and alpha between zero and one')
    return 1-math.exp(math.log(alpha)/n)


def zero_failure_sample_size(max_failure_probability:float,alpha:float=0.05)->int:
    if not 0<max_failure_probability<1 or not 0<alpha<1:
        raise ValueError('probabilities must be in (0,1)')
    # strict upper bound < target: calculate and verify due to round-off
    n=max(1,math.floor(math.log(alpha)/math.log1p(-max_failure_probability))+1)
    while zero_failure_upper(n,alpha)>=max_failure_probability:
        n+=1
    return n


def inherited_models():
    b=json.loads(INHERITED.read_text(encoding='utf8'))
    r=b['reliability']
    mission=math.exp(-r['mission_h']*(r['independent_failure_rate_per_h']+r['shared_failure_rate_per_h']))
    availability=r['mtbf_h']/(r['mtbf_h']+r['mttr_h']+r['mean_logistics_delay_h'])
    energy=sum(b['energy'][key] for key in ('traction','heating','communications'))
    return b['baseline'],mission,availability,energy


def report(evidence_override=None,timing_override=None):
    req=rows('requirements.csv'); plan=rows('test-plan.csv')
    evidence=evidence_override if evidence_override is not None else rows('evidence-register.csv')
    latency=timing_override if timing_override is not None else rows('latency-synthetic.csv')
    discrepancies=rows('discrepancies.csv')
    required={x['requirement_id'] for x in req}
    if len(required)!=len(req):raise ValueError('duplicate requirement IDs')
    proc={x['procedure'] for x in plan}
    if len(proc)!=len(plan):raise ValueError('duplicate procedure IDs')
    if {x['requirement'] for x in plan}!=required:raise ValueError('test-plan coverage gap')
    ids=[x['evidence_id'] for x in evidence]
    if len(set(ids))!=len(ids):raise ValueError('duplicate evidence identifiers')
    if {x['requirement_id'] for x in evidence}!=required:
        raise ValueError('missing or unexpected requirement evidence')
    for record in evidence:
        if record['requirement_id'] not in required or record['procedure'] not in proc:
            raise ValueError('orphan evidence reference')
        if record['configuration']!='NS-DI7.1' and record['status']!='STALE':
            raise ValueError('older baseline presented as applicable evidence')
        if record['status']=='STALE' and record['configuration']=='NS-DI7.1':
            raise ValueError('stale evidence incorrectly marked current')
    for issue in discrepancies:
        if issue['requirement'] not in required:raise ValueError('orphan discrepancy')
        if issue['state']!='OPEN':raise ValueError('unexpected closure without evidence')
    trials=[float(x['measured_ms']) for x in latency]
    if not trials or any(not math.isfinite(x) or x<0 for x in trials):
        raise ValueError('invalid latency measurement')
    if any(x['configuration']!='NS-DI7.1' or x['origin']!='SYNTHETIC' for x in latency):
        raise ValueError('invalid test population or baseline')
    n=len(trials); exceed=sum(x>500 for x in trials)
    if exceed != 0:  # current teaching case specifically zero failures
        raise ValueError('case changed: replace zero-exceedance formula with general binomial bound')
    baseline,mission,availability,energy=inherited_models()
    if baseline!='NS-DI7.1':raise ValueError('received baseline mismatch')
    reasons=[]
    if mission<0.98:reasons.append('MODEL_RELIABILITY_BELOW_TARGET')
    if availability<0.99:reasons.append('MODEL_AVAILABILITY_BELOW_TARGET')
    if zero_failure_upper(n)>0.01:reasons.append('INSUFFICIENT_P99_STATISTICAL_EVIDENCE')
    status={x['evidence_id']:x['status'] for x in evidence}
    for eid,flag in [('TE8-E06','STALE'),('TE8-E07','PLANNED'),('TE8-E08','SYNTHETIC_FAIL')]:
        if status.get(eid)!=flag:raise ValueError('case fails to preserve controlled known gap '+eid)
    reasons.extend(['STALE_HIL_RECORD','MISSING_CYBER_TEST','FAILED_RECOVERY_DRILL'])
    if any(x['status']=='MODEL_ONLY' for x in evidence):reasons.append('MODEL_ONLY_NOT_VERIFICATION')
    return {'campaign':'NS-TE8.1','product':baseline,'trials':n,'observed_exceedances':exceed,
            'min_ms':min(trials),'max_ms':max(trials),
            'one_sided_95pct_upper_exceedance':zero_failure_upper(n),
            'ideal_zero_failure_trials_for_1pct':zero_failure_sample_size(0.01),
            'boundary_guardband_threshold_ms':500-12,'boundary_493ms_accepted':493<=500-12,
            'energy_kwh_model':energy,'mission_reliability_model':mission,
            'availability_model':availability,'recovery_drill_minutes':14,
            'operational_decision':'HOLD' if reasons else 'UNREVIEWED',
            'hold_reasons':reasons,'discrepancies_open':len(discrepancies)}

if __name__=='__main__':
    print(json.dumps(report(),indent=2))
