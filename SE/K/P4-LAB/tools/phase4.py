"""Synthetic Phase 4 teaching calculations. Not a safety/assurance certification tool."""
import math,statistics

def flow_time(wip,throughput):
    if wip<0 or throughput<=0: raise ValueError("WIP must be nonnegative and throughput positive")
    return wip/throughput

def mm1_time(lam,mu):
    if lam<0 or mu<=0 or lam>=mu: raise ValueError("M/M/1 must be stable: 0 <= lambda < mu")
    return 1/(mu-lam)

def option_net(premium,saving,count):
    if count<0: raise ValueError("count nonnegative")
    return saving*count-premium

def energy_range(kwh,consumption):
    if kwh<0 or consumption<=0: raise ValueError("invalid energy/consumption")
    return kwh/consumption

def fresh(age_seconds,max_age_seconds):
    if age_seconds<0 or max_age_seconds<0:raise ValueError("negative age")
    return age_seconds<=max_age_seconds

def audit_links(requirements,links):
    """Requirement keys are (id,rev). Returns exact unverified revision keys."""
    proved={(row['req'],row['rev']) for row in links if row['status']=='passed'}
    return [x for x in requirements if x not in proved]

def lead_summary(values):
    if not values or any(x<0 for x in values): raise ValueError("nonnegative samples required")
    v=sorted(values)
    def quantile(p):
        k=(len(v)-1)*p;i=int(k);return v[i]+(v[min(i+1,len(v)-1)]-v[i])*(k-i)
    return {'mean':sum(v)/len(v),'median':quantile(.5),'p90':quantile(.9)}

def paired_difference(a,b):
    """Normal-approximation 95% CI for paired b-a differences (small n: consider t/other methods)."""
    if len(a)!=len(b) or len(a)<2:raise ValueError("at least two paired observations")
    d=[y-x for x,y in zip(a,b)];mean=statistics.mean(d)
    se=statistics.stdev(d)/math.sqrt(len(d))
    return mean,(mean-1.96*se,mean+1.96*se)

def scaled_mission_success(component_success,shared_dependency):
    """Only under explicitly independent component events and a common AND mission path."""
    if any(x<0 or x>1 for x in component_success+[shared_dependency]):raise ValueError("probabilities in [0,1]")
    return math.prod(component_success)*shared_dependency
