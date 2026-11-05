# Hypothetical Lab 11 — The Evidence That Isn't There

**Course:** EN.645.662 Week 11 · **Reading:** [Chapter 11](../chapters/11-realization-and-evidence.md) · **Time:** 100–140 minutes.

## Evidence packet

The team reports: “All 24 critical requirements are covered.” Each has a planned test case. Eighteen tests have passed; three were not executed; two failed; one was run against an old interface. One report lacks software revision, and a simulated accessible boarding trial uses a standard curb and no representative users. The team asks the fictional concept board to approve operational transition.

## Tasks

1. Compute planned coverage, passed-execution coverage, and the number of unresolved cases. State why the old-interface execution is not automatically acceptable.
2. Create a four-column verification/evidence table for a booking-status requirement, telemetry freshness, accessible boarding, and operator escalation. Each row needs method, expected result, configuration and provenance.
3. Draft a progressive integration plan: contract-level messages → state model → simulated dispatch/vehicle → fault injection → human-in-the-loop rehearsal → higher-fidelity testing. Include entry and exit criteria.
4. Write two validation scenarios from a rider and an operator perspective that cannot be replaced by low-level software tests alone.
5. Make a board decision explicitly distinguishing concept advancement, limited prototype continuation and real-world service approval. No real deployment approval is available from this educational exercise.
6. List enabling products for transition and sustainment: staffing, maintenance, incident response, training, monitoring and eventual retirement.

## Deliverables

`LAB11_VVMatrix.csv`, `LAB11_IntegrationGates.md`, `LAB11_ValidationScenarios.md`, and `LAB11_Decision.md`.

<details><summary>Reference reasoning</summary>

Planned coverage is 24/24 = 100%. Passed-execution coverage is 18/24 = 75% if the 18 pass claims are valid for the relevant controlled configurations. The remaining six include three unexecuted, two failed and one applicability gap. A report missing configuration information requires provenance investigation. A nominal curb demonstration is not intended-user validation of accessible service. The board should withhold real operational authorization; it may permit bounded concept work only under approved review conditions and action closures.

</details>

## Transfer

Produce the original `662_W11_ConceptReview_v1.0` with its broader V&V, integration, transition and review records. Treat this lab's invented cases as examples only.
