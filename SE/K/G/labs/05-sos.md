# Laboratory — Network cuts and multi-agency interface agreements

*Advanced Graduate Practice · Synthetic Northstar case · Independent submission*

[Read the corresponding textbook chapter](../chapters/05-sos.html) · [Download the Python model](../code/system_models.py) · [Open notebook](../notebooks/05-sos.ipynb) · [Browse diagrams](../INDEX.html)

## Scenario and objective

A fictional regional emergency-transfer mission requires coordinated transport, road status, communication and hospital acceptance. Each organization controls its own change schedule. The integration board must defend an architecture against one constituent's withdrawal and one invalid interface assumption.

**Learning objective.** Construct a reproducible engineering argument in which a specific claim follows from explicitly justified assumptions, observable evidence and an appropriate analytical method. Your evaluation should distinguish model output from operational truth.

## Assigned investigation

1. Build a directed mission graph and run `reachable()` with an excluded bridge or constituent. Identify the smallest mission cut you can exhibit and list the unmodeled constraints.
2. Calculate `any_path_available(.9,.8)` with explicit independence assumptions. Describe two common-cause failures that violate them.
3. Update a `Beta(1,9)` interface-failure model after 2 failures and 18 successes; explain the prior and independence assumptions.
4. Draft a versioned authority and data-contract table for a road agency, operator, hospital, and dispatch vendor.
5. Design a migration exercise in which one participant changes corridor identifiers and another continues using an old revision. Explain the fallbacks and stop criteria.

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

For independent paths the at-least-one-path probability is 0.98. The Bayesian update is Beta(3,27) with mean 0.10. Neither figure covers shared roads, cross-agency conflict, or correlated emergency conditions. An effective architecture recommendation treats unsigned institutional agreements as feasibility gaps, not merely low weighted scores.

**Watch for:** confusing an accepted test with a validated mission claim; missing error or common-cause assumptions; silently excluding unsuccessful requests; asserting autonomy where authority is distributed; and treating simulation outputs as certification. A reviewer should be able to repeat the result and explain its domain of validity.
</details>

## Connection to assessed coursework

EN.645.771 System of Systems Engineering; EN.645.753 Enterprise Systems Engineering. This is ungraded hypothetical practice. Use the corresponding course guide for the graded engineering assignment and mastery gate; do not submit this reference response in place of independent work.
