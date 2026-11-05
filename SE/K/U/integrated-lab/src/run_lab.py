"""Run the self-contained integrated laboratory. Python 3.10+; no third-party packages."""
import argparse
import csv
import hashlib
import json
from pathlib import Path
from .northstar import Config, load_requests, dispatch, synthetic_replications
from .assurance import read_rows, audit_traceability

ROOT=Path(__file__).resolve().parents[1]

def run(output_dir=None):
    output = Path(output_dir) if output_dir else ROOT/'outputs'
    output.mkdir(parents=True,exist_ok=True)
    data = ROOT/'data'
    events = load_requests(data/'requests.csv')
    cfg=Config(**json.loads((data/'config.json').read_text(encoding='utf-8')))
    baseline=dispatch(events,cfg)
    degraded=dispatch(events,Config(**{**cfg.__dict__,'vehicles':1}))
    stochastic=synthetic_replications(cfg)
    trace=audit_traceability(read_rows(data/'requirements.csv'),
                             read_rows(data/'verification-matrix.csv'),
                             read_rows(data/'hazards.csv'))
    checks={
      'REQ-01-idempotency':baseline['duplicates_ignored']==1 and baseline['unique_requests']==12,
      'REQ-02-no-overlap':no_vehicle_overlap(baseline['assignments']),
      'REQ-03-service-target-on-fixed-fixture':baseline['served_fraction']>=cfg.target_served,
      'REQ-04-p90-wait-on-fixed-fixture':baseline['p90_wait_min']<=cfg.target_p90_wait_min,
      'REQ-05-trace-links-present':trace['link_integrity_pass'],
      'REQ-06-degraded-scenario-exposes-capacity-risk':degraded['served_fraction']<cfg.target_served,
    }
    results=dict(version='v11.0 teaching laboratory', assumptions='synthetic data; no safety certification',
                 baseline=baseline,degraded_one_vehicle=degraded,stochastic=stochastic,
                 traceability=trace,verification_results=checks,
                 all_fixture_checks_pass=all(checks.values()))
    path=output/'results.json'
    path.write_text(json.dumps(results,indent=2)+'\n',encoding='utf-8')
    with (output/'dispatch-assignments.csv').open('w',newline='',encoding='utf-8') as f:
        writer=csv.DictWriter(f,fieldnames=list(baseline['assignments'][0]));writer.writeheader();writer.writerows(baseline['assignments'])
    sums={name:hashlib.sha256((data/name).read_bytes()).hexdigest() for name in
        ['config.json','requests.csv','requirements.csv','verification-matrix.csv','hazards.csv']}
    (output/'input-hashes.json').write_text(json.dumps(sums,indent=2)+'\n',encoding='utf-8')
    return results

def no_vehicle_overlap(assignments):
    per={}
    for a in assignments:
        if a['status']!='completed':continue
        per.setdefault(a['vehicle'],[]).append((a['start_min'],a['finish_min']))
    for trips in per.values():
        for first,second in zip(sorted(trips),sorted(trips)[1:]):
            if first[1]>second[0]+1e-9:return False
    return True

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--output',default=None)
    opts=p.parse_args();out=run(opts.output)
    print(json.dumps({'fixed_scenario_pass':out['baseline']['demonstration_pass'],
                      'degraded_scenario_pass':out['degraded_one_vehicle']['demonstration_pass'],
                      'trace_links_pass':out['traceability']['link_integrity_pass'],
                      'fixture_tests_pass':out['all_fixture_checks_pass']},indent=2))
