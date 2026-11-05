"""Toy mission throughput model, not a service guarantee."""
def cycles(vehicles, minutes, availability, cycle_minutes):
    if vehicles < 0 or minutes < 0 or not 0 <= availability <= 1 or cycle_minutes <= 0:
        raise ValueError('invalid throughput assumptions')
    return vehicles * minutes * availability / cycle_minutes

def boardings(vehicles, minutes, availability, cycle_minutes, mean_riders_per_cycle):
    if mean_riders_per_cycle < 0: raise ValueError('riders must be nonnegative')
    return cycles(vehicles, minutes, availability, cycle_minutes) * mean_riders_per_cycle

if __name__=='__main__':
    print('Illustrative cycles/day:',cycles(2,480,.85,24))
    print('Illustrative boardings/day:',boardings(2,480,.85,24,3))
