# 6. Enterprise dynamics, equity and responsible intervention

*Graduate engineering sequence · Enterprise and Complex Systems · Regional mobility policy*

**Prerequisites:** Chapter 5, system dynamics, causal inference, decision analysis and critical systems thinking. **Courses:** Enterprise Systems Engineering, Management of Complex Systems, Systems Thinking and Dynamics.

## 6.1 An enterprise is not a large machine

An enterprise is a purposeful and adaptive collection of organizations, roles, incentives, policies, infrastructure and capabilities. Its goals are not always unified. A regional mobility initiative might seek shorter travel times, financial sustainability, reduced emissions, equitable access, resilient emergency response and political legitimacy. These objectives can conflict, and stakeholders may disagree about which outcomes count as success. An engineering intervention changes incentives and information flows as well as technical assets.

The 'system boundary' is therefore a claim that should be challenged. Counting only riders who successfully complete a trip may make a dispatch platform appear efficient while excluding people who cannot access the app, users whose requests are denied, rural communities lacking vehicles, and agencies bearing uncounted coordination burdens. The boundary of an evaluation determines which outcomes are visible. One of the most important graduate-level skills is to explain how a conclusion changes when the boundary or stakeholder population changes.

A useful enterprise model has several linked views: a capability map (what the enterprise must accomplish), an institutional map (who may decide and fund), an operational process model (how work and information move), a resource and financial model, and an outcome map (who benefits or bears risk). No one view is the enterprise. The views should share identifiers and revisions so that conflicting assumptions can be surfaced in review.

![Enterprise feedback and accountability](../diagrams/06-enterprise.svg)

## 6.2 Feedback loops and policy resistance

Policies often create their own feedback. Imagine a dispatch organization that responds to rising waiting times by penalizing teams whose average trip duration exceeds a target. Staff may prioritize short urban trips over long rural pickups. The recorded average improves, but rural access deteriorates. This is not necessarily fraud or individual incompetence; it is a predictable response to a narrow measure coupled to incentives.

A basic stock-flow model represents a backlog $B(t)$ of unresolved transport needs:

$$
\frac{dB}{dt}=d(t)-s(B,C),
$$

where $d(t)$ is incoming demand and $s$ is service completion depending on backlog and capacity $C$. If service rate is capped at 10 needs/hour while demand is 12/hour, the backlog grows at 2/hour under constant conditions. Raising the dispatch software's message throughput will not remove the physical capacity constraint. A more elaborate system can include recruitment, vehicle maintenance, public trust, induced demand, and delayed policy effects.

An Euler approximation $B_{k+1}=\max(0,B_k+\Delta t[d_k-s_k])$ is useful for a first model, but step size and discontinuous policy rules can create numerical artifacts. For a 4-hour horizon, initial backlog 8, demand 12/hour, service 10/hour, the simple model gives $B(4)=16$. That is a **conditional scenario**, not a forecast of actual communities. Demand, service capacity, cancellations, triage and operating hours would need empirical calibration.

## 6.3 Optimization can shift burdens

An aggregate objective can hide unequal outcomes. Suppose urban trips wait an average of 8 minutes and rural trips wait 35 minutes, with 90 urban and 10 rural trips. The population-weighted average is $(90\cdot8+10\cdot35)/100=10.7$ minutes. Another policy could deliver 11 minutes for both groups, raising the overall mean slightly while greatly reducing disparity. Which is 'better' depends on obligations, constraints and stakeholder priorities, not on arithmetic alone.

Several equity measures are possible: maximum group waiting time, difference or ratio between group means, rejection rate by area, service coverage, affordability, accessibility for disabled riders, and exposure to dangerous conditions. No scalar fairness metric captures all harms. Some categories may be sensitive or inappropriate to collect, and small subgroups require careful privacy and uncertainty treatment. Define an outcomes measurement plan and governance process before selecting an optimizer.

Use a *constrained multiobjective* formulation. For decision vector $x$, one possible problem is

$$
\min_x \{E[W(x)],\ Cost(x),\ Emissions(x)\}\quad\text{subject to }\max_g E[W_g(x)]\le W_{max},\ Safety(x)=true.
$$

The safety statement is shorthand for a defined set of verifiable constraints; it is not a numeric function unless formalized. If no feasible design satisfies all hard constraints, the correct output is **infeasible**, not an arbitrary weighted compromise. Pareto analysis can describe tradeoffs among feasible designs; it cannot decide by itself whose welfare should prevail.

## 6.4 Causal evaluation of an enterprise intervention

A before/after improvement may be caused by seasonal demand, staffing, weather, a simultaneous policy change or regression to the mean. Consider evaluating a new routing program with a comparison region. In a simple difference-in-differences illustration, the treated region's average wait drops from 24 to 17 minutes, while the comparison region drops from 20 to 18. The estimated treatment effect is

$$
\widehat{\delta}_{DiD}=(17-24)-(18-20)=-5\text{ minutes}.
$$

This subtracts the 2-minute general improvement to estimate a 5-minute additional decline. The result has a causal interpretation only under assumptions such as parallel counterfactual trends, no differential contemporaneous shocks, appropriate group composition, and limited interference or spillover. A regional intervention may violate the no-spillover assumption if vehicles or passengers cross boundaries. Plot pre-intervention trends, test alternative controls, and investigate mechanisms before attributing the full change to the program.

The average effect may mask adverse subgroups. Repeat analyses by geography, disability-access needs, trip urgency and other legitimate operational strata where data handling is appropriate. Avoid treating an apparent overall improvement as proof that every stakeholder benefits.

## 6.5 Critical boundary critique

Complex public systems require questions beyond technical feasibility: who defined the problem? Who counts as a beneficiary? Who bears cost without representation? Who can challenge data and decision rules? Whose interpretation of 'successful trip' is privileged? Who is responsible for unintended harms? These questions are not substitutes for mathematical models; they define the scope and legitimacy of their use.

One plausible boundary choice treats declined requests as zero waiting time because no ride was completed. The average-completed-trip wait can improve even while access deteriorates. Another choice excludes maintenance staff from 'users' of the system, hiding an unsafe workload increase. A third assumes all agencies consent to a global optimizer, hiding governance feasibility. A good analysis shows these choices and tests alternative boundaries.

## 6.6 Governance and learning loops

An intervention should have a *theory of change*: what actions affect which mechanisms, with which delays, under what assumptions, and with what possible unintended consequences? State the decision rights for funding, local exceptions, data use, auditing and stopping unsafe programs. Design pilot measures to detect both intended improvements and displacement harms. A reversible pilot with clear stop criteria is often better evidence than a large irreversible rollout based only on a persuasive simulation.

For Northstar, the review board could demand: no unsafe route permissions; subgroup service levels within approved bounds; no hidden exclusion of rejected requests; resilience to at least one constituent outage; a configuration-specific evidence report; and a public process for challenging outcomes. Some values will remain contested. A legitimate engineering recommendation should identify unresolved disagreement instead of falsely presenting a single 'optimal' social objective.

## Problems — solve first

1. Demand is 14/hour and service capacity is 11/hour for five hours, with initial backlog 3. Under constant-flow assumptions, what is the final backlog?
2. Urban trips: 80 trips at 9 minutes; rural trips: 20 trips at 30 minutes. Compute aggregate mean. A new allocation yields 12 minutes for each group. Compare the mean and equity implications.
3. A treated region changes from 30 to 20 minutes, a comparison region from 25 to 22. Compute the illustrative difference-in-differences effect; state two threats to its causal meaning.
4. A successful-trip metric excludes rejected passengers and unserved areas. Describe a revised dashboard, accountability structure, and pilot stop rule.

<details><summary>Worked solutions</summary>

1. $B(5)=3+(14-11)5=18$ unresolved needs, assuming constant rates, no cancellations, and sufficient demand for the service to operate at its cap.
2. $(80\cdot9+20\cdot30)/100=13.2$ minutes. The uniform 12-minute option lowers the overall mean to 12 and substantially reduces the disparity, but could have other resource or mission costs requiring evaluation.
3. $(20-30)-(22-25)=-7$ minutes. Differential weather, group composition, pre-existing trends, and cross-region spillover could invalidate the counterfactual inference.
4. Track acceptance/rejection, request-to-service time, group coverage, accessibility, safety and cost. Give affected communities and constituent owners a review path. Pause expansion if a specified safety or severe access inequity threshold is crossed, pending investigation.
</details>

## Practicum and references

[Run the intervention-evaluation laboratory](../labs/06-enterprise.html) · [Python model](../code/system_models.py) · [Notebook](../notebooks/06-enterprise.ipynb). The assessed course deliverable should contain explicit boundary choices, stakeholder assumptions, sensitivity analysis and a reviewable intervention plan.

**Further reading:** Systems Engineering Body of Knowledge (SEBoK) enterprise and complex-systems discussions; NASA Systems Engineering Handbook. The numerical example is synthetic, not a claim about an actual region.
