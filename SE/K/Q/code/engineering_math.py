"""Independent teaching calculations for the quantitative methods companion.
Units and sampling assumptions are documented in the book; models are instructional.
"""
import math
import heapq

def poisson_zero(rate, hours):
    if rate < 0 or hours < 0: raise ValueError("nonnegative input required")
    return math.exp(-rate * hours)

def posterior_gamma_mean(shape, rate, arrivals, exposure):
    if shape <= 0 or rate <= 0 or arrivals < 0 or exposure < 0: raise ValueError("invalid Gamma or exposure")
    return (shape + arrivals) / (rate + exposure)

def zero_failure_upper(n, confidence=.95):
    if n < 1 or not 0 < confidence < 1: raise ValueError("invalid sample or confidence")
    return 1-(1-confidence)**(1/n)

def mm1(arrivals_per_hour, service_per_hour):
    if arrivals_per_hour < 0 or service_per_hour <= arrivals_per_hour: raise ValueError("requires 0<=lambda<mu")
    util=arrivals_per_hour/service_per_hour
    w=1/(service_per_hour-arrivals_per_hour)
    wq=arrivals_per_hour/(service_per_hour*(service_per_hour-arrivals_per_hour))
    return dict(utilization=util, minutes_in_system=60*w, minutes_in_queue=60*wq)

def factorial_effects(low_old,low_new,high_old,high_new):
    effect_a=((high_old+high_new)-(low_old+low_new))/2
    effect_b=((low_new+high_new)-(low_old+high_old))/2
    interaction=high_new-high_old-low_new+low_old
    return (effect_a,effect_b,interaction,interaction/4)

def euler_decay(x0,k,h,steps):
    if h<=0 or steps<0 or k<0: raise ValueError("invalid step")
    x=float(x0)
    for _ in range(steps): x+=h*(-k*x)
    return x

def decay_exact(x0,k,t):
    return x0*math.exp(-k*t)

def control_multiplier(a,b,gain,h):
    if h<=0: raise ValueError("positive step required")
    return 1-h*(a+b*gain)

def expected_values(disruption_probability):
    p=disruption_probability
    if not 0<=p<=1:raise ValueError("invalid probability")
    a=100*(1-p)+20*p
    b=75*(1-p)+60*p
    perfect=100*(1-p)+60*p
    return dict(A=a,B=b,EVPI=perfect-max(a,b),prefer='A' if a>=b else 'B')

def linear_uncertainty(sigma_a,sigma_b,cov=0):
    # y = 2a + b. cov is covariance in a*b units.
    var=4*sigma_a**2+sigma_b**2+4*cov
    if var<0: raise ValueError("inconsistent covariance")
    return math.sqrt(var)

def deterministic_queue(arrivals, service_minutes):
    if service_minutes <= 0: raise ValueError('positive service required')
    free_at=0
    out=[]
    for t in arrivals:
        if t < 0: raise ValueError('nonnegative times')
        start=max(t,free_at)
        finish=start+service_minutes
        out.append(dict(arrival=t,start=start,finish=finish,wait=start-t))
        free_at=finish
    return out
