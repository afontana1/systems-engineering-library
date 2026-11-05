"""Northstar teaching tools: evidence applicability and constrained trade studies.
Run: python tools.py. Uses only the Python standard library.
"""
from pathlib import Path
import csv, json
HERE=Path(__file__).parent

def read_csv(filename):
    with (HERE/filename).open(newline='',encoding='utf-8') as f:
        return list(csv.DictReader(f))

def evidence_status(record):
    if record['result']=='NONE': return 'NO_TEST'
    if record['current_rev']!=record['test_rev']: return 'STALE'
    if record['release_config']!=record['test_config']: return 'WRONG_CONFIGURATION'
    return 'VERIFIED_PASS' if record['result']=='PASS' else 'VALID_FAILURE'

def evidence_summary(records):
    statuses=[evidence_status(r) for r in records]
    return {'requirements':len(statuses),'admissible':sum(x in ('VERIFIED_PASS','VALID_FAILURE') for x in statuses),
            'supported':statuses.count('VERIFIED_PASS'),'valid_failures':statuses.count('VALID_FAILURE'),
            'details':dict(zip((r['id'] for r in records),statuses))}

def trade(choices,cost_weight=.25):
    if not (0<=cost_weight<=1):raise ValueError('Cost weight must be in [0,1]')
    # Remaining preference weights maintain the 0.35:0.40 ratio.
    other=1-cost_weight
    weights=(cost_weight,other*7/15,other*8/15)
    out=[]
    for c in choices:
        cost, wait, cover = float(c['cost_m']), float(c['wait_p90']), float(c['coverage'])
        feasible=cost<=5 and wait<=20 and cover>=.95
        u=(1-(cost-4),1-(wait-10)/20,(cover-.9)/.1)
        score=sum(w*v for w,v in zip(weights,u)) if feasible else None
        out.append({'id':c['id'],'feasible':feasible,'score':score})
    return out

if __name__=='__main__':
    print(json.dumps({'evidence':evidence_summary(read_csv('trace.csv')),
         'trade':trade(read_csv('trade.csv'))},indent=2))
