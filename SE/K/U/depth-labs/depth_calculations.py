"""Reproducible educational calculations for v8 concept derivations.
Standard library only; no claim of validation for operational engineering use.
"""
from math import log

def zero_failure_upper(n,confidence=.95):
    if n<=0 or not 0<confidence<1: raise ValueError("invalid trial count or confidence")
    return 1-(1-confidence)**(1/n)

def trials_for_zero_failure(target,confidence=.95):
    if not 0<target<1 or not 0<confidence<1: raise ValueError("invalid target")
    from math import ceil
    return ceil(log(1-confidence)/log(1-target))

def bayes_two_state(prior, sensitivity, false_positive):
    if not all(0<=v<=1 for v in [prior,sensitivity,false_positive]): raise ValueError("probabilities")
    ppos=prior*sensitivity+(1-prior)*false_positive
    pneg=1-ppos
    return {"p_positive":ppos,"posterior_positive":prior*sensitivity/ppos if ppos else None,
            "posterior_negative":prior*(1-sensitivity)/pneg if pneg else None}

def sample_information_value(prior=.1,sensitivity=.8,false_positive=.1,defect_loss=100,reject_loss=18):
    def decision(p):return min(p*defect_loss,reject_loss)
    x=bayes_two_state(prior,sensitivity,false_positive)
    before=decision(prior)
    after=x['p_positive']*decision(x['posterior_positive'])+(1-x['p_positive'])*decision(x['posterior_negative'])
    return before-after

def trade_difference(weight):
    if not 0<=weight<=1:raise ValueError('weight')
    a=8*weight+4*(1-weight)
    b=6*weight+8*(1-weight)
    return a,b,a-b

def factorial_effects(y):
    """y is mapping of (A,B) in {-1,+1} to response; main effects and interaction contrast."""
    lo=y[-1,-1];alo=y[1,-1];hi=y[-1,1];ahi=y[1,1]
    return {"A":(alo+ahi-lo-hi)/2,"B":(hi+ahi-lo-alo)/2,"AB":(ahi-hi)-(alo-lo),"beta_AB":((ahi-hi)-(alo-lo))/4}

def mm1(arrival,service):
    if not 0<=arrival<service:raise ValueError('queue not stationary under M/M/1 conditions')
    w=1/(service-arrival)
    return {'utilization':arrival/service,'W_hours':w,'Wq_hours':w-1/service,'L':arrival*w}

def joint_failure_common_cause(common=.01,independent=.02):
    if not 0<=common<=1 or not 0<=independent<=1:raise ValueError('probabilities')
    return common+(1-common)*independent**2

def euler_decay(x0=100,k=.4,steps=4,total_time=1):
    if steps<=0 or total_time<0 or k<0:raise ValueError('bad model settings')
    h=total_time/steps
    x=x0
    for _ in range(steps):x=x*(1-k*h)
    return x

def critical_path(durations,predecessors):
    """Computes earliest starts/finishes for a precedence-only DAG; no resource constraints."""
    values={}; todo=set(durations)
    while todo:
        ready=sorted(k for k in todo if set(predecessors.get(k,[]))<=values.keys())
        if not ready:raise ValueError('cycle or missing predecessor')
        for item in ready:
            st=max([values[p]['finish'] for p in predecessors.get(item,[])],default=0)
            values[item]={'start':st,'finish':st+durations[item]}
            todo.remove(item)
    return values,max(a['finish'] for a in values.values())

def earned_value(pv,ev,ac):
    if pv<=0 or ac<=0:raise ValueError('zero denominator')
    return {'SPI':ev/pv,'CPI':ev/ac,'SV':ev-pv,'CV':ev-ac}

def difference_in_differences(tbefore,tafter,cbefore,cafter):
    return (tafter-tbefore)-(cafter-cbefore)
