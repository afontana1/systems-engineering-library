"""Run: python -m unittest discover -s tools -v from phase-0-textbook directory."""
import unittest
from phase0_calculators import weighted_score, cost_estimate, cpm, evm

class CalculatorsTest(unittest.TestCase):
 def setUp(self):
  self.net={'A':{'duration':3,'preds':[]},'B':{'duration':5,'preds':['A']},
            'C':{'duration':4,'preds':['A']},'D':{'duration':3,'preds':['B','C']},
            'E':{'duration':2,'preds':['D']}}
 def test_trade(self):
  self.assertAlmostEqual(weighted_score((90,60,70),(.5,.3,.2)),77)
  self.assertAlmostEqual(weighted_score((70,85,80),(.5,.3,.2)),76.5)
 def test_cost(self):
  t=cost_estimate(160,130,(18000,2500,6000),.1)
  self.assertEqual(t['subtotal'],47300)
  self.assertAlmostEqual(t['planned_total'],52030)
 def test_cpm(self):
  a=cpm(self.net)
  self.assertEqual(a['finish'],13)
  self.assertEqual(a['activities']['C']['float'],1)
  self.assertEqual(a['critical'],['A','B','D','E'])
 def test_cpm_switch(self):
  self.net['B']['duration']=3
  a=cpm(self.net)
  self.assertEqual(a['finish'],12)
  self.assertEqual(a['critical'],['A','C','D','E'])
 def test_cycle(self):
  self.net['A']['preds']=['E']
  with self.assertRaises(ValueError):cpm(self.net)
 def test_evm(self):
  t=evm(500000,250000,200000,240000)
  self.assertAlmostEqual(t['CPI'],5/6)
  self.assertAlmostEqual(t['SPI'],.8)
  self.assertAlmostEqual(t['EAC_CPI'],600000)
  self.assertAlmostEqual(t['TCPI_BAC'],300/260)

if __name__=='__main__':unittest.main()
