# Laboratory — Regional outage, replay and mission recovery

*Advanced Graduate Practice · Synthetic Northstar case · Independent submission*

[Read the corresponding textbook chapter](../chapters/04-resilience.html) · [Download the Python model](../code/system_models.py) · [Open notebook](../notebooks/04-resilience.ipynb) · [Browse diagrams](../INDEX.html)

## Scenario and objective

Two booking-service replicas share a regional identity provider and a route cache. The service dashboard declares recovery when the API health check returns green, but some permissions and reservations still refer to old configuration revisions. You must determine which redundancy and recovery claims are actually justified.

**Learning objective.** Construct a reproducible engineering argument in which a specific claim follows from explicitly justified assumptions, observable evidence and an appropriate analytical method. Your evaluation should distinguish model output from operational truth.

## Assigned investigation

1. Calculate `serial_availability(.995,.995,.995)` and `parallel_common_cause(.98,.01,2)`; compare both with naive independence assumptions.
2. Calculate the nominal monthly failure budget for 300,000 eligible requests at a 99.95% success objective.
3. Design fault injection for an identity-service outage, duplicate event replay, route-token expiry, partial event-store corruption and a delayed consumer after leader failover.
4. Define independent checkpoints for process recovery, data reconciliation and safety-authorized mission resumption. Record configuration hashes and operator approvals.
5. Prepare an assurance-claim table showing which evidence supports availability, which supports route safety, and which supports recovery. Identify gaps that remain unproven.

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

Three independent serial 99.5% services provide about 98.51% path availability. Two 98% local replicas with a 1% system-wide outage achieve 98.9604% under the specified model, not 99.96%. The nominal 99.95% SLO allows 150 failed eligible requests among 300,000; hazardous commands require separate assessment.

**Watch for:** confusing an accepted test with a validated mission claim; missing error or common-cause assumptions; silently excluding unsuccessful requests; asserting autonomy where authority is distributed; and treating simulation outputs as certification. A reviewer should be able to repeat the result and explain its domain of validity.
</details>

## Connection to assessed coursework

EN.645.764 Software Systems Engineering; EN.645.782 Digital and Mission Engineering. This is ungraded hypothetical practice. Use the corresponding course guide for the graded engineering assignment and mastery gate; do not submit this reference response in place of independent work.
