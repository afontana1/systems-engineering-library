# Hypothetical Lab 12 — Defend a Concept with Imperfect Evidence

**Course:** EN.645.662 Week 12 · **Reading:** [Chapter 12](../chapters/12-synthesis-and-defense.md) · **Time:** 120–180 minutes · **Role:** fictional final review and oral defense.

## Board brief

Northstar's team requests permission to proceed to a more detailed engineering phase. The concept baseline is nominally complete, but an audit finds a stale architecture cost estimate, an unallocated degraded-communications function, a requirement whose verification procedure uses a prior schema, and a rider-accessibility need supported only by a vehicle-level demo. A risk log lists “network outage” without treatment or owner. The mission itself remains provisional and restricted to a synthetic campus mobility service.

## Your assignment

1. Write an executive brief stating exactly what permission is being requested and explicitly excluding approval for public transport operation.
2. Build a ten-row chain linking need, ConOps scenario, requirement, function, architecture allocation, interface, risk/hazard, test/validation plan, configuration and evidence limitation.
3. Conduct an automated structural check if useful, then manually review at least three high-criticality chains for semantic correctness. Report *both* structural coverage and actual evidence sufficiency.
4. Resolve or classify each of the five seeded defects; identify owner, severity, corrective action and review status. Do not close a finding by deleting its row.
5. Recreate the Chapter 8 architecture score ranking and name the sensitivity condition that could change the choice. Clearly separate hypothetical preferences from stakeholder-approved data.
6. Present a five-minute oral defense; if studying solo, record yourself responding to the reviewer questions below, and write a candid retrospective and next-course skills roadmap.

## Review-board questions

- Which operating conditions are outside your claims? What is the biggest unknown?
- Who owns the stop-accessibility interface, and what would validate it with appropriate users?
- What would make the proposed telemetry freshness control fail despite passing schema tests?
- If one vehicle is lost, what measured outcomes remain, and which claims no longer hold?
- Which configuration corresponds to the evidence in your presentation?
- Under what change in weights or estimates would the architecture recommendation reverse?

## Deliverables

`LAB12_FinalExecutiveBrief.md`, `LAB12_TraceDefense.csv`, `LAB12_Findings.md`, `LAB12_OralDefenseNotes.md`, and `LAB12_LearningRoadmap.md`.

<details><summary>Illustrative board decision</summary>

A responsible decision is to **withhold unrestricted concept baseline approval** until the unallocated degraded function and stale evidence links are resolved and accessibility validation is appropriately planned. Limited exploratory work can continue if authorized without prejudging safety or deployment. A trace matrix that is 100% populated but semantically wrong is not a valid assurance argument. An honest defense must retain uncertainty, scope the requested approval, and identify the independent evidence that would permit progression.

</details>

## Transfer to your actual capstone

Complete the original course's Week 12 final package, self-assessment and oral defense from its own rubric. The hypothetical board is rehearsal for engineering judgment; your independent assessed work must stand on its own.
