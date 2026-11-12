#!/usr/bin/env python3
"""Analytic delta method and Monte Carlo for correlated distance/speed inputs.

Synthetic inputs only; Python standard library. Rejection at nonphysical values
is visible and counted, not silently replaced by a positive number.
"""
from __future__ import annotations
from math import sqrt
from random import Random


def delta_time(*, mean_distance=120.0, sd_distance=6.0,
               mean_speed=12.0, sd_speed=1.2, rho=-0.6) -> tuple[float,float]:
    if mean_speed <= 0 or min(sd_distance,sd_speed)<0 or abs(rho)>1:
        raise ValueError('Invalid parameters')
    dd=1/mean_speed
    dv=-mean_distance/mean_speed**2
    covariance=rho*sd_distance*sd_speed
    variance=(dd*sd_distance)**2+(dv*sd_speed)**2+2*dd*dv*covariance
    return mean_distance/mean_speed,sqrt(max(0,variance))


def quantile(sorted_values:list[float], p:float) -> float:
    if not 0<=p<=1 or not sorted_values:raise ValueError('Invalid quantile')
    pos=(len(sorted_values)-1)*p
    lo=int(pos);hi=min(lo+1,len(sorted_values)-1)
    if lo==hi:return sorted_values[lo]
    return sorted_values[lo]*(hi-pos)+sorted_values[hi]*(pos-lo)


def sample_times(*, rho=-.6, n=100000, seed=74301, threshold=12.0) -> dict:
    if abs(rho)>1 or n<100:raise ValueError('Require valid correlation and sample size')
    rng=Random(seed)
    vals=[];rejected=0
    while len(vals)<n:
        z1,z2=rng.gauss(0,1),rng.gauss(0,1)
        distance=120+6*z1
        speed=12+1.2*(rho*z1+sqrt(1-rho*rho)*z2)
        if distance<=0 or speed<=0:
            rejected+=1
            continue
        vals.append(distance/speed)
    vals.sort()
    avg=sum(vals)/n
    variance=sum((v-avg)**2 for v in vals)/(n-1)
    count=sum(v>threshold for v in vals)
    p=count/n
    return {'mean':avg,'sd':sqrt(variance),'p_exceed':p,
            'p_exceed_mc_se':sqrt(p*(1-p)/n),
            'q05':quantile(vals,.05),'q50':quantile(vals,.5),'q95':quantile(vals,.95),
            'rejected':rejected,'n':n}


if __name__=='__main__':
    for rho in (-.6,0):
        print('rho',rho,'delta nominal/stdev',delta_time(rho=rho))
        print(sample_times(rho=rho))
