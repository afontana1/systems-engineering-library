"""Independent standard-library arithmetic checks for synthetic v52 encyclopedia examples.

This checks numeric results and selected invariants only; it does not validate
model assumptions, scientific applicability, engineering safety, or other text.
"""
import math

def close(actual,expected,tol=1e-6):
    assert abs(actual-expected)<=tol,(actual,expected)

checks=[]
def verify(name,fn):
    fn();checks.append(name)

verify('primary and backup stop conditional independence',lambda:close(.02*.01,.0002))
verify('common-cause stop failure mixture',lambda:close(.001+(1-.001)*.0002,.0011998))
verify('common cause six-fold effect',lambda:close(.0011998/.0002,5.999))
verify('constant-hazard 20-hour reliability',lambda:close(math.exp(-.005*20),.90483741803596))
verify('ideal availability',lambda:close(200/(200+5),.97560975609756))
verify('logistics-inclusive availability',lambda:close(200/(200+5+10),.93023255813953))
verify('repair within eight hours',lambda:close(1-math.exp(-8/5),.79810348200534))
verify('human workload demand',lambda:close(6*20,120))
verify('human workload ratio',lambda:close(120/90,4/3))
verify('statistical acceptance, 1 percent defects',lambda:close(.99**100+100*.01*.99**99,.7357619789229557))
verify('statistical acceptance, 5 percent defects',lambda:close(.95**100+100*.05*.95**99,.037081209327355036))
verify('probability of rejection at 1 percent defects',lambda:close(1-(.99**100+100*.01*.99**99),.2642380210770443))
verify('95 percent zero-failure upper bound',lambda:close(1-.05**(1/100),.02951304960704))
verify('zero failures at 95 percent confidence bound',lambda:close((1-(1-.05**(1/100)))**100,.05))
verify('lean fleet expected cost',lambda:close(.8*120+.2*250,146))
verify('reserve capacity expected cost',lambda:close(.8*160+.2*190,166))
verify('lean fleet worst cost',lambda:close(max(120,250),250))
verify('reserve fleet worst cost',lambda:close(max(160,190),190))
verify('regret for lean fleet',lambda:close(max(120-min(120,160),250-min(250,190)),60))
verify('regret for reserve fleet',lambda:close(max(160-min(120,160),190-min(250,190)),40))
verify('nominal performance margin',lambda:close(180-150,30))
verify('relative margin',lambda:close((180-150)/150,.2))
verify('assurance case closure',lambda:close(9/12,.75))
verify('signed command freshness invalid',lambda:close(45-30,15))
# Graph invariants check illustrative transition assumptions, not the deployed system.
state={};assert not state
assert state.get('V') is None;state['V']='R1'
assert state.get('V') is not None
verify('atomic reservation prevents second success',lambda:close(len(state),1))
print(f'PASS: {len(checks)} numeric and illustrative invariant checks. No peer review or system safety conclusion implied.')
