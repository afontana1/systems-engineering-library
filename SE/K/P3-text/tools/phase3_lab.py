"""Phase 3 teaching lab: transparent illustrative mathematics and models.

Standard library only. These examples are neither field-calibrated nor
appropriate for safety or certification decisions. Python 3.10+ recommended.
Run: python phase3_lab.py [demo]
"""
from __future__ import annotations
import csv
import heapq
import math
import random
import statistics
import sys
from dataclasses import dataclass
from pathlib import Path


def mean_interval_normal(data: list[float], z: float = 1.96):
    """Large-sample approx. CI for population mean under independent sampling.
    Use a t-critical value or bootstrap for small samples; this isn't a prediction interval.
    """
    if len(data) < 2: raise ValueError('need >=2 samples')
    mean = statistics.mean(data)
    se = statistics.stdev(data) / math.sqrt(len(data))
    return mean - z*se, mean, mean + z*se


def factorial_2x2(y_minus_minus, y_plus_minus, y_minus_plus, y_plus_plus):
    """Effects are changes on switching factor between - and + averaged over the other.
    Interaction is difference of B effects at A+ vs A-, divided by 2.
    """
    a = ((y_plus_minus+y_plus_plus)-(y_minus_minus+y_minus_plus))/2
    b = ((y_minus_plus+y_plus_plus)-(y_minus_minus+y_plus_minus))/2
    interaction = (y_plus_plus-y_plus_minus-y_minus_plus+y_minus_minus)/2
    return {'A_effect':a, 'B_effect':b, 'AB_effect':interaction}


def correlated_sum_mc(n=10000, rho=0.0, seed=73, mu1=12.0, sd1=2.0, mu2=3.0, sd2=1.0):
    """Joint normal illustrative model; rho∈[-1,1]. Normal can be unphysical for durations.
    For real durations, use bounded/positive distributions and scenario validated inputs.
    """
    if n<2 or not -1 <= rho <= 1:raise ValueError('invalid n or rho')
    r=random.Random(seed)
    vals=[]
    for _ in range(n):
        z1,z2=r.gauss(0,1),r.gauss(0,1)
        vals.append(mu1+sd1*z1 + mu2+sd2*(rho*z1+math.sqrt(max(0,1-rho*rho))*z2))
    vals.sort()
    return {'mean':statistics.mean(vals),'sd':statistics.stdev(vals),
            'p95':vals[math.ceil(.95*n)-1], 'analytic_sd':math.sqrt(sd1**2+sd2**2+2*rho*sd1*sd2)}


def mm1_metrics(lam:float, mu:float):
    """Ideal infinite-capacity stationary M/M/1 queue: Poisson arrivals,
    exponential service, independent sources, 0<=lambda<mu.
    Returns rho, L, Lq, W, Wq; W is hours if rates are per hour.
    """
    if not (0<=lam<mu):raise ValueError('stable M/M/1 needs 0<=lambda<mu')
    rho=lam/mu
    return {'rho':rho,'L':lam/(mu-lam),'Lq':lam*lam/(mu*(mu-lam)),
            'W':1/(mu-lam),'Wq':lam/(mu*(mu-lam))}


def deterministic_queue(arrivals:list[float], service_min:float):
    """FCFS single-server discrete-event equivalent for supplied arrival times.
    Returns per-rider waits and finish times; deterministic service, no reneging.
    """
    if service_min<=0 or arrivals!=sorted(arrivals):raise ValueError('invalid service or unsorted arrivals')
    finish=0.0; waits=[]; departures=[]
    for t in arrivals:
        start=max(finish,t);waits.append(start-t)
        finish=start+service_min;departures.append(finish)
    return {'waits':waits,'departures':departures,'mean_wait':statistics.mean(waits) if waits else 0.0}


def des_queue(arrivals:list[float], service_times:list[float]):
    """Discrete event calendar with explicit arrival/departure order.
    A departure at time t occurs before an arrival at the same t (tie-break).
    """
    if arrivals!=sorted(arrivals) or len(arrivals)!=len(service_times) or any(s<=0 for s in service_times):
        raise ValueError('invalid inputs')
    calendar=[];busy=False; waiting=[]; completed={}; starts={}
    for i,t in enumerate(arrivals):heapq.heappush(calendar,(t,1,i,'arrival'))
    while calendar:
        t,_,i,etype=heapq.heappop(calendar)
        if etype=='arrival':
            waiting.append(i)
        else:
            busy=False;completed[i]=t
        if not busy and waiting:
            j=waiting.pop(0);starts[j]=t;busy=True
            heapq.heappush(calendar,(t+service_times[j],0,j,'departure'))
    return {'starts':[starts[i] for i in range(len(arrivals))],
            'departures':[completed[i] for i in range(len(arrivals))],
            'waits':[starts[i]-arrivals[i] for i in range(len(arrivals))]}


def stock_flow(initial:float, arrivals_per_hour:float, capacity_per_hour:float, step_h=0.1, hours=8):
    """Explicit Euler example, bounded departure flow; nonnegative backlog."""
    if min(initial,arrivals_per_hour,capacity_per_hour)<0 or step_h<=0 or hours<0:raise ValueError('invalid inputs')
    result=[(0.0,float(initial))]; stock=float(initial); t=0.0
    while t < hours-1e-12:
        dt=min(step_h,hours-t)
        incoming=arrivals_per_hour*dt
        departed=min(stock+incoming,capacity_per_hour*dt)
        stock=stock+incoming-departed
        t+=dt;result.append((t,stock))
    return result


def euler_cooling(t0_c=50, ambient_c=20, k_per_min=.1, step_min=.5, minutes=10):
    """Euler cooling and analytical reference; stable for small step*k."""
    if k_per_min<0 or step_min<=0 or minutes<0:raise ValueError('invalid inputs')
    t=0.;temp=float(t0_c);trajectory=[(0.,temp)]
    while t<minutes-1e-12:
        dt=min(step_min,minutes-t)
        temp+=dt*(-k_per_min*(temp-ambient_c));t+=dt;trajectory.append((t,temp))
    exact=ambient_c+(t0_c-ambient_c)*math.exp(-k_per_min*minutes)
    return {'Euler':temp,'exact':exact,'abs_error':abs(temp-exact),'trajectory':trajectory}


def pareto_min(points:list[tuple[float,...]]):
    """Indices of nondominated points for all-objectives-minimization."""
    if not points or len({len(p) for p in points})!=1:raise ValueError('nonempty same-dimensional points needed')
    return [i for i,p in enumerate(points) if not any(
        all(qk<=pk for qk,pk in zip(q,p)) and any(qk<pk for qk,pk in zip(q,p))
        for j,q in enumerate(points) if j!=i)]


def expected_value_and_evpi(payoffs:list[list[float]], probabilities:list[float]):
    """payoffs[action][state], higher better. Returns best no-info action and EVPI."""
    if not payoffs or not probabilities or any(len(row)!=len(probabilities) for row in payoffs):
        raise ValueError('invalid payoffs')
    if any(x<0 for x in probabilities) or abs(sum(probabilities)-1)>1e-9:raise ValueError('invalid probabilities')
    evs=[sum(p*x for p,x in zip(probabilities,row)) for row in payoffs]
    perfect=sum(p*max(row[s] for row in payoffs) for s,p in enumerate(probabilities))
    best=max(range(len(evs)),key=evs.__getitem__)
    return {'expected_values':evs, 'best_action_index':best,'perfect_information_value':perfect,
            'EVPI':perfect-evs[best]}


def sample_cost_npv(initial_cost:float, annual_savings:float, years:int, discount:float):
    """Constant end-of-year cash flow, all in same currency year."""
    if years<0 or discount<=-1:raise ValueError('invalid years/discount')
    return -initial_cost+sum(annual_savings/((1+discount)**t) for t in range(1,years+1))


def write_demo_csv(path):
    """Write paired synthetic experiment fixtures (not observational evidence)."""
    out=Path(path);out.parent.mkdir(parents=True,exist_ok=True)
    r=random.Random(2026)
    with out.open('w',newline='',encoding='utf-8') as f:
        wr=csv.writer(f);wr.writerow(['replication','scenario','fleet','arrival_rate_hr','mean_wait_min'])
        for seed in range(1,13):
            demand=r.uniform(9,19)
            for fleet in (2,3):
                wait=max(0, 2.5+(demand-10)*1.3-(fleet-2)*3+r.gauss(0,.45))
                wr.writerow([seed,'synthetic peak',fleet,f'{demand:.3f}',f'{wait:.3f}'])
    return out


def demo():
    print('Phase 3 illustrative learning lab — not decision-grade evidence')
    print('normal-approx CI',mean_interval_normal([7,8,9,10,11,12]))
    print('2x2 factorial effects',factorial_2x2(14,12,18,11))
    print('correlated time',correlated_sum_mc(n=2000,rho=.6))
    print('M/M/1 queue',mm1_metrics(8,12))
    print('DES queue',des_queue([0,1,2],[3,3,3]))
    print('stock at 4h',stock_flow(5,8,10,hours=4)[-1])
    print('cooling', {k:v for k,v in euler_cooling().items() if k!='trajectory'})
    print('Pareto',pareto_min([(900,15),(1000,12),(1100,14)]))
    print('decision',expected_value_and_evpi([[50,-20],[25,25]],[.5,.5]))
    print('NPV',round(sample_cost_npv(25000,9000,4,.05),2))

if __name__=='__main__':
    demo()
