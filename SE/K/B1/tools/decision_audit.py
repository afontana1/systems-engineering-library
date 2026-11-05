"""Educational deterministic trade calculator: scores are invented for teaching."""
from pathlib import Path
import csv

SCORES = Path(__file__).resolve().parents[1] / "data" / "architecture-scores.csv"

def weighted_scores(weights=(0.50,0.30,0.20), rows=None):
    if any(w < 0 for w in weights) or abs(sum(weights)-1) > 1e-10:
        raise ValueError("Weights must be nonnegative and sum to one")
    if rows is None:
        with SCORES.open(newline="") as f:
            rows=list(csv.DictReader(f))
    out={}
    for row in rows:
        nums=[float(row[k]) for k in ("resilience","affordability","maintainability")]
        if any(x < 0 or x > 100 for x in nums):raise ValueError("Scores must be from 0 to 100")
        out[row['concept']]=sum(w*x for w,x in zip(weights,nums))
    return out

def pairwise_threshold():
    """For F/T with maintainability weight fixed at 0.20."""
    return 23/55

def winners(resilience_weights):
    for w in resilience_weights:
        if not 0 <= w <= 0.8:raise ValueError("Invalid weight with maintainability fixed at .20")
        scores=weighted_scores((w,0.8-w,0.2))
        yield w, max(scores, key=scores.get), scores

if __name__ == '__main__':
    print("Nominal scores:",weighted_scores())
    print("Pairwise F/T crossover:",pairwise_threshold())
    for w,name,s in winners([0.3,0.4,0.5,0.6]):print(f"resilience={w:.2f}: {name} {s}")
