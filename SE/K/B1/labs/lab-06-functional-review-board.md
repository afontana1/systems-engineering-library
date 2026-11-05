# Hypothetical Lab 6 — The Functional Review Board

**Course:** EN.645.662 Week 6 · **Reading:** [Chapter 6](../chapters/06-reviewing-the-functional-baseline.md) · **Time:** 75–110 minutes · **Nature:** simulated technical board.

## Situation

A Northstar team wants authorization to proceed to physical-architecture concepts. Its controlled packet claims eight review criteria were met. Your simulated board discovers the following:

| Finding seed | Observed condition |
|---|---|
| F-01 | Stale telemetry has no defined safe state transition |
| F-02 | One noncritical flow record lacks an accountable recipient |
| F-03 | Requirements matrix references model revision 2; current state diagram is revision 4 |
| F-04 | Three critical needs have source-to-function links but no described relationship rationale |

The team argues that the slides are clear and that 7/8 checklist items have green marks. The review charter requires no unaddressed major safety-relevant finding before concept allocation.

## Assignments

1. Declare the board's decision and scope. Can the team develop exploratory architecture sketches while formal concept allocation is withheld? Separate permitted learning work from controlled commitments.
2. Create an evidence index containing at least six items, each with identifier, revision, approval state, and criterion supported. Explicitly mark any missing source.
3. Write formal findings for F-01 to F-04: condition, expectation, consequence, severity, owner, due date and closure evidence. Decide whether any seeds must be split into multiple findings.
4. Prepare a two-minute technical briefing plus a one-page decision record. Do not treat the green-mark percentage as proof of readiness.
5. Propose a change-impact path for F-01: revised function/state model, requirement and flow implications, scenario replay, and independent closure checking.
6. Have another learner or a hypothetical reviewer challenge whether the evidence actually proves what the team claims. If working alone, write the objection yourself and then answer it.

## Deliverables

`LAB06_ReviewCriteria.md`, `LAB06_EvidenceIndex.csv`, `LAB06_Findings.csv`, and `LAB06_BoardDecision.md`. Keep the final decision separate from a list of suggestions.

<details><summary>Reference board disposition</summary>

F-01 is a potential major finding because undefined failure response undermines the safety argument; it blocks formal approval under the given charter. F-03 is an applicability/configuration finding requiring reconciliation. F-02 may be moderate if the flow is truly noncritical; F-04 requires semantic trace review before the critical need claims can be trusted. The board should withhold unrestricted proceed authority. A well-defined action plan can permit bounded exploration while requiring a controlled state-model revision, scenario test evidence, closure owner, and explicit re-review. The raw count of green rows does not overrule the major gate.

</details>

## Transfer

Carry this process into the full original Week 6 `662_W06_FBR_Package_v1.0`. Use its own criteria and mastery threshold rather than copying this fictional board vote.
