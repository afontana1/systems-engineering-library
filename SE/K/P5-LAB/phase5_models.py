"""Reproducible *synthetic* teaching models for three Phase 5 books.
No function here validates a real medical, transport, or public-policy service.
"""
from itertools import combinations

def bayes_positive(prior, sensitivity, false_positive):
    """P(H|+) assuming calibrated rates for the *same defined event*."""
    if not (0 <= prior <= 1 and 0 <= sensitivity <= 1 and 0 <= false_positive <= 1):
        raise ValueError("probabilities must lie in [0,1]")
    support=prior*sensitivity
    denom=support+(1-prior)*false_positive
    if denom == 0: raise ValueError("observation has zero likelihood")
    return support/denom

def chain_availability(probabilities, independent=False):
    """Naive product is allowed only when independence is explicitly assumed."""
    if not independent: raise ValueError("independence assumption required")
    result=1.0
    for value in probabilities:
        if not 0<=value<=1: raise ValueError("probability out of range")
        result*=value
    return result

def accessible_outcomes(served_by_group,requested_by_group):
    if set(served_by_group)!=set(requested_by_group): raise ValueError("groups mismatch")
    if not served_by_group: raise ValueError("no groups")
    results={}
    for group,denom in requested_by_group.items():
        value=served_by_group[group]
        if denom<=0 or not 0<=value<=denom: raise ValueError("invalid counts")
        results[group]=value/denom
    return {"group_rates":results,"aggregate":sum(served_by_group.values())/sum(requested_by_group.values()),"gap":max(results.values())-min(results.values())}

def select_portfolio(options,budget,required=None):
    """Exhaustive 0-1 portfolio; assumes additive value unless separately modeled."""
    if budget<0: raise ValueError("budget negative")
    names=list(options); required=set(required or [])
    if not required.issubset(names): raise ValueError("unknown mandatory option")
    best=(-float('inf'),(),0)
    for count in range(len(names)+1):
        for group in combinations(names,count):
            if not required.issubset(group): continue
            cost=sum(options[name][0] for name in group)
            value=sum(options[name][1] for name in group)
            if cost<=budget and value>best[0]:best=(value,group,cost)
    if best[0]==-float('inf'): raise ValueError("no feasible portfolio")
    return {"value":best[0],"chosen":best[1],"cost":best[2]}

def workforce_next(current,qualified_hires,exits):
    if min(current,qualified_hires,exits)<0 or exits>current+qualified_hires: raise ValueError("invalid workforce")
    return current+qualified_hires-exits

def mm1_time(arrivals_per_hour,service_per_hour):
    """Hours in system under stationary M/M/1 assumptions, not field prediction."""
    if arrivals_per_hour<0 or service_per_hour<=0 or arrivals_per_hour>=service_per_hour: raise ValueError("unstable or invalid M/M/1")
    return 1/(service_per_hour-arrivals_per_hour)

def mission_reachable(graph,origin,target,disabled_edges=()):
    disabled=set(tuple(x) for x in disabled_edges); visited={origin}; queue=[origin]
    while queue:
        node=queue.pop(0)
        if node==target:return True
        for nxt in graph.get(node,[]):
            if (node,nxt) not in disabled and nxt not in visited:
                visited.add(nxt);queue.append(nxt)
    return False

def lead_time(wait_intervals,active_minutes):
    if active_minutes<0 or any(i<0 for i in wait_intervals): raise ValueError("invalid times")
    return sum(wait_intervals)+active_minutes
