"""Educational, standard-library-only calculations for the Systems Engineering Atlas.

Not certified software. Document assumptions before using any result in a decision.
"""
from __future__ import annotations
from math import exp, log, isfinite
from random import Random
from collections import deque


def zero_failure_upper_bound(trials: int, confidence: float = 0.95) -> float:
    """Exact one-sided upper bound on iid Bernoulli failure p given 0 failures."""
    if not isinstance(trials, int) or trials <= 0 or not 0 < confidence < 1:
        raise ValueError('trials must be a positive integer, confidence between 0 and 1')
    return 1.0 - (1.0 - confidence) ** (1.0 / trials)


def factorial_2x2(y_mm: float, y_pm: float, y_mp: float, y_pp: float) -> dict:
    """Factor A and B main effects and A-B interaction difference-of-differences.
    Inputs are outcomes for (-,-), (+,-), (-,+), (+,+) factor settings.
    """
    return {
        'A_effect': ((y_pm + y_pp) - (y_mm + y_mp)) / 2,
        'B_effect': ((y_mp + y_pp) - (y_mm + y_pm)) / 2,
        'interaction_contrast': (y_pp - y_mp) - (y_pm - y_mm),
        'regression_interaction_coefficient': ((y_pp - y_mp) - (y_pm - y_mm)) / 4,
    }


def pareto_indices(rows: list[tuple[float, ...]], minimize: tuple[bool, ...]) -> list[int]:
    """Indices of nondominated alternatives; all rows must already satisfy hard constraints."""
    if not rows: return []
    if any(len(row) != len(minimize) for row in rows): raise ValueError('dimension mismatch')
    if not minimize: raise ValueError('objectives required')
    for row in rows:
        if any(not isfinite(float(x)) for x in row): raise ValueError('nonfinite objective')
    def better_or_eq(a,b):
        return all((x<=y if m else x>=y) for x,y,m in zip(a,b,minimize))
    def strictly_better(a,b):
        return any((x<y if m else x>y) for x,y,m in zip(a,b,minimize))
    return [i for i,row in enumerate(rows) if not any(j!=i and better_or_eq(other,row) and strictly_better(other,row) for j,other in enumerate(rows))]


def expected_value_perfect_info(probabilities: list[float], payoffs: list[list[float]]) -> tuple[int,float,float,float]:
    """Returns (best_now_action, best_now_expected_value, perfect_info_value, EVPI).
    payoffs[action][state]. Assumes finite, comparable utility units.
    """
    if not probabilities or any(p<0 or not isfinite(p) for p in probabilities) or abs(sum(probabilities)-1)>1e-9:
        raise ValueError('probabilities must be nonnegative and sum to 1')
    if not payoffs or any(len(a)!=len(probabilities) for a in payoffs): raise ValueError('payoff dimensions')
    vals=[sum(p*u for p,u in zip(probabilities,a)) for a in payoffs]
    best_idx=max(range(len(vals)),key=lambda i: vals[i])
    perfect=sum(p*max(a[s] for a in payoffs) for s,p in enumerate(probabilities))
    return best_idx, vals[best_idx], perfect, max(0.,perfect-vals[best_idx])


def mm1_mean_system_time(arrivals_per_hour: float, service_per_hour: float) -> float:
    """Idealized stationary M/M/1 mean system time in hours."""
    if arrivals_per_hour < 0 or service_per_hour <= 0 or arrivals_per_hour >= service_per_hour:
        raise ValueError('requires 0<=lambda<mu and mu>0')
    return 1/(service_per_hour-arrivals_per_hour)


def little_law_wip(throughput_per_hour: float, mean_time_hours: float) -> float:
    if throughput_per_hour < 0 or mean_time_hours < 0: raise ValueError('nonnegative quantities required')
    return throughput_per_hour*mean_time_hours


def euler_decay(x0: float, k_per_hour: float, step_hours: float, n_steps: int) -> tuple[float,float]:
    """Forward Euler and analytical comparison for dx/dt=-k*x."""
    if k_per_hour<0 or step_hours<=0 or not isinstance(n_steps,int) or n_steps<0: raise ValueError('invalid parameters')
    x=x0
    for _ in range(n_steps): x-=step_hours*k_per_hour*x
    return x, x0*exp(-k_per_hour*step_hours*n_steps)


def simple_critical_path(tasks: dict[str,tuple[float,list[str]]]) -> tuple[float,list[str]]:
    """Deterministic precedence longest path. Durations >=0, no resources/calendars."""
    if not tasks:return 0,[]
    memo={}; visiting=set()
    def visit(t):
        if t not in tasks:raise ValueError(f'missing predecessor {t}')
        if t in visiting: raise ValueError('cycle in dependencies')
        if t in memo: return memo[t]
        visiting.add(t)
        dur,preds=tasks[t]
        if dur<0:raise ValueError('negative duration')
        before=[visit(p) for p in preds]
        prior=max(before,key=lambda x:x[0]) if before else (0.,[])
        result=(prior[0]+dur,prior[1]+[t]);memo[t]=result;visiting.remove(t)
        return result
    return max((visit(t) for t in tasks),key=lambda x:x[0])


def reliability_series(rs: list[float]) -> float:
    if any(not 0<=r<=1 for r in rs):raise ValueError('reliabilities between 0 and 1')
    value=1.
    for r in rs:value*=r
    return value


def reliability_parallel(rs: list[float]) -> float:
    if any(not 0<=r<=1 for r in rs):raise ValueError('reliabilities between 0 and 1')
    fail=1.
    for r in rs:fail*=1-r
    return 1-fail


def difference_in_differences(pilot_before: float,pilot_after: float,control_before: float,control_after: float) -> float:
    """Arithmetical estimator only; causal identification assumptions are NOT tested."""
    return (pilot_after-pilot_before)-(control_after-control_before)


def audit_traceability(requirements: set[str], tests: set[str], evidence: set[str], edges: list[tuple[str,str,str]]) -> dict[str,list[str]]:
    """Detect missing links in typed requirement->test->evidence chains.
    Edges are (source, relation, target); accepted relations 'verified_by', 'produces'.
    """
    byreq={r:set() for r in requirements}; bytest={t:set() for t in tests}
    for source,relation,target in edges:
        if relation=='verified_by' and source in requirements and target in tests: byreq[source].add(target)
        if relation=='produces' and source in tests and target in evidence: bytest[source].add(target)
    no_test=sorted(r for r in requirements if not byreq[r])
    no_evidence=sorted(r for r in requirements if byreq[r] and not any(bytest[t] for t in byreq[r]))
    return {'no_verification_method':no_test, 'no_evidence_chain':no_evidence}


def simulate_mm1(arrival_rate:float,service_rate:float,customers:int=10000,seed:int=2026) -> dict:
    """Single FIFO infinite-capacity queue using independent exponential samples.
    Times in hours; uses a finite sample starting empty, so not a stationary estimate.
    """
    if arrival_rate<=0 or service_rate<=0 or customers<1:raise ValueError('invalid queue parameters')
    rng=Random(seed);arrival=0.;last_finish=0.;waits=[]
    for _ in range(customers):
        arrival+=rng.expovariate(arrival_rate)
        wait=max(0.,last_finish-arrival)
        last_finish=max(arrival,last_finish)+rng.expovariate(service_rate)
        waits.append(wait)
    return {'mean_queue_wait_h':sum(waits)/customers,
            'mean_system_time_h':sum(waits)/customers+1/service_rate,
            'p95_queue_wait_h':sorted(waits)[int(.95*(customers-1))],
            'utilization_nominal':arrival_rate/service_rate}
