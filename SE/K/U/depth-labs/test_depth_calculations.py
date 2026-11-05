import math,unittest
from depth_calculations import *
class DepthChecks(unittest.TestCase):
 def test_upper(self):self.assertAlmostEqual(zero_failure_upper(300),.00993608194445772)
 def test_upper_invalid(self):
  with self.assertRaises(ValueError):zero_failure_upper(0)
 def test_required(self):self.assertEqual(trials_for_zero_failure(.001),2995)
 def test_bayes(self):
  z=bayes_two_state(.1,.8,.1);self.assertAlmostEqual(z['posterior_positive'],.08/.17)
 def test_evsi(self):self.assertAlmostEqual(sample_information_value(),4.94)
 def test_trade(self):self.assertAlmostEqual(trade_difference(2/3)[-1],0)
 def test_factor(self):
  z=factorial_effects({(-1,-1):7,(1,-1):5,(-1,1):15,(1,1):10})
  self.assertEqual((z['A'],z['B'],z['AB'],z['beta_AB']),(-3.5,6.5,-3,-.75))
 def test_queue(self):
  z=mm1(12,15);self.assertAlmostEqual(z['W_hours'],1/3);self.assertEqual(z['L'],4)
 def test_queue_unstable(self):
  with self.assertRaises(ValueError):mm1(16,15)
 def test_common(self):self.assertAlmostEqual(joint_failure_common_cause(),.010396)
 def test_decay(self):
  self.assertAlmostEqual(euler_decay(steps=1),60);self.assertAlmostEqual(euler_decay(steps=4),65.61)
 def test_critical(self):
  vals,d=critical_path({'A':3,'B':5,'C':4,'D':2,'E':3},{'C':['A'],'D':['B'],'E':['C','D']});self.assertEqual(d,10)
 def test_earned(self):self.assertEqual(earned_value(80,60,75),{'SPI':.75,'CPI':.8,'SV':-20,'CV':-15})
 def test_did(self):self.assertEqual(difference_in_differences(12,8,10,9),-3)
if __name__=='__main__':unittest.main()
