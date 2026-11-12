# Chapter 4 — Architecture is the set of costly-to-reverse decisions

*Book V: Software Systems Engineering · Week 4 — Frame the software architecture within the system architecture*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 4](../labs/lab-04-frame-the-software-architecture-within-the-sy.md) before attempting [the assessed Week 4 coursework](../../../C/P1/EN645764.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/645-764-w04.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **frame the software architecture within the system architecture** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

Software architecture defines components, connectors, deployment constraints and rationale for quality attributes. Many diagrams are possible; useful views show runtime behavior, deployment, data ownership and failure domains. Select viewpoints by stakeholder concerns. Architecture decisions should include alternative, context, consequences and the scenario that would invalidate the choice.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## A deeper explanation: software architecture as the allocation of uncertainty

### Components are less important than the boundaries between them

Architectural diagrams naturally draw attention to boxes called “booking service,” “dispatch,” and “vehicle gateway.” A graduate-level architectural analysis asks a harder question: **what becomes independently changeable, independently fallible, and jointly constrained when those boxes are separated?** Two functions in one process can share memory and a transaction. Place them in different processes and their communication now has delay, potential duplication, ambiguous ordering, and partial failure. The functional goal may be unchanged, but the obligations of the architecture have expanded.

Northstar illustrates the tradeoff. In a single reservation component, checking remaining capacity and recording a seat hold can be one atomic operation. In a decomposed system, the booking component may send a request to dispatch, wait for a response, and then update its own record. If the response is lost, it may not know whether dispatch accepted the hold. Retrying can create duplicate reservations unless commands have stable identities and the receiver handles repetitions safely. The architecture must decide where authority resides and how uncertainty will be resolved.

### Data ownership is a systems decision

A database is sometimes treated as a storage detail. In distributed systems, deciding which component owns a fact determines what the rest of the system can guarantee. If the booking service and dispatch service both believe they are authoritative for available seats, temporary network separation can cause conflicting promises. A single logical authority simplifies consistency but can become a bottleneck or a failure dependency. Replication improves access but introduces rules for reconciling updates and interpreting stale reads.

A design therefore needs explicit answers to questions such as: What event makes a reservation final? Can a command be accepted provisionally? What must the user see during uncertainty? Can an offline vehicle override the dispatcher? What is the recovery procedure if components disagree after reconnection? These are architectural contracts, not implementation trivia. They also connect software design to human factors because a technically honest “pending” status may be more operationally useful than an incorrect “confirmed” response.

### Quality attributes are scenarios, not adjectives

Calling a system “reliable,” “secure,” or “scalable” is too vague to guide architecture. The useful unit is a **quality-attribute scenario**: a stimulus, an operating condition, an affected element, and a measurable response. “During peak demand, when the communication link to a vehicle is unavailable for up to 90 seconds, the service must not promise a capacity allocation that it cannot reconcile” is informative because it exposes the fault and required behavior. “The system shall be robust” is not.

Different attributes interact. Reducing latency through aggressive caching can increase staleness. Adding replication can increase availability while complicating consistency. Strict authorization checks can reduce unauthorized actions while increasing the time required for emergency intervention. The architectural goal is not to maximize every quality attribute independently. It is to choose a tolerable set of compromises and show that the resulting system can satisfy its most important scenarios.

### Why availability calculations can mislead

If two independent services must both be operational for a request to succeed, a simple steady-state approximation multiplies their availabilities. If each is available 99.5% of the time, the combined path is approximately \(0.995^2 = 0.990025\), or 99.0025%. That calculation is useful but rests on independence and an extremely simplified success path. Shared identity infrastructure, networking, deployments, or power failures can correlate outages. A redundant architecture that duplicates servers but not their failure domains may deliver far less resilience than its block diagram implies.

Availability is also not the same as successful service. A dispatch API can be reachable while returning answers too late to help passengers. A database can be healthy while containing inconsistent reservation state. A useful architecture therefore connects infrastructure measures to mission outcomes and defines recovery, degraded operation, and human-visible uncertainty, not only component uptime.

### Architecture is an economic and organizational commitment

Every boundary incurs coordination overhead. Splitting services can enable teams to deploy independently, but only if their interfaces are stable and the organization can operate the resulting distributed system. A component boundary that looks elegant in a diagram may impose more monitoring, testing, security review, and incident response than a small team can sustain. Conversely, a tightly coupled monolith can hinder changes that must be independently certified or deployed.

The correct choice depends on rate of change, assurance needs, team capability, failure isolation, and lifecycle costs. The enduring principle is that architecture distributes **state, authority, failure, and change**. The component diagram is a visible artifact of those deeper decisions.

## The mechanism beneath the method

Software architecture determines the distribution of state, authority and failure, making some changes cheap and others expensive.

### Distinguishing related ideas

Module decomposition optimizes code organization, while operational architecture determines where decisions are committed and how partial failures are handled.

### Interpretation and boundary conditions

A reservation service split across processes needs explicit transactional boundaries even if its class diagram is elegant.

## Worked Northstar example

A monolithic reservation service simplifies atomic capacity holds but can be less independent to deploy; separate booking and dispatch services improve isolation yet introduce consistency and messaging contracts. Evaluate both against failure tolerance and team capabilities, not fashion.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Microservices do not automatically confer scalability or reliability; each network boundary is another partial-failure mechanism.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 4: Architecture is the set of costly-to-reverse decisions](../labs/lab-04-frame-the-software-architecture-within-the-sy.md), you will: Draw two alternative component/deployment views and record an architecture decision with explicit rejection conditions. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 4 deliverable and grading rubric.


## Graduate depth: architecture as optimization over change and failure
### Architecture decisions create a long-lived feasible region

A software architecture allocates computation, state, communication, security authority, and failure containment across components. It is not synonymous with a diagram or technology stack. A decision to centralize dispatch state, partition services by bounded context, or run control loops at the edge determines which performance and assurance options remain feasible. Later optimization occurs inside the limits created by those decisions. The architecture should therefore be assessed against a family of quality-attribute scenarios—ordinary load, peak load, degraded communication, malicious traffic, and maintenance—rather than one nominal benchmark.

Architectural coupling has several forms. Static dependency coupling makes code changes propagate. Runtime coupling creates correlated outages through shared infrastructure or blocking calls. Data coupling creates schema and migration dependencies. Governance coupling makes separate teams wait on the same decision authority. Breaking one form of coupling can increase another: microservices may improve deployment independence while introducing distributed transactions, observability demands, and network failure modes. There is no architecture style that is best independent of the system's constraints and organizational capabilities.

### Quality attributes interact through shared resources

Latency, availability, confidentiality, consistency, and cost are often competing attributes. If average arrival rate is `lambda` and service capacity is `mu`, an ideal M/M/1 queue is stable only when `lambda < mu`, and its mean time in the system is `1/(mu - lambda)`. This is an illustrative queueing result under Poisson arrivals, exponential service, and one server; real dispatcher workloads may be bursty and correlated. The lesson is the nonlinear rise in delay as utilization approaches saturation. Replication may reduce queueing, but shared databases and coordination protocols can limit its benefit.

Consistency decisions are also scenario-dependent. A rider-facing status board may tolerate temporarily stale positions; exclusive vehicle assignment may not tolerate two simultaneous authoritative allocations. Classify state by the consequences of inconsistency, rather than applying one global consistency rule. Likewise, authentication and audit logging consume CPU, storage, and human attention, but removing them to meet a latency target can invalidate safety or trust claims.

### Architecture evaluation requires counterfactuals

Consider two Northstar options: a central decision service with strong transaction control and edge services that can make local degraded-mode choices. The centralized option offers a simpler global invariant but depends on communication and server availability. The distributed option can preserve some service during disconnection but must define reconciliation and authority transfer. The decision should evaluate explicit scenarios, thresholds, and uncertainty: how long can links fail, which actions are allowed offline, how are conflicts resolved, and how will engineers demonstrate correctness?

Useful architecture records preserve the decision, alternatives considered, assumptions, expected quality consequences, evidence, and reversal cost. Testability and observability deserve explicit treatment: a sophisticated architecture that cannot explain or reproduce its failures is difficult to assure. Prototypes can test risky mechanisms, but a successful prototype under one load profile cannot establish production reliability. This connects software design to system-level trade studies, verification architecture, and lifecycle economics. The best choice is the one whose constraints, risks, and future evolution costs are legible for the intended mission.

## Continuity

This chapter builds from [previous chapter](03-interpret-and-critique-the-system-model-for-s.md) and leads toward [next chapter](05-integrate-agile-product-engineering-with-syst.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/645-764-w04.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.


## Step 03 integrated reference: choose architecture against measured obligations

### Identify the decisions that are expensive to reverse

NS-SW5.1 proposes six ownership boundaries, but only some need deployable process boundaries. The important decisions are where reservation state is authoritative, how uncertain replies are reconciled, which dependencies are allowed to block an acknowledgment, and how the operator learns the system cannot serve a request. Turning every component into a network microservice would add fault modes without automatically improving these obligations. A modular service with a transactional store may be simpler than a fully distributed orchestration, provided its scaling and isolation limits are understood.

In [the interface contract](../case/interfaces.csv), IF-02's uncertain outcome is fundamental. A robust design assigns each requested reservation an idempotency token, records the accepted outcome atomically with the slot assignment, and returns the same outcome on a bounded repeat. The database protects uniqueness while the API protects the request semantics; neither alone guarantees exactly-once network delivery.

### Compare dependencies quantitatively

A simplistic two-service serial dependency with independent interval availabilities of 0.9995 each yields

\[A_{\mathrm{series}}=0.9995^2=0.99900025\approx99.9000\%.\]

If a separately modeled common-cause condition disables the path with probability 0.001 in the same interval, an illustrative expression is

\[A_{\mathrm{shared}}=(1-0.001)\,A_{\mathrm{series}}\approx99.8001\%.\]

These are interval probabilities under strong assumptions, **not** derived monthly uptime or safety performance. Their purpose is to show how shared dependencies can cancel a redundancy benefit. The [checker](../tools/step03_book5_system_check.py) calculates both values so students can vary the shared-cause assumption.

### Architecture decision record

For a change to a distributed reservation service, document the issue, alternatives, quality scenarios, constraints, supporting evidence, limitations and revisit trigger. Alternative A may keep a single transaction boundary; B may split inventory and policy services; C may replicate read state but serialize writes. A decision that favors B for team independence must still explain what happens when policy succeeds and inventory times out. Reject any proposed architecture whose failure semantics cannot be explained under load and partial failure.

**Exercise.** An architect claims that adding an independent cache makes no-overlap correctness more reliable because it eliminates database reads. **Answer.** A cache might reduce normal read latency, but stale cached availability cannot enforce authoritative unique allocation. The decision must preserve the atomic write constraint and specify invalidation and reconciliation. The architecture is a collection of justified failure-boundary choices, not a component-count competition.
