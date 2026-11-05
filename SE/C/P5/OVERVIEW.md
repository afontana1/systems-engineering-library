# Phase 5 — Systems of systems, enterprises, and complex adaptive systems

Phase 5 changes the unit of analysis again. Earlier phases controlled a system baseline, an engineering operating system, and a set of mission and analytic evidence. This phase studies what happens when the capability depends on **independently useful systems, autonomous organizations, conflicting objectives, distributed authority, legacy constraints, and continual adaptation**.

The learner must no longer assume that one chief engineer can command every constituent, that one lifecycle governs all work, that one architecture repository is authoritative everywhere, or that a globally optimal design can simply be imposed. The central challenge is to improve mission and enterprise outcomes while constituent systems and organizations continue to pursue their own purposes, budgets, schedules, policies, incentives, and evolution paths.

The phase retains three distinct courses:

1. [**EN.645.771 — System of Systems Engineering**](EN645771.md)
2. [**EN.645.753 — Enterprise Systems Engineering**](EN645753.md)
3. [**EN.645.742 — Management of Complex Systems**](EN645742.md)

System of Systems Engineering develops mission threads, capability dependencies, logical/physical/information architectures, interoperability, federated modeling, distributed T&E, and evolution decisions. Enterprise Systems Engineering broadens the analysis to value, governance, organizations, portfolios, processes, incentives, investment, and enterprise transformation. Management of Complex Systems focuses on emergence, nonlinearity, irreducible uncertainty, adaptation, resilience, intervention, and learning in dynamic sociotechnical environments.

[Back to program README](OVERVIEW.md)

---

## 1. Recommended sequence

1. **EN.645.771 — System of Systems Engineering**
2. **EN.645.753 — Enterprise Systems Engineering**
3. **EN.645.742 — Management of Complex Systems**

This order moves from the most concrete engineering problem—coordinating constituent systems to deliver a capability—to the broader enterprise that funds, governs, operates, and changes those systems, and finally to the complexity-management problem of intervening when behavior cannot be predicted or controlled by decomposition alone.

Systems Thinking and Systems Dynamics is strongly recommended preparation for all three. Decision Science, MBSE analytics, advanced M&S, digital/mission engineering, and process improvement should be available for reuse rather than relearned.

## 2. Phase entry gate

Before beginning Phase 5, the learner should be able to:

* maintain a controlled requirements, architecture, interface, risk, integration, test, model, decision, and configuration baseline;
* distinguish system, system family, platform, product line, system of systems, enterprise, ecosystem, and complex adaptive system;
* build and query mission threads, capability dependencies, model-based architectures, and evidence chains;
* evaluate uncertainty, sensitivity, resilience, and model credibility without collapsing them into a single risk score;
* plan integration and T&E across hardware, software, data, people, operations, and external systems;
* identify authority, ownership, incentives, contracts, suppliers, policy, and governance as engineering constraints;
* conduct reproducible network, simulation, decision, and causal analyses;
* recognize where local optimization, hidden coupling, delay, adaptation, or strategic behavior can defeat a technically elegant intervention.

A learner missing these capabilities should complete targeted Phase 2–4 remediation before continuing.

## 3. Shared Phase 5 case

### Regional Mobility and Emergency Access Network 2040

The Phase 5 case scales the earlier campus mobility capability into a fictional regional public-service ecosystem. The region wants reliable, accessible mobility and emergency access during normal demand, major events, severe weather, utility outages, cyber incidents, infrastructure failures, and public-health emergencies.

The capability depends on independently managed constituents:

* municipal bus and rail operators;
* three campus mobility services;
* paratransit and accessibility-service providers;
* emergency medical services and hospital transport coordinators;
* traffic-management centers and connected-signal infrastructure;
* regional emergency communications and public-alert systems;
* utility, charging, telecommunications, mapping, identity, and payment services;
* private micromobility, rideshare, logistics, and autonomy vendors;
* law-enforcement, public-works, regulatory, labor, privacy, cybersecurity, and community organizations;
* state and federal data, weather, safety, and funding partners.

No organization owns the full capability. Each constituent remains useful outside the regional mission, evolves on a different schedule, controls different data, and can decline or constrain a proposed change.

Each course treats a different question:

| Course | Phase question |
|---|---|
| EN.645.771 | How should constituent systems, mission threads, interfaces, information, models, tests, risks, and evolution decisions be engineered to deliver regional capability? |
| EN.645.753 | How should the enterprise align value, governance, investment, processes, organizations, incentives, suppliers, and transformation across independent actors? |
| EN.645.742 | How should leaders reason and intervene when behavior is emergent, adaptive, nonlinear, path-dependent, politically contested, and only partially observable? |

## 4. Phase-wide operating principles

1. **Constituent systems remain independently useful and managed.** Treating them as subordinate components hides the central engineering problem.
2. **Authority is an architecture variable.** Decision rights, contracts, policy, ownership, and consent shape feasible technical solutions.
3. **Mission outcomes cut across organizational boundaries.** Capability evidence must follow end-to-end threads rather than stop at constituent acceptance boundaries.
4. **Interoperability is multidimensional.** Physical connection is insufficient without syntactic, semantic, temporal, behavioral, security, policy, and organizational compatibility.
5. **Evolution is continuous.** Baselines, interfaces, threats, suppliers, missions, and constituencies change asynchronously.
6. **Models are federated and purpose-bounded.** No model is presumed to contain the whole truth; provenance, synchronization, credibility, and use limits remain explicit.
7. **Local success can create global failure.** Measures and incentives must expose shifted risk, hidden queues, burden transfer, and mission-level degradation.
8. **Resilience requires graceful adaptation, not only prevention.** The portfolio must anticipate disruption, degraded operation, reconfiguration, recovery, and learning.
9. **Participation and legitimacy matter.** Public, workforce, privacy, accessibility, safety, and community concerns are not externalities to be added after the architecture is chosen.
10. **Interventions are hypotheses.** Every governance, architecture, investment, or policy change needs expected mechanisms, evidence, guardrails, and reversal criteria.

## 5. Common Phase 5 repository

Use a shared controlled repository:

* `/00-phase-governance-and-charter`
* `/01-constituents-organizations-and-authority`
* `/02-mission-capabilities-and-scenarios`
* `/03-architectures-interfaces-and-information`
* `/04-models-data-and-uncertainty`
* `/05-risk-resilience-security-and-safety`
* `/06-integration-test-and-operational-evidence`
* `/07-enterprise-value-process-and-investment`
* `/08-complexity-interventions-and-learning`
* `/09-reviews-decisions-and-handoffs`

Every significant artifact must record owner, source, version, status, assumptions, dependencies, authority, review state, applicability, and change rationale.

## 6. Shared evidence chain

Maintain an end-to-end chain:

> regional outcome → mission scenario → capability → mission thread → constituent contribution → interface/information dependency → analytic or test evidence → operational observation → governance or investment decision → constituent and enterprise change → updated outcome evidence

Broken links, disputed ownership, incompatible semantics, stale evidence, and unmodeled adaptation are Phase 5 risks—not documentation defects.

## 7. Phase review gates

| Gate | Course | Purpose | Minimum evidence |
|---|---|---|---|
| SoS Framing and Governance Review | EN.645.771 | Confirm SoS boundary, constituents, mission, authority, lifecycle, and evolution problem | Constituent registry, authority map, mission outcomes, SoS classification, assumptions |
| SoS Architecture Review | EN.645.771 | Approve logical, physical, and information architecture for stated mission threads | Capability dependencies, thread models, interface and information contracts, alternatives |
| SoS Evidence and Evolution Review | EN.645.771 | Decide whether risk, M&S, T&E, uncertainty, resilience, and evolution evidence support the recommendation | Federated model plan, test strategy, Bayesian/decision analysis, roadmap, residual risk |
| Enterprise Framing and Value Review | EN.645.753 | Confirm enterprise boundary, value system, stakeholders, governance, and transformation purpose | Enterprise model, value measures, actor objectives, process and authority views |
| Enterprise Architecture and Investment Review | EN.645.753 | Compare capability, process, organizational, information, and investment alternatives | Enterprise architectures, portfolio analysis, incentives, affordability, transition plan |
| Enterprise Transformation Review | EN.645.753 | Approve a governed transformation with adoption and performance evidence | Roadmap, operating model, measures, governance, risks, implementation experiments |
| Complexity Framing Review | EN.645.742 | Establish dynamic hypotheses, adaptation, emergence, uncertainty, and intervention limits | Reference modes, causal structure, actor behavior, uncertainty and observability map |
| Intervention and Resilience Review | EN.645.742 | Evaluate robust interventions, safe-to-learn experiments, and resilience strategies | Policy portfolio, simulations, stress tests, guardrails, monitoring and adaptation plan |
| Phase Portfolio Defense | All | Defend an integrated regional capability and enterprise strategy under live change | Controlled repository, cross-course traceability, evidence, decisions, limitations, defense |

## 8. Relationship among the courses

Repeated topics must increase in scale and evidentiary difficulty:

* EN.645.771 treats organizations and governance as constraints on engineering a capability; EN.645.753 makes the enterprise itself the engineered system.
* EN.645.771 uses uncertainty and resilience to support SoS architecture and evolution decisions; EN.645.742 examines emergence, adaptation, strategic response, and irreducible uncertainty as primary subjects.
* EN.645.753 develops a transformation roadmap; EN.645.742 tests whether that roadmap remains credible when actors learn, conditions shift, feedback changes, and interventions produce unintended consequences.
* Digital threads, models, simulations, processes, and decision methods from earlier phases are reused as integrated evidence—not retaught as isolated techniques.

## 9. Phase workload and pacing

Fully expanded courses target **10–13 hours per week**. Additional time may be needed for:

* cross-organization role simulation and negotiation;
* data, interface, and semantic reconciliation;
* federated model and distributed-test debugging;
* stakeholder, legal, policy, privacy, accessibility, and public-interest review;
* red-team analysis of incentives, cascading failure, adaptation, and unintended consequences;
* review preparation, finding disposition, and controlled revision.

Do not compress the phase by pretending authority, interoperability, or uncertainty problems are merely technical details.

## 10. Current development status

| Course | Status | Next action |
|---|---|---|
| EN.645.771 System of Systems Engineering | Fully expanded | Complete and pilot the course |
| EN.645.753 Enterprise Systems Engineering | Fully expanded | Complete and pilot the course |
| EN.645.742 Management of Complex Systems | Fully expanded | Complete and pilot the course |

All Phase 5 courses are fully expanded. The program-wide quality review is complete; the remaining work is controlled implementation, pilot feedback, workload calibration, and periodic maintenance.

## 11. Phase exit criteria

Phase 5 is complete when the learner can:

* distinguish an SoS, enterprise, ecosystem, and complex adaptive system and select appropriate engineering assumptions;
* model constituent independence, authority, mission threads, capabilities, interfaces, information, and evolution;
* develop logical, physical, and information architectures that remain credible under partial control;
* plan federated M&S, distributed T&E, information fusion, uncertainty analysis, and operational evidence;
* evaluate interoperability, COTS/vendor, cyber, safety, resilience, cascading-risk, and lifecycle concerns;
* model enterprise value, governance, processes, organizations, investment, incentives, and transformation;
* reason about emergence, adaptation, delay, nonlinearity, policy resistance, and path dependence;
* design robust interventions, safe-to-learn experiments, monitoring, and reversal or adaptation criteria;
* defend a regional capability and enterprise recommendation without overstating control, prediction, consensus, or evidence.

---

## Course files

- [EN.645.771 — System of Systems Engineering](EN645771.md)
- [EN.645.753 — Enterprise Systems Engineering](EN645753.md)
- [EN.645.742 — Management of Complex Systems](EN645742.md)

[Back to program README](OVERVIEW.md)
