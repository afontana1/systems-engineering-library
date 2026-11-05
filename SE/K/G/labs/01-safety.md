# Laboratory — Stale authority and controlled departure

*Advanced Graduate Practice · Synthetic Northstar case · Independent submission*

[Read the corresponding textbook chapter](../chapters/01-safety.html) · [Download the Python model](../code/system_models.py) · [Open notebook](../notebooks/01-safety.ipynb) · [Browse diagrams](../INDEX.html)

## Scenario and objective

A regional corridor closes during an active departure window. A signed route permission is already in transit. The scheduler has limited information about the road authority's clock, and an emergency dispatcher asks for a degraded-mode exception. The objective is to decide which departure actions must be refused and what evidence a review board would need to approve a controlled exception.

**Learning objective.** Construct a reproducible engineering argument in which a specific claim follows from explicitly justified assumptions, observable evidence and an appropriate analytical method. Your evaluation should distinguish model output from operational truth.

## Assigned investigation

1. Run `conservative_age(18,4,7,3)` and compare the result against a 30-second evidence-age budget. Record the nominal and conservative margins.
2. Use `authorize()` for four conditions: fresh correct-scope data; stale but validly signed data; current data with invalid scope; current data with a previous configuration revision. Preserve the rejected cases in the result table.
3. Construct a loss–hazard–constraint–unsafe-action table with at least two causal scenarios for each hazard. Do **not** call a signature check an independent route validation.
4. Propose a temporary degraded mode that retains access for emergency transfers while bounding the permission's spatial, temporal and institutional scope.
5. Trace each proposed constraint to a test, operator instruction, monitoring record, and stop criterion.

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

Under the stipulated timing budget, nominal delay is 29 seconds and conservative age is 32 seconds; a 30-second requirement cannot be substantiated. The authorization predicate rejects old, unauthorized or wrong-revision evidence even if its digital signature is valid. A good answer explains why that predicate is a teaching proxy, not cryptographic verification, and does not claim a real road-safety outcome.

**Watch for:** confusing an accepted test with a validated mission claim; missing error or common-cause assumptions; silently excluding unsuccessful requests; asserting autonomy where authority is distributed; and treating simulation outputs as certification. A reviewer should be able to repeat the result and explain its domain of validity.
</details>

## Connection to assessed coursework

EN.645.768 System Design and Integration; EN.645.769 System Test and Evaluation. This is ungraded hypothetical practice. Use the corresponding course guide for the graded engineering assignment and mastery gate; do not submit this reference response in place of independent work.
