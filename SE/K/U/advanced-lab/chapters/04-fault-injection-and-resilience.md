# A04 — Fault injection, degraded modes and resilience

**Competency:** specify a fault hypothesis, inject it reproducibly, evaluate system response and distinguish recovery from success under normal conditions.

## Faults as experiments, not as decorations

A fault test must name a mechanism, occurrence interval, affected subsystem, expected observable signature, and the assumption that makes the result meaningful. The [fault register](../data/fault-register.csv) contains five interventions. Their common purpose is to make the baseline's hidden dependencies visible: fleet availability, network receipt, communication timing, telemetry trust, and staffing/capacity.

In the *OUTAGE* scenario vehicle V01 cannot be used between minutes 0 and 70. In *LOSS*, a seeded Bernoulli process drops 40% of logical request attempts before intake. In *DELAY*, all requests arrive at intake 12 minutes late. In *TELEMETRY*, scheduling is conservatively blocked until minute 45. In *LOW-CAPACITY*, the model is reduced to one vehicle. These are deliberately simple operational abstractions: they do not simulate malicious actors, radio protocols, physical repair, or user experience.

## Resilience requires a trajectory

A resilience argument should say what function degrades, how badly, for how long, and by what mechanism it recovers. In this exercise you can measure service fraction over a fixed horizon, but you cannot yet measure how long a real vehicle repair takes. A scenario with an outage that ends at minute 70 models a stipulated restoration time, not an empirically inferred recovery distribution. Recovery-time requirements would require a separate physical or organizational model.

A useful stress test should *expose* a weakness, not guarantee a pass. The fixture's outage completes six of twelve requests. The telemetry block completes even fewer. Those are observations for model review, not evidence that either degradation is acceptable. Do not quietly change the acceptance threshold to make an unfavorable condition appear successful.

## Fault containment and interpretation

For request loss, the simulated truth ledger records attempts that disappeared. A real system might need client acknowledgements, retransmission deadlines, a separate request-count reconciliation, or an explicit degraded-mode warning to detect a subset of lost attempts. Each proposed mitigation introduces new interfaces and failure modes. Fault injection is also a chance to challenge the assurance architecture—not just the dispatcher.

## Practice and deliverable

**Exercise 1.** How could a telemetry pause improve safety but worsen the completion fraction?

<details><summary>Worked answer</summary>Conservatively holding dispatch when status data is untrusted can avoid committing a potentially unavailable resource; the cost is a longer queue and more expirations. Quantify both outcomes and record why trust takes precedence.</details>

**Exercise 2.** Does a fixed downtime interval demonstrate resilience to repair uncertainty?

<details><summary>Worked answer</summary>No. It tests one stipulated interval. Add distributions or a repair state model, justify them with evidence, and test sensitivity; without empirical data, results remain hypothetical.</details>

**Submit:** fault-injection matrix, before/after service metrics, detection assumptions, and one revised hazard. Related: [v11 human factors and safety](../../integrated-lab/chapters/08-human-factors-safety.md).

## U2 cross-lab credibility challenge — NS-U2.1

**Focus: Fault injection, common modes and degraded policy.** This adds a controlled cross-version analysis to the original learning stage, which remains unchanged.

The six provided v12 scenarios target distinct causes: capacity reduction, vehicle outage, dropped input messages, communications delay, telemetry blocking and nominal operation. A **failure taxonomy** is needed because a single completion percentage can mask fundamentally different safety and recovery obligations.

**Worked comparison:** Under the original fixture, BASE completes 12/12, OUTAGE 6/12, LOSS 8/12 (four lost messages), and TELEMETRY 4/12. These are independent synthetic *interventions* rather than a reliability estimate. Treat the differences as causal outcomes **inside this deterministic/specified fault model**, not measured real incidence or severity.

**Exercise and solution:** If LOSS yields lower mean waiting time among completed requests, is it an improvement? No: removing requests from the served population can artificially improve wait statistics. Include all unique arrivals in the denominator and display unknown/lost status rather than silently discarding the most harmful observations.

**Reproduce:** [Cross-lab lab guide](../../lab-credibility-u2/README.md) · [Evidence gates](../../lab-credibility-u2/data/gates.json) · [Computed results](../../lab-credibility-u2/outputs/u2-cross-lab-results.json).
