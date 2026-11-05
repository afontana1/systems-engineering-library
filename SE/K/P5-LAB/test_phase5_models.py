import unittest
from phase5_models import *
class TestPhase5(unittest.TestCase):
 def test_bayes(self):self.assertAlmostEqual(bayes_positive(.7,.9,.2),.63/.69)
 def test_bayes_zero(self):
  with self.assertRaises(ValueError):bayes_positive(0,.9,0)
 def test_bayes_invalid(self):
  with self.assertRaises(ValueError):bayes_positive(-.1,.9,.1)
 def test_bayes_equal(self):self.assertAlmostEqual(bayes_positive(.4,.6,.6),.4)
 def test_chain(self):self.assertAlmostEqual(chain_availability([.98,.95,.97],True),.90307)
 def test_chain_requires_assumption(self):
  with self.assertRaises(ValueError):chain_availability([.9,.9])
 def test_chain_bad_probability(self):
  with self.assertRaises(ValueError):chain_availability([1.2],True)
 def test_portfolio(self):self.assertEqual(select_portfolio({'A':(3,5),'B':(4,7),'C':(6,8)},7)['chosen'],('A','B'))
 def test_portfolio_required(self):self.assertEqual(select_portfolio({'A':(3,5),'B':(4,7),'C':(6,8)},7,required=['C'])['chosen'],('C',))
 def test_portfolio_infeasible(self):
  with self.assertRaises(ValueError):select_portfolio({'A':(3,5)},1,required=['A'])
 def test_group(self):
  d=accessible_outcomes({'A':90,'B':30},{'A':100,'B':60})
  self.assertAlmostEqual(d['aggregate'],.75);self.assertAlmostEqual(d['gap'],.4)
 def test_group_mismatch(self):
  with self.assertRaises(ValueError):accessible_outcomes({'A':1},{'B':2})
 def test_group_empty(self):
  with self.assertRaises(ValueError):accessible_outcomes({}, {})
 def test_group_bounds(self):
  with self.assertRaises(ValueError):accessible_outcomes({'A':4},{'A':3})
 def test_workforce(self):self.assertEqual(workforce_next(50,4,6),48)
 def test_workforce_negative(self):
  with self.assertRaises(ValueError):workforce_next(4,1,6)
 def test_mm1(self):self.assertEqual(mm1_time(8,10),.5)
 def test_mm1_congested(self):self.assertEqual(mm1_time(9,10),1.)
 def test_mm1_unstable(self):
  with self.assertRaises(ValueError):mm1_time(10,10)
 def test_network(self):self.assertTrue(mission_reachable({'rail':['dispatch'],'dispatch':['hospital']},'rail','hospital'))
 def test_network_failure(self):self.assertFalse(mission_reachable({'rail':['dispatch'],'dispatch':['hospital']},'rail','hospital',[('dispatch','hospital')]))
 def test_network_cycle(self):self.assertFalse(mission_reachable({'a':['b'],'b':['a']},'a','c'))
 def test_lead(self):self.assertEqual(lead_time([120,300,60],40),520)
 def test_lead_invalid(self):
  with self.assertRaises(ValueError):lead_time([-10,20],40)
if __name__=='__main__':unittest.main()
