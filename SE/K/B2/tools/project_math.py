"""Fictional EN.645.667 demonstration arithmetic; no external dependencies."""
from collections import defaultdict

def proposal_price(pmb:float, reserve:float, fee:float)->float:
    if min(pmb,reserve,fee)<0:raise ValueError("negative values")
    return round(pmb+reserve+fee,8)

def estimate_hours(hours:float, rate:float, materials:float=0)->float:
    if min(hours,rate,materials)<0:raise ValueError("negative inputs")
    return hours*rate+materials

def evm(bac:float,pv:float,ev:float,ac:float)->dict:
    if bac<=0 or ac<=0 or pv<=0 or ev<0:raise ValueError("invalid EVM inputs")
    cpi=ev/ac; spi=ev/pv
    return dict(sv=ev-pv,cv=ev-ac,spi=spi,cpi=cpi,eac_simple=(bac/cpi if cpi>0 else float("inf")))

def cpm(tasks:dict)->dict:
    """Tasks: {id: {'duration': positive, 'predecessors': [ids]}}; finish to earliest completion."""
    done={}; visiting=set()
    def visit(k):
        if k in visiting:raise ValueError('cycle')
        if k in done:return done[k]
        if k not in tasks:raise ValueError('unknown task '+k)
        visiting.add(k); deps=tasks[k]['predecessors']; dur=tasks[k]['duration']
        if dur<0:raise ValueError('negative duration')
        es=max((visit(p)['EF'] for p in deps),default=0)
        visiting.remove(k);done[k]={'ES':es,'EF':es+dur}
        return done[k]
    for k in tasks:visit(k)
    finish=max((x['EF'] for x in done.values()),default=0)
    successors=defaultdict(list)
    for k,task in tasks.items():
        for predecessor in task['predecessors']:successors[predecessor].append(k)
    for k in reversed(list(done)):
        dur=tasks[k]['duration']; lf=min((done[s]['LS'] for s in successors[k]),default=finish)
        done[k].update(LS=lf-dur,LF=lf,float=lf-dur-done[k]['ES'])
    return {'finish':finish,'tasks':done,'critical':[k for k,v in done.items() if abs(v['float'])<1e-9]}
