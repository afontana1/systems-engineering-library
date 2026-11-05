"""Run all v12 synthetic scenarios and export reproducible records.

From advanced-lab directory: python -m src.run_advanced
"""
from __future__ import annotations
import csv
import json
from pathlib import Path
from .architecture import load_model,validate_model
from .event_sim import Scenario,load_events,simulate,paired_experiment
from .evidence import read_csv,trace_audit,manifest,sha

ROOT=Path(__file__).resolve().parents[1]

def run(output_dir=None,replications=120):
    out=Path(output_dir) if output_dir else ROOT/'outputs'
    out.mkdir(parents=True,exist_ok=True)
    architecture=validate_model(load_model(ROOT/'models/architecture.json'))
    cases=json.loads((ROOT/'data/scenarios.json').read_text())
    events=load_events(ROOT/'data/requests.csv')
    specs={s['id']:Scenario(**s) for s in cases}
    results={key:simulate(events,spec) for key,spec in specs.items()}
    comparative=paired_experiment(specs['BASE'],specs['OUTAGE'],replications=replications)
    trace=trace_audit(read_csv(ROOT/'data/requirements-v12.csv'),
                      read_csv(ROOT/'data/verification-plan.csv'),set(specs))
    checks={
      'architecture_graph_valid':architecture['valid'],
      'trace_links_valid':trace['pass_links'],
      'baseline_no_overlap':results['BASE']['vehicle_nonoverlap'],
      'outage_no_overlap':results['OUTAGE']['vehicle_nonoverlap'],
      'duplicate_idempotency_fixture':results['BASE']['duplicates_ignored']==1,
      'outage_fault_reduces_or_matches_service':results['OUTAGE']['completed']<=results['BASE']['completed'],
      'message_loss_visible':results['LOSS']['lost_messages']>0,
      'telemetry_suppression_is_modeled':results['TELEMETRY']['completion_fraction']<=results['BASE']['completion_fraction'],
    }
    artifact=dict(edition='v12.0',system='Northstar synthetic lab only',
                  architecture=architecture,trace=trace,scenarios=results,
                  experiment=comparative,checks=checks,fixture_checks_pass=all(checks.values()),
                  board_recommendation='NOT READY FOR FIELD USE: only synthetic model and local software evidence')
    (out/'scenario-results.json').write_text(json.dumps(artifact,indent=2)+'\n')
    with (out/'scenario-summary.csv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=['scenario_id','unique_requests','completed','lost_messages','unserved_capacity','completion_fraction','p90_wait_min','vehicle_nonoverlap'])
        w.writeheader()
        for k,r in results.items():w.writerow({ 'scenario_id':k,**{n:r[n] for n in w.fieldnames if n!='scenario_id'}})
    paths=['models/architecture.json','data/requests.csv','data/scenarios.json',
           'data/requirements-v12.csv','data/verification-plan.csv',
           'src/architecture.py','src/event_sim.py','src/evidence.py','src/run_advanced.py']
    record={'inputs_and_implementation':manifest(ROOT,paths),
            'outputs':{name:sha(out/name) for name in ['scenario-results.json','scenario-summary.csv']},
            'warning':'Hashes support change detection only; they do not certify truth or safety'}
    (out/'provenance.json').write_text(json.dumps(record,indent=2)+'\n')
    return artifact

if __name__=='__main__':
    x=run();print(json.dumps({'checks':x['checks'],'paired_experiment':x['experiment'],
                              'field_ready':False},indent=2))
