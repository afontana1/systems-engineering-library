# Hypothetical Laboratory 04 — Use estimation, confidence intervals, hypothesis, equivalence, and engineering significance

*Book 10 · EN.645.756 · fictional Northstar rehearsal; this is not the graded course assignment.*

## A new problem arrives

The engineering review board is about to decide whether a proposed Northstar change can proceed. The team presents the following preliminary argument:

> An estimated mean reduction of 0.4 minutes with 95% CI [0.1,0.7] can be statistically distinguishable from zero yet below a 1-minute engineering threshold. Failure to reject a difference is not an equivalence test; predefine the equivalence region.

Your responsibility is to **challenge, reproduce and bound** that argument. All facts and values are synthetic. There is no real-world performance or safety claim in this lab.

## Lab packet and required files

Start with the supplied `datasets/course-645-756-case.csv` and the mathematical or modeling walkthrough in [Chapter 4](../chapters/04-use-estimation-confidence-intervals-hypothesis-equivalence-and-engin.md). Save the following editable artifacts using Week 4 IDs:

1. `w04-decision.md` — the decision, two alternatives and who bears the consequence;
2. `w04-model.md` — definitions, units, equations or architecture/causal model, assumptions, and sensitivity check;
3. `w04-evidence.csv` — `claim,source,configuration,method,result,limitation,status`;
4. `w04-review.md` — one serious objection, its proposed test, and your revised recommendation.

### Experiment or investigation

1. Reproduce the chapter's worked engineering example. **Do not use the answer in the source guide as a substitute for a derivation.**
2. Change one factor relevant to **use estimation, confidence intervals, hypothesis, equivalence, and engineering significance**. If the method is statistical, change the population or dependence assumption. If it is dynamic, change a rate or delay. If it is model-based, remove or contradict an essential relation. If it is decision analysis, change a constraint or declared preference.
3. Record whether your preferred answer changes, becomes uncertain, or remains robust. Explain *why* in model terms.
4. Define a falsifiable acceptance/decision criterion and the observation or review necessary to apply it. Separate simulated results from real validation evidence.
5. State at least two limitations: one about model structure, one about evidence or applicability.

## Independent numerical checkpoint

**Solve before opening guidance:** An event occurs 0 times in n=30 independent Bernoulli trials. Compute the exact one-sided 95% upper failure-probability bound.

<details><summary>Reference computation and engineering interpretation</summary>

p_upper = 1−0.05^(1/30) ≈ 0.0950. The result does not demonstrate failure probability below 1%.

**Challenge:** The computation's assumptions are part of the claim. Check units, sample construction, parameter source and whether the number is a metric on the population you care about. The model can be correct and still unfit for an operational readiness decision.

</details>

## Review board prompts

- What is the decision and the credible alternative to the team's preferred recommendation?
- What would change if the adverse scenario were more common than assumed?
- Which single additional measurement, model check, or controlled experiment has the greatest chance of changing the decision?
- Can another engineer reproduce this conclusion with the files, units and configuration identifiers provided?

**Self-rating (10 points):** decision clarity 2; reproducible model 2; adverse case and sensitivity 2; evidence and assumptions 2; honest limitations and review response 2. An excellent lab may conclude **defer pending evidence** rather than approve.

## Return to assessed course work

Once you can defend your lab reasoning, return to [Course Week 4](../../../C/P3/EN645756.md) and produce the full independent submission under the original rubric. See [Chapter 4](../chapters/04-use-estimation-confidence-intervals-hypothesis-equivalence-and-engin.md) for the linked explanation. Do not submit this fictional exercise as field or operational evidence.
