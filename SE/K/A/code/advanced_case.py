"""NS-AA4.1: reproducible architecture/assurance teaching analysis.

No third-party dependencies. The sample data, acceptance criteria, scenario
weights, and interface assumptions are invented. Computational checks do not
validate the model, certify safety or authorize operations.
"""
from __future__ import annotations

import csv
import json
import math
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]


def require_probability(x: float) -> float:
    if isinstance(x, bool) or not isinstance(x, (int, float)) or not math.isfinite(x) or not 0 <= x <= 1:
        raise ValueError('probability must be finite in [0, 1]')
    return float(x)


def load_case(path: Path | None = None) -> dict:
    return json.loads((path or BASE/'data'/'advanced-case.json').read_text(encoding='utf-8'))


def load_requests(path: Path | None = None) -> list[dict]:
    with (path or BASE/'data'/'advanced-requests.csv').open(newline='', encoding='utf-8') as fp:
        return list(csv.DictReader(fp))


def adjudicate_service(rows: list[dict], max_wait: float, endpoint_bound: float) -> dict:
    """All eligible requests remain in denominator; worst-case clock guard band."""
    if not rows or any(isinstance(v,bool) or not isinstance(v,(int,float)) or not math.isfinite(v) or v < 0 for v in (max_wait,endpoint_bound)):
        raise ValueError('valid positive population and finite nonnegative limits required')
    ids = [r['request_id'] for r in rows]
    if len(ids) != len(set(ids)):
        raise ValueError('duplicate request id')
    if any(r.get('group') not in ('accessible','standard') for r in rows):
        raise ValueError('unknown group')
    if any(r.get('result') not in ('PICKUP','UNSERVED') for r in rows):
        raise ValueError('unknown result')
    out = {}
    for group in ('all','accessible','standard'):
        cohort = [r for r in rows if group=='all' or r['group']==group]
        if not cohort: raise ValueError('missing group')
        measured=robust=completed=0
        for r in cohort:
            wait = r.get('wait_minutes','')
            if r['result']=='UNSERVED':
                if wait != '': raise ValueError('unserved request must not have pickup wait')
                continue
            if wait == '': raise ValueError('pickup missing wait')
            try: w=float(wait)
            except (TypeError, ValueError): raise ValueError('invalid wait') from None
            if not math.isfinite(w) or w < 0: raise ValueError('invalid wait')
            completed += 1
            measured += w <= max_wait
            robust += w + 2*endpoint_bound <= max_wait
        out[group]={'eligible':len(cohort),'completed':completed,'measured_timely':measured,
                    'robust_timely':robust,'completion_rate':completed/len(cohort),
                    'measured_timely_rate':measured/len(cohort),
                    'robust_timely_rate':robust/len(cohort)}
    return out


def latency_budget(steps: list[dict], limit_s: float, common_delay_s: float = 0) -> dict:
    if not steps or len({s['id'] for s in steps}) != len(steps): raise ValueError('invalid steps')
    vals=[s.get('nominal_s') for s in steps]+[s.get('uncertainty_s') for s in steps]+[limit_s,common_delay_s]
    if any(isinstance(x,bool) or not isinstance(x,(float,int)) or not math.isfinite(x) or x<0 for x in vals):
        raise ValueError('nonnegative finite time inputs required')
    nominal=sum(s['nominal_s'] for s in steps)
    worst=nominal+sum(s['uncertainty_s'] for s in steps)+common_delay_s
    return {'nominal_s':nominal,'worst_s':worst,'margin_s':limit_s-worst,'passes':worst<=limit_s}


def shared_cause_reliability(channel_r:float, common_q:float) -> float:
    r=require_probability(channel_r); q=require_probability(common_q)
    return (1-q)*(1-(1-r)**2)


def unsafe_dispatch_counterexamples(max_age_min:float) -> list[dict]:
    """Finite truth-table check of a deliberately unsafe OR guard.

    Dispatch should require OPEN and age<=limit and authorization.
    The incorrect guard 'OPEN OR authorized' permits unsafe transitions.
    """
    if not isinstance(max_age_min,(int,float)) or isinstance(max_age_min,bool) or not math.isfinite(max_age_min) or max_age_min<0:
        raise ValueError('invalid maximum age')
    failed=[]
    for status in ('OPEN','CLOSED','UNKNOWN'):
        for age in (0.0, max_age_min, max_age_min+1):
            for authorized in (False,True):
                correct=(status=='OPEN' and age<=max_age_min and authorized)
                buggy=(status=='OPEN' or authorized)
                if buggy and not correct:
                    failed.append({'status':status,'age_min':age,'authorized':authorized})
    return failed


def evidence_screen(case:dict, expected_revision: str) -> dict:
    """Syntactic and configuration screen only; never declares field readiness."""
    if not expected_revision: raise ValueError('expected revision required')
    nodes=case['model']['nodes']; edges=case['model']['edges']
    idx={n['id']:n for n in nodes}
    if len(idx)!=len(nodes): raise ValueError('duplicate node')
    from model_checks import validate_model
    model_defects = validate_model(case['model'])
    if model_defects: raise ValueError('invalid typed model: '+','.join(model_defects))
    out={}
    for rid in case['requirements']:
        if rid not in idx or idx[rid]['type']!='Requirement': raise ValueError('invalid requirement')
        allocations=[e['target'] for e in edges if e['source']==rid and e['type']=='allocatedTo' and idx.get(e['target'],{}).get('type')=='Component']
        tests=[e['target'] for e in edges if e['source']==rid and e['type']=='verifiedBy' and idx.get(e['target'],{}).get('type')=='Test']
        produced=[e['target'] for e in edges if e['source'] in tests and e['type']=='produces' and idx.get(e['target'],{}).get('type')=='Evidence']
        defects=[]
        if not allocations: defects.append('no-allocation')
        if not tests: defects.append('no-test')
        if not produced: defects.append('no-evidence-path')
        evidence_defects=[]
        applicable=False
        for eid in produced:
            record=case['evidence'].get(eid)
            current=[]
            if record is None: current.append('evidence-record-absent')
            else:
                if record['revision']!=expected_revision: current.append('stale-revision')
                if record['status']!='PASS': current.append('nonpassing-evidence')
                if not record.get('scenario'): current.append('unscoped-evidence')
            if not current: applicable=True
            evidence_defects.extend(current)
        if not applicable: defects.extend(evidence_defects)
        out[rid]=sorted(set(defects))
    return out


def evaluate(case:dict|None=None, rows:list[dict]|None=None) -> dict:
    c=case or load_case(); r=rows if rows is not None else load_requests()
    service=adjudicate_service(r,c['acceptance']['wait_limit_min'],c['acceptance']['endpoint_clock_bound_min'])
    required=c['acceptance']; revision=c['configuration']['target_revision']
    budget=latency_budget(c['latency']['steps'],c['latency']['limit_s'])
    rel=shared_cause_reliability(c['reliability']['channel_r'],c['reliability']['common_cause_q'])
    evidence=evidence_screen(c,revision)
    failures=[]
    if service['all']['robust_timely_rate']<required['all_timely_min']: failures.append('all-request-timeliness')
    if service['accessible']['robust_timely_rate']<required['accessible_timely_min']: failures.append('accessible-timeliness')
    if not budget['passes']: failures.append('latency-budget')
    if rel<required['reliability_min']: failures.append('shared-cause-reliability')
    if any(evidence.values()): failures.append('evidence-applicability')
    if not all(c['authorizations'].values()): failures.append('missing-authorization')
    # Engineering release is intentionally never asserted by this educational model.
    return {'service':service,'latency':budget,'reliability':rel,'evidence_findings':evidence,
            'screen_failures':failures,'disposition':'HOLD','authorization_inferred':False}


if __name__=='__main__':
    print(json.dumps(evaluate(),indent=2,sort_keys=True))
