#!/usr/bin/env python3
"""Synthetic M/M/1 queue: independent replications and paired common-random-number comparison.

Python 3 standard library only. This is verification of a simplified stochastic
example, not validation of a real transport or dispatch system.
"""
from __future__ import annotations
from dataclasses import dataclass
from math import sqrt
from random import Random


@dataclass(frozen=True)
class Estimate:
    mean_minutes: float
    standard_error_minutes: float
    halfwidth_95_minutes: float
    replications: int


def summarize(values: list[float]) -> Estimate:
    if len(values) < 2:
        raise ValueError('At least two independent replication means are required')
    n = len(values)
    avg = sum(values) / n
    variance = sum((x-avg)**2 for x in values)/(n-1)
    se = sqrt(variance/n)
    # t(.975,39) only; rather than silently using a normal approximation.
    if n != 40:
        raise ValueError('This small teaching example tabulates t critical only for 39 degrees of freedom')
    return Estimate(avg, se, 2.02269092*se, n)


def queue_means(*, rate_arrivals: float=9.0, rates_service: tuple[float,...]=(12.0,13.0),
                warmup: int=2000, measured: int=6000, seed: int=20261110,
                replications: int=40) -> dict:
    """Return independent mean times per run (hours) using coupled A/B streams.

    Each replication starts empty and uses separate arrival and service streams.
    Within a replication the two service designs share uniforms (common random
    numbers). Replications use distinct PRNG seeds and are independently drawn.
    """
    if rate_arrivals <= 0 or len(rates_service)!=2 or any(mu <= rate_arrivals for mu in rates_service):
        raise ValueError('Require stable M/M/1 queues with positive arrival and higher service rates')
    if measured < 1 or warmup < 0 or replications < 2:
        raise ValueError('Invalid replication design')
    results = {mu: [] for mu in rates_service}
    for r in range(replications):
        arrivals_rng=Random(seed+100003*r)
        service_rng=Random(seed+100003*r+17)
        clock=0.0
        previous_departure={mu:0.0 for mu in rates_service}
        total_wait={mu:0.0 for mu in rates_service}
        for j in range(warmup+measured):
            clock += arrivals_rng.expovariate(rate_arrivals)
            unit_service=service_rng.expovariate(1.0)
            for mu in rates_service:
                finish=max(clock,previous_departure[mu])+unit_service/mu
                if j >= warmup:
                    total_wait[mu] += (finish-clock)
                previous_departure[mu]=finish
        for mu in rates_service:
            results[mu].append(60.0*total_wait[mu]/measured)
    estimates={mu:summarize(results[mu]) for mu in rates_service}
    base,upgrade=rates_service[:2]
    paired=[u-b for b,u in zip(results[base], results[upgrade])]
    return {'individual':results, 'estimates':estimates,
            'difference':summarize(paired),'analytic_minutes':{mu:60.0/(mu-rate_arrivals) for mu in rates_service},
            'paired_minutes':paired}


if __name__=='__main__':
    output=queue_means()
    for mu,estimate in output['estimates'].items():
        print(f'service rate {mu:g}/hour: mean {estimate.mean_minutes:.3f} min '
              f'+/- {estimate.halfwidth_95_minutes:.3f} (95% t CI); '
              f'M/M/1 benchmark {output["analytic_minutes"][mu]:.3f} min')
    d=output['difference']
    print(f'paired upgraded-minus-baseline: {d.mean_minutes:.3f} '
          f'+/- {d.halfwidth_95_minutes:.3f} min (95% t CI)')
