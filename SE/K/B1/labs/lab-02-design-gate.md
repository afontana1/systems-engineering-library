# Hypothetical Lab 2 — The Design-Gate Debate

**Course link:** EN.645.662 Week 2 · **Book:** [Chapter 2](../chapters/02-lifecycle-evidence.md) · **Time:** 90 minutes · **Type:** lifecycle and review design.

## Situation

The campus wants a service opening in 16 weeks. Its new dispatch-to-vehicle interface has never been tested under message duplication. A supervisory fallback procedure exists only as draft text. The team has built a working booking interface but not an end-to-end passenger scenario. The sponsor proposes skipping the Preliminary Concept Review to preserve schedule.

## Your work

1. Compare a sequential approach, two restricted service increments, and a risk-directed spiral. Rate each against interface uncertainty, safety consequence, integration cost, and speed of feedback. Justify criteria in prose rather than inventing a universal score.
2. Define a **Gate 1** with three entry conditions, three acceptance questions, four evidence artifacts, and two possible findings that block release.
3. Create a two-column list: evidence needed before *architecture selection* and evidence that can appropriately wait until *integration or operational assessment*.
4. Write a recommendation when the duplication test fails but vehicle functional tests pass. Do not confuse component test success with permission for passenger operation.
5. Produce a one-page tailoring note that states which process formality is reduced and which assurance obligations remain unchanged.

## Output

Submit `LAB02_GatePlan.md`, one review checklist, and one evidence register. No simulation or claim of actual shuttle safety is required; this is a fictional design exercise.

<details><summary>Example reasoning — reveal after attempting</summary>

A risk-directed incremental approach is plausible: use early interface contract tests and restricted integration, maintain a controlled operating domain, and delay broader deployment until degraded behavior is understood. The gate should name the model or software revision, defined duplicate-message behavior, fault-injection evidence, responsible technical and safety reviewers, and unresolved exceptions. Failure of the duplicate-message test requires rework or a specifically justified containment condition; it is not neutralized by vehicle-only functional passes. Review decisions should be **proceed, proceed conditionally, revise, or stop** with explicit authority and closure dates.

</details>

## Transfer

Use this exercise to prepare the original Week 2 lifecycle-tailoring memo and review strategy. If a review has no explicit decision or possible no-go outcome, it has probably been reduced to a status meeting.
