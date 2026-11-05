"""First-order recovery: Euler trajectory and exact solution for comparison."""
import math

def euler(x0: float, k: float, dt: float, steps: int) -> list:
    if k < 0 or dt <= 0 or type(steps) is not int or steps < 0: raise ValueError('bad inputs')
    values=[x0]
    for _ in range(steps): values.append(values[-1]*(1-k*dt))
    return values

def exact(x0: float, k: float, time: float) -> float:
    return x0*math.exp(-k*time)

if __name__ == '__main__':
    print('Euler:',euler(10,.5,1,5),'Exact t=1:',exact(10,.5,1))
