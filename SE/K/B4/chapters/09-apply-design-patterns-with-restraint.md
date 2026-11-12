# Chapter 9 — Patterns are named tradeoffs

*Book IV: Object-Oriented Analysis and Design · Week 9 — Apply design patterns with restraint*

**Reading contract:** Work through the explanations, attempt the questions without looking at the answers, and complete [Hypothetical Lab 9](../labs/lab-09-apply-design-patterns-with-restraint.md) before attempting [the assessed Week 9 coursework](../../../C/P1/EN605704.md). For a shorter overview use the [earlier Phase 1 primer](../../P1-text/lessons/605-704-w09.md).

## The problem this chapter solves

The fictional *Northstar Campus Shuttle* begins with stakeholders asking for dependable, understandable transportation. By this stage of the curriculum, the team has learned that a system can be logically plausible and still fail when its information, behavior, software and evidence disagree. This chapter examines **apply design patterns with restraint** through a specific design decision. The objective is not to memorize a diagram type or programming term; it is to understand what claim that representation can support and what evidence it cannot supply.

A design pattern helps when a recurring force matches your problem; it becomes harmful when applied as decoration. Strategy varies a policy behind one contract; State localizes behavior by lifecycle mode; Observer distributes change notifications with eventual consistency costs. Every pattern adds indirection and therefore a maintenance burden.

## How to reason about it

Start by identifying the **decision**, the **system boundary**, and the **source of authority**. Next list the elements or constraints required to reach that decision, including abnormal operations. Explain which statements are observations and which are assumptions. Make the smallest useful model or design that exposes the important relationships. Then challenge its weakest assumption with a concrete counterexample. This reasoning discipline links directly to the technical review gates in the course.

A strong model or software design has a measurable purpose, not just syntactic correctness. Ask four questions: (1) what would a reviewer need to know to trust this representation? (2) what changes would invalidate it? (3) what does it omit? and (4) which test, scenario or inspection would reveal that omission? Use these questions to explain why the chosen representation is warranted rather than merely conventional.

## The mechanism beneath the method

Design patterns encode a response to recurring forces such as change isolation, coupling, state variation or resource ownership.

### Distinguishing related ideas

A pattern is a tradeoff, not an endorsement: adding layers to a tiny subsystem can obscure accountability as readily as it can improve extensibility.

### Interpretation and boundary conditions

Explain which future change or failure the pattern makes cheaper, and what new interface or complexity it introduces.

## Deeper theory: design patterns manage forces rather than guarantee quality

### A pattern is a reusable solution with an envelope of validity

Design patterns compress experience into named choices, but the name does not establish fitness. Observer, Strategy, Adapter, State, and Factory all move dependencies; none eliminates them. A pattern is justified by the forces in a particular problem: variability, ownership, failure isolation, testability, performance, and the expected cost of change. A class diagram that resembles a textbook pattern can still be a poor design if it introduces indirection where no meaningful variation exists.

For example, Strategy allows different algorithms to satisfy a shared interface. It is useful when dispatch policies change independently of clients and when the policies truly share a contract. If the policies disagree about fairness, safety priority, or data freshness, a common method signature conceals a semantic mismatch. The architecture needs explicit preconditions, postconditions, units, and invariant preservation. Replaceability is a claim about behavior, not just about compiling against the same interface.

### Abstraction relocates coupling

A dependency graph helps distinguish superficial modularity from actual independence. In an Adapter design, clients depend on a stable abstraction while adapters depend on vendor-specific interfaces. This can localize vendor changes, but the abstraction must still expose the capabilities necessary for the business. If it omits vendor error categories or timing semantics, compatibility becomes illusory. Adding more layers may reduce direct dependencies while increasing latency, diagnosis difficulty, and configuration complexity.

A useful evaluation therefore examines change propagation. Imagine modifying the booking protocol: which modules need source changes, which interfaces need requalification, which tests must be repeated, and which operational procedures change? A pattern earns its place when this dependency footprint is smaller or more controlled under credible change scenarios. Counting interfaces is not a substitute for measuring propagation.

### Event-driven patterns introduce queueing and ordering problems

Observer or publish–subscribe can decouple a dispatcher from notification consumers, but it introduces delivery semantics. If the event bus retries, may a consumer receive duplicates? If messages can arrive out of order, what happens when a cancellation arrives before a confirmation? If consumers are slower than producers, queues accumulate and eventually shift overload back to the producer. Little's law, `L = lambda × W` for a stable system, reminds us that throughput and waiting time imply an average number of in-flight messages; decoupling does not abolish capacity constraints.

Correctness may require idempotent consumers, explicit ordering keys, bounded retries, dead-letter handling, and versioned event schemas. These policies should be modeled as part of system behavior, not postponed as implementation trivia. Their verification requires fault scenarios rather than only normal notifications.

### Choose patterns by counterfactual comparison

A defensible architecture compares a simple direct design with the patterned design under specific future changes and stresses. The patterned version may have higher initial implementation cost but lower expected maintenance cost if variant frequency is high. Conversely, speculative extensibility can create an abstraction that users must understand and test indefinitely without ever exercising its flexibility. Cost of ownership includes diagnosis, operational monitoring, configuration management, and evidence regeneration.

Pattern application is therefore an engineering hypothesis: “This dependency structure will better tolerate these changes and failure modes.” The hypothesis can be challenged with architecture scenarios, prototypes, performance measurements, and change-impact analysis. Naming a pattern documents an intention; demonstrating its effects establishes its value.

## Worked Northstar example

A dispatch algorithm can be switched between NearestVehicle and LeastLoadedVehicle behind DispatchStrategy. Both must honor the same safety and availability constraints. Selection remains a separate policy concern; it must not mutate Reservation directly.

To turn the example into engineering evidence, record a stable identifier for every requirement or model element you invoke; identify the baseline configuration and scenario; write the decision rule before you compute or inspect the outcome; and state what would falsify the conclusion. A successful demonstration in this artificial shuttle case is an illustration of the method, never a claim about a real transportation service.



## What can go wrong—and why

Creating a factory, strategy and observer for a single immutable method needlessly multiplies code paths and tests.

Test the proposed design against a counterexample. If the representation cannot express what happens when a message is duplicated, a dependency fails, a configuration changes or a stakeholder rejects an assumption, it may be too weak for the decision. Some omissions are deliberate and acceptable; the engineering obligation is to name their scope and make the next necessary evidence request explicit.

## Worked reasoning checkpoint

**Question 1.** Which fact in this week's example is a requirement, which is an assumption and which is evidence? **Explanation:** A requirement states a normative needed outcome; an assumption limits when a prediction applies; evidence is an observed or inspected result tied to an identified artifact and context. If the example contains no actual execution result, explicitly answer “evidence not yet obtained.”

**Question 2.** What single counterexample would most effectively challenge the proposed method? **Explanation:** Choose an event that violates an implicit simplifying assumption—such as a duplicate command, stale position, incompatible model relation, race, resource shortage or obsolete test configuration—then show which invariant or mission claim fails.

**Question 3.** What must be versioned before a reviewer can reproduce this result? **Explanation:** Keep the model/design revision, interface and requirements baseline, input or fixture, acceptance criteria, procedure version and reviewer disposition. Which of these are actually necessary depends on the type of result, but omitted context must not be silently presumed.

## Hypothetical application before the course assignment

In [Lab 9: Patterns are named tradeoffs](../labs/lab-09-apply-design-patterns-with-restraint.md), you will: Compare a direct conditional with Strategy for two dispatch policies. Implement one reversible design and justify its additional interfaces. The lab provides practice rather than a ready-to-submit answer. When you can explain your method, alternative, limits and evidence, return to the real course's Week 9 deliverable and grading rubric.

## Continuity

This chapter builds from [previous chapter](08-realize-use-cases-with-dynamic-design-models.md) and leads toward [next chapter](10-express-precise-constraints-with-ocl-and-exec.md). Revisit the corresponding [weekly primer](../../P1-text/lessons/605-704-w09.md) only if you need a quick overview; use this book chapter for the deeper explanation and the assigned guide for the actual mastery standard.

## Step 03 integrated reference: when patterns improve the design—and when they do not

### 9.1 Apply patterns to a documented change or failure pressure

The case uses a *policy/strategy* boundary for vehicle eligibility. A future wheelchair-capacity rule can be implemented behind `AssignmentPolicy` without rewriting the reservation lifecycle. A *repository* port isolates the application contract from SQLite. A *transactional outbox* may become appropriate when audit or notification must cross a process boundary, but the current single-database case does not need it simply for fashion.

A pattern is useful when its consequences are better than the simpler alternative. Before choosing one, write a change scenario and a failure scenario. Example: “Different campuses require independently versioned eligibility rules” motivates strategy selection; “the audit service can be unavailable during commit” motivates a durable delivery mechanism rather than a synchronous dual write.

### 9.2 Compare alternatives with explicit decision criteria

| Design alternative | Modularity | Commit consistency | New operational burden |
|---|---|---|---|
| Policy and repository in one process | Moderate, testable ports | One local transaction | Low |
| Separate eligibility microservice | Independently deployable | Remote result may become stale | Network and contract management |
| Separate audit broker, direct publish | Independent consumer | Dual-write gap without mitigation | Failure recovery and duplication |
| Transactional outbox plus broker | Independent consumers with stored intent | Atomic local write plus eventual delivery | Worker, retention, deduplication |

There is no universal winner. If policy must remain synchronously authoritative, remote service availability becomes a hard dependency. If audit events can be eventually delivered but must not be lost, outbox semantics may help, at the cost of duplicate delivery and eventual-consistency handling. These are architecture choices, not diagram decorations.

### 9.3 An anti-pattern example

A `SingletonReservationManager` with mutable global state may pass single-threaded unit tests while failing concurrent requests and complicating isolation. Replacing it with a `Repository` abstraction is not enough if both implementations still rely on read-before-write checks. The invariant needs a storage-level constraint or a justified concurrency-control protocol. A pattern changes software structure; it does not waive the need to prove domain rules.

**Solved checkpoint.** The team suggests an `Observer` pattern to update the audit log after booking. If the observer callback runs after the database commit and fails, the log can be missing. For `SW-07`, an in-transaction audit write better meets the stated teaching contract. If an asynchronous observer is needed, introduce durable event intent and idempotent consumption.

**Exercise.** Propose a versioned selection strategy for two campuses with different accessibility policies. Define the strategy interface, configuration provenance, and a test that detects the wrong strategy being deployed.
