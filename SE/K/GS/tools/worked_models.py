"""Small deterministic worked models for advanced engineering studies.
Educational examples only; no operational certification implied.
Run: python -m unittest discover -s tools -p 'test_*.py' (from K/GS).
"""
from itertools import product

def earned_value(ev,ac,pv,bac):
    assert ac>0 and pv>0 and bac>=0
    return dict(cpi=ev/ac,spi=ev/pv,cost_variance=ev-ac,eac=bac/(ev/ac))

def energy_margin(d,e,hours,aux,battery,soc,eta,reserve):
    assert d>=0 and e>=0 and hours>=0 and aux>=0 and battery>=0 and 0<=soc<=1 and 0<=eta<=1
    return battery*soc*eta-reserve-d*e-hours*aux

def guard_time(e0,emin,power):
    assert power>0 and e0>=emin
    return (e0-emin)/power

def euler_multiplier(k,h):
    assert k>=0 and h>0
    return 1-k*h

def evpi(p,an,as_,bn,bs):
    assert 0<=p<=1
    a=(1-p)*an+p*as_; b=(1-p)*bn+p*bs
    perfect=(1-p)*max(an,bn)+p*max(as_,bs)
    return dict(a=a,b=b,perfect=perfect,evpi=perfect-max(a,b))

def flow_time(wip,throughput):
    assert wip>=0 and throughput>0
    return wip/throughput

def evidence_freshness(now,sample,max_age):
    assert now>=sample and max_age>=0
    return (now-sample)<=max_age

def diff_in_diff(tpre,tpost,cpre,cpost):
    return (tpost-tpre)-(cpost-cpre)

def mission_availability(pa,pb,pc,common):
    assert all(0<=x<=1 for x in (pa,pb,pc,common))
    independent=1-(1-pa*pb)*(1-pc)
    return dict(independent=independent,with_common=(1-common)*independent)

def portfolio_value(costs,values,budget,dependencies=None):
    assert len(costs)==len(values) and budget>=0
    n=len(costs); dependencies=dependencies or []
    choices=[]
    for mask in product((0,1),repeat=n):
        if sum(mask[i]*costs[i] for i in range(n))>budget:continue
        if any(mask[i] and not mask[j] for i,j in dependencies):continue
        choices.append((sum(mask[i]*values[i] for i in range(n)),mask))
    return max(choices,key=lambda a:(a[0],-sum(a[1])))

def group_delay(urban_fraction,before,after):
    assert 0<=urban_fraction<=1 and len(before)==len(after)==2
    avg=lambda xs: urban_fraction*xs[0]+(1-urban_fraction)*xs[1]
    return dict(before=avg(before),after=avg(after),rural_change=after[1]-before[1])
