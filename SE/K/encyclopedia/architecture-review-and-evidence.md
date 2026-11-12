# Architecture reviews: prove readiness for the next engineering commitment

**Reference entry · Concept design, system integration and assurance · Worked technical treatment**

## Reviews are structured decisions, not presentations

A **technical architecture review** examines whether an engineering baseline and its supporting evidence justify a specific next commitment: continued concept exploration, detailed design, integration, qualification, production or operation. Review labels such as SRR, PDR or CDR may have formal meanings within a program or agency. They are not interchangeable, and a collection of completed slides is not itself an engineering readiness argument.

Start by naming the decision: *May the team commit to detailed design of this interface and architecture under the declared operating envelope?* State the applicable requirements, approved concept and architecture baseline, major risks and uncertainties, decision authorities, dissenting findings and conditions for advancement. Separate “evidence exists” from “the evidence is strong enough for this decision.”

## A reviewable evidence thread

For a hypothetical Campus Mobility door interlock, a review packet could include:

| Claim | Evidence item | What it does **not** prove |
|---|---|---|
| Door opening is inhibited above declared speed | Configuration-labeled fault-injection tests | Reliability under all sensor common-cause failures |
| Signal freshness is defined at the boundary | ICD signal table with clock and timeout | Correctness of every deployed network timing path |
| Controller and requirement are linked | Typed allocation and test records | That the requirement captures every safety need |
| Architecture supports degraded mode | Mode-transition model and counterexamples | Field-operational validity of the abstract model |

These are **illustrative** artifacts and limitations. A review would have to confirm the exact hardware, software, environment, method, calibration and test scope before accepting the packet as applicable.

## Technical review flow

1. **Freeze the question and baseline:** version of architecture, requirements, ICDs, assumptions, hazards and alternatives.
2. **Show feasibility:** physical interfaces, budget equations, margins, technology readiness and integration constraints.
3. **Show design integrity:** consistent functions, allocations, behavior models, variant choices and verification approaches.
4. **Challenge the argument:** negative tests, independent review, unresolved anomalies and credible counterexamples.
5. **Record decisions:** accepted, conditional, deferred or rejected, with owners, evidence due dates and expiry conditions.
6. **Reopen on change:** changed requirements, new hazard mechanisms or configuration drift invalidate assumptions supporting an earlier decision.

A conditional exit should identify concrete closure criteria. “Risk to be watched” is not an acceptable substitute for a responsible owner, target evidence and review trigger.

## Quantifying margins without pretending away uncertainty

Suppose a model predicts power demand of 3.0 kW against a 3.2 kW architectural limit. Nominal margin is \(M=3.2-3.0=0.2\,\mathrm{kW}\), or \(6.25\%\) of the limit. If the predicted demand has meaningful uncertainty, the 0.2 kW difference cannot automatically be called an acceptable margin. Review the [parametric model](parametric-models-and-units.md), the uncertainty model and the acceptance decision rule. Margin definitions should use a documented denominator and avoid conflating design allowance, contingency and stochastic confidence.

## What the review should leave behind

A disciplined review yields a decision record, artifact index, controlled findings, residual risk register, change triggers and next-phase evidence plan. The purpose is to make later teams understand **why** a design was advanced, under which assumptions, and what must be revisited if the assumptions change.

## Pitfalls, exercise and references

Typical problems are demonstration-driven optimism, missing stakeholders, unversioned slides, green status without data, reviews that postpone critical interface decisions, and treating a conditional finding as automatically closed. For an architecture change from CM-B2 to CM-B3, classify each evidence row as transferable, conditionally transferable, invalid or unknown; explain the decision and required retest.

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — technical reviews, baselines and risk-based engineering decisions.
- [NASA Systems Modeling Handbook](https://standards.nasa.gov/node/3111) — model-backed engineering products and review views.
- Related: [design risk retirement](design-risk-retirement.md); [assurance cases](assurance-cases-and-evidence.md); [configuration assurance](configuration-assurance-and-change-control.md); [Campus Mobility artifacts](../methods/campus-mobility-engineering-artifacts.md).

*Scope:* The example is a teaching review framework, not an official program review checklist or release authorization.

## Step 02 deeper treatment: a numerical margin can change the release decision

**Worked example:** A controller must respond within 150 ms. The design review reports a measured 139 ms response and a declared one-sided 12 ms allowance for measurement, variation and decision conservatism. If the program's approved rule is “upper acceptance bound no greater than the limit,” then \(139+12=151\) ms **fails** the gate, even though the observed central value is below 150 ms. An architect cannot close the finding by rounding 139 down or by asking for more tests without a revised sampling plan. Options include improving the architecture, clarifying the guard-band model, or obtaining approval for a different risk-based rule *before* new data are interpreted.

A useful architecture review therefore couples a claim to numerical evidence, requirement configuration, accepted rule, responsible owner and corrective action. It records which negative or extreme environmental conditions were exercised, what simulations were calibrated, and what downstream interfaces will change if the finding requires redesign. The review outputs a **decision log** rather than a generic maturity score.

**Practice:** If the measured response is 134 ms using the same declared 12 ms allowance, the computed upper bound is 146 ms and passes this illustrative rule only for the tested configuration and modes. List three conditions—software build, power level, network load, temperature—that could invalidate a broader claim. See [NASA's Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) for review and technical assessment context.
