import unittest, math
from architecture_models import *
from optimization_control import *
from safety_events import *
from simulation_credibility import *
from enterprise_portfolio import *
class TestV10(unittest.TestCase):
    def test_series(self):self.assertAlmostEqual(series_availability([.99]*3),.970299)
    def test_parallel(self):self.assertAlmostEqual(parallel_availability([.99,.99]),.9999)
    def test_cause(self):self.assertAlmostEqual(common_cause_parallel([.99,.99],.02),.979902)
    def test_invalid_probability(self):
        with self.assertRaises(AssertionError):parallel_availability([1.1])
    def test_transition(self):self.assertEqual(accept_event('Pending',2,'assign',3),('Assigned',3,True))
    def test_replay(self):self.assertEqual(accept_event('Cancelled',3,'assign',2),('Cancelled',3,False))
    def test_stale_revision(self):self.assertEqual(accept_event('Pending',2,'assign',2),('Pending',2,False))
    def test_fleet_best(self):self.assertEqual(fleet_options()[0],(16,5,2,26))
    def test_fleet_limit(self):self.assertEqual(fleet_options(budget=15),[])
    def test_fleet_access(self):self.assertTrue(all(x[2]>=3 for x in fleet_options(min_accessible=3)))
    def test_control_path(self):self.assertEqual(scalar_path(1,.5,1,16,3),[16,8,4,2])
    def test_control_oscillation(self):self.assertEqual(scalar_path(1,.5,3,16,1),[16,-8])
    def test_stable(self):self.assertTrue(scalar_stable(1,.5,3))
    def test_unstable(self):self.assertFalse(scalar_stable(1,.5,5))
    def test_tree(self):self.assertAlmostEqual(chain_probability([.01,.1,.2]),.0002)
    def test_expected(self):self.assertEqual(expected_direct_loss([(.002,50000)]),100)
    def test_sensitivity(self):self.assertEqual(len(probability_sensitivity(.01,[.1,.2],.2)),2)
    def test_invalid_tree(self):
        with self.assertRaises(AssertionError):chain_probability([.1,-.2])
    def test_variance(self):self.assertAlmostEqual(variance_of_sum(3,2,.6),20.2)
    def test_independent_var(self):self.assertEqual(variance_of_sum(3,2,0),13)
    def test_summary(self):
        r=replication_summary([8,9,7,10,6],2.776)
        self.assertAlmostEqual(r['mean'],8)
        self.assertAlmostEqual(r['se'],math.sqrt(.5))
        self.assertAlmostEqual(r['lower'],8-2.776*math.sqrt(.5))
    def test_seed(self):self.assertEqual(synthetic_replications(15),synthetic_replications(15))
    def test_new_seed(self):self.assertNotEqual(synthetic_replications(15),synthetic_replications(16))
    def test_paired(self):self.assertEqual(len(paired_improvement(n=20)),20)
    def test_portfolio(self):self.assertEqual(optimize_portfolio({'A':(4,8),'B':(5,11),'C':(3,5)},8),(16,8,('B','C')))
    def test_portfolio_dep(self):self.assertEqual(optimize_portfolio({'A':(4,8),'B':(5,11),'C':(3,5)},8,[('B','A')]),(13,7,('A','C')))
    def test_reachable(self):self.assertTrue(reachable({'A':['B'],'B':['C']},'A','C'))
    def test_cut(self):self.assertFalse(reachable({'A':['B'],'B':['C']},'A','C',['B']))
    def test_empty_portfolio(self):self.assertEqual(optimize_portfolio({'A':(4,8)},0),(0,0,()))
if __name__=='__main__':unittest.main()
