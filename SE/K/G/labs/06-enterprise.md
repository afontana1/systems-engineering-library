# Laboratory — Policy feedback, causal evidence and subgroup outcomes

*Advanced Graduate Practice · Synthetic Northstar case · Independent submission*

[Read the corresponding textbook chapter](../chapters/06-enterprise.html) · [Download the Python model](../code/system_models.py) · [Open notebook](../notebooks/06-enterprise.ipynb) · [Browse diagrams](../INDEX.html)

## Scenario and objective

A regional board funds a faster dispatch algorithm. The average completion time improves, but rural rejections rise and staffing decisions change. The enterprise team must decide whether to scale the program, redesign incentives, or halt the rollout. This is a contested intervention, not just a throughput optimization.

**Learning objective.** Construct a reproducible engineering argument in which a specific claim follows from explicitly justified assumptions, observable evidence and an appropriate analytical method. Your evaluation should distinguish model output from operational truth.

## Assigned investigation

1. Calculate `backlog(8,12,10,4)` and explain the capacity assumption, missing cancellations and how backlog interacts with public confidence.
2. Calculate `subgroup_mean([(90,8),(10,35)])` and compare with 11-minute uniform outcomes. Explain why the preferred policy depends on obligations and costs.
3. Compute `difference_in_differences(24,17,20,18)`; create two counterexamples to the parallel-trends assumption and a possible spillover mechanism.
4. Write an explicit causal theory of change linking investment, capacity, operator behavior, access, demand and trust. Mark delays and reinforcing loops.
5. Propose an enterprise review charter with stakeholder participation, hard safety and access limits, funding authority, transparent measures, and a stop/revision decision.

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

Under constant rates, backlog rises to 16 needs after four hours; the initial weighted mean is 10.7 minutes; the illustrative DiD is −5 minutes. None is an unconditional real-world effect. A strong decision memo explores policy-induced rejection and subgroup effects, includes adverse evidence, and states who has authority to amend the decision.

**Watch for:** confusing an accepted test with a validated mission claim; missing error or common-cause assumptions; silently excluding unsuccessful requests; asserting autonomy where authority is distributed; and treating simulation outputs as certification. A reviewer should be able to repeat the result and explain its domain of validity.
</details>

## Connection to assessed coursework

EN.645.753 Enterprise Systems Engineering; EN.645.742 Management of Complex Systems. This is ungraded hypothetical practice. Use the corresponding course guide for the graded engineering assignment and mastery gate; do not submit this reference response in place of independent work.
