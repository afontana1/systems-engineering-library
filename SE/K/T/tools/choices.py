"""Weighted utilities and switch points for a two-criterion comparison."""
def score(rel: float, cost: float, reliability_weight: float) -> float:
    if not 0 <= reliability_weight <= 1: raise ValueError('weight outside [0,1]')
    return reliability_weight*rel+(1-reliability_weight)*cost

def compare(w: float) -> tuple:
    return score(.8,.4,w),score(.6,.9,w)

if __name__ == '__main__':
    for w in (.4,.6,5/7,.9): print(w,compare(w))
