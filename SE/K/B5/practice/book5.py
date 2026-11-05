"""Independent teaching model — synthetic inputs and simplified assumptions."""
from math import exp, log

def independent_retry_success(p_failure, attempts):
    if not 0 <= p_failure <= 1 or attempts < 1 or int(attempts) != attempts:
        raise ValueError('domain')
    return 1 - p_failure ** attempts

def retry_load(arrival_rate, p_failure, attempts):
    """Expected attempts/request for independent failures and capped retry count."""
    if arrival_rate < 0:
        raise ValueError('arrival rate')
    independent_retry_success(p_failure, attempts)
    return arrival_rate * sum((p_failure ** i for i in range(attempts)))

def mm1_metrics(lam, mu):
    if lam < 0 or mu <= lam:
        raise ValueError('unstable or invalid queue')
    return {'utilization': lam / mu, 'mean_hours': 1 / (mu - lam), 'p95_hours': -log(0.05) / (mu - lam)}

if __name__ == '__main__':
    print('retry success',independent_retry_success(.15,3)); print('attempts/s',retry_load(100,.15,3)); print('queue',mm1_metrics(8,10))
