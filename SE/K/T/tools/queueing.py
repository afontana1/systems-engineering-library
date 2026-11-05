"""M/M/1 ideal steady-state; do not apply to arbitrary fleet routes."""
def mm1(arrivals_per_hour: float, service_per_hour: float) -> dict:
    if arrivals_per_hour < 0 or service_per_hour <= 0: raise ValueError('invalid rate')
    if arrivals_per_hour >= service_per_hour: raise ValueError('stationary mean undefined')
    w = 1/(service_per_hour-arrivals_per_hour)
    return {'utilization': arrivals_per_hour/service_per_hour,
            'hours_in_system': w, 'mean_in_system': arrivals_per_hour*w}

if __name__ == '__main__':
    for rate in (6,8,9): print(rate,mm1(rate,10))
