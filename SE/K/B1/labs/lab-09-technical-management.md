# Hypothetical Lab 9 — The Baseline Audit

**Course:** EN.645.662 Week 9 · **Reading:** [Chapter 9](../chapters/09-managing-the-technical-baseline.md) · **Time:** 90–130 minutes.

## Situation

Northstar approved `CR-017` to reduce the maximum acceptable vehicle-readiness age from ten to five seconds in a fictional design. The requirement record says rev 4, the interface sheet still says rev 3 and ten seconds, the simulation configuration assumes eight seconds, and a verification report cites software rev 2. Management's dashboard shows p95 response times of 6.2, 7.1, and 8.4 seconds for three claimed “comparable” builds, without stating workload.

## Tasks

1. Write a concise SEMP rule for engineering changes that affect safety-relevant interfaces: initiator, technical authority, impact analysis, sign-off, baseline creation and independent closure evidence.
2. Make a four-row configuration status table for the requirement, interface, simulator and verification report. Mark which revision is authoritative, which is stale, and what must be reviewed before changing status.
3. Record an issue for the already contradictory revisions and a future risk for undetected stale telemetry. Write the risk in cause–event–consequence form.
4. Define a TPM for p95 dispatch notification time: population, configuration, load, method, threshold, frequency, accountable owner and action when exceeded.
5. Explain why the p95 trend alone cannot prove worsening product behavior when workload profiles differ. List the minimal data required for a comparable trend.
6. Draft a change closure checklist including the affected state machine, interface schema, verification plan, operating instructions and risk controls.

## Deliverables

`LAB09_SEMPAddendum.md`, `LAB09_ConfigStatus.csv`, `LAB09_RiskIssue.md`, and `LAB09_TPM.md`.

<details><summary>Reference audit position</summary>

The conflicting revisions are current configuration issues. The report on software rev 2 does not automatically verify an interface that is controlled at rev 4. The p95 values are warning signals, but if workload or instrumentation changed they cannot be interpreted as a clean product trend. The five-second rule needs an authorized basis and controlled propagation to interfaces, models, tests and operator procedures. Closure requires an independent comparison of the authoritative set and applicable new evidence.

</details>

## Transfer

The assessed Week 9 `662_W09_TechnicalManagement_v1.0` is a larger controlled management mini-baseline. Build it independently from your own project assumptions.
