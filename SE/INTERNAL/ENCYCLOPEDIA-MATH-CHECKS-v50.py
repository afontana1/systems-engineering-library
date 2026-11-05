# Internal publishing QA, not a coursework assignment. Standard-library only.
# v50 audit: independent arithmetic checks for representative examples.
from math import log,sqrt,isclose
import math

checks={
 'risk_zero_trials_min': math.ceil(log(.05)/log(.99))==299,
 'zero_failure_upper': abs(1-math.pow(.05,1/299)-0.00997)<1e-4,
 'bayes_positive': isclose((.9*.2+.05*.8),.22),
 'bayes_post_positive': isclose(.9*.2/.22,9/11),
 'bayes_post_negative': isclose(.1*.2/.78,1/39),
 'EVSI': isclose(15000-(.22*15000+.02*100000),9700),
 'EVPI': isclose(15000-.2*15000,12000),
 'MM1_flow_lead': isclose(1/(12-11),1),
 'MM1_flow_wip': isclose(11/(12-11),11),
 'MM1_DES_wait': isclose((.75**2/(1-.75))/9*60,15),
 'DOE_A': isclose((10+4-14-12)/2,-6),
 'DOE_B': isclose((12+4-14-10)/2,-4),
 'DOE_AB_contrast':(14-10-12+4)==-4,
 'redundancy_common_cause': isclose(.01+.99*.02**2,.010396),
 'trade_A': isclose(.5*.75+.2*.32+.3*.50,.589),
 'trade_B': isclose(.5*.50+.2*.8+.3*.75,.635),
 'trade_switch':isclose(.296/.5,.592),
 'process_case_mix_initial':isclose(.8*.95+.2*.2,.8),
 'process_case_mix_new':isclose(.95*.95+.05*.2,.9125),
 'model_uncertainty':isclose(math.hypot(1,.6),1.1661903789690602),
 'resilience_integrated':isclose((1-.5)*6,3),
 'measurement_upper':isclose(59.5+1.2,60.7),
}

failed=[name for name,passed in checks.items() if not passed]
print(f"v50 independent arithmetic checks: {len(checks)-len(failed)}/{len(checks)} passed")
if failed: raise SystemExit("FAIL: "+", ".join(failed))
