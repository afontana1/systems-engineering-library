# 5. Systems of systems, authority and mission dependencies

*Graduate engineering sequence · Enterprise and Complex Systems · Regional emergency access*

**Prerequisites:** system architecture, probability, graph theory, enterprise governance and assurance. **Course connections:** System of Systems Engineering, Enterprise Systems Engineering, Digital and Mission Engineering.

## 5.1 Why a network of components is not necessarily a system of systems

A system of systems (SoS) has constituents that retain some operational and managerial independence. In Northstar's emergency-access scenario, road authorities, transit providers, hospitals, emergency dispatchers and communication networks may belong to different organizations. The regional mission depends on their cooperation, but the mission authority may not control their budgets, priorities, release schedules or local procedures. A central architecture drawing that labels every participant as a 'subsystem' can hide this critical fact.

Two different graphs are required. A **technical graph** represents information flow, service dependency, physical routes and resource movement. A **governance graph** represents who may approve changes, who bears loss, who supplies data, who can withdraw participation and who can stop unsafe operations. Technical interoperability does not imply agreement about semantics or authority. A road closure message may be delivered perfectly but interpreted as a recommendation by one participant and a binding prohibition by another.

To define the *system of interest*, explicitly identify constituent objectives and mission-level outcomes. Suppose a transit agency optimizes fleet utilization, a hospital prioritizes urgent transfers, and a road authority maximizes emergency vehicle access. Their local policies are reasonable but can conflict. A SoS engineer must design interfaces, agreements and measures that make cooperation possible without assuming away independent incentives.

![Mission dependence and authority paths](../diagrams/05-sos.svg)

## 5.2 Capability as a mission thread

A capability is not merely a collection of equipment. 'Reach a hospital within 30 minutes during a corridor disruption' is an end-to-end **mission thread** requiring detection, route authorization, vehicle assignment, physical movement, patient handoff, and verified closure of the event. Break the thread into constituent services and failure conditions. Assign operational owners and evidence for each interface. This provides a basis for evaluating whether a regional capability survives the loss or withdrawal of a participant.

Graph theory reveals some structural vulnerabilities. Represent the mission network as a directed graph $G=(V,E)$ with edges that enable mission flow. A **cut set** is a set of edges or nodes whose loss disconnects essential origin-destination pairs. If every route to hospital H uses bridge B, B is a single point of mission vulnerability even when dispatch software and communications are redundant. Counting redundant servers cannot compensate for a single physical bridge.

For a simple teaching graph, let the origin O reach hospital H by two paths: $O\to A\to H$ and $O\to B\to H$. If path A is available with probability 0.9 and path B with probability 0.8, and the path failures are independent, the probability at least one path is available is $1-(0.1)(0.2)=0.98$. This calculation breaks if the two paths share the same floodplain, bridge approach, fuel supply, or decision authority. The physical and organizational common-cause structure matters more than the number of lines on a diagram.

## 5.3 Independence and evidence integration

A constituent may publish evidence of passing local acceptance tests, yet those results may not support the SoS mission claim. Consider a hospital reporting 99% ambulance-entry uptime and a transit service reporting 99% vehicle dispatch success. Even if independent, multiplying gives only the probability that two individual services are available under their separate definitions; it does not establish that transfer coordination meets a 30-minute mission deadline. Interfaces, queues, human handoffs, and external corridor constraints must be modeled and tested. Evidence inheritance needs equivalence of configuration, operating context, failure model and acceptance criterion.

A SoS assurance argument should explicitly contain **assumption contracts**: 'Agency A supplies closure events no more than X seconds after verification'; 'Agency B treats closure messages as binding for identified corridor identifiers'; 'Hospital C acknowledges arrival capacity within Y seconds.' Each constituent must accept its obligations and specify change-notification and exception handling. An agreement without a measurable interface definition is not an engineering contract; a technical protocol without institutional acceptance is not an operational agreement.

## 5.4 Bayesian evidence and uncertainty

Suppose an interface is believed to fail with probability $p$. A Beta prior $p\sim Beta(\alpha,\beta)$ and independent Bernoulli observations with $f$ failures and $s$ successes produce $p\mid data\sim Beta(\alpha+f,\beta+s)$. With $Beta(1,9)$ and two failures in 20 observed transfers, the posterior is $Beta(3,27)$ with mean $3/30=0.10$. That mean is not a frequentist failure-rate estimate, nor does it guarantee the next mission will have a 10% failure chance if emergency conditions differ from the sample.

The posterior depends on the prior and the exchangeability assumption. If failures cluster during the same storm event, independent Bernoulli likelihoods overcount information. If one agency changes its software revision mid-campaign, combining results may conceal a configuration-dependent failure mode. Better evidence separates scenarios, revisions, and environmental regimes, and it uses sensitivity analysis to show which judgments depend on prior assumptions.

## 5.5 Who can change what?

Distributed change is an assurance risk. A road authority may revise corridor identifiers without a transit vendor's approval. A hospital may introduce a new triage interface. Under independent management, a central program's configuration baseline cannot guarantee uniform change control. Instead, maintain published interface versions, compatibility rules, conformance tests, dependency alerts, migration windows and contingency procedures. Record which mission claims are invalidated by a unilateral change.

A useful governance matrix identifies: the organization owning each data element; who may issue operational authority; who may independently audit it; who authorizes exceptions; and how conflicts are resolved. Consider a closure announcement contradicted by a local responder's observations. The technical system should neither automatically override the road authority nor blindly dismiss responder evidence. It needs a pre-agreed dispute and emergency escalation path. That path should be tested, including after-hours staffing and network outages.

## 5.6 Architecture tradeoffs under constituent independence

Centralized control can improve consistency and simplify auditing but can create a bottleneck or single governance failure. Federated control preserves agency autonomy and local knowledge but complicates global optimization and change coordination. A hybrid architecture may retain local authorization while sharing a mission-level event format, correlation identifiers, common minimum constraints, and an independent evidence store.

A trade study must consider more than throughput and cost. Compare solutions against mission effectiveness, safety constraints, organizational autonomy, resilience, legal authority, interoperability cost, and the ability to recover when an agency withdraws. Treat hard requirements as feasibility gates before calculating weighted preferences. A highly efficient architecture that relies on an agreement no participant has signed is **not feasible**; adding a low governance score to a weighted average would disguise the issue.

## 5.7 A defensible SoS decision

The final recommendation should state the intended mission, participating authorities, valid operational conditions, interfaces, evidence ownership and rollback plan. Report residual vulnerabilities, not just successful integration demonstrations. When possible, perform a **mission-thread rehearsal** with realistic data, delays, escalation paths, and partial failures. Disagreement among parties is itself relevant evidence about system readiness.

## Problems — attempt before solutions

1. Two alternative independent paths have availabilities 0.85 and 0.90. Compute the probability at least one succeeds. Then name two reasons independence may fail.
2. A $Beta(2,8)$ prior is updated after one failure and nine successes. Give the posterior and mean.
3. A hospital's acceptance test shows its API responds within 1 second. Explain why that does not establish 30-minute patient delivery.
4. The central integration office has no authority to stop a constituent from changing corridor IDs. Propose an enforceable interface-change process and a mission assurance fallback.

<details><summary>Worked solutions</summary>

1. $1-(0.15)(0.10)=0.985$. A shared physical corridor, common infrastructure, or single authorization authority can correlate the paths.
2. $Beta(3,17)$ with posterior mean $3/20=0.15$ under the stated model; clustered observations or changes of regime challenge the update.
3. End-to-end capability also needs staffing, route authority, vehicle availability, road conditions, handoff, and latency at every interface. Test evidence must match the mission thread.
4. Use versioned schemas, published deprecation periods, automated conformance tests, escalation rights, configuration-specific mission evidence and a documented degraded route policy. Governance obligations require institutional approval, not only code.
</details>

## Practice

[Run the mission-thread failure laboratory](../labs/05-sos.html) · [Python dependency model](../code/system_models.py) · [Notebook](../notebooks/05-sos.ipynb). The original assessed course deliverable should include both the technical and governance dependency networks.

**Further reading:** [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) and the SEBoK systems-of-systems and enterprise discussions. The graphs here are simplified educational examples.

<!-- STEP04-ADVANCED-STUDIES-START -->
## Integrated case NS-G4.1 — Constituent authority and network flow

> **NS-G4.1 case convention.** Every number in this extension comes from a controlled, fictional emergency-dispatch dataset, unless explicitly identified as an illustrative assumption. A Python screening result is not an operational safety finding, a validated queue model, or an authorization from independently managed agencies. The case is shared with the other five advanced-studies chapters; use the same `revision: 1.0` throughout.

**Reproduce:** [controlled JSON](../data/ns-g4.1-case.json) · [Python model](../code/ns_advanced_case.py) · [computed results](../outputs/ns-g4.1-results.json) · [integrated laboratory](../labs/INTEGRATED-CASE.html).

### G1. An accessible mission thread is a constrained network

Requests reach a dispatch hub, then rail and paratransit constituents, and finally a care destination. The owners of rail, paratransit, road access, and dispatch independently control their capacity and interfaces. For an initial *upper-bound screening exercise*, assign each directed arc a synthetic maximum number of accessible trip slots in a common decision window. Let \(f_{ij}\) be flow on arc \((i,j)\) and \(c_{ij}\) its capacity. Maximize sink flow subject to

\[
0\le f_{ij}\le c_{ij},\qquad
\sum_i f_{iv}=\sum_j f_{vj}\quad\text{for each internal node }v.
\]

The included Edmonds–Karp implementation finds an augmenting path in the residual graph and increases its flow until no positive-capacity source-to-sink path remains. Its result is a **structural upper bound on trip slots**, not a vehicle timetable, proof of accessibility compliance, or endorsement by constituent owners. Travel times, charging, scheduling, patient needs and jurisdictional rules are outside this small model.

**Worked calculation.** The baseline route capacities to care are 43 via rail and 25 via paratransit, while the shared Request→Dispatch arc holds 70. Thus nominal maximum flow is \(43+25=68\) slots, above the illustrative requirement of 55. With the coordinated policy, rail and paratransit arcs are increased but the shared dispatch input still caps total nominal flow at **70 slots**. Removing the rail constituent leaves only **32 slots** via paratransit under that policy, below 55. In the compound disruption, the shared input falls by 12 to **58** while demand is \(55(1.13)=62.15\) slots. The loss occurs even though more downstream resources are available: the bottleneck moved upstream.

### G2. Constituent change control must be explicit

The network graph encodes only capacity. To deliver a genuine mission thread, every constituent must publish: compatible interface revision, service interpretation, data-protection scope, real-time status semantics, authority to pause or override, and the evidence supporting each claim. A supplier revision can invalidate a thread without deleting any graph edges. In the `interface_drift` scenario, the route authority expects R3 but the coordinated policy still presents R2; the safety authorization check fails despite 70 nominal slots.

A federation integration test should exercise unavailable constituents, mismatched time bases, incompatible priorities, and emergency handoffs. It should also check provenance: *who asserted the capacity, when, at what revision, and under what obligation?* A central architect can propose a change, but cannot simply declare independent agencies to be under central command.

### G3. Bayesian evidence belongs to a declared question

Suppose the prior probability of a route blockage is \(P(B)=0.15\), the alarm sensitivity is 0.80 and its false positive probability is 0.10. A positive alarm yields

\[
P(B\mid+)=\frac{0.80(0.15)}{0.80(0.15)+0.10(0.85)}\approx0.5854.
\]

This belief update may guide what to investigate next, not a self-authorizing route closure or departure. Two alarms produced from one shared sensor do not count as conditionally independent confirmations. Keep belief about the hazard separate from legal authority and the route freshness evidence required to act.

### Worked exercise with explained solution

**Problem.** Eliminate the paratransit constituent under the coordinated policy. What is the maximum flow, and which assumptions prevent you from asserting that all 55 accessible requests can be served?

**Solution.** Rail has \(43+8=51\) slots into care, so max flow is **51**, below 55. Even a nominal 55 or greater would not establish geographic reachability, vehicle availability, journey timing, or patient suitability. Agency ownership and interface evidence remain independent gates.
<!-- STEP04-ADVANCED-STUDIES-END -->
