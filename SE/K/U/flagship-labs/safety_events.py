"""Conditional event-tree arithmetic, not hazard acceptance criteria."""
def chain_probability(conditional_probabilities):
    import math
    assert conditional_probabilities and all(0<=p<=1 for p in conditional_probabilities)
    return math.prod(conditional_probabilities)
def expected_direct_loss(events):
    assert all(0<=p<=1 and c>=0 for p,c in events)
    return sum(p*c for p,c in events)
def probability_sensitivity(initiation, detection_failures, recovery_failure):
    return [(p,chain_probability((initiation,p,recovery_failure))) for p in detection_failures]
