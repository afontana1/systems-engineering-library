import unittest
from project_math import evm,proposal_price,estimate_hours,cpm
class ProjectTests(unittest.TestCase):
 def test_price(self):self.assertAlmostEqual(proposal_price(7.2,.6,.6),8.4)
 def test_budget_ceiling(self):self.assertLess(proposal_price(7.2,.6,.6),8.8)
 def test_estimate(self):self.assertEqual(estimate_hours(1800,140,90000),342000)
 def test_delay_cost(self):self.assertEqual(estimate_hours(2040,140,90000),375600)
 def test_evm_spi(self):self.assertAlmostEqual(evm(7.2,2.4,2.04,2.55)['spi'],.85)
 def test_evm_cpi(self):self.assertAlmostEqual(evm(7.2,2.4,2.04,2.55)['cpi'],.8)
 def test_evm_cost_variance(self):self.assertAlmostEqual(evm(7.2,2.4,2.04,2.55)['cv'],-.51)
 def test_evm_schedule_variance(self):self.assertAlmostEqual(evm(7.2,2.4,2.04,2.55)['sv'],-.36)
 def test_evm_eac(self):self.assertAlmostEqual(evm(7.2,2.4,2.04,2.55)['eac_simple'],9.0)
 def test_bad_input(self):
  with self.assertRaises(ValueError):evm(7.2,2.4,2.04,0)
 def test_critical_path(self):
  s=cpm({'A':{'duration':2,'predecessors':[]},'B':{'duration':4,'predecessors':['A']},'C':{'duration':3,'predecessors':['A']},'D':{'duration':5,'predecessors':['B','C']},'E':{'duration':2,'predecessors':['D']}})
  self.assertEqual(s['finish'],13);self.assertEqual(s['tasks']['C']['float'],1);self.assertEqual(set(s['critical']),{'A','B','D','E'})
 def test_cycle(self):
  with self.assertRaises(ValueError):cpm({'A':{'duration':1,'predecessors':['B']},'B':{'duration':1,'predecessors':['A']}})
if __name__=='__main__':unittest.main()
