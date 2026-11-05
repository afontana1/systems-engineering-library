"""Reproducible teaching calculations for Graduate Methods VI.
All quantities are synthetic; results are not operational certification.
Python standard library only.
"""
from __future__ import annotations
import hashlib
import math
from dataclasses import dataclass
from pathlib import Path


def feasible(capacity: float, wait_p90: float, min_capacity=105, max_wait=16) -> bool:
    return capacity >= min_capacity and wait_p90 <= max_wait


def score_difference(cost_weight: float) -> float:
    if not 0 <= cost_weight <= 1:
        raise ValueError('weight outside [0,1]')
    return 0.5 * cost_weight - 0.2


def posterior(prior: float, sensitivity: float, specificity: float) -> tuple[float,float,float]:
    if not all(0 <= x <= 1 for x in (prior,sensitivity,specificity)):
        raise ValueError('invalid probability')
    p_plus=prior*sensitivity+(1-prior)*(1-specificity)
    p_minus=1-p_plus
    p_fail_plus=prior*sensitivity/p_plus if p_plus else 0.0
    p_fail_minus=prior*(1-sensitivity)/p_minus if p_minus else 0.0
    return p_plus,p_fail_plus,p_fail_minus


def expected_test_cost(prior=.25, sensitivity=.85, specificity=.90, recovery=2.4,
                       mitigation_cost=.34, residual_failure=.04, test_fee=.05) -> tuple[float,float]:
    p_plus,post_plus,post_minus=posterior(prior,sensitivity,specificity)
    mitigation_loss=mitigation_cost+residual_failure*recovery
    no_test=min(prior*recovery,mitigation_loss)
    after_test=(p_plus*min(post_plus*recovery,mitigation_loss)
                +(1-p_plus)*min(post_minus*recovery,mitigation_loss)+test_fee)
    return no_test,after_test


def deterministic_budget(stage_bounds: tuple[float,...],deadline: float) -> float:
    if min((*stage_bounds,deadline)) < 0:
        raise ValueError('negative latency')
    return deadline-sum(stage_bounds)


def quantile_joint_guarantee(stage_failure_probs: tuple[float,...]) -> float:
    if not all(0 <= p <= 1 for p in stage_failure_probs):
        raise ValueError('bad probabilities')
    return max(0.0,1-sum(stage_failure_probs))


def zero_failure_upper(n:int,alpha=.05)->float:
    if n < 1 or not 0 < alpha < 1: raise ValueError('invalid n or alpha')
    return 1-alpha**(1/n)


def required_zero_failure_trials(target:float,alpha=.05)->int:
    if not 0 < target < 1 or not 0 < alpha < 1: raise ValueError('invalid params')
    return math.ceil(math.log(alpha)/math.log1p(-target))


def paired_summary(values:list[float],tcrit:float)->tuple[float,float,float]:
    if len(values)<2 or tcrit <0: raise ValueError('insufficient pairs or t critical')
    n=len(values);mean=sum(values)/n
    sd=math.sqrt(sum((x-mean)**2 for x in values)/(n-1))
    half=tcrit*sd/math.sqrt(n)
    return mean,mean-half,mean+half


def mm1(lam:float,mu:float)->tuple[float,float,float]:
    if lam<0 or mu<=lam:raise ValueError('unstable or invalid M/M/1')
    return lam/mu,1/(mu-lam),lam/(mu*(mu-lam))


def coverage(rows:list[dict],current_build:str)->tuple[float,float]:
    """Each row: linked, passing, revision, threshold, evidence."""
    if not rows:raise ValueError('empty requirements')
    structural=sum(bool(r['linked']) for r in rows)
    actionable=sum(bool(r['linked'] and r['passing'] and r['threshold'] and r['evidence']
                        and r['revision']==current_build) for r in rows)
    return structural/len(rows),actionable/len(rows)


def digest(path:str|Path)->str:
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def difference_in_differences(t_pre:float,t_post:float,c_pre:float,c_post:float)->float:
    return (t_post-t_pre)-(c_post-c_pre)


def workforce_step(stock:float, trained:float, attrition:float, reassigned:float)->float:
    if min(stock,trained,attrition,reassigned)<0 or attrition+reassigned>stock+trained:
        raise ValueError('invalid workforce flow')
    return stock+trained-attrition-reassigned
