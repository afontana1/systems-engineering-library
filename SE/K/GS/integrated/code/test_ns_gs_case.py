"""Independent executable arithmetic and adverse-input checks, NS-GS4.1."""
import copy,importlib.util,json,math,unittest
from pathlib import Path
from ns_gs_case import INPUT,OUTPUT,run,finite_number,portfolio,policy_screen

class TestGraduateMethods(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case=json.loads(INPUT.read_text())
        cls.results=run(cls.case)
    def test_identity_and_disposition(self):
        self.assertEqual(self.results['case_id'],'NS-GS4.1')
        self.assertEqual(self.results['readiness']['disposition'],'HOLD')
        self.assertFalse(self.results['readiness']['authorize'])
        self.assertEqual([self.results['readiness'][k] for k in ('joint_technical_pass','evidence_complete','authority_complete','no_group_harm')],[False]*4)
    def test_earned_value(self):
        r=self.results['cost_and_evidence']
        for k,v in {'cpi':.8,'spi':.8,'evidence_cpi':.675,'efficiency_eac_m':11.25,'bottomup_eac_m':10.3}.items():
            with self.subTest(k=k):self.assertAlmostEqual(r[k],v,12)
    def test_energy(self):
        r=self.results['energy']
        for k,v in {'consumption_kwh':22,'usable_kwh':21.636,'margin_kwh':-.364,'derivative_intensity_km':-80,'derivative_distance_kwh_per_km':-.23}.items():
            with self.subTest(k=k):self.assertAlmostEqual(r[k],v,10)
    def test_hybrid(self):
        r=self.results['hybrid'];self.assertAlmostEqual(r['exact_final_kwh'],3.75)
        self.assertAlmostEqual(r['exact_threshold_h'],2.9544511501033224)
        for row,h,e in zip(r['euler'],(.5,.25,.125),(.375,.1875,.09375)):
            with self.subTest(h=h):
                self.assertAlmostEqual(row['step_h'],h)
                self.assertAlmostEqual(row['error_kwh'],e)
                self.assertAlmostEqual(row['final_kwh'],3.75+e)
        self.assertIsNone(r['euler'][0]['first_grid_trigger_h'])
        self.assertEqual(r['euler'][1]['first_grid_trigger_h'],3)
        self.assertEqual(r['euler'][2]['first_grid_trigger_h'],3)
    def test_feedback(self):
        r=self.results['delayed_feedback']
        self.assertAlmostEqual(r['safe_gain']['last'],.54223,5)
        self.assertGreater(r['unstable_gain']['max_abs'],33)
        self.assertLess(r['safe_gain']['max_abs'],r['unstable_gain']['max_abs'])
    def test_policy(self):
        rows={v['id']:v for v in self.results['policy_screen']}
        self.assertEqual(len(rows),4)
        for k,v in {'status_quo':.792,'throughput_push':.882,'assurance_first':.859,'integrated':.933}.items():
            self.assertAlmostEqual(rows[k]['weighted_timely'],v)
        self.assertAlmostEqual(rows['integrated']['weighted_accessible'],.917)
        self.assertEqual(rows['integrated']['screening_coverage'],.8)
        self.assertFalse(rows['integrated']['scenario_pass']['compound'])
        self.assertTrue(rows['integrated']['resource_feasible'])
        self.assertFalse(any(p['passes_all_scenarios'] for p in rows.values()))
    def test_flow(self):
        self.assertAlmostEqual(self.results['flow']['internal_flow_days'],24)
        self.assertAlmostEqual(self.results['flow']['evidence_backed_flow_days'],30)
    def test_evidence(self):
        r=self.results['digital_evidence'];self.assertEqual(r['actionable'],1);self.assertEqual(r['total'],4)
        bad={row['requirement']:row['reasons'] for row in r['records']}
        self.assertEqual(bad['R-SAFETY'],['stale','unapproved'])
        self.assertEqual(bad['R-INTEROP'],['revision_mismatch'])
        self.assertEqual(bad['R-PRIVACY'],['unapproved'])
        self.assertEqual(bad['R-ACCESS'],[])
    def test_did(self):self.assertEqual(self.results['pilot_did']['estimate_min'],-4)
    def test_network(self):
        r=self.results['mission_network']
        self.assertAlmostEqual(r['independent_availability'],.99506)
        self.assertAlmostEqual(r['common_cause_availability'],.9552576)
        self.assertEqual(r['available_slots'],66)
        self.assertTrue(r['accessible_demand_met'])
    def test_portfolio(self):
        r=self.results['portfolio'];self.assertEqual(r['best']['investments'],['inclusion','interop'])
        self.assertAlmostEqual(r['best']['value'],3.9);self.assertAlmostEqual(r['best']['cost_m'],1.35)
        self.assertEqual(r['best']['staff'],4);self.assertEqual(r['feasible_count'],8)
    def test_equity(self):
        r=self.results['equity'];self.assertEqual(r['before_min'],15)
        self.assertEqual(r['after_min'],13.25);self.assertEqual(r['rural_harm_min'],5)
        self.assertFalse(r['no_group_harm'])
    def test_recomputed_output(self):self.assertEqual(json.loads(OUTPUT.read_text()),self.results)
    def invalid(self,path,value):
        x=copy.deepcopy(self.case);target=x
        for key in path[:-1]:target=target[key]
        target[path[-1]]=value
        with self.subTest(path=path,value=value),self.assertRaises((ValueError,KeyError,TypeError)):
            run(x)
    def test_negative_values(self):
        cases=[(('id',),'INCORRECT'),(('project','pv_m'),0),(('project','accepted_ev_m'),4),
           (('energy','soc'),1.1),(('energy','distance_km'),-3),(('hybrid','horizon_h'),0),
           (('hybrid','steps_h'),[.7]),(('feedback','safe_gain'),-1),(('feedback','steps'),-2),
           (('scenarios',0,'weight'),-.1),(('policies',3,'timely'),[.1]),
           (('flow','accepted_rate_per_day'),.85),(('evidence','requirements'),[]),
           (('evidence','requirements',0,'approved'),'yes'),(('network','common_cause'),1.1),
           (('portfolio','budget_m'),-1),(('portfolio','options'),[]),(('authority','road_authority'),'yes'),
           (('authority',),{'road_authority':True})]
        for keys,value in cases:self.invalid(keys,value)
    def test_bad_duplicate_entities(self):
        x=copy.deepcopy(self.case);x['scenarios'][1]['id']='clear'
        with self.assertRaises(ValueError):run(x)
        x=copy.deepcopy(self.case);x['policies'][1]['id']='status_quo'
        with self.assertRaises(ValueError):run(x)
        x=copy.deepcopy(self.case);x['portfolio']['options'][1]['requires']=['missing']
        with self.assertRaises(ValueError):run(x)
        x=copy.deepcopy(self.case);x['evidence']['requirements'][1]['id']='R-ACCESS'
        with self.assertRaises(ValueError):run(x)
    def test_authorities_cannot_override_bad_evidence(self):
        x=copy.deepcopy(self.case);x['authority']={k:True for k in x['authority']}
        result=run(x)
        self.assertFalse(result['readiness']['authorize'])
        self.assertEqual(result['readiness']['disposition'],'HOLD')
    def test_evidence_fix_alone_cannot_authorize(self):
        x=copy.deepcopy(self.case)
        for e in x['evidence']['requirements']:
            e['age_days']=0;e['artifact_rev']=e['expected_rev'];e['approved']=True
        result=run(x);self.assertTrue(result['readiness']['evidence_complete'])
        self.assertFalse(result['readiness']['authorize'])
    def test_invalid_nan(self):
        with self.assertRaises(ValueError):finite_number(float('nan'),'x')
        with self.assertRaises(ValueError):finite_number(float('inf'),'x')
        with self.assertRaises(ValueError):finite_number(True,'x')
    def test_failure_change_capacity(self):
        x=copy.deepcopy(self.case);x['network']['dispatch_slots']=60
        self.assertFalse(run(x)['mission_network']['accessible_demand_met'])
    def test_joint_scenario_overweight_rejected(self):
        x=copy.deepcopy(self.case);x['scenarios'][0]['weight']=.6
        with self.assertRaises(ValueError):run(x)
    def test_alternative_control_pilot(self):
        x=copy.deepcopy(self.case);x['pilot']['control_post_min']=13
        self.assertEqual(run(x)['pilot_did']['estimate_min'],0)
    def test_rural_weight_does_not_cancel_harm(self):
        x=copy.deepcopy(self.case);x['equity']['urban_share']=.9
        r=run(x)['equity'];self.assertAlmostEqual(r['mean_improvement_min'],3.1)
        self.assertFalse(r['no_group_harm'])

if __name__=='__main__':unittest.main()
