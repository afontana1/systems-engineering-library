# Practice lab: State machines, contracts, and distributed failures

*Self-study exercise · T05 · Fictional Northstar context*

## Brief

Draw a seven-state request machine and list five transition guards. Write test sequences for lost acknowledgment, duplicate request, cancellation after boarding, and a delayed completion event.

## Stage 1 — Establish your model

Identify the system boundary, stakeholders, measurable outcome, and at least three assumptions. If a quantity is not supplied, mark it as a synthetic hypothesis rather than inventing real-world evidence.

## Stage 2 — Analyze a failure or alternative

Prepare a comparison of at least two plausible designs, conditions, or interpretations. Calculate any relevant metrics, identify a condition that reverses your conclusion, and explicitly name what the provided information cannot establish.

## Stage 3 — Present an engineering argument

Write a one-page decision memo containing the claim, supporting reasoning, evidence table, limitations, recommended test, and open risk. Your recommendation should be conditional when there is insufficient evidence.

## Deliverables

- Assumptions and context register
- Worked analysis or annotated model
- One-page evidence-based recommendation
- Two additional experiments or observations needed before real-world use

<details><summary>Self-review guidance</summary>

A defensible design identifies illegal states, defines idempotency scope, and handles ambiguous outcomes without creating a second assignment.

An excellent answer makes it easy for a skeptical reviewer to trace each claimed conclusion back to assumptions and observations.

</details>

[Return to the concept chapter](../05-software-contracts.md)
