"""Book 12: deterministic teaching calculations, not operational validation."""
import math

def queue_mm1(arrival,service):
    if arrival<0 or service<=arrival:raise ValueError('Require 0 <= arrival < service')
    return 1/(service-arrival)

def exact_zero_failure_upper(n,alpha=.05):
    if n<1 or not 0<alpha<1:raise ValueError('Invalid sample or alpha')
    return 1-alpha**(1/n)

def euler_decay(rate,step,steps,x0=1.0):
    if step<=0 or steps<0:raise ValueError('invalid time step')
    xs=[x0]
    for _ in range(steps):xs.append(xs[-1]+step*(-rate*xs[-1]))
    return xs

def weighted_switch():
    return (0.9-0.6)/(0.2+0.4)

def test():
    assert abs(queue_mm1(8,10)-0.5)<1e-12
    assert abs(exact_zero_failure_upper(30)-0.09503385285530419)<1e-8
    assert abs(euler_decay(2,.2,2)[-1]-.36)<1e-12
    assert abs(weighted_switch()-.5)<1e-12
    for fn, args in [(queue_mm1,(3,3)),(exact_zero_failure_upper,(0,))]:
        try:fn(*args);raise AssertionError('Must reject invalid input')
        except ValueError:pass
    return True
if __name__=='__main__':
    test();print('all 6 checks passed')
