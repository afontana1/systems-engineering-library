"""Independent teaching model — synthetic inputs and simplified assumptions."""
from math import exp, log

def charging_feasible(vehicles, kwh_per_vehicle, chargers, kw, hours, efficiency=0.85):
    if min(vehicles, kwh_per_vehicle, chargers, kw, hours, efficiency) < 0 or efficiency > 1:
        raise ValueError('domain')
    demand = vehicles * kwh_per_vehicle
    supply = chargers * kw * hours * efficiency
    return {'demand_kwh': demand, 'supply_kwh': supply, 'margin_kwh': supply - demand, 'feasible': supply >= demand}

def regret_matrix(losses):
    """losses: dict of alternative -> sequence of scenario losses; smaller better."""
    if not losses or len({len(v) for v in losses.values()}) != 1:
        raise ValueError('dimensions')
    n = len(next(iter(losses.values())))
    if n == 0:
        raise ValueError('empty')
    mins = [min((v[i] for v in losses.values())) for i in range(n)]
    return {k: [v[i] - mins[i] for i in range(n)] for k, v in losses.items()}

def expected_losses(losses, scenario_probabilities):
    if abs(sum(scenario_probabilities) - 1) > 1e-09 or any((p < 0 for p in scenario_probabilities)):
        raise ValueError('probabilities')
    if any((len(v) != len(scenario_probabilities) for v in losses.values())):
        raise ValueError('dimensions')
    return {k: sum((p * x for p, x in zip(scenario_probabilities, v))) for k, v in losses.items()}

if __name__ == '__main__':
    print('energy',charging_feasible(4,12,2,7,3)); losses={'A':[25,75],'B':[38,45],'C':[40,40]}; print('expected',expected_losses(losses,[.75,.25])); print('regret',regret_matrix(losses))
