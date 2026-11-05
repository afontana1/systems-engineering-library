# Laboratory — Operator workload and misleading alarms

*Advanced Graduate Practice · Synthetic Northstar case · Independent submission*

[Read the corresponding textbook chapter](../chapters/02-human.html) · [Download the Python model](../code/system_models.py) · [Open notebook](../notebooks/02-human.ipynb) · [Browse diagrams](../INDEX.html)

## Scenario and objective

A single operator oversees Northstar's emergency exceptions. During a storm, the intervention rate rises sharply. The operations team requests a second operator, while the interface team claims that a new alert design will solve the problem. You must distinguish workload capacity, information quality, decision authority, and human error.

**Learning objective.** Construct a reproducible engineering argument in which a specific claim follows from explicitly justified assumptions, observable evidence and an appropriate analytical method. Your evaluation should distinguish model output from operational truth.

## Assigned investigation

1. Compute M/M/1 baseline `mm1(5,8)` and storm `mm1(7,8)` waiting times. Explain why the model could be wrong during bursty correlated incidents.
2. Evaluate alarm positive predictive value for prevalence 1%, sensitivity 95%, false-positive rate 5%; then test a prevalence of 5% with unchanged detector characteristics.
3. Write an explicit authority-handoff protocol, including what happens to pending departure tokens and how a handoff is reversed after recovery.
4. Design a matched-participants usability experiment with counterbalanced order, predeclared severe-error criteria, and confidence interval reporting.
5. Write a staffing recommendation that distinguishes averages, tails, safety events, and institutional authorization constraints.

## Submission package

Submit: (1) a succinct claim and operating-context statement; (2) the baseline data and the exact parameters, model revision and run log; (3) at least two deliberate adverse or counterexample cases; (4) a traceability table from each claim to the supporting observation, model result or test; (5) a paragraph on statistical, model and institutional uncertainty; and (6) a **600–900 word engineering decision memo** with limitations and next experiments. Include any negative outcome, not just favorable runs. Use original work for the memo.

## Suggested evaluation rubric (100 points)

| Criterion | Points | Evidence expected |
|---|---:|---|
| Correct model and assumptions | 25 | Units, inputs, distributions, boundaries, invariants |
| Reproducible experiments | 20 | Fixed parameters, negative tests, captured outputs |
| Interpretation and counterevidence | 25 | Alternative causes, sensitivity and unproven claims |
| Engineering decision and constraints | 20 | Feasible recommendation, stop rules, owner responsibilities |
| Clarity and provenance | 10 | Tables, source revision, unambiguous figures |

## Instructor-style checkpoint — read only after attempting

<details><summary>Reference findings and common pitfalls</summary>

Queue delay increases from 12.5 minutes to 52.5 minutes as arrival rate rises from 5 to 7/hour for one 8/hour server. Under a 1% hazard base rate, only about 16.1% of alarms are true positives for the detector specified. These are model-based findings that require scenario-specific validation; neither one proves how a real operator will behave.

**Watch for:** confusing an accepted test with a validated mission claim; missing error or common-cause assumptions; silently excluding unsuccessful requests; asserting autonomy where authority is distributed; and treating simulation outputs as certification. A reviewer should be able to repeat the result and explain its domain of validity.
</details>

## Connection to assessed coursework

EN.645.768 System Design and Integration; EN.645.780 Agile Systems Engineering. This is ungraded hypothetical practice. Use the corresponding course guide for the graded engineering assignment and mastery gate; do not submit this reference response in place of independent work.
