"""Replication statistics; approximate confidence intervals assume independent observations."""
import math,statistics,random
def variance_of_sum(sd_x,sd_y,correlation):
    assert sd_x>=0 and sd_y>=0 and -1<=correlation<=1
    return sd_x**2+sd_y**2+2*correlation*sd_x*sd_y
def replication_summary(values,t_multiplier):
    v=list(values)
    assert len(v)>=2 and t_multiplier>=0
    mean=statistics.mean(v); se=statistics.stdev(v)/math.sqrt(len(v))
    return {'mean':mean,'se':se,'lower':mean-t_multiplier*se,'upper':mean+t_multiplier*se}
def synthetic_replications(seed=17,n=20):
    assert n>=1
    r=random.Random(seed)
    return [max(0,r.gauss(8,2)) for _ in range(n)]
def paired_improvement(seed=17,n=20):
    assert n>=1
    r=random.Random(seed)
    outcomes=[]
    for _ in range(n):
        shock=r.gauss(0,2); base=9+shock+r.gauss(0,.5); new=7.5+shock+r.gauss(0,.5)
        outcomes.append(base-new)
    return outcomes
