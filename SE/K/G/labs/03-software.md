# Laboratory — Idempotency, timeouts and split authority

*Advanced Graduate Practice · Synthetic Northstar case · Independent submission*

[Read the corresponding textbook chapter](../chapters/03-software.html) · [Download the Python model](../code/system_models.py) · [Open notebook](../notebooks/03-software.ipynb) · [Browse diagrams](../INDEX.html)

## Scenario and objective

A passenger retries a reservation when the network acknowledgement is lost. Meanwhile two workers compete for the final seat, and an old regional leader issues a delayed departure command. The exercise investigates what exactly one reservation means when there is no single atomic transaction across every service.

**Learning objective.** Construct a reproducible engineering argument in which a specific claim follows from explicitly justified assumptions, observable evidence and an appropriate analytical method. Your evaluation should distinguish model output from operational truth.

## Assigned investigation

1. Run `ReservationService(1)` to confirm the same idempotency key/payload combination twice; verify one capacity change. Retry the key with a different payload and record the conflict.
2. Build a two-request concurrency schedule showing how check-then-decrement can accept two requests without atomicity; contrast it with a serialized reference outcome.
3. Evaluate `retry_amplification(80,.25,100)` and locate the first retry probability at which a 100/s server becomes nominally overloaded.
4. Specify the database constraint, transactional outcome record, event-outbox and downstream deduplication boundary. State which parts remain outside atomic control.
5. Introduce an epoch/fencing token to the route permission consumer and construct one stale-leader negative test.

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

The logical reference object preserves a single seat allocation for repeated commands but does **not** implement concurrent transactions. Geometric retries yield 106.7 attempts/second against 100/second processing capacity. A strong submission separates modeled invariants from the deployment mechanisms needed to enforce them under crashes, concurrency and partitions.

**Watch for:** confusing an accepted test with a validated mission claim; missing error or common-cause assumptions; silently excluding unsuccessful requests; asserting autonomy where authority is distributed; and treating simulation outputs as certification. A reviewer should be able to repeat the result and explain its domain of validity.
</details>

## Connection to assessed coursework

EN.605.704 Object-Oriented Analysis and Design; EN.645.764 Software Systems Engineering. This is ungraded hypothetical practice. Use the corresponding course guide for the graded engineering assignment and mastery gate; do not submit this reference response in place of independent work.
