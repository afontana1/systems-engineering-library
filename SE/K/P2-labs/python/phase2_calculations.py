"""Reproducible teaching calculations for Phase 2. Not approved design tools."""
from math import ceil

def latency_budget(*segments,deadline):
    if deadline<=0 or any(v<0 for v in segments): raise ValueError('Invalid timing')
    total=sum(segments)
    return {'nominal_s':total,'margin_s':deadline-total,'meets_nominal':total<=deadline}

def energy_window(vehicles,kwh_per_vehicle,usable_kw):
    if vehicles<0 or kwh_per_vehicle<0 or usable_kw<=0: raise ValueError('Invalid energy inputs')
    return vehicles*kwh_per_vehicle/usable_kw

def throughput_backlog(arrivals_per_hour,service_per_hour,hours):
    if min(arrivals_per_hour,service_per_hour,hours)<0:raise ValueError('Negative demand')
    return max(0.,(arrivals_per_hour-service_per_hour)*hours)

def series_reliability(probabilities):
    from math import prod
    if any(not 0<=p<=1 for p in probabilities): raise ValueError('Probability outside [0,1]')
    return prod(probabilities)

def intrinsic_availability(mtbf_h,mttr_h):
    if mtbf_h<=0 or mttr_h<0:raise ValueError('Invalid repair times')
    return mtbf_h/(mtbf_h+mttr_h)

def zero_failure_upper(n,alpha=0.05):
    if n<1 or not 0<alpha<1:raise ValueError('Invalid sample or alpha')
    return 1-alpha**(1/n)

def weighted_value(values,weights):
    if len(values)!=len(weights) or not values:raise ValueError('Dimension mismatch')
    if any(not 0<=v<=1 for v in values) or any(w<0 for w in weights):raise ValueError('Scale error')
    if abs(sum(weights)-1)>1e-9:raise ValueError('Weights must sum to 1')
    return sum(v*w for v,w in zip(values,weights))

def mean(values):
    if not values:raise ValueError('Empty list')
    return sum(values)/len(values)

def nearest_rank(values,p):
    if not values or not 0<p<=1:raise ValueError('Invalid percentile input')
    v=sorted(values)
    return v[max(0,ceil(p*len(v))-1)]

def coverage(claim_to_tests):
    if not claim_to_tests:raise ValueError('Missing claims')
    good=sum(bool(tests) for tests in claim_to_tests.values())
    return good/len(claim_to_tests)

def compare_decision(first,second,uncertainty):
    if uncertainty<0:raise ValueError('Negative uncertainty')
    return {'nominal_margin':first-second,'robust_order': 'first' if first-second>uncertainty else 'second' if second-first>uncertainty else 'unresolved'}
