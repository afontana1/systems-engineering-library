# Hypothetical Laboratory 07 — Reframe the engineering design problem and generate alternatives through morphology

*Book 14 · EN.645.784 · fictional Northstar rehearsal; this is not the graded course assignment.*

## A new problem arrives

The engineering review board is about to decide whether a proposed Northstar change can proceed. The team presents the following preliminary argument:

> A morphological table combines choices for energy source, dispatch mode and fleet size. Three sources × two modes × three sizes yield 18 nominal combinations, but incompatibilities and constraints may reduce feasible designs.

Your responsibility is to **challenge, reproduce and bound** that argument. All facts and values are synthetic. There is no real-world performance or safety claim in this lab.

## Lab packet and required files

Start with the supplied `datasets/course-645-784-case.csv` and the mathematical or modeling walkthrough in [Chapter 7](../chapters/07-reframe-the-engineering-design-problem-and-generate-alternatives-thr.md). Save the following editable artifacts using Week 7 IDs:

1. `w07-decision.md` — the decision, two alternatives and who bears the consequence;
2. `w07-model.md` — definitions, units, equations or architecture/causal model, assumptions, and sensitivity check;
3. `w07-evidence.csv` — `claim,source,configuration,method,result,limitation,status`;
4. `w07-review.md` — one serious objection, its proposed test, and your revised recommendation.

### Experiment or investigation

1. Reproduce the chapter's worked engineering example. **Do not use the answer in the source guide as a substitute for a derivation.**
2. Change one factor relevant to **reframe the engineering design problem and generate alternatives through morphology**. If the method is statistical, change the population or dependence assumption. If it is dynamic, change a rate or delay. If it is model-based, remove or contradict an essential relation. If it is decision analysis, change a constraint or declared preference.
3. Record whether your preferred answer changes, becomes uncertain, or remains robust. Explain *why* in model terms.
4. Define a falsifiable acceptance/decision criterion and the observation or review necessary to apply it. Separate simulated results from real validation evidence.
5. State at least two limitations: one about model structure, one about evidence or applicability.

## Independent numerical checkpoint

**Solve before opening guidance:** Alternative A scores 0.8 on cost and 0.6 on reliability, while B scores 0.5 and 0.9. At cost weight w, derive the preference switching point.

<details><summary>Reference computation and engineering interpretation</summary>

A=0.6+0.2w; B=0.9−0.4w. Equate them: 0.6w=0.3, so w=0.5. Feasibility and scaling of value scores remain separate questions.

**Challenge:** The computation's assumptions are part of the claim. Check units, sample construction, parameter source and whether the number is a metric on the population you care about. The model can be correct and still unfit for an operational readiness decision.

</details>

## Review board prompts

- What is the decision and the credible alternative to the team's preferred recommendation?
- What would change if the adverse scenario were more common than assumed?
- Which single additional measurement, model check, or controlled experiment has the greatest chance of changing the decision?
- Can another engineer reproduce this conclusion with the files, units and configuration identifiers provided?

**Self-rating (10 points):** decision clarity 2; reproducible model 2; adverse case and sensitivity 2; evidence and assumptions 2; honest limitations and review response 2. An excellent lab may conclude **defer pending evidence** rather than approve.

## Return to assessed course work

Once you can defend your lab reasoning, return to [Course Week 7](../../../C/P3/EN645784.md) and produce the full independent submission under the original rubric. See [Chapter 7](../chapters/07-reframe-the-engineering-design-problem-and-generate-alternatives-thr.md) for the linked explanation. Do not submit this fictional exercise as field or operational evidence.
