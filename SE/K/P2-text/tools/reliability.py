"""Simplified reliability models; independence assumptions are substantive."""
def serial_independent(reliabilities):
    x=1.0
    for p in reliabilities:
        if not 0<=p<=1: raise ValueError('probability outside 0..1')
        x*=p
    return x

def parallel_independent(reliabilities):
    return 1-serial_independent([1-p for p in reliabilities])

def simple_common_cause(branch_reliabilities,common_cause_success):
    return serial_independent([parallel_independent(branch_reliabilities),common_cause_success])

def inherent_availability(mtbf_hours,mttr_hours):
    if mtbf_hours <= 0 or mttr_hours < 0: raise ValueError('invalid reliability interval')
    return mtbf_hours/(mtbf_hours+mttr_hours)

if __name__=='__main__':
    print('Serial:',serial_independent([.98,.98]))
    print('Idealized redundant:',parallel_independent([.98,.98]))
    print('Shared cause:',simple_common_cause([.98,.98],.99))
