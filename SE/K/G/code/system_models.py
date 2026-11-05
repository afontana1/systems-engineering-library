"""Northstar synthetic graduate-level learning models.
Not for real-world dispatch, authorization, or safety decisions.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import sqrt


def conservative_age(processing: float, scheduling: float, execution: float, skew: float = 0.0) -> float:
    if min(processing, scheduling, execution, skew) < 0:
        raise ValueError('time components must be nonnegative')
    return processing + scheduling + execution + skew


def authorize(current: float, observed: float, limit: float, skew: float = 0.0,
              signature_valid: bool = True, correct_scope: bool = True,
              current_revision: bool = True) -> bool:
    """Safety-constraint teaching predicate; does not verify a real signature."""
    if limit < 0 or skew < 0: raise ValueError('bad budget')
    return (current >= observed and current - observed + skew <= limit
            and signature_valid and correct_scope and current_revision)


def mm1(arrival: float, service: float) -> dict[str,float]:
    if arrival < 0 or service <= arrival: raise ValueError('queue not stationary')
    rho=arrival/service
    return {'utilization':rho,'wait_queue_h': arrival/(service*(service-arrival)),
            'time_system_h':1/(service-arrival)}


def alarm_ppv(prevalence: float, sensitivity: float, false_positive_rate: float) -> float:
    if any(not 0<=x<=1 for x in [prevalence,sensitivity,false_positive_rate]):
        raise ValueError('probabilities out of range')
    hit=sensitivity*prevalence
    denominator=hit+false_positive_rate*(1-prevalence)
    if denominator == 0: raise ValueError('alarm event has zero probability')
    return hit/denominator


class ReservationService:
    """Sequential reference specification; not a concurrent database implementation."""
    def __init__(self, capacity: int):
        if capacity < 0: raise ValueError('bad capacity')
        self.capacity=capacity
        self.outcomes: dict[str,tuple[str, str]]={}

    def reserve(self,key: str,payload: str) -> str:
        if key in self.outcomes:
            old_payload,outcome=self.outcomes[key]
            if old_payload != payload: return 'CONFLICT'
            return outcome
        if self.capacity <= 0:
            outcome='FULL'
        else:
            self.capacity-=1
            outcome='CONFIRMED'
        self.outcomes[key]=(payload,outcome)
        return outcome


def retry_amplification(external: float, retry_probability: float, service: float) -> dict[str,float|bool]:
    if external < 0 or service<=0 or not 0<=retry_probability<1:
        raise ValueError('invalid load assumptions')
    offered=external/(1-retry_probability)
    return {'offered':offered,'rho':offered/service,'stable':offered<service}


def serial_availability(*components: float) -> float:
    result=1.0
    for a in components:
        if not 0<=a<=1: raise ValueError('availability out of range')
        result*=a
    return result


def parallel_common_cause(local_availability: float, common_outage: float, replicas: int=2) -> float:
    if not 0<=local_availability<=1 or not 0<=common_outage<=1 or replicas<1:
        raise ValueError('invalid availability inputs')
    return (1-common_outage)*(1-(1-local_availability)**replicas)


def error_budget(eligible:int, target:float) -> float:
    if eligible<0 or not 0<=target<=1: raise ValueError('invalid SLO')
    return eligible*(1-target)


def any_path_available(a:float,b:float) -> float:
    if not 0<=a<=1 or not 0<=b<=1: raise ValueError('invalid probability')
    return 1-(1-a)*(1-b)


def reachable(edges: list[tuple[str,str]], start: str, target: str,
              excluded_nodes: set[str]|None=None) -> bool:
    excluded_nodes=excluded_nodes or set()
    if start in excluded_nodes or target in excluded_nodes: return False
    seen={start}; stack=[start]; adj={}
    for u,v in edges: adj.setdefault(u,[]).append(v)
    while stack:
        u=stack.pop()
        if u==target: return True
        for v in adj.get(u,[]):
            if v not in excluded_nodes and v not in seen:
                seen.add(v);stack.append(v)
    return False


def beta_bernoulli_update(alpha:float,beta:float,failures:int,successes:int) -> tuple[float,float,float]:
    if alpha<=0 or beta<=0 or failures<0 or successes<0: raise ValueError('invalid beta inputs')
    a,b=alpha+failures,beta+successes
    return a,b,a/(a+b)


def backlog(initial:float,demand_rate:float,service_rate:float,hours:float)->float:
    if min(initial,demand_rate,service_rate,hours)<0: raise ValueError('invalid rates')
    return max(0,initial+(demand_rate-service_rate)*hours)


def subgroup_mean(groups:list[tuple[int,float]]) -> float:
    if not groups or sum(n for n,_ in groups)<=0 or any(n<0 or x<0 for n,x in groups):
        raise ValueError('invalid groups')
    return sum(n*x for n,x in groups)/sum(n for n,_ in groups)


def difference_in_differences(t_before:float,t_after:float,c_before:float,c_after:float)->float:
    return (t_after-t_before)-(c_after-c_before)
