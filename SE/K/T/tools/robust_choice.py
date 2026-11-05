"""Enumerate hard constraints; do not use scoring to override infeasibility."""
def evaluate(options, service_min=10, energy_cap=30, service_multiplier=1):
    if service_min<0 or energy_cap<0 or service_multiplier<0: raise ValueError('invalid constraints')
    out=[]
    for name,service,energy,cost in options:
        out.append(dict(name=name,service=service*service_multiplier,energy=energy,cost=cost,
                        feasible=(service*service_multiplier>=service_min and energy<=energy_cap)))
    return out

if __name__=='__main__':
    options=[('A',6,12,2),('B',12,24,4),('C',18,36,5)]
    for multiplier in (1,2/3):print(multiplier,evaluate(options,service_multiplier=multiplier))
