import unittest
from phase5_lab import *
class Phase5Labs(unittest.TestCase):
 def test_bayes_base(self):self.assertAlmostEqual(bayes_positive(.05,.9,.15),.24)
 def test_bayes_perfect(self):self.assertAlmostEqual(bayes_positive(.2,1,0),1)
 def test_bayes_bounds(self):
  with self.assertRaises(ValueError):bayes_positive(-.1,.8,.2)
 def test_bayes_zero(self):
  with self.assertRaises(ValueError):bayes_positive(0,.8,0)
 def test_series(self):self.assertAlmostEqual(independent_series_success([.95,.9,.9]),.7695)
 def test_series_empty(self):
  with self.assertRaises(ValueError):independent_series_success([])
 def test_cutsets(self):self.assertEqual(minimal_cut_sets([['b','h','r'],['p','h','u']]),[('h',),('b','p'),('b','u'),('p','r'),('r','u')])
 def test_cutsets_simple(self):self.assertEqual(minimal_cut_sets([['a'],['b']]),[('a','b')])
 def test_cutsets_and(self):self.assertEqual(minimal_cut_sets([['a','b']]),[('a',),('b',)])
 def test_cutsets_always_success(self):self.assertEqual(minimal_cut_sets([[]]),[])
 def test_age(self):self.assertEqual(time_age_seconds('2026-10-01T12:00:00Z','2026-10-01T12:07:00Z',180),(420,False))
 def test_age_timezone(self):self.assertEqual(time_age_seconds('2026-10-01T12:00:00+00:00','2026-10-01T05:01:00-07:00',90),(60,True))
 def test_age_negative(self):
  with self.assertRaises(ValueError):time_age_seconds('2026-10-01T12:01:00Z','2026-10-01T12:00:00Z',60)
 def test_stock(self):self.assertEqual(stock_flow(120,[15,18,23,25],[22,21,19,18]),[120.,113.,110.,114.,121.])
 def test_stock_invalid(self):
  with self.assertRaises(ValueError):stock_flow(1,[0],[2])
 def test_portfolio(self):
  x=[dict(id='a',cost=150,value=3),dict(id='b',cost=200,value=5,requires=['a']),dict(id='c',cost=350,value=7)]
  results=portfolio_feasible(x,400);self.assertEqual(results[0]['ids'],('a','b'))
 def test_portfolio_dependency(self):
  x=[dict(id='a',cost=400,value=10,requires=['b']),dict(id='b',cost=250,value=1)]
  self.assertNotIn(('a',),[p['ids'] for p in portfolio_feasible(x,500)])
 def test_portfolio_duplicate(self):
  with self.assertRaises(ValueError):portfolio_feasible([dict(id='a',cost=1,value=2),dict(id='a',cost=1,value=2)],10)
 def test_rate(self):
  avg,parts=subgroup_rate([(855,900),(50,100)]);self.assertAlmostEqual(avg,.905);self.assertEqual(parts,[.95,.5])
 def test_rate_invalid(self):
  with self.assertRaises(ValueError):subgroup_rate([(9,3)])
 def test_queue(self):self.assertAlmostEqual(queue_mm1_system_time(9.8,10),5)
 def test_queue_unstable(self):
  with self.assertRaises(ValueError):queue_mm1_system_time(10,10)
 def test_area(self):self.assertAlmostEqual(mission_recovery_area([0,2,4],[1,.5,1]),1.)
 def test_area_bad(self):
  with self.assertRaises(ValueError):mission_recovery_area([0,0],[.5,.5])
 def test_did(self):self.assertAlmostEqual(diff_in_diff(18,13,19,18),-4)
if __name__=='__main__':unittest.main()
