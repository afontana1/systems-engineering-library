"""Transparent illustrative additive value scoring with explicit hard constraints."""
def evaluate(options, weights, hard_constraints):
    if abs(sum(weights.values())-1)>1e-9 or any(w<0 for w in weights.values()):
        raise ValueError('nonnegative weights must sum to one')
    results=[]
    for name,attrs in options.items():
        eligible=all(predicate(attrs) for predicate in hard_constraints.values())
        values=[attrs[k] for k in weights]
        if any(not 0<=v<=1 for v in values):
            raise ValueError('value functions must be normalized 0..1')
        score=sum(weights[k]*attrs[k] for k in weights) if eligible else None
        results.append((name,eligible,score))
    return sorted(results,key=lambda x:(x[1],x[2] if x[2] is not None else -1),reverse=True)

def tie_weight(a_avail,a_cost,b_avail,b_cost):
    # A(w) = w*a_avail + (1-w)*a_cost; solve A(w)=B(w)
    denominator=(a_avail-a_cost)-(b_avail-b_cost)
    if denominator == 0: return None
    return (b_cost-a_cost)/denominator

if __name__=='__main__':
    options={'A':{'availability':.9,'affordability':.4},'B':{'availability':.7,'affordability':.8}}
    print(evaluate(options,{'availability':.6,'affordability':.4},{}))
    print('Tie availability weight:',tie_weight(.9,.4,.7,.8))
