"""Reproducible arithmetic and small invariants in v51 illustrative worked examples.
Uses Python 3 stdlib only; no installation or network required.
This verifies listed computations, not the realism of their engineering assumptions.
"""
import math
checks={}
def record(name,ok):
 checks[name]=bool(ok)
def near(name,a,b,tol=1e-9):record(name,math.isclose(a,b,rel_tol=tol,abs_tol=tol))
# Agile life cycle
near('agile_total_lead_days',4+1+15,20)
near('agile_active_fraction',(4+1)/20,.25)
near('agile_reduced_total_days',2+1+15,18)
# Allocation
near('allocation_naive_peak_watts',200+150+120,470)
near('allocation_mode_peak_watts',max(200+150,120),350)
# Governance
near('authority_net_expected_k',120-60-.20*100,40)
# Interfaces
near('boundary_retry_backlog_delta', (16-10)*30,180)
# Complexity branching
near('branching_expected_total',1/(1-.8),5)
# Conservation
near('model_requests_remaining',0+180-167,13)
# ConOps metrics
near('conops_accepted_punctual',150/170*100,88.23529411764706)
near('conops_eligible_punctual',150/180*100,83.33333333333334)
near('conops_gap_pp',(150/170-150/180)*100,4.901960784313727)
# Enterprise stock balance
near('enterprise_initial_months',120/(8-3),24)
near('enterprise_slower_delta',3-4,-1)
near('enterprise_growth_delta',3-2,1)
# Physical common cause
near('physical_private_joint',.02**2,.0004)
near('physical_shared_top',.01+.99*.02**2,.010396)
# Integration
near('integration_serial_days',2+3+4,9)
near('integration_parallel_days',max(2,3)+4,7)
# Unit conversion
near('interface_speed_mps',72*1000/3600,20)
near('interface_unit_factor',72/20,3.6)
# Causal inference example
near('intervention_diff_in_diff_pp',(12-20)-(15-18),-5)
# Metrics
near('metrics_conditional',950/990*100,95.95959595959596)
near('metrics_eligible',950/1000*100,95)
# Mission chain
near('mission_availability',.95**3,.857375)
# Model dimensional analysis
near('model_energy_kwh',2*(30/60),1)
# Concurrency CAS single winner invariant
vehicle_state='free';successes=0
for request in ['r1','r2']:
 if vehicle_state=='free':vehicle_state='reserved';successes+=1
record('object_reservation_one_winner',successes==1)
# Risk expected values
near('risk_unmitigated_expected_k',.10*100,10)
near('risk_mitigated_expected_k',.03*100,3)
near('risk_net_expected_k',10-3-4,3)
# CI evidence
near('software_suite_pass_fraction',480/480,1)
# Percentile with nearest-rank convention
latencies=sorted([100]*95+[2100]*5)
near('software_latency_mean_ms',sum(latencies)/len(latencies),200)
near('software_latency_p95_ms',latencies[math.ceil(.95*len(latencies))-1],100)
near('software_latency_p99_ms',latencies[math.ceil(.99*len(latencies))-1],2100)
# SoS
near('sos_independent_feeds',.98*.97,.9506)
# Stakeholder subgroups
near('stakeholders_overall_rate',(90+2)/(100+10),92/110)
near('stakeholders_accessible_rate',2/10,.20)
near('stakeholders_general_rate',90/100,.90)
# SoI boundary
near('system_end_to_end_success',.99*.95,.9405)
# Traceability
near('traceability_link_coverage',72/80,.90)
near('traceability_current_closure',60/80,.75)
# View consistency
near('view_samples_per_second',1/.050,20)
near('view_rate_discrepancy',20/10,2)
# Earned-value extrapolation
near('wbs_cpi',200/250,.8)
near('wbs_eac_k',500/.8,625)
near('wbs_overrun_k',625-500,125)
failed=[k for k,v in checks.items() if not v]
print(f'v51 arithmetic/invariant checks: {len(checks)} total, {len(checks)-len(failed)} passed')
if failed:
 print('FAILED:',', '.join(failed))
 raise SystemExit(1)
