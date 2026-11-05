# Chapter 03 — Develop and analyze the functional architecture from black-box behavior to allocated white-box functions

*Book 9 · EN.645.632 · Applied Analytics for Model-Based Systems Engineering · Week 3 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 3](../labs/lab-03-develop-and-analyze-the-functional-architecture-from-black-box-behav.md) → attempt the [original Week 3 assessment](../../../C/P3/EN645632.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-632-w03.md) remains available for a quick recap.

## The decision behind the theory

The system must transform inputs into outcomes across many scenarios before a physical solution is chosen. **Essential question:** What must the system do, in what sequence and conditions, and where are the functional gaps, overloads, and couplings?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the applied analytics for model-based systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Begin with system-as-a-black-box behavior for each mission thread. Name functions as verb-object transformations and define entry, exit, input, output, control, and performance semantics.

Functional decomposition is not an organization chart. Decompose only when child functions collectively explain the parent and provide useful allocation, interface, requirement, or analysis detail.

Model support and enabling behavior: initialize, monitor, secure, diagnose, recover, maintain, update, configure, and transition. These functions often dominate lifecycle risk and are absent from nominal scenario diagrams.

White-box analysis introduces logical performers and responsibility allocation. Keep logical performers technology-neutral enough to compare implementation concepts.

Use N2, allocation, CRUD-like responsibility, and flow matrices to find duplicated control, unowned data, cyclic dependencies, excessive coupling, and single performers carrying incompatible responsibilities.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Analyze stakeholders, mission, scenarios, outcomes, and measures in the authoritative model**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Model state-based behavior, modes, exceptions, hazards, and temporal consistency**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Functional architecture represents transformations and obligations independent of their eventual implementation.

### Distinguishing related ideas

A black-box contract defines accepted inputs, outputs and conditions; decomposing it reveals internal responsibility without forcing physical packaging.

### Interpretation and boundary conditions

An interface mismatch becomes visible when a child function assumes a signal or timing guarantee absent from the parent contract.

## Deeper theory: black-box behavior and the hidden architecture of causation

A black-box model describes observable inputs, outputs and externally meaningful behavior without committing to an internal implementation. A white-box model explains how internal responsibilities and interactions generate that behavior. Moving from one to the other is not merely drawing more boxes. It is a process of **constructing a causal explanation** that preserves the required observable behavior while allocating responsibility for it.

Suppose Northstar's black-box contract states that a trip request receives either a confirmed reservation or a reasoned refusal within a fixed response window. The internal design might include identity checks, route eligibility, capacity reservation, pricing policy, durable storage and notification. The black-box claim says nothing about how those functions are organized, but it constrains what their composition must achieve. If the internal decomposition includes a workflow in which a booking can remain indefinitely in an ambiguous “pending” state, the white-box architecture does not implement the promised external behavior under that condition.

### Refinement is preservation of observations

Let \(B\) denote the set of externally permitted behavior traces under the abstract contract, and \(W\) the traces generated by the detailed design. A simplified correctness criterion is that the externally observable projection of \(W\) lies within \(B\), under stated environmental assumptions. In symbols, \(\pi(W)\subseteq B\). This idea is **behavioral refinement**. It explains why a detailed design can be more complicated yet still wrong: added internal machinery may generate new externally visible failures that the abstract contract forbids.

The projection \(\pi\) hides internal events that the outside world cannot distinguish. Choosing it carefully is important. If customers can observe a duplicate charge, then payment effects cannot be hidden as internal detail. If a rejected request creates a long but invisible background task, the task might be safely abstracted unless it consumes shared capacity and degrades later requests. A boundary choice therefore determines which behaviors the refinement argument must preserve.

### Functional decomposition produces dependencies

A function should be described by its inputs, outputs, state assumptions and constraints before being assigned to a physical element. In the shuttle case, `DetermineEligibleVehicle` depends on passenger accessibility needs, current capacity, location, route permissions and vehicle health. If location data is stale, the function's result cannot be interpreted as an unconditional eligibility fact. Decomposition must preserve assumptions as part of the contract, not erase them in a simplified output label such as `eligible = true`.

Functional flows are not always linear pipelines. Eligibility may depend on updated capacity, which depends on another concurrent booking; route permission may depend on a central authority that is temporarily unreachable. A white-box architecture therefore needs explicit state, feedback and timing models where the mission claim depends on them. A functional hierarchy can organize responsibilities, while activity and interaction models explain their dynamic composition.

### Allocation transforms internal assumptions into interfaces

When two functions are performed inside one trusted process, they may share memory and transactional state. Allocating them to independently deployed services creates an interface and new possibilities for delay, duplication, loss, and disagreement. The same logical function can have very different dependability properties depending on allocation. This is why functional analysis should precede but not replace architecture trade studies.

A model-based analytics workflow can trace a stakeholder outcome to functions, allocations, interface properties, and predicted performance measures. Yet a trace graph alone does not prove satisfaction. Suppose an analysis claims that capacity allocation meets a ninety-ninth-percentile response limit. The evidence must include the actual workload assumptions, queue behavior, model version and validation range. A perfectly connected model with the wrong arrival process produces a precise but misleading prediction.

### Control and observation are distinct roles

A system may have the authority to change a state without being able to observe it immediately. A dispatch service may issue a cancellation command while vehicle acknowledgment is delayed; it should not automatically assume the physical mission has stopped. This distinction between **command**, **observed state**, and **belief about state** is essential for safe feedback and distributed operation. It should be represented early enough that the interface architecture can account for uncertainty rather than pretending every commanded transition is instantly achieved.

The value of moving from black box to white box is thus explanatory and predictive. The internal design should make the externally required behavior plausible, reveal the dependencies on which it rests, and expose the failure paths that require testing. A larger diagram alone does none of these things.

## Worked engineering example from the course

The black-box function ‘Provide On-Demand Accessible Trip’ is decomposed into accept request, assess eligibility/accommodation, plan service, reserve capacity, dispatch vehicle, board passenger, transport, alight, and confirm completion. An initial allocation puts request validation, dispatch optimization, vehicle assignment, and exception management in one logical performer. The responsibility matrix reveals a high-coupling control bottleneck and no performer for degraded communications. The learner separates policy validation, service orchestration, and vehicle control and adds an offline dispatch-recovery function.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

A black-box function `fulfillRideRequest` may be decomposed into authentication, eligibility, assignment, pickup, and completion. If output `assignment` has no producer for the degraded-communications path, the model has a functional gap even if every normal-flow diagram is visually complete.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** A model relation table contains 28 requirements, of which 21 link to at least one test and 18 have both source need and test. Calculate test-link coverage and complete-chain coverage.

<details><summary>Show a reasoned solution</summary>

Test-link coverage = 21/28 = 75%; complete-chain coverage = 18/28 ≈ 64.3%. These are structural metrics, not proof that test quality or need validity is sufficient.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Functions are named as components or organizations.
* Nominal behavior is modeled while safety, recovery, maintenance, or transition behavior is absent.
* Allocation selects physical products before logical alternatives are analyzed.
* A query finds critical unowned behavior and no disposition is recorded.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is black-box behavior?
2. What is white-box behavior?
3. Why model enabling functions?
4. What is functional cohesion?

<details><summary>Explain the answers</summary>

**1. What is black-box behavior?** Externally observable transformation and interaction without exposing internal performers.

**2. What is white-box behavior?** Behavior expressed through internal responsibilities, interactions, and allocations.

**3. Why model enabling functions?** They make mission behavior possible, safe, secure, supportable, recoverable, and maintainable.

**4. What is functional cohesion?** The degree to which a performer or decomposition groups closely related responsibilities.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 3](../labs/lab-03-develop-and-analyze-the-functional-architecture-from-black-box-behav.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[02 — Previous chapter](02-analyze-stakeholders-mission-scenarios-outcomes-and-measures-in-the-.md) · [04 — Next chapter](04-model-state-based-behavior-modes-exceptions-hazards-and-temporal-con.md) · [Book index](../README.md)
