import math, unittest
from confidence import upper_zero_failures
from queueing import mm1
from choices import compare
from dynamics import euler, exact

class ConceptsTest(unittest.TestCase):
 def test_confidence_30(self): self.assertAlmostEqual(upper_zero_failures(30), 1-.05**(1/30))
 def test_confidence_300(self): self.assertLess(upper_zero_failures(300),.01)
 def test_confidence_invalid(self):
  with self.assertRaises(ValueError): upper_zero_failures(0)
 def test_queue(self): self.assertAlmostEqual(mm1(8,10)['hours_in_system'],.5)
 def test_queue_length(self): self.assertAlmostEqual(mm1(8,10)['mean_in_system'],4)
 def test_queue_unstable(self):
  with self.assertRaises(ValueError): mm1(10,10)
 def test_trades_low(self): self.assertLess(*compare(.2))
 def test_trades_high(self): self.assertGreater(*compare(.9))
 def test_trade_switch(self): self.assertAlmostEqual(compare(5/7)[0],compare(5/7)[1])
 def test_euler(self): self.assertAlmostEqual(euler(10,.5,1,1)[-1],5)
 def test_exact(self): self.assertAlmostEqual(exact(10,.5,1),10*math.exp(-.5))
 def test_euler_unstable_factor(self): self.assertGreater(abs(1-.5*5),1)

if __name__=='__main__': unittest.main()
