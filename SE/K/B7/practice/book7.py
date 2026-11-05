"""Independent teaching model — synthetic inputs and simplified assumptions."""
from math import exp, log

def latency_path(serial, parallel, end, retry=0):
    if min(*serial, *parallel, end, retry) < 0:
        raise ValueError('domain')
    return sum(serial) + max(parallel) + end + retry

def series_availability(values):
    out = 1
    for v in values:
        if v < 0 or v > 1:
            raise ValueError('domain')
        out *= v
    return out

def parallel_availability(a, common_cause=0):
    if not 0 <= a <= 1 or not 0 <= common_cause <= 1:
        raise ValueError('domain')
    return (1 - common_cause) * (1 - (1 - a) ** 2)

if __name__ == '__main__':
    print('latency (ms)',latency_path([120],[200,150],80)); print('series',series_availability([.99,.98,.995])); print('parallel common cause',parallel_availability(.98,.01))
