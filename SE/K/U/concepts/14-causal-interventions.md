# 14 · Causal interventions, emergence, and equitable evaluation

**Concept dossier · systems dynamics / process improvement / management of complex systems**

## Prediction is not intervention evidence

A model may predict that high demand accompanies long waits. That does not establish that demand alone *causes* delays or that increasing fleet size is the best intervention. Causal analysis asks what would happen to an outcome if an action were taken, compared with an appropriate counterfactual. In complex systems, actors adapt to policy: users alter behavior, providers change participation, managers change incentives and the intervention changes the conditions being measured.

## Draw a minimal causal story

Suppose a dispatch team proposes “more automated assignments will reduce waiting.” Potential pathways include:

- Automation → faster assignment → shorter wait (desired path).
- Automation → more incorrect assignments → cancellations → longer total journey (unintended path).
- Automation → reduced operator oversight → missed accessibility conditions (equity risk).
- Peak demand → both automation adoption and longer wait (confounder if pilots start during busy periods).

A causal diagram reveals that “before versus after” is not necessarily an effect estimate. It also forces identification of outcomes that aggregate wait measures omit.

## Difference-in-differences: a careful illustration

Two comparable regions have average eligible-trip completion rates before and after a pilot:

| Region | Before | After | Change |
|---|---:|---:|---:|
| Pilot | 80% | 89% | +9 percentage points |
| Comparison | 83% | 87% | +4 percentage points |

The difference-in-differences estimate is `9 − 4 = +5 percentage points`. Interpretation as a causal effect depends on a credible **parallel trends** assumption without the intervention, consistent outcome definitions, minimal spillover and absence of simultaneous differential shocks. With only one pre-period, parallel trends cannot be credibly tested. This calculation is a teaching illustration, not causal proof.

## Emergence and adaptation

System behavior emerges from interactions and feedback: no individual dispatcher intends a retry storm, yet local retry logic can produce one. No single manager intends a rework crisis, yet deadline pressure, hidden technical debt and delayed reviews can jointly create it. Emergence does not imply unpredictability in every respect; it indicates that understanding isolated parts is insufficient for system-level reasoning.

Interventions may need **safe-to-learn probes** rather than a single irreversible rollout: deploy a bounded pilot, define guardrails and stop criteria, gather multiple forms of evidence, check distributional consequences, and revise the theory of change. Safety-critical interventions may require formal qualification before even limited deployment.

## Equity is a system property, not a reporting appendix

A service might improve average waiting time while excluding low-volume neighborhoods. Disaggregate metrics along dimensions justified by stakeholders and lawful data governance: accessible trips, neighborhoods, time of day, disruption conditions and complaint channels. But disaggregation by itself does not settle ethical questions—decision rights, privacy, participation, burden sharing and remediation matter.

A critical-systems inquiry also asks who defined the boundary, who was allowed to participate, who benefits, who bears risks and who can challenge the success criteria. A technical solution can be locally effective and still illegitimate or undesirable at the enterprise level.

## Exercise with answers

**A.** Why might completion rate rise after a pilot even if the pilot has no effect? **Answer:** seasonal demand, staffing changes, selection of easier requests, or altered outcome definitions can explain the rise.

**B.** What does the +5-point difference-in-differences estimate require? **Answer:** among other things, plausible parallel trends and no important differential contemporaneous changes or spillovers.

**C.** Is maximizing the average outcome sufficient? **Answer:** not when critical constraints, tail risks, distributional harms and stakeholder rights matter.

**Transfer artifact:** causal influence diagram, measurement plan with counterfactual logic, equity impact questions, pilot guardrails and a learning/rollback protocol.

## Connections

[Outcomes and stakeholders](01-outcomes-boundaries.md) · [Experimental evidence](07-experimental-evidence.md) · [Systems of systems governance](13-sos-enterprise-governance.md) · [Queue feedback](09-queues-feedback.md).  
**Existing primer:** [Intervention and learning](../../encyclopedia/intervention-and-learning.md).
