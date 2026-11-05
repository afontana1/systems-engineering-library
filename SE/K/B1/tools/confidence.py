"""One-sided Wilson lower confidence bound for independent Bernoulli observations.

Requires a prespecified sampling design; not appropriate for correlated repeated simulations.
"""
from math import sqrt
from statistics import NormalDist


def wilson_lower(successes, trials, confidence=0.95):
    if not (isinstance(successes, int) and isinstance(trials, int) and 0 <= successes <= trials and trials>0):
        raise ValueError('Require integer 0 <= successes <= trials, trials positive')
    if not 0.5 < confidence < 1:
        raise ValueError('One-sided confidence must be in (0.5, 1)')
    z = NormalDist().inv_cdf(confidence)
    p = successes / trials
    return (p + z*z/(2*trials) - z*sqrt(p*(1-p)/trials + z*z/(4*trials**2))) / (1+z*z/trials)


if __name__=='__main__':
    print('Observed = 99.2%; one-sided 95% Wilson lower =',round(100*wilson_lower(992, 1000),3),'%')
