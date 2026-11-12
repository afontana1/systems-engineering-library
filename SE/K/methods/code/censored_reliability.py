#!/usr/bin/env python3
"""Right-censored exponential MLE and Kaplan-Meier, standard library only.

The input comprises independent units, each with one end-of-follow-up observation.
Censoring must be justified as non-informative in any real application.
"""
from __future__ import annotations
import csv
import math
import sys
from collections import defaultdict
from pathlib import Path


def analyze(path: Path) -> dict:
    observations = []
    with path.open(newline='', encoding='utf-8') as f:
        for row in csv.DictReader(f):
            t = float(row['hours'])
            flag = int(row['failed'])
            if not math.isfinite(t) or t <= 0 or flag not in (0, 1):
                raise ValueError('Require positive finite hours and 0/1 failed flag')
            observations.append((t, flag))
    if not observations:
        raise ValueError('No observations')
    count_fail = sum(d for _, d in observations)
    exposure = sum(t for t, _ in observations)
    rate = count_fail / exposure if count_fail else None
    by_time = defaultdict(lambda: [0, 0])  # [failure, censored]
    for t, failed in observations:
        by_time[t][0 if failed else 1] += 1
    at_risk = len(observations)
    survival = 1.0
    steps = []
    for t, (fail, cens) in sorted(by_time.items()):
        if fail:
            survival *= (1 - fail / at_risk)
            steps.append((t, at_risk, fail, survival))
        at_risk -= fail + cens
        if at_risk < 0:
            raise ValueError('Invalid risk set')
    return {'units': len(observations), 'failures': count_fail,
            'censored': len(observations)-count_fail, 'exposure_hours': exposure,
            'exponential_rate_per_hour': rate, 'km': steps}


def profile_rate_interval(failures: int, exposure_hours: float,
                          cutoff: float = 3.841458820694124) -> tuple[float, float]:
    """Asymptotic LR interval under iid, noninformatively censored exponential lives.

    Uses chi-square(1) 95% cutoff by default. With few failures this is an
    approximation, not an exact-coverage interval or an acceptance decision.
    """
    if not (isinstance(failures, int) and failures > 0 and
            math.isfinite(exposure_hours) and exposure_hours > 0 and
            math.isfinite(cutoff) and cutoff > 0):
        raise ValueError('Require positive failures, exposure and cutoff')
    mle = failures / exposure_hours
    def deviance(rate):
        return 2 * (failures*math.log(mle/rate) + exposure_hours*(rate-mle))
    # Left root: deviance decreases from above cutoff to zero at MLE.
    lo, hi = mle*1e-15, mle
    for _ in range(100):
        mid = (lo+hi)/2
        if deviance(mid) > cutoff:
            lo=mid
        else:
            hi=mid
    lower=(lo+hi)/2
    # Right root: deviance increases from zero to infinity.
    lo, hi = mle, 2*mle
    while deviance(hi) < cutoff:
        hi*=2
    for _ in range(100):
        mid=(lo+hi)/2
        if deviance(mid) > cutoff:
            hi=mid
        else:
            lo=mid
    upper=(lo+hi)/2
    return lower, upper


def exponential_survival(rate: float, t: float) -> float:
    if not (math.isfinite(rate) and rate >= 0 and math.isfinite(t) and t >= 0):
        raise ValueError('Rate and mission time must be finite and nonnegative')
    return math.exp(-rate*t)


def redundant_parallel_survival(component_r: float, common_cause_probability: float = 0) -> float:
    if not (0 <= component_r <= 1 and 0 <= common_cause_probability <= 1):
        raise ValueError('Probabilities outside [0,1]')
    return (1-common_cause_probability)*(1-(1-component_r)**2)


if __name__ == '__main__':
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).parents[1]/'data/module-life-test.csv'
    result = analyze(path)
    print('Analysis:', result)
    if result['exponential_rate_per_hour'] is None:
        print('No failures: exponential MLE is at the boundary; do not claim zero hazard.')
    else:
        print('Exponential estimated survival at 50 h:', exponential_survival(result['exponential_rate_per_hour'], 50))
        print('Approximate profile rate interval:', profile_rate_interval(result['failures'], result['exposure_hours']))
    print('Two-channel survival with 5% common cause:', redundant_parallel_survival(.9, .05))
