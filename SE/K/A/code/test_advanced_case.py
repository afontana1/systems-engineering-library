"""Adverse-case tests for NS-AA4.1; run with unittest discover in this directory."""
import copy
import math
import unittest
from advanced_case import (load_case,load_requests,adjudicate_service,
    latency_budget,shared_cause_reliability,unsafe_dispatch_counterexamples,
    evidence_screen,evaluate)

class AdvancedIntegrationCase(unittest.TestCase):
    def setUp(self):
        self.c=load_case()
        self.rows=load_requests()

    def test_population(self):
        self.assertEqual(len(self.rows),50)
        self.assertEqual(len({r['request_id'] for r in self.rows}),50)

    def test_rates_and_guard(self):
        r=adjudicate_service(self.rows,20,.4)
        self.assertEqual((r['all']['eligible'],r['all']['completed'],r['all']['measured_timely'],r['all']['robust_timely']),(50,48,46,43))
        self.assertEqual((r['accessible']['eligible'],r['accessible']['measured_timely'],r['accessible']['robust_timely']),(12,11,10))
        self.assertAlmostEqual(r['all']['robust_timely_rate'],.86)
        self.assertAlmostEqual(r['accessible']['robust_timely_rate'],10/12)

    def test_smaller_clock_bound_changes_adjudication_not_validation(self):
        r=adjudicate_service(self.rows,20,.1)
        self.assertEqual(r['all']['robust_timely'],46)
        self.assertEqual(r['accessible']['robust_timely'],11)

    def test_unserved_exclusion_cannot_improve_denominator(self):
        r=adjudicate_service(self.rows,20,.4)
        self.assertEqual(r['all']['eligible'],50)
        self.assertLess(r['all']['robust_timely_rate'],r['all']['robust_timely']/r['all']['completed'])

    def test_duplicate_rejected(self):
        with self.assertRaises(ValueError):adjudicate_service(self.rows+[self.rows[0]],20,.4)

    def test_missing_wait_rejected(self):
        a=copy.deepcopy(self.rows);a[0]['wait_minutes']=''
        with self.assertRaises(ValueError):adjudicate_service(a,20,.4)

    def test_unserved_with_wait_rejected(self):
        a=copy.deepcopy(self.rows);a[-1]['wait_minutes']='1'
        with self.assertRaises(ValueError):adjudicate_service(a,20,.4)

    def test_invalid_wait_values_rejected(self):
        for value in ('NaN','inf','-2','abc'):
            a=copy.deepcopy(self.rows);a[0]['wait_minutes']=value
            with self.subTest(value=value), self.assertRaises(ValueError):adjudicate_service(a,20,.4)

    def test_unknown_group_and_result(self):
        for key,value in [('group','other'),('result','LOST')]:
            a=copy.deepcopy(self.rows);a[0][key]=value
            with self.subTest(key=key),self.assertRaises(ValueError):adjudicate_service(a,20,.4)

    def test_invalid_population_and_bounds(self):
        for n,e,rows in [(-1,.2,self.rows),(20,-.2,self.rows),(math.inf,.2,self.rows),(20,.2,[])]:
            with self.subTest(case=(n,e)),self.assertRaises(ValueError):adjudicate_service(rows,n,e)

    def test_latency(self):
        s=self.c['latency']['steps'];b=latency_budget(s,7)
        self.assertAlmostEqual(b['nominal_s'],5.5)
        self.assertAlmostEqual(b['worst_s'],6.7)
        self.assertAlmostEqual(b['margin_s'],.3)
        self.assertTrue(b['passes'])
        self.assertAlmostEqual(latency_budget(s,7,.5)['margin_s'],-.2)
        self.assertFalse(latency_budget(s,7,.5)['passes'])

    def test_invalid_latency(self):
        with self.assertRaises(ValueError):latency_budget(self.c['latency']['steps'],math.nan)
        with self.assertRaises(ValueError):latency_budget(self.c['latency']['steps'],7,-1)
        with self.assertRaises(ValueError):latency_budget(self.c['latency']['steps']*2,7)

    def test_reliability(self):
        self.assertAlmostEqual(shared_cause_reliability(.95,.03),.967575)
        self.assertAlmostEqual(shared_cause_reliability(.95,.02),.97755)
        self.assertAlmostEqual(shared_cause_reliability(.95,.025),.9725625)
        self.assertAlmostEqual(1-.97/.9975,.0275689223057644,places=11)

    def test_reliability_invalid(self):
        for val in (-.1,1.1,float('nan'),float('inf'),True):
            with self.subTest(val=val),self.assertRaises(ValueError):shared_cause_reliability(.95,val)

    def test_bad_guard_has_counterexamples(self):
        ce=unsafe_dispatch_counterexamples(5)
        self.assertTrue(ce)
        self.assertIn({'status':'CLOSED','age_min':0.,'authorized':True},ce)
        self.assertIn({'status':'OPEN','age_min':6,'authorized':False},ce)
        self.assertIn({'status':'OPEN','age_min':6,'authorized':True},ce)

    def test_bad_guard_age_invalid(self):
        for age in (-1,float('inf'),float('nan'),True):
            with self.subTest(age=age),self.assertRaises(ValueError):unsafe_dispatch_counterexamples(age)

    def test_evidence_stale(self):
        e=evidence_screen(self.c,'rev2')
        self.assertEqual(e['R-TIME'],[])
        self.assertEqual(e['R-ACCESS'],[])
        self.assertEqual(e['R-ROUTE'],['stale-revision'])

    def test_one_applicable_evidence_path_is_enough_for_structural_screen(self):
        a=copy.deepcopy(self.c)
        a['model']['nodes'].extend([{'id':'T-ROUTE-2','type':'Test'},{'id':'E-ROUTE-2','type':'Evidence'}])
        a['model']['edges'].extend([{'source':'R-ROUTE','target':'T-ROUTE-2','type':'verifiedBy'},
                                     {'source':'T-ROUTE-2','target':'E-ROUTE-2','type':'produces'}])
        a['evidence']['E-ROUTE-2']={'revision':'rev2','status':'PASS','scenario':'new-test'}
        self.assertEqual(evidence_screen(a,'rev2')['R-ROUTE'],[])

    def test_evidence_missing_and_nonpass(self):
        for mutate,expected in [('absent','evidence-record-absent'),('fail','nonpassing-evidence'),('scope','unscoped-evidence')]:
            a=copy.deepcopy(self.c)
            if mutate=='absent':del a['evidence']['E-ROUTE']
            elif mutate=='fail':a['evidence']['E-ROUTE']['status']='FAIL'
            else:a['evidence']['E-ROUTE']['scenario']=''
            with self.subTest(mutate=mutate):self.assertIn(expected,evidence_screen(a,'rev2')['R-ROUTE'])

    def test_missing_allocation_and_typed_invalid(self):
        a=copy.deepcopy(self.c)
        a['model']['edges']=[x for x in a['model']['edges'] if not(x['source']=='R-ROUTE' and x['type']=='allocatedTo')]
        with self.assertRaisesRegex(ValueError,'missing-allocation'):evidence_screen(a,'rev2')
        a=copy.deepcopy(self.c)
        a['model']['edges'][0]['type']='invalid'
        with self.assertRaisesRegex(ValueError,'unknown-edge'):evidence_screen(a,'rev2')

    def test_evaluate_holds(self):
        outcome=evaluate(self.c,self.rows)
        self.assertEqual(outcome['disposition'],'HOLD')
        self.assertFalse(outcome['authorization_inferred'])
        self.assertEqual(set(outcome['screen_failures']),{'all-request-timeliness','accessible-timeliness',
          'shared-cause-reliability','evidence-applicability','missing-authorization'})

    def test_even_permissive_thresholds_do_not_create_authorization(self):
        a=copy.deepcopy(self.c)
        a['acceptance']['all_timely_min']=.1
        a['acceptance']['accessible_timely_min']=.1
        a['acceptance']['reliability_min']=.1
        a['evidence']['E-ROUTE']['revision']='rev2'
        a['authorizations']={k:True for k in a['authorizations']}
        result=evaluate(a,self.rows)
        self.assertEqual(result['screen_failures'],[])
        self.assertEqual(result['disposition'],'HOLD')
        self.assertFalse(result['authorization_inferred'])

if __name__=='__main__':unittest.main()
