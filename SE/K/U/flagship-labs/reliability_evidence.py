"""Exact zero-event bounds under Bernoulli assumptions; simplified reliability logic."""
import math


def zero_failure_upper(n, confidence=.95):
    if not isinstance(n,int) or n<=0 or not 0<confidence<1:
        raise ValueError('n positive integer and 0 < confidence < 1')
    return -math.expm1(math.log1p(-confidence)/n)


def zero_failure_sample_size(target_failure, confidence=.95):
    if not 0<target_failure<1 or not 0<confidence<1:
        raise ValueError('Probabilities must be strictly between zero and one')
    # Correct rounding for exact floating threshold.
    n = math.ceil(math.log1p(-confidence)/math.log1p(-target_failure))
    while n>1 and zero_failure_upper(n-1,confidence)<=target_failure:
        n-=1
    while zero_failure_upper(n,confidence)>target_failure:
        n+=1
    return n


def series_reliability(*r):
    if any(not 0<=x<=1 for x in r):
        raise ValueError('Reliability must lie in [0,1]')
    return math.prod(r)


def two_channel_redundancy(channel_failure_probability, common_cause_failure_probability=0):
    p,q=channel_failure_probability,common_cause_failure_probability
    if not (0<=p<=1 and 0<=q<=1):raise ValueError('Probabilities must lie in [0,1]')
    return (1-q)*(1-p*p)


def exponential_survival(failure_rate_per_hour, exposure_hours):
    if failure_rate_per_hour<0 or exposure_hours<0:
        raise ValueError('Nonnegative rate and duration required')
    return math.exp(-failure_rate_per_hour*exposure_hours)


def beta_posterior_mean(prior_a, prior_b, failures, trials):
    if prior_a<=0 or prior_b<=0 or not isinstance(trials,int) or not isinstance(failures,int) or trials<0 or failures<0 or failures>trials:
        raise ValueError('Invalid Beta-binomial parameters')
    return (prior_a+failures)/(prior_a+prior_b+trials)

if __name__=='__main__':
    print('zero failures 300:',zero_failure_upper(300))
    print('n for 0.1%:',zero_failure_sample_size(.001))
    print('series:',series_reliability(.98,.99,.97))
    print('redundant with common cause:',two_channel_redundancy(.08,.02))
