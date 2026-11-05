# Hypothetical Lab 3 — The Stakeholder Hearing

**Course link:** EN.645.662 Week 3 · **Book:** [Chapter 3](../chapters/03-needs-and-conops.md) · **Time:** 90–120 minutes · **Type:** stakeholder analysis and evidence design.

## Situation

You are given five fictitious statements: (1) “Every pickup should be under five minutes”; (2) “No rider should need an attendant to board”; (3) “Stop the system immediately when sensors become uncertain”; (4) “The two-vehicle budget cannot be exceeded”; (5) “We must be able to close a route at any time.” These statements come from different roles and are not mutually consistent.

## Your work

1. Record each raw quote unchanged in a stakeholder table. Write a separate interpreted need, intended outcome, source, and open conflict. Do not prematurely choose a technical architecture.
2. Draft one nominal trip scenario, one communications-loss scenario, and one accessible-boarding scenario. For each, identify actor, precondition, trigger, steps, exception path, and observed outcome.
3. Define two candidate MOEs, two MOPs, and one TPM. Explain the distinct decision each informs.
4. Use the fictional `request-outcomes.csv` dataset. Compute completion, timely-among-completed, and timely-among-eligible request proportions, first overall and then for each time period. Explain why these denominators differ.
5. Write a one-paragraph conflict-resolution recommendation to a sponsor. Note which decisions require additional accessibility or safety expertise.

## Deliverables

`LAB03_StakeholderRegister.csv`, `LAB03_Scenarios.md`, and `LAB03_MeasuresMemo.md`. Use the companion script `tools/service_measures.py` if desired; calculate at least one metric by hand first.

<details><summary>Reference logic and interpretive cautions</summary>

A need such as “predictable mobility” does not justify changing the original quote to “average pickup below five minutes.” Short waiting times are one possible measurable expression of service quality; accessibility, missed trips, and cancellation matter independently. Likewise, a two-vehicle cap should be recorded as a program constraint or assumption until its source and authority are established. The dataset is intentionally constructed so that a group can show favorable *timely among completed* performance while performing poorly on *eligible-request service*. A transparent analysis includes both the missed trips and the served-trip distribution.

</details>

## Transfer

The original Week 3 course guide requires a far larger stakeholder, scenario, and ConOps baseline. Treat this lab as a short experiment in thinking, not as the submitted baseline.
