"""Simple transparent test calculations; not a statistical qualification plan."""
import math

def zero_failure_upper_bound(n,confidence=.95):
    """One-sided Clopper-Pearson bound for zero failures in IID Bernoulli trials."""
    if n<=0 or not 0<confidence<1: raise ValueError('invalid n or confidence')
    return 1-(1-confidence)**(1/n)

def nearest_rank_percentile(observations,percentile):
    """Descriptive empirical statistic, NOT a confidence bound on population percentile."""
    if not observations or not 0<percentile<=1:raise ValueError('invalid sample or percentile')
    vals=sorted(observations)
    return vals[math.ceil(percentile*len(vals))-1]

def pass_fraction(outcomes):
    if not outcomes: raise ValueError('empty outcomes')
    return sum(1 for x in outcomes if x)/len(outcomes)

if __name__=='__main__':
    print('0 failures /100: bound',zero_failure_upper_bound(100))
    print('p99 descriptive:',nearest_rank_percentile([320,510,590,720,860],.99))
