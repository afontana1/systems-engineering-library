"""Test numerical examples, boundaries and validation conditions in the flagship chapters."""
import math
import pytest
from evidence_graph import Requirement, Evidence, audit, structural_coverage
from decision_analysis import ALTERNATIVES, weighted_score, safety_weight_crossover, value_of_test, bayes_positive
from reliability_evidence import zero_failure_upper, zero_failure_sample_size, series_reliability, two_channel_redundancy, exponential_survival, beta_posterior_mean
from operational_dynamics import backlog, euler_decay, mm1, min_service_rate_for_queue_wait, resilience_loss


def test_evidence_good_and_bad():
    rows=audit([Requirement('R1','curb_seconds',True),Requirement('R2','api_ms')],
               [Evidence('E1','R1','2','accepted','api_ms'), Evidence('E2','R2','2','accepted','api_ms')], '2')
    assert structural_coverage(rows)==.5
    assert rows[0]['wrong_observable_ids']==['E1']

def test_stale_evidence():
    row=audit([Requirement('R','seconds')],[Evidence('E','R','4.1','accepted','seconds')],'4.2')[0]
    assert not row['has_applicable_accepted_evidence'] and row['stale_ids']==['E']

def test_empty_coverage_is_undefined():assert structural_coverage([]) is None

def test_weighted_scores():
    assert math.isclose(weighted_score(ALTERNATIVES['A']),.825)
    assert math.isclose(weighted_score(ALTERNATIVES['B']),.830)
    assert math.isclose(weighted_score(ALTERNATIVES['C']),.8035)

def test_weight_validation():
    with pytest.raises(ValueError):weighted_score((1,1),(0.5,-0.5))

def test_crossover():assert math.isclose(safety_weight_crossover(),.1975/.45)

def test_bayes():
    p,posterior=bayes_positive(.12,.8,.1)
    assert math.isclose(p,.184) and math.isclose(posterior,.096/.184)

def test_evsi():
    x=value_of_test()
    assert math.isclose(x['loss_no_test'],12)
    assert math.isclose(x['loss_with_test_before_cost'],4.976)
    assert math.isclose(x['evsi'],7.024)
    assert math.isclose(x['evpi'],10.32)
    assert x['evsi']<=x['evpi']

def test_bound():assert math.isclose(zero_failure_upper(300),.00993608194445772, rel_tol=1e-10)

def test_samples():assert zero_failure_sample_size(.001)==2995

def test_more_tests_tighten():assert zero_failure_upper(500)<zero_failure_upper(100)

def test_bad_sample():
    with pytest.raises(ValueError):zero_failure_upper(0)

def test_series():assert math.isclose(series_reliability(.98,.99,.97),.941094)

def test_common_cause():assert math.isclose(two_channel_redundancy(.08,.02),.973728)

def test_series_bad():
    with pytest.raises(ValueError):series_reliability(1.1)

def test_survival():assert math.isclose(exponential_survival(1e-4,100), math.exp(-.01))

def test_beta_posterior():assert math.isclose(beta_posterior_mean(1,1,0,300),1/302)

def test_backlog():assert backlog(4,12,9,2)==10

def test_invalid_backlog():
    with pytest.raises(ValueError):backlog(1,0,10,2)

def test_euler():assert math.isclose(euler_decay(1,.25,4),.31640625)

def test_euler_refinement():
    coarse=abs(euler_decay(1,.25,4)-math.exp(-1))
    fine=abs(euler_decay(1,.125,8)-math.exp(-1))
    assert fine<coarse

def test_mm1():
    q=mm1(12,15)
    assert math.isclose(q['mean_queue_hours']*60,16)
    assert math.isclose(q['mean_system_hours']*60,20)

def test_mm1_high_service():assert math.isclose(mm1(12,18)['mean_queue_hours']*60, 20/3)

def test_mm1_unstable():
    with pytest.raises(ValueError):mm1(12,12)

def test_capacity():assert math.isclose(min_service_rate_for_queue_wait(12,1/12),(12+math.sqrt(720))/2)

def test_loss():assert resilience_loss(100,60,2)==80 and resilience_loss(100,80,3)==60
