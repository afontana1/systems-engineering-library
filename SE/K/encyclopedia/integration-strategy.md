# Integration build-up and readiness evidence

**Reference entry · Concept, design, integration and test · Expanded reference**

## Definition and diagnostic distinction

An **integration strategy** selects the order, facilities, configurations, and evidence gates by which separately realized elements become a working system. It is not just an assembly sequence. Integration deliberately creates new interactions that may expose interface defects, unmodeled dynamics, timing conflicts, and shared resource constraints. A good strategy minimizes expensive late discovery while avoiding premature coupling of unstable subsystems.

## Theory: dependencies determine the build-up sequence

Represent components and interfaces as a directed dependency graph. Nodes are realizations with maturity states; edges identify interfaces and evidence dependencies. Critical or highly connected interfaces should be exercised before downstream work becomes expensive. A risk-weighted build sequence might prioritize an interface with high failure consequence and uncertain behavior even when its hardware is not on the nominal schedule's critical path.

Integration levels serve different purposes. Pure software emulation can isolate algorithmic defects; software-in-the-loop validates interfaces and control logic; hardware-in-the-loop exposes physical timing, I/O, and some failure modes; field trials reveal human, environmental, and organizational interactions. Fidelity must match the claims being made. A successful simulated sensor exchange cannot establish electrical immunity, vibration robustness, or operator usability.

## Worked example: late discovery versus early contract testing

A shuttle prototype uses a reservation app, dispatch backend, gateway, and vehicle controller. The original plan integrates all four in week 20. A revised plan first tests the app–backend API in week 4, the gateway–controller timing contract in week 7, and the complete closed-loop command path in week 11. During the gateway test, peak-load acknowledgement takes 240 ms against a 200 ms budget. Early detection leaves time to redesign before expensive fleet installation. The gain depends on the earlier tests accurately representing the timing and configuration of the eventual deployment.

## Engineering use and evidence

Publish an interface dependency matrix, sequence rationale, required facilities and simulators, configuration identifiers, entry criteria, exit criteria, rollback steps, and discrepancy ownership. Create vertical slices that demonstrate one mission-critical thread across layers before attempting full functionality. Maintain an integration log connecting every observed anomaly to affected requirements and retest results. Separate “assembled,” “communicates,” “behaves correctly,” and “is operationally acceptable” as different states.

## Limitations and connections

An incremental sequence can create false confidence if substitutes hide the hardest interactions. A big-bang test may still be needed to expose emergent load and environmental conditions, but it should not be the first discovery method. Connect integration strategy to **interface control**, **allocation**, **verification matrices**, **resilience**, and **baseline governance**.

## Technical analysis: integration order is a dependency problem

Integration sequencing is constrained by an acyclic dependency graph where practical, but real programs also contain cycles requiring stubs, simulators, service virtualization, or early joint tests. The engineering objective is to expose dangerous interactions while the responsible teams and configurations can still change them—not merely to assemble in the cheapest order.

For an illustrative system, components `A` and `B` can each be verified independently, while `C` requires both. A valid order is `A → B → C` or `B → A → C`. Attempting to qualify `C` before either upstream interface exists leaves its evidence conditional on a surrogate. If **A has a 2-day** integration check, **B 3 days**, and **C 4 days**, and A/B work proceeds in parallel with independent teams, the shortest dependency-limited path is `max(2,3)+4 = 7 days`, not `2+3+4 = 9`. This ignores resources, rework, and shared test rigs.

**Evidence boundary.** Record integration environments, surrogate fidelity, build hashes, interface revisions, exit criteria, and unresolved anomalies. A mock can verify protocol conformance but may not reproduce clock drift, electromagnetic coupling, operator workload, or power transients. Reassess the plan when shared equipment turns nominal parallel tasks into a serial queue.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** Product integration checks subsystem interactions and possible adverse emergent behavior. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §5.2 Product Integration](https://www.nasa.gov/reference/5-2-product-integration/) · *direct guidance*.
- **C2:** Interface management controls the compatibility of the products that will be integrated. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §6.3 Interface Management](https://www.nasa.gov/reference/6-3-interface-management/) · *direct guidance*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 (2016/2017)](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle engineering, technical management, requirements, verification and validation.
- [NASA · Distinctions between product verification and validation](https://www.nasa.gov/reference/2-4-distinctions-between-product-verification-and-product-validation/) — Separate conformity to specifications from fitness for intended use.


## Step 02 review exercise: ordering by interface risk, not organizational chart

Suppose modules A (dispatch), B (gateway) and C (vehicle) must interoperate. A–B exchanges an authenticated authorization, B–C has a 100 ms freshness constraint, and A–C shares a fail-safe state rule. A staged integration strategy verifies the contracts with representative doubles before full integration, then exercises negative cases (stale messages, dropped updates, mismatched versions), then runs end-to-end timing and hazard tests. Integrating in department order can hide a safety-critical edge until the final demonstration.

The timing budget might allocate 30 ms to A, 20 ms to B, 30 ms to C and 20 ms to transport, totaling **100 ms**. This is a bookkeeping budget, not proof that worst-case delays add exactly as estimated; include measurement uncertainty, clock skew and scheduling interference. If 15 ms of unbudgeted retry delay is discovered, the path can take **115 ms** and the architecture must either change or renegotiate an authorized requirement—not silently report the previous 100 ms.

**Exercise (answer).** If transport can be limited to 12 ms and retry to 5 ms, the revised path upper budget is \(30+20+30+12+5=97\) ms. The claim still requires evidence that all five assumed bounds hold in the same target configuration and environment.

## Follow the knowledge

**Related concepts**

- [Interface control and integration contracts](interface-control.md)
- [Verification cross-reference matrices and test design](verification-matrix.md)
- [Verification, validation, and acceptance: the three different decisions](v-and-v.md)
- [Work breakdown structures and technical baselines](wbs-and-baselines.md)

**Go deeper in the 240-chapter textbooks**

- [Book 7, Chapter 10: Book 7 · Chapter 10: Integration readiness and sequencing](../B7/chapters/10-plan-system-integration-and-conduct-the-integration-rea.md)
- [Book 8, Chapter 05: Book 8 · Chapter 5: Integration and SIL/HIL paths](../B8/chapters/05-construct-the-integration-test-approach-sil-hil-paths-a.md)
- [Book 18, Chapter 10: Week 10 · System of Systems Engineering · Chapter 10 — Distributed integration, verification, validation, and operational T&E](../B18/chapters/10.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
