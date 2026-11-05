# Chapter 06 — Specify interfaces, exchanges, allocations, ownership, and model-based change exposure

*Book 9 · EN.645.632 · Applied Analytics for Model-Based Systems Engineering · Week 6 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 6](../labs/lab-06-specify-interfaces-exchanges-allocations-ownership-and-model-based-c.md) → attempt the [original Week 6 assessment](../../../C/P3/EN645632.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-632-w06.md) remains available for a quick recap.

## The decision behind the theory

Interfaces are where independently designed responsibilities meet and where changes propagate. **Essential question:** Are the exchanges, contracts, ownership, and allocations precise enough to support physical synthesis, integration, and change control?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the applied analytics for model-based systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

An interface is a boundary and agreement; an exchange is what crosses it. Model both. A line labeled ‘data’ is insufficient for architecture or verification.

Define semantic, physical, temporal, quality, security, and failure properties. Examples include schema, units, coordinate frame, valid range, update rate, latency, jitter, freshness, authority, acknowledgment, retry, and degraded behavior.

Assign an interface owner and configuration authority while preserving provider and consumer responsibilities. Ownership does not mean one side may change the contract unilaterally.

Allocations are analytic assertions and must be checked. Behavior may be split across elements; requirements may constrain interactions; measures may be computed from multiple properties.

Change-impact analysis follows the relationship graph and configuration rules. Distinguish potentially affected from confirmed affected elements, and preserve the query, baseline, rationale, and disposition.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Specify and evaluate the logical architecture and its responsibilities**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Elicit, derive, validate, and query system requirements from the integrated analysis**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Analytic interface models translate exchanges into units, rates, latency and ownership, enabling quantitative feasibility checks.

### Distinguishing related ideas

A connected port does not imply compatible sampling rates or legal timing; two correctly typed signals can still be temporally inconsistent.

### Interpretation and boundary conditions

Communication feasibility depends on peak demand and correlated bursts, not just a nominal throughput comparison.

## Worked engineering example from the course

A proposal changes accessible boarding events from a binary flag to a structured accommodation request. The impact query identifies the passenger app contract, dispatch policy, vehicle reservation function, privacy requirement, state transitions, data store, training procedure, six tests, and the wait-time analytics notebook. The learner distinguishes required changes from false-positive graph neighbors, updates the interface schema and version policy, and records compatibility and migration behavior.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

An interface record should distinguish a message field from a contract: `request_id` is a field, while duplicate suppression, acknowledgement within 2 seconds, and retention of event order are behavioral obligations. If two consumers disagree on sequence numbering, interface completeness is not demonstrated by matching JSON schemas.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** If demand rises 30% from 20 to 26 requests/hour while modeled capacity is 24/hour, calculate the nominal capacity gap.

<details><summary>Show a reasoned solution</summary>

The gap is 26−24=2 requests/hour. This is an arithmetic screening calculation; burstiness and queue buildup require a dynamic model.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Critical exchanges remain untyped or unitless.
* No configuration authority or verification owner exists for a critical interface.
* A change is declared low impact based only on diagram inspection.
* Provider and consumer assumptions conflict without disposition.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is an interface contract?
2. What is an item flow?
3. What is impact overreach?
4. Why version interfaces?

<details><summary>Explain the answers</summary>

**1. What is an interface contract?** The controlled agreement defining the boundary, exchanges, obligations, constraints, quality, failure, compatibility, and verification semantics.

**2. What is an item flow?** A modeled specification of an item or value conveyed across a connector or interaction path.

**3. What is impact overreach?** Treating every graph neighbor as truly affected without engineering confirmation.

**4. Why version interfaces?** Consumers and providers may evolve independently; versioning supports compatibility, migration, and controlled retirement.

</details>


## Deeper theory: interface contracts as semantic and temporal agreements

### Interfaces connect interpretations, not only connectors

A physical connector, API route, or message schema identifies how information or energy crosses a boundary. It does not settle what the receiver is entitled to infer. A message field `available=true` might mean that a vehicle is powered, locally self-tested, authorized by dispatch, or able to accept a passenger. Each interpretation permits different actions. An interface contract should therefore define the proposition represented by each state, the producing authority, units, coordinate frames, timestamps, validity periods, and expected behavior when information is missing or contradictory.

An interface may also express *assume–guarantee* reasoning. Component A guarantees an output property if its environment supplies specified inputs and timing; component B guarantees the needed input conditions if its own assumptions hold. Composition succeeds only when the assumptions are mutually satisfied. If B guarantees fresh location data within five seconds but A implicitly assumes data no older than one second, the components are incompatible even though all packet formats match. Such mismatches should be discovered in modeling rather than in field incidents.

### Time and state consistency shape system behavior

In distributed systems, messages can be delayed, duplicated, reordered, or lost. A sender's timestamp does not automatically establish what the receiver currently knows. Clock synchronization has uncertainty, and a state update can become invalid while in transit. A robust interface contract defines maximum tolerated age, sequence or version semantics, detection of gaps, acknowledgment expectations, retries, and safe behavior when updates stop. For safety-critical commands, it must also address authorization, replay protection, and how to resolve conflicting instructions.

A simple freshness rule might accept a report if `receiver_time − source_time ≤ 2 s`. This is valid only if clocks use compatible epochs and their error is bounded; otherwise the computed age can be negative or misleading. A conservative contract may account for worst-case clock offset and transport delay, or use a receiver-side timeout with explicit limitations. A protocol test should challenge the uncertainty around the boundary, not merely send a few correctly formed messages.

### Interface ownership is a governance mechanism

An interface control document is meaningful only when changes require coordinated review from both sides. A supplier may update field precision, default status values, or retry semantics while believing backward compatibility is preserved. If downstream engineering depended on the old interpretation, the change can invalidate tests and safety arguments. Contracts should identify the authoritative owner, approved versions, compatibility rules, failure codes, and evidence needed to accept a change. A machine-readable schema can check syntax; semantic conformance still requires scenario-based verification.

For the Northstar dispatch-to-vehicle boundary, a defensible agreement would define assignment identity, expiration, who can cancel or supersede it, vehicle confirmation semantics, localization uncertainty, communication loss handling, and reconciliation after reconnection. This connects interface engineering to transaction theory, formal state machines, cybersecurity, and human operations. The boundary of the method is explicit: a complete contract is a necessary basis for integration, but an implementation can still violate it, and an agreed contract can still be based on an invalid mission assumption.

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 6](../labs/lab-06-specify-interfaces-exchanges-allocations-ownership-and-model-based-c.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[05 — Previous chapter](05-specify-and-evaluate-the-logical-architecture-and-its-responsibiliti.md) · [07 — Next chapter](07-elicit-derive-validate-and-query-system-requirements-from-the-integr.md) · [Book index](../README.md)
