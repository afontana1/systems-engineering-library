# A07 — Independent review and engineering decision gates

**Competency:** write a review decision that separates local software correctness from model credibility, safety, and authorization.

## A review is not a victory presentation

A review board examines the claims a project makes, the evidence offered for those claims, credible alternative explanations, and the consequences of being wrong. The advanced lab is designed to produce unfavorable data deliberately. A one-vehicle outage halves completions on the fixed teaching fixture; message loss and telemetry blocking create different failure signatures. These are reasons to refine the design and the safety argument, not reasons to discard the scenarios.

The [review gates](../review/evidence-gates.csv) include graph integrity, interface idempotency, failure observability, nonoverlap, statistical reproducibility, provenance, and field readiness. The field-readiness gate is marked **FAIL** because it would require operational validation, credible hazard mitigation and an accountable approval process. Nothing in the package provides those things.

## Three levels of possible conclusion

1. **Simulation code behaves according to its declared toy rules** under the tests: a plausible pass if tests and review support it.
2. **A particular design is promising for further study** under stated invented assumptions: an analytical conclusion with significant uncertainty.
3. **The system is safe or ready for field operation:** unsupported by this laboratory.

Confusing these levels is a systems engineering failure of argumentation, even when the code passes every unit test.

## Challenge sessions

Assign three roles: *designer* defends model choices, *test engineer* challenges failure coverage, *independent reviewer* asks which mechanisms have not been modeled. Each person should produce one **defeater**—a credible condition that would make an attractive claim false. Examples: simultaneous duplicate processing, partial stale telemetry rather than total outage, a customer group whose service duration differs, or a geographical bottleneck that breaks constant-trip assumptions.

A successful gate records its evidence, limitations, responsible reviewer and open actions. A failed gate records a disposition: redesign, gather evidence, narrow the intended use, or reject release. Avoid vague labels such as “acceptable risk” without risk ownership and acceptance authority.

## Practice and deliverable

**Exercise 1.** The graph audit passes. Can the board sign off on real-world interface integrity?

<details><summary>Worked answer</summary>No. It checked declared endpoints and links, not temporal behavior, external data integrity, failure recovery, security, interoperability in deployed environments or independent stakeholders' requirements.</details>

**Exercise 2.** What is the strongest defensible release decision for this package?

<details><summary>Worked answer</summary>Approve **continued laboratory learning and controlled synthetic experimentation**; do not approve external dispatch use, safety qualification or mission performance claims.</details>

**Submit:** a two-page review memo with supporting links, dissenting observations and explicit authorization limits. Related: [v11 review board](../../integrated-lab/review/REVIEW-BOARD.md).
