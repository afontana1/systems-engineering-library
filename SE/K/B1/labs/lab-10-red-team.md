# Hypothetical Lab 10 — The Fault That Passed Every Green Check

**Course:** EN.645.662 Week 10 · **Reading:** [Chapter 10](../chapters/10-failures-and-controls.md) · **Time:** 110–150 minutes.

## Scenario

In a Northstar test run, the vehicle reports its position at time 19:00:00. Network buffering delays delivery until 19:00:09. The gateway overwrites the measurement timestamp with receipt time; dispatch sees a “fresh” message and assigns the vehicle. An operator has been trained to trust a green dashboard whose freshness indicator uses the same receipt timestamp. An inspection had verified field names but not the time semantics.

## Red-team sequence

1. Distinguish proximate unsafe decision, causal mechanism, contributing organizational conditions and failed barriers. Avoid starting from a presumed negligent individual.
2. Construct a causal map with at least six labeled relationships and identify what evidence would support or contradict each.
3. Draw a two-level fault tree for unsafe assignment requiring stale-data acceptance plus failed protective response. Write its logical assumptions; do **not** present guessed event probabilities as an actual hazard rate.
4. Create a preventive/detective/limiting/recovery control table. Explain which checks share the same timestamp error and thus are not independent.
5. Write one red-team finding each for accessibility, operations, safety, supplier integration, software, and assurance.
6. Revise three proposed artifacts: interface control sheet, state-machine guard, and delayed-message test case. Identify their controlled versions and closure evidence.

## Deliverables

`LAB10_CausalMap.md`, `LAB10_FailedControls.csv`, `LAB10_Findings.md`, and `LAB10_ChangeImpact.md`.

<details><summary>Reference interpretation</summary>

The causal mechanism is a semantic timestamp substitution under network delay, not simply “a nine-second late message.” The green dashboard is not an independent barrier because it uses the same corrupted data. A meaningful control could retain signed or otherwise trusted measurement timestamps, validate measurement age, reject ambiguous events, and define degraded operation. An independent test must inject delayed/reordered events; verifying schema shape alone is insufficient. The red-team should also challenge an accessibility assumption about the assigned vehicle and stop even though the fault scenario centers on time semantics.

</details>

## Transfer

The original course's Week 10 failure-analysis memo requires using the NASA Mars Climate Orbiter report and evaluating systemic causes. Study its authoritative documents separately; this fictional lab is not a substitute for historical evidence.
