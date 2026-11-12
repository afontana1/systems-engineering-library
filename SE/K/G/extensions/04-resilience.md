## Integrated case NS-G4.1 — Common-cause dependence and recovery claims

> **NS-G4.1 case convention.** Every number in this extension comes from a controlled, fictional emergency-dispatch dataset, unless explicitly identified as an illustrative assumption. A Python screening result is not an operational safety finding, a validated queue model, or an authorization from independently managed agencies. The case is shared with the other five advanced-studies chapters; use the same `revision: 1.0` throughout.

**Reproduce:** [controlled JSON](../data/ns-g4.1-case.json) · [Python model](../code/ns_advanced_case.py) · [computed results](../outputs/ns-g4.1-results.json) · [integrated laboratory](../labs/INTEGRATED-CASE.html).

### G1. Derive rather than assume redundant availability

For two local nodes that fail independently with availability \(A_L\), both are unavailable with probability \((1-A_L)^2\). Thus parallel availability is \(1-(1-A_L)^2\). However, the nodes share a power/control domain with assumed common-outage probability \(q\). A simple conditional model yields

\[
A_{pair}=(1-q)\{1-(1-A_L)^2\}.
\]

The mission path also requires a route authority \(A_R=0.998\) and a dispatch dependency \(A_D=0.996\), treated here as independent of the paired nodes and of each other. The joint model is \(A_{mission}=A_{pair}A_RA_D\). Independence is an **assumption needing evidence**, not a property inferred from two boxes in a diagram.

**Worked comparison.** Baseline \(A_L=0.988,q=0.012\) gives mission availability about **98.19%**. Technical redundancy improves \(A_L=0.992,q=0.005\), yielding about **98.90%**. Coordinated guardrails use the same local-node availability with \(q=0.003\) and yield about **99.10%**, clearing the illustrative 98.5% screen. With an extra common-outage exposure of 0.035 in the compound scenario, the guarded result falls to **95.62%** and fails. Adding replicas without reducing shared causes can produce little benefit.

### G2. Availability is not a recovery-time guarantee

Availability often uses the stationary approximation \(A=MTBF/(MTBF+MTTR)\) for a specific repairable-component model. It does not determine recovery-time percentiles, cascading time-to-failure, data age, or service continuity during incident response. A 98.5% availability figure could conceal a single long outage incompatible with emergency operations. Define recovery time objective (RTO), recovery point objective (RPO), critical-service dependencies, and the disturbance class to which each applies. Ensure the route and dispatch authorities agree on failover decision rights.

For observability, retain logs showing the configuration identifier, route evidence revision, monotonic sequence, clock offset, operator action, and cause of recovery. Otherwise a green uptime dashboard is weak evidence about the control structure that mattered. Instrument exception paths and verify that degraded operation maintains accessibility and incident reporting.

### G3. Threat, fault, and confidence boundaries

Use fault injection for network partitions, shared-cause power loss, stale cache reads, double acknowledgements, supplier interface drift, and operator workload spikes. A security vulnerability can be a safety causal mechanism; yet an attack model and a statistical failure model have different evidence requirements. The toy calculation does not model malicious adversaries, correlated replicas, overload during failover, or supplier governance. It must not be promoted to an accredited reliability forecast.

### Worked exercise with explained solution

**Problem.** Keep coordinated \(A_L=0.992\) and serial dependencies, but increase common outage probability from 0.003 to 0.02. Compute mission availability and compare it with 98.5%.

**Solution.** \(A_{mission}=(0.98)(1-0.008^2)(0.998)(0.996)\approx0.9741\), or **97.41%**, below the 98.5% screen. Improving local-node availability further is unlikely to close the gap without reducing the shared outage mechanism. Validate the dependency graph and restoration assumptions with fault-injection and operations records.
