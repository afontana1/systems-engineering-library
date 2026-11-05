"""Northstar teaching tools: zero-failure bounds and completeness-aware T&E."""
from pathlib import Path
import csv, math, json
HERE=Path(__file__).parent

def zero_failure_bound(n,confidence=.95):
    if not isinstance(n,int) or n<=0 or not 0<confidence<1:raise ValueError('Invalid n or confidence')
    return 1-(1-confidence)**(1/n)

def n_for_bound(target,confidence=.95):
    if not 0<target<1 or not 0<confidence<1:raise ValueError('Invalid target or confidence')
    return math.ceil(math.log(1-confidence)/math.log(1-target))

def nearest_rank(vals,prob):
    if not vals or not 0<prob<=1:raise ValueError('Invalid sample or probability')
    return sorted(vals)[math.ceil(prob*len(vals))-1]

def evaluate(records):
    all_n=len(records)
    served=[float(r['wait_min']) for r in records if r['status']=='served']
    return {'requests':all_n,'served':len(served),'completion':len(served)/all_n,
            'served_p90_nearest_rank':nearest_rank(served,.9),'completion_gate':len(served)/all_n>=.95,
            'latency_gate':nearest_rank(served,.9)<=18}

if __name__=='__main__':
    with (HERE/'requests.csv').open(newline='') as f:rs=list(csv.DictReader(f))
    print(json.dumps({'p_u_30':zero_failure_bound(30),'n_target_1pct':n_for_bound(.01),
            'service':evaluate(rs)},indent=2))
