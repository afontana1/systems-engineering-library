# Hypothetical Laboratory 02 — Analyze stakeholders, mission, scenarios, outcomes, and measures in the authoritative model

*Book 9 · EN.645.632 · fictional Northstar rehearsal; this is not the graded course assignment.*

## A new problem arrives

The engineering review board is about to decide whether a proposed Northstar change can proceed. The team presents the following preliminary argument:

> An operational goal of 90% completed accessible trips is not interchangeable with average wait under 12 minutes. If 42 of 50 accessible requests complete, the observed 84% is below the goal, irrespective of fleet-wide wait performance. Model separate denominators, operational conditions, and a decision owner.

Your responsibility is to **challenge, reproduce and bound** that argument. All facts and values are synthetic. There is no real-world performance or safety claim in this lab.

## Lab packet and required files

Start with the supplied `datasets/course-645-632-case.csv` and the mathematical or modeling walkthrough in [Chapter 2](../chapters/02-analyze-stakeholders-mission-scenarios-outcomes-and-measures-in-the-.md). Save the following editable artifacts using Week 2 IDs:

1. `w02-decision.md` — the decision, two alternatives and who bears the consequence;
2. `w02-model.md` — definitions, units, equations or architecture/causal model, assumptions, and sensitivity check;
3. `w02-evidence.csv` — `claim,source,configuration,method,result,limitation,status`;
4. `w02-review.md` — one serious objection, its proposed test, and your revised recommendation.

### Experiment or investigation

1. Reproduce the chapter's worked engineering example. **Do not use the answer in the source guide as a substitute for a derivation.**
2. Change one factor relevant to **analyze stakeholders, mission, scenarios, outcomes, and measures in the authoritative model**. If the method is statistical, change the population or dependence assumption. If it is dynamic, change a rate or delay. If it is model-based, remove or contradict an essential relation. If it is decision analysis, change a constraint or declared preference.
3. Record whether your preferred answer changes, becomes uncertain, or remains robust. Explain *why* in model terms.
4. Define a falsifiable acceptance/decision criterion and the observation or review necessary to apply it. Separate simulated results from real validation evidence.
5. State at least two limitations: one about model structure, one about evidence or applicability.

## Independent numerical checkpoint

**Solve before opening guidance:** If demand rises 30% from 20 to 26 requests/hour while modeled capacity is 24/hour, calculate the nominal capacity gap.

<details><summary>Reference computation and engineering interpretation</summary>

The gap is 26−24=2 requests/hour. This is an arithmetic screening calculation; burstiness and queue buildup require a dynamic model.

**Challenge:** The computation's assumptions are part of the claim. Check units, sample construction, parameter source and whether the number is a metric on the population you care about. The model can be correct and still unfit for an operational readiness decision.

</details>

## Review board prompts

- What is the decision and the credible alternative to the team's preferred recommendation?
- What would change if the adverse scenario were more common than assumed?
- Which single additional measurement, model check, or controlled experiment has the greatest chance of changing the decision?
- Can another engineer reproduce this conclusion with the files, units and configuration identifiers provided?

**Self-rating (10 points):** decision clarity 2; reproducible model 2; adverse case and sensitivity 2; evidence and assumptions 2; honest limitations and review response 2. An excellent lab may conclude **defer pending evidence** rather than approve.

## Return to assessed course work

Once you can defend your lab reasoning, return to [Course Week 2](../../../C/P3/EN645632.md) and produce the full independent submission under the original rubric. See [Chapter 2](../chapters/02-analyze-stakeholders-mission-scenarios-outcomes-and-measures-in-the-.md) for the linked explanation. Do not submit this fictional exercise as field or operational evidence.
