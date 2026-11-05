"""Phase 5 teaching calculators. Synthetic examples; not operational decision or safety tools.

Standard library only. Each function documents limitations and raises on invalid inputs.
"""
from __future__ import annotations
import itertools, math
from datetime import datetime


def bayes_positive(prior:float, sensitivity:float, false_positive_rate:float)->float:
    """Posterior P(event|alarm) for a calibrated binary observation; no causal claims."""
    if any(not 0<=v<=1 for v in (prior,sensitivity,false_positive_rate)):
        raise ValueError('probabilities must be in [0,1]')
    numerator=prior*sensitivity
    denominator=numerator+(1-prior)*false_positive_rate
    if denominator==0:raise ValueError('alarm has zero probability under both hypotheses')
    return numerator/denominator


def independent_series_success(probabilities:list[float])->float:
    """Product of independent required element success probabilities, NOT correlated mission risk."""
    if not probabilities:raise ValueError('at least one event required')
    if any(not 0<=p<=1 for p in probabilities):raise ValueError('invalid probability')
    return math.prod(probabilities)


def minimal_cut_sets(success_paths:list[list[str]])->list[tuple[str,...]]:
    """For OR of AND paths, return minimum-by-inclusion failure hitting sets.

    Each success path is a set of elements required to make one route work.
    Empty path means unconditional success; there are no cut sets.
    Assumes boolean failures and correct paths; not timed/probabilistic.
    """
    if not success_paths:raise ValueError('need at least one path')
    if any(not p for p in success_paths):return []
    paths=[set(p) for p in success_paths]
    if any(not all(isinstance(v,str) and v.strip() for v in p) for p in paths):
        raise ValueError('element names must be nonempty strings')
    all_nodes=sorted(set.union(*paths))
    cuts=[]
    for n in range(1,len(all_nodes)+1):
        for items in itertools.combinations(all_nodes,n):
            candidate=set(items)
            if any(set(c).issubset(candidate) for c in cuts):continue
            if all(candidate & p for p in paths):cuts.append(items)
    return cuts


def time_age_seconds(observed_iso:str,decision_iso:str,max_age:float)->tuple[float,bool]:
    """Timestamp age (nonnegative) and allowed-use freshness; consistent UTC offsets required."""
    if max_age<0:raise ValueError('negative max age')
    o=datetime.fromisoformat(observed_iso.replace('Z','+00:00'))
    d=datetime.fromisoformat(decision_iso.replace('Z','+00:00'))
    diff=(d-o).total_seconds()
    if diff<0:raise ValueError('observation is in the future')
    return diff,diff<=max_age


def stock_flow(initial:float,inflows:list[float],outflows:list[float])->list[float]:
    """Finite-step stock ledger; assumes supplied flows correspond to each complete interval."""
    if initial<0 or len(inflows)!=len(outflows):raise ValueError('stock/series invalid')
    state=float(initial); history=[state]
    for i,o in zip(inflows,outflows):
        if i<0 or o<0 or state+i-o<-1e-10:raise ValueError('invalid or infeasible flow')
        state=state+i-o;history.append(round(state,10))
    return history


def portfolio_feasible(options:list[dict],budget:float)->list[dict]:
    """Enumerate feasible portfolios with prerequisite IDs (illustrative, exponential time).

    options rows: {id, cost, value, requires:[ids]}; value is a hypothetical scalar,
    not a legitimate substitute for human/ethical constraints or multi-objective analysis.
    """
    if budget<0 or len(options)>18:raise ValueError('budget invalid or too many options')
    ids=[x['id'] for x in options]
    if len(set(ids))!=len(ids):raise ValueError('duplicate id')
    if any(x['cost']<0 or x['value']<0 or any(r not in ids for r in x.get('requires',[])) for x in options):
        raise ValueError('bad option or dependency')
    results=[]
    for n in range(len(options)+1):
        for subset in itertools.combinations(options,n):
            chosen={x['id'] for x in subset}
            if not all(set(x.get('requires',[]))<=chosen for x in subset):continue
            cost=sum(x['cost'] for x in subset)
            if cost>budget+1e-9:continue
            results.append({'ids':tuple(sorted(chosen)),'cost':cost,'value':sum(x['value'] for x in subset)})
    return sorted(results,key=lambda x:(-x['value'],x['cost'],x['ids']))


def subgroup_rate(groups:list[tuple[int,int]])->tuple[float,list[float]]:
    """Overall success rate plus disaggregated rates; pairs=(successes,eligible)."""
    if not groups:raise ValueError('at least one group')
    if any(n<=0 or k<0 or k>n for k,n in groups):raise ValueError('invalid group counts')
    return sum(k for k,n in groups)/sum(n for k,n in groups),[k/n for k,n in groups]


def queue_mm1_system_time(arrival:float,service:float)->float:
    """Expected time in system under IDEAL M/M/1 stationarity: Poisson arrivals, exponential service."""
    if arrival<0 or service<=0 or arrival>=service:raise ValueError('unstable or invalid M/M/1')
    return 1/(service-arrival)


def mission_recovery_area(times:list[float],service_fractions:list[float])->float:
    """Trapezoidal integral of lost service fraction over time; units are service-hours if time in hours."""
    if len(times)!=len(service_fractions) or len(times)<2:raise ValueError('need paired points')
    if any(times[i+1]<=times[i] for i in range(len(times)-1)):raise ValueError('times must increase')
    if any(not 0<=x<=1 for x in service_fractions):raise ValueError('fractions outside [0,1]')
    return sum((times[i+1]-times[i])*(2-service_fractions[i]-service_fractions[i+1])/2 for i in range(len(times)-1))


def diff_in_diff(pre_t:float,post_t:float,pre_c:float,post_c:float)->float:
    """Difference-in-differences of four mean outcomes; causal inference requires parallel trends etc."""
    return (post_t-pre_t)-(post_c-pre_c)

if __name__=='__main__':
    print('Posterior for route obstruction after alarm:',round(bayes_positive(.05,.9,.15),3))
    print('Minimal cut sets:',minimal_cut_sets([['bus','hospital','city_radio'],['paratransit','hospital','backup_radio']]))
    print('Staff trajectory:',stock_flow(120,[15,18,23,25],[22,21,19,18]))
    print('M/M/1 system time at arrival 9, service 10:',queue_mm1_system_time(9,10),'hours')
    print('Subgroup rate:',subgroup_rate([(855,900),(50,100)]))
