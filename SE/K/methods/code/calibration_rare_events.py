#!/usr/bin/env python3
"""Synthetic Poisson-rate calibration and importance sampling for a Gaussian rare event.
Only the Python standard library is required. All observations and assumptions are educational.
"""
from __future__ import annotations
import csv, math, random
from pathlib import Path

DATA=Path(__file__).resolve().parents[1]/'data'/'calibration_counts.csv'


def poisson_log_likelihood(count: int, exposure_h: float, rate_h: float) -> float:
    if count < 0 or exposure_h <= 0 or rate_h <= 0: raise ValueError('invalid count/exposure/rate')
    return count*math.log(rate_h)-exposure_h*rate_h


def profile_interval(count: int, exposure_h: float, cutoff: float=3.841458820694124) -> tuple[float,float]:
    """Asymptotic 95% profile LR interval, for positive count only (chi-square 1 df cutoff)."""
    if count <= 0 or exposure_h <= 0: raise ValueError('this example requires positive events and exposure')
    mle=count/exposure_h
    top=poisson_log_likelihood(count,exposure_h,mle)
    def dev(rate):return 2*(top-poisson_log_likelihood(count,exposure_h,rate))
    low,high=1e-12,mle
    for _ in range(90):
        mid=(low+high)/2
        if dev(mid)>cutoff:low=mid
        else:high=mid
    lower=(low+high)/2
    low,high=mle,max(mle*2,1)
    while dev(high)<cutoff:high*=2
    for _ in range(90):
        mid=(low+high)/2
        if dev(mid)>cutoff:high=mid
        else:low=mid
    return lower,(low+high)/2


def poisson_upper_tail(k: int, mean: float) -> float:
    """P(X >= k) computed via the finite lower tail, for moderate means only."""
    if k<0 or mean<0: raise ValueError('invalid tail parameters')
    if k==0:return 1.0
    term=math.exp(-mean)
    cdf=term
    for j in range(1,k):
        term*=mean/j;cdf+=term
    return max(0.0,min(1.0,1-cdf))


def calibrate(path: Path=DATA):
    with path.open(newline='',encoding='utf-8') as f:rows=list(csv.DictReader(f))
    calibration=[r for r in rows if r['split']=='calibration']
    holdouts=[r for r in rows if r['split']=='holdout']
    n=sum(int(r['arrivals']) for r in calibration)
    t=sum(float(r['exposure_hours']) for r in calibration)
    rate=n/t
    lo,hi=profile_interval(n,t)
    withheld=[(int(r['arrivals']),float(r['exposure_hours'])) for r in holdouts]
    return {'count':n,'hours':t,'rate':rate,'profile_interval':(lo,hi),
            'holdout':[(k,h,poisson_upper_tail(k,rate*h)) for k,h in withheld]}


def naive_normal_tail(threshold:float,draws:int=50000,seed:int=156):
    rng=random.Random(seed)
    hits=sum(rng.gauss(0,1)>threshold for _ in range(draws))
    return hits/draws,hits


def importance_normal_tail(threshold:float=4.0,shift:float=4.0,draws:int=50000,seed:int=156):
    """Importance sample X~N(shift,1); E_q[1(X>t)*phi(X)/q(X)]."""
    if draws<2:raise ValueError('need >=2 draws')
    rng=random.Random(seed)
    contributions=[]
    for _ in range(draws):
        x=rng.gauss(shift,1)
        contributions.append(math.exp(-shift*x+shift*shift/2) if x>threshold else 0.0)
    mean=sum(contributions)/draws
    s2=sum((x-mean)**2 for x in contributions)/(draws-1)
    return mean,math.sqrt(s2/draws)


def main():
    c=calibrate();p_true=.5*math.erfc(4/math.sqrt(2))
    p_naive,hits=naive_normal_tail(4)
    p_is,se=importance_normal_tail()
    print(f"calibration n={c['count']} exposure={c['hours']:g} h MLE={c['rate']:.4f}/h")
    print('95% approximate profile-LR interval: [{:.4f}, {:.4f}]/h'.format(*c['profile_interval']))
    for k,h,p in c['holdout']:
        print(f'holdout: {k} arrivals/{h:g}h; modeled P(N >= {k})={p:.4f}')
    print(f'normal P(Z>4) exact={p_true:.8f}; naive={p_naive:.8f} ({hits} hits)')
    print(f'importance sampling={p_is:.8f}, MC standard error={se:.8f}')

if __name__=='__main__':main()
