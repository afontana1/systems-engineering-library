"""Toy integer fleet and scalar discrete-time feedback controller."""
def fleet_options(required=24,min_accessible=2,budget=None,max_count=20):
    assert required>=0 and min_accessible>=0 and max_count>=0
    ans=[]
    for ordinary in range(max_count+1):
        for accessible in range(min_accessible,max_count+1):
            capacity=4*ordinary+3*accessible; cost=2*ordinary+3*accessible
            if capacity>=required and (budget is None or cost<=budget):
                ans.append((cost,ordinary,accessible,capacity))
    return sorted(ans)
def scalar_path(a,b,gain,e0,steps,disturbance=0):
    assert steps>=0
    path=[float(e0)]
    for _ in range(steps): path.append((a-b*gain)*path[-1]+disturbance)
    return path
def scalar_stable(a,b,gain):return abs(a-b*gain)<1
