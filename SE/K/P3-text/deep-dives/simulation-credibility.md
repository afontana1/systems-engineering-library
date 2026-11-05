# Verification, validation and credibility are not synonyms

**Cross-course pathways:** MBSE Analytics 12; Foundations M&S 6, 10–12; Advanced M&S 1 and 12.

## One model, three separate questions

1. **Verification:** Did the implementation calculate the intended equations, state transitions and event logic correctly? A deterministic oracle and conservation check provide evidence.
2. **Validation:** Is that conceptual representation adequate for the real phenomena and scenarios in the *stated* intended use? Compare independent data and challenge omitted mechanisms.
3. **Credibility / acceptance for use:** Does a decision authority judge the combined evidence sufficient for a specific consequence and application? A credible screening model may not support safety certification.

NASA-STD-7009 supplies a framework for appropriate modeling-and-simulation practices and assessment of use; it is not a magic validation certificate for every model. Record configuration, evidence and limitations at the exact decision boundary.

## Construct a claim–argument–evidence chain

**Claim:** The simplified model is appropriate for comparing two dispatch policies under weekday dry-weather peak demand. **Argument:** The policy comparison relies on relative waiting-time differences, the demand inputs cover weekday peaks, the event logic has known-answer tests, and held-out observed wait distributions agree within predeclared limits. **Evidence:** event trace test logs, time-stamped demand data, withheld-scenario comparison, replications with fixed seeds, peer review. **Qualifier:** does not support emergency-mode or severe-weather performance claims.

A change to a charging policy or software version invalidates claims that depend on those interfaces until re-evaluated. A traceability graph should connect `intended use → model assumptions → evidence → decision`. Keep a living model-risk register rather than a one-time validation stamp.

## Model-form uncertainty exercise

Two simulators use the same measured arrival distribution, but one models group boarding and one models each person as an independent job. They agree on daily throughput yet differ in the 95th-percentile wait. Agreement on an aggregate is insufficient: identify which operational mechanism produces the different tails, design an observation that discriminates between them, and limit use while the issue is unresolved.

**Review checklist:** purpose; scope; assumptions; data provenance; numeric checks; empirical comparison; uncertainty; alternatives; applicability; reviewer authority; reopen conditions.

---

[Back to Phase 3 knowledge library](../README.md) · [Toolkit](../tools/README.md)
