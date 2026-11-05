"""Conservation, Euler, M/M/1 reference models: illustrative, not calibrated."""
import math


def backlog(initial, arrivals_per_hour, completions_per_hour, hours, abandonments=0):
    if min(initial, arrivals_per_hour, completions_per_hour, hours, abandonments)<0:
        raise ValueError('Inputs must be nonnegative')
    final=initial+(arrivals_per_hour-completions_per_hour)*hours-abandonments
    if final<0: raise ValueError('Requested departures exceed stock; model needs flow constraint')
    return final


def euler_decay(k, h, steps, initial=1.0):
    if k<0 or h<=0 or steps<0 or not isinstance(steps,int):
        raise ValueError('Invalid integration parameters')
    x=initial
    for _ in range(steps):x+=h*(-k*x)
    return x


def mm1(lam,mu):
    if not (0<=lam<mu):raise ValueError('Stable M/M/1 requires 0 <= arrival rate < service rate')
    return {'utilization':lam/mu, 'mean_queue_hours':lam/(mu*(mu-lam)),
            'mean_system_hours':1/(mu-lam), 'mean_system_jobs':lam/(mu-lam)}


def min_service_rate_for_queue_wait(lam, max_wait_hours):
    if lam<0 or max_wait_hours<=0:
        raise ValueError('Require nonnegative arrival rate and positive wait bound')
    # lam / (mu * (mu-lam)) = max_wait_hours, positive root.
    return (lam+math.sqrt(lam*lam+4*lam/max_wait_hours))/2 if lam>0 else 0


def resilience_loss(target, observed, duration_hours):
    if duration_hours<0:raise ValueError('Duration must be nonnegative')
    return max(0,target-observed)*duration_hours

if __name__=='__main__':
    print('Backlog after 2h',backlog(4,12,9,2))
    print('Euler x(1)',euler_decay(1,.25,4),'exact',math.exp(-1))
    print('M/M/1',mm1(12,15))
    print('Capacity needed',min_service_rate_for_queue_wait(12,1/12))
