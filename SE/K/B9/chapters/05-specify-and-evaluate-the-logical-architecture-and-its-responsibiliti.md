# Chapter 05 — Specify and evaluate the logical architecture and its responsibilities

*Book 9 · EN.645.632 · Applied Analytics for Model-Based Systems Engineering · Week 5 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 5](../labs/lab-05-specify-and-evaluate-the-logical-architecture-and-its-responsibiliti.md) → attempt the [original Week 5 assessment](../../../C/P3/EN645632.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-632-w05.md) remains available for a quick recap.

## The decision behind the theory

The program needs an internal solution concept that organizes responsibilities without locking into vendors, products, or deployment choices. **Essential question:** Which logical architecture best realizes the required behavior while controlling coupling, failure propagation, change, and verification complexity?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the applied analytics for model-based systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Logical architecture answers who or what is responsible in an abstract sense. Elements may represent services, control domains, information stores, human roles, or operational resources without naming implementation products.

Allocate behavior and states, but also model ownership of information, policy, time, safety constraints, and exception handling. Hidden ownership is a common source of integration failure.

Use ports and exchanges to express required interaction semantics. Avoid drawing generic associations that conceal direction, type, units, timing, security, or contractual responsibility.

Analyze cohesion, coupling, fan-in/fan-out, cyclic dependence, trust boundaries, failure containment, test isolation, and likely volatility. No single metric determines architecture quality.

Compare at least two decompositions, such as centralized orchestration versus federated zone control. Record why the preferred logical baseline is chosen and which decisions are deferred.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Model state-based behavior, modes, exceptions, hazards, and temporal consistency**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Specify interfaces, exchanges, allocations, ownership, and model-based change exposure**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Logical architecture allocates obligation without freezing technology

A logical component is a responsibility boundary, not necessarily a deployed processor, organization, or software service. Logical architecture answers what functions and information must be grouped coherently to satisfy the mission. Physical architecture later answers where those responsibilities will reside and how they communicate. If this distinction is lost, early modeling choices become accidental procurement decisions before alternatives have been considered.

The most useful logical boundaries align with invariants and rates of change. Functions that must coordinate atomically may belong together, while those with different safety, security, or scaling needs may be intentionally separated. Yet separation introduces communication delays and potential partial failure. Logical decomposition is therefore not a purely aesthetic exercise in tidy boxes; it is a provisional hypothesis about where coupling is necessary and where independence has value. Interface contracts turn that hypothesis into testable design obligations.

## Deeper theory: logical architecture as a map of responsibilities and invariants

A logical architecture specifies how the necessary system behavior is organized into abstract elements and relationships before all implementation choices are fixed. Its components are **responsibility-bearing abstractions**, not disguised pieces of particular hardware. Two architectures can realize the same functions yet differ greatly in their coupling, fault containment, authority boundaries and adaptation cost. The point of logical architecture is to expose these differences while physical alternatives are still open.

A useful responsibility is more than a verb. “Manage requests” is too broad to define what must remain true. “Ensure each accepted request has at most one active capacity allocation” is a responsibility expressed as an invariant. It leads directly to questions about state ownership, synchronization, failure response and evidence. Responsibilities that share one invariant may need coordinated design. Responsibilities whose failures must be isolated may need separation, even if centralizing them would be computationally convenient.

### Interfaces are created by allocation

Suppose route eligibility and booking commitment are separate logical functions. If they share one internal state store, a transaction can potentially validate route permission and reserve capacity atomically. If they belong to different subsystems, the architecture must define what happens when permission expires between checking and committing. The decomposition introduces an interface problem whose complexity was absent from a simple function list. Good logical architecture therefore considers not only functional coverage but the **cost of preserving invariants across boundaries**.

This is related to coupling. A highly coupled architecture may require coordinated releases whenever an interface changes. A loosely coupled architecture can localize change but may need explicit contracts and asynchronous consistency mechanisms. The right trade depends on whether the information shared across elements is stable, whether decisions require immediate consistency, and whether common-cause failure or independent assurance dominates the mission risk.

### Alternative logical allocations should be compared on scenarios

Consider two candidates for Northstar. Architecture A evaluates route permissions centrally, giving one authoritative source and simpler policy updates. Architecture B gives vehicles a locally cached permission set so they can continue limited service during network outages. A is attractive for policy coherence; B is attractive for disconnection tolerance. Neither is categorically superior. A requires a credible central-service availability argument, while B requires a bounded-staleness and safe-reconciliation argument. The architectural choice is best evaluated through scenarios involving policy updates, lost connectivity, recovery and conflicting commands.

Qualitative labels such as “scalable,” “secure” and “modular” are not evidence until translated into observable behavior. If “resilient” means that already authorized trips can complete during a ten-minute network interruption, the architecture can be examined against that scenario. If the policy requires immediate revocation of all route permissions after a hazard report, cached operation may be unacceptable. The conflict is not resolved by drawing cleaner component boxes.

### Logical and physical views must remain related but distinct

A single logical service may be deployed to several redundant physical machines; several logical responsibilities may share one controller. These mappings alter availability, latency, security and maintenance. Physical redundancy does not guarantee logical independence if all replicas depend on one database or share the same faulty configuration. Conversely, a logical boundary does not imply physical isolation if the elements share power, cooling, network or personnel.

For dependability analysis, the logical architecture defines which services must work for the mission; the physical architecture defines how those services can fail together. A series mission dependency may be modeled by \(R_{\text{mission}}=\prod_i R_i\) only under appropriate independence and mission-success assumptions. If failures are dependent, multiplying marginal reliabilities can substantially overstate confidence. A trace from logical element to physical deployment must therefore preserve the relevant failure dependencies, not just the intended function allocation.

### Model completeness is contextual

No logical architecture is complete for all questions. A model adequate for functional coverage may be insufficient for cyber trust boundaries or human supervisory authority. A model meant to support resource estimates may omit detailed state transitions. Maturity should be judged by whether the model contains the relationships necessary for its declared engineering decisions. Adding irrelevant detail can actually reduce reviewability while leaving essential assumptions hidden.

The core architectural question is: **who is responsible for each system promise, what information and authority do they require, and what happens when their assumptions fail?** A logical architecture that answers those questions is far more valuable than one that merely matches a preferred diagramming style.

## Worked engineering example from the course

Two logical alternatives are modeled. Alternative L1 uses one Campus Mobility Orchestrator for request intake, dispatch, charging coordination, and incident response. Alternative L2 separates Service Policy, Dispatch Optimization, Energy Coordination, and Incident Management. L1 has fewer interfaces but creates a safety and availability concentration. L2 has clearer ownership and containment but more contracts and synchronization. The model query shows that 68% of critical functions depend on L1’s single performer; the selected hybrid retains common policy but separates safety-critical vehicle authorization and charging isolation.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Two logical designs have the same set of functions but allocate loss-of-network handling differently. In design A, the vehicle handles safe stopping; in B, a central dispatcher sends the decision. A 15-second communication outage creates different failure exposures. Map responsibilities before assigning computers or suppliers.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A model relation table contains 28 requirements, of which 21 link to at least one test and 18 have both source need and test. Calculate test-link coverage and complete-chain coverage.

<details><summary>Show a reasoned solution</summary>

Test-link coverage = 21/28 = 75%; complete-chain coverage = 18/28 ≈ 64.3%. These are structural metrics, not proof that test quality or need validity is sufficient.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Vendor products or deployment nodes appear in the logical baseline without justified abstraction.
* Critical information or safety decisions have no owner.
* Architecture selection is based only on element or interface count.
* No alternative logical decomposition is considered.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is a logical performer?
2. What is cohesion?
3. What is a trust boundary?
4. Why model deferred decisions?

<details><summary>Explain the answers</summary>

**1. What is a logical performer?** An abstract element assigned responsibility for behavior or information without committing to a physical implementation.

**2. What is cohesion?** The degree to which responsibilities within an element belong together.

**3. What is a trust boundary?** A boundary across which identity, integrity, confidentiality, authority, or assurance assumptions change.

**4. Why model deferred decisions?** They preserve uncertainty and prevent an unmade choice from becoming an implicit baseline.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 5](../labs/lab-05-specify-and-evaluate-the-logical-architecture-and-its-responsibiliti.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[04 — Previous chapter](04-model-state-based-behavior-modes-exceptions-hazards-and-temporal-con.md) · [06 — Next chapter](06-specify-interfaces-exchanges-allocations-ownership-and-model-based-c.md) · [Book index](../README.md)

## Step 03 integrated technical reference: NS-MBA9.1 — logical architecture is a hypothesis

### Partition responsibilities without hiding coupling

A logical architecture allocates behavior to coherent responsibilities independent of specific vendor hardware. In NS-MBA9.1, Dispatch handles request intake and assignment, SafetyGateway governs exclusive authorization, and Depot manages charging constraints. This separation creates a potential safety benefit but also introduces an interface whose freshness and ownership must be controlled. The [model's `I01` and `I02` definitions](../case/model.json) make those commitments inspectable.

A review of cohesion asks whether a component's responsibilities change for common reasons. A review of coupling asks which data types, timing constraints and failure modes cross boundaries. Counting connectors is insufficient: one stale authorization message may be more consequential than ten display updates. A high-risk interface deserves an exact owner, typed payload, unit convention, timing policy, failure response, and change authority.

### Compare architectures after hard feasibility screening

The [three candidates](../case/INDEX.html) have different fleet sizes and cycle estimates. Screening under the declared equations gives:

| Variant | Vehicles | Cycle (min) | Ideal trips/h | Daily energy (kWh) | Screening result |
|---|---:|---:|---:|---:|---|
| A | 10 | 45 | 13.33 | 200 | Capacity below 14 |
| B | 12 | 48 | 15.00 | 240 | Meets capacity and 260-kWh energy screens |
| C | 14 | 50 | 16.80 | 280 | Energy exceeds 260 |

Variant B survives the two displayed screens. It is therefore a **candidate for more analysis**, not an approved architecture. Accessibility evidence, charger feasibility, command latency distribution, and safety test currency are additional constraints. Hard feasibility limits should precede weighting preferences; otherwise a cheaper unsafe design can win a compensatory scoring formula.

**Exercise.** A reviewer proposes choosing variant A because it is $0.3 million cheaper than B. What change to the model or decision process could make that defensible?

<details><summary>Worked answer</summary>

First demonstrate an authorized change in requirements or a credible alternative capacity model that satisfies the same requirement under a stated operating envelope. Otherwise A remains infeasible regardless of cost. An explicit waiver by the responsible authority is a governance decision, not a mathematical proof of compliance.

</details>
