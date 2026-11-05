"""Typed trace graph: deliberately small standard-library teaching example."""
from collections import deque

class ModelError(ValueError): pass

class ModelGraph:
    ALLOWED = {"derivesFrom", "allocatedTo", "realizedBy", "verifiedBy", "calls", "dependsOn"}
    def __init__(self): self.nodes={}; self.links=[]
    def element(self, identifier, kind, title, revision="1"):
        if identifier in self.nodes: raise ModelError(f"duplicate: {identifier}")
        self.nodes[identifier]={"kind":kind,"title":title,"revision":revision}
        return identifier
    def link(self, source, relation, target):
        if source not in self.nodes or target not in self.nodes: raise ModelError("missing endpoint")
        if relation not in self.ALLOWED: raise ModelError("unknown relation")
        if (source,relation,target) not in self.links: self.links.append((source,relation,target))
    def successors(self, identifier, *, reverse=False):
        return sorted(a if reverse else b for a,r,b in self.links if (b if reverse else a)==identifier)
    def impact(self, identifier):
        """Return reachability treating trace links as dependencies for review, not proof of impact."""
        if identifier not in self.nodes: raise ModelError("unknown element")
        seen={identifier}; queue=deque([identifier]); out=[]
        while queue:
            n=queue.popleft()
            for s,r,t in self.links:
                # Most trace relations point from more specific to source or realization;
                # a human must decide propagation direction for each relation.
                if s==n and t not in seen: seen.add(t);out.append(t);queue.append(t)
                if t==n and s not in seen: seen.add(s);out.append(s);queue.append(s)
        return sorted(out)
    def orphan_requirements(self):
        return sorted(n for n,d in self.nodes.items() if d['kind']=='Requirement'
                      and not any(n in (s,t) for s,r,t in self.links))

def sample():
    g=ModelGraph()
    for i,k,t in [('N-1','Need','Riders get reliable status'),('R-1','Requirement','Show status freshness'),
                  ('F-1','Function','Publish status'),('SW-1','SoftwareService','Notification service'),
                  ('T-1','Test','Stale events rejected')]:g.element(i,k,t)
    for s,r,t in [('R-1','derivesFrom','N-1'),('F-1','realizedBy','R-1'),
                  ('F-1','allocatedTo','SW-1'),('R-1','verifiedBy','T-1')]:g.link(s,r,t)
    return g
if __name__=='__main__':
    g=sample(); print('Change review queue for R-1:', ', '.join(g.impact('R-1')))
