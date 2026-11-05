"""Ideal exponential reliability and independent series/parallel components."""
import math

def mission_reliability(mtbf_hours, mission_hours):
    if mtbf_hours<=0 or mission_hours<0: raise ValueError('invalid duration')
    return math.exp(-mission_hours/mtbf_hours)

def availability(mtbf,mttr):
    if mtbf<=0 or mttr<0: raise ValueError('invalid time')
    return mtbf/(mtbf+mttr)

def series(*r):
    if not r or any(not 0<=v<=1 for v in r): raise ValueError('invalid reliability')
    return math.prod(r)

def parallel(*r):
    if not r or any(not 0<=v<=1 for v in r): raise ValueError('invalid reliability')
    return 1-math.prod(1-v for v in r)

if __name__=='__main__': print(mission_reliability(500,10),availability(500,5),series(.95,.95),parallel(.95,.95))
