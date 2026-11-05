"""Transparent toy trade study and decision-analysis calculations."""
import math

ALTERNATIVES = {
    'A': (0.85, 0.75, 0.95),
    'B': (0.75, 0.95, 0.70),
    'C': (0.65, 0.88, 0.90),
}

def weighted_score(values, weights=(0.35, 0.45, 0.20)):
    if len(values) != len(weights) or any(w < 0 for w in weights) or not math.isclose(sum(weights), 1, abs_tol=1e-12):
        raise ValueError('Use same-length nonnegative weights summing to one')
    return sum(v*w for v,w in zip(values, weights))


def safety_weight_crossover():
    # w_response=.35; w_affordability=.65 - s
    # A intercept .35*.85 + .65*.95; slope .75-.95
    # B intercept .35*.75 + .65*.70; slope .95-.70
    A0 = .35*.85+.65*.95
    B0 = .35*.75+.65*.70
    As = .75-.95
    Bs = .95-.70
    return (A0-B0)/(Bs-As)


def bayes_positive(prior, sensitivity, false_positive):
    p_plus = prior*sensitivity+(1-prior)*false_positive
    if p_plus == 0:
        raise ValueError('Positive event probability zero')
    return p_plus, prior*sensitivity/p_plus


def expected_loss_without_test(prior=.12, defect_loss=100, fix_cost=14):
    return min(prior*defect_loss, fix_cost)


def value_of_test(prior=.12, sensitivity=.8, false_positive=.1, defect_loss=100, fix_cost=14):
    """Assumes a correct fix eliminates modeled defect and test itself has zero harm."""
    p_plus, p_def_plus = bayes_positive(prior, sensitivity, false_positive)
    p_minus = 1-p_plus
    p_def_minus = prior*(1-sensitivity)/p_minus if p_minus else 0.0
    positive_policy_loss = min(defect_loss*p_def_plus, fix_cost)
    negative_policy_loss = min(defect_loss*p_def_minus, fix_cost)
    with_test = p_plus*positive_policy_loss+p_minus*negative_policy_loss
    no_test = expected_loss_without_test(prior, defect_loss, fix_cost)
    evpi = no_test-(prior*min(defect_loss,fix_cost)+(1-prior)*min(0,fix_cost))
    return {'p_positive':p_plus,'p_defect_positive':p_def_plus,
            'p_defect_negative':p_def_minus,'loss_no_test':no_test,
            'loss_with_test_before_cost':with_test, 'evsi':no_test-with_test,'evpi':evpi}

if __name__ == '__main__':
    for name,score in ALTERNATIVES.items():
        print(name, round(weighted_score(score),6))
    print('Crossover safety weight',safety_weight_crossover())
    print(value_of_test())
