# 11 · Digital threads, provenance, and credible digital twins

**Concept dossier · MBSE / digital engineering / assurance**

## Digital is not automatically connected or authoritative

A **digital thread** connects information and evidence across requirements, models, configurations, test results, operations and decisions. A **digital twin** is a purposeful digital representation linked to a specific physical asset or system that may be updated using operational data and used to support specified decisions. A dashboard of telemetry is not automatically a validated twin, and a collection of URLs is not automatically a trustworthy thread.

The hard problem is **meaning and authority**: which entity does each record describe, what does a field mean, who controls changes, what configuration was in use, and which evidence supports each decision?

## Provenance as an answerable question

For a claim such as “the system satisfies braking requirement R-14,” a reviewer should be able to traverse:

`R-14 → test procedure T-14 → raw telemetry dataset D-23 → calibration C-6 → vehicle configuration V-8 → analysis A-21 → approved claim K-3`.

Each link has direction and a role: `verified_by`, `produced`, `calibrated_with`, `measured_on`, `analyzed_by`, `supports`. Records carry version, timestamp, owner, source identity and integrity checks. A data lake full of files cannot replace these semantics.

## Freshness and validity are separate

Suppose a battery model uses the latest temperature reading, but the installed battery chemistry has changed since model calibration. Data are *fresh* but the model may be *invalid*. Conversely, an older calibration might still be appropriate if the hardware configuration and operating regime remain unchanged and its use is justified.

A twin-use contract should state:

1. **Purpose:** predict remaining charge for dispatch decisions, not certify every battery safety property.
2. **Asset identity and configuration:** battery ID, hardware revision, firmware and sensor installation.
3. **Update semantics:** data delay, aggregation window, missing-data rule and maximum tolerated staleness.
4. **Model validity:** domain, calibration version, residual monitoring and uncertainty bounds.
5. **Action authority:** advisory output or automated actuator command; fail-safe behavior and human oversight.
6. **Evidence:** validation dataset, scenarios, degradation monitoring and retirement/rollback rules.

## Example: model drift

A battery state-of-charge model trained at mild temperatures begins to underpredict energy consumption in cold weather. The system should detect out-of-range conditions, mark estimates as less credible, and route dispatch to a conservative policy or human review. “More real-time data” may not solve missing physics or an unmodeled operational mode.

## Data relationships as a graph

Useful validation queries include: Which active claims depend on a superseded test procedure? Which tests were run against the wrong firmware? Which assets generate telemetry without a controlled identifier? Which decisions used a model outside its declared domain? These are graph or database governance questions; the answer depends on typed relations and version policy, not visual polish.

## Exercises with answers

**A.** A dashboard receives live telemetry. Why might it not be a digital twin? **Answer:** it may lack an explicit model, asset/configuration identity, defined use, predictive or analytic mechanism and credibility/decision contract.

**B.** A dataset is traceable but its timestamps are wrong. Is provenance sufficient? **Answer:** no. Provenance tells origin; calibration, semantic correctness, completeness and integrity still need assessment.

**C.** What invalidates a previous test claim after a firmware update? **Answer:** not every update necessarily does, but change-impact analysis must determine whether the behavior, test conditions or evidence mappings have changed.

**Transfer artifact:** small typed provenance graph, twin-purpose contract, freshness/drift rules and two data-quality tests.

## Connections

[Requirements evidence](02-requirements-evidence.md) · [Architecture semantics](03-architecture-states.md) · [Model credibility](08-model-credibility.md) · [Agile baseline control](12-agility-assurance.md).  
**Legacy primer:** [Digital thread and twin](../../encyclopedia/digital-thread-and-twin.md).
