"""Brute-force portfolio exploration for small teaching inputs."""
def optimize_portfolio(items,budget,dependencies=()):
    """items is mapping name -> (cost,benefit); dependencies (dependent, prerequisite)."""
    assert budget>=0 and len(items)<=20
    names=list(items); choices=[]
    for mask in range(1<<len(names)):
        selected={name for j,name in enumerate(names) if mask>>j&1}
        if any(dep in selected and pre not in selected for dep,pre in dependencies):continue
        cost=sum(items[n][0] for n in selected)
        if cost>budget:continue
        value=sum(items[n][1] for n in selected)
        choices.append((value,cost,tuple(sorted(selected))))
    return max(choices,key=lambda t:(t[0],-t[1],t[2]))
def reachable(graph,start,goal,failed=()):
    failed=set(failed)
    if start in failed or goal in failed:return False
    seen={start}; pending=[start]
    while pending:
        node=pending.pop()
        if node==goal:return True
        for dst in graph.get(node,()):
            if dst not in failed and dst not in seen:
                seen.add(dst);pending.append(dst)
    return False
