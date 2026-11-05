"""Teaching toy models for software contracts and architecture availability.
No estimate is calibrated to a real service or safety target.
"""
def series_availability(values):
    import math
    assert values and all(0<=v<=1 for v in values)
    return math.prod(values)
def parallel_availability(values):
    import math
    assert values and all(0<=v<=1 for v in values)
    return 1-math.prod(1-v for v in values)
def common_cause_parallel(replica_availabilities,shared_outage):
    assert 0<=shared_outage<=1
    return (1-shared_outage)*parallel_availability(replica_availabilities)
def accept_event(state,version,event,new_version):
    """Simplified transition rule: events require monotone adjacent revisions."""
    allowed={'Requested':{'queue':'Pending'},'Pending':{'assign':'Assigned','cancel':'Cancelled'},'Assigned':{'cancel':'Cancelled','complete':'Completed'},'Cancelled':{},'Completed':{}}
    if new_version!=version+1 or event not in allowed.get(state,{}):return state,version,False
    return allowed[state][event],new_version,True
