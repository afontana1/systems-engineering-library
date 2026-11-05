# Chapter 04 — Model state-based behavior, modes, exceptions, hazards, and temporal consistency

*Book 9 · EN.645.632 · Applied Analytics for Model-Based Systems Engineering · Week 4 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 4](../labs/lab-04-model-state-based-behavior-modes-exceptions-hazards-and-temporal-con.md) → attempt the [original Week 4 assessment](../../../C/P3/EN645632.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-632-w04.md) remains available for a quick recap.

## The decision behind the theory

Many failures occur because the system behaves correctly in a nominal flow but incorrectly during mode changes, interruptions, retries, or recovery. **Essential question:** Are the system and its critical elements behaviorally complete and consistent across states, events, modes, and exceptional conditions?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the applied analytics for model-based systems engineering perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

A state represents a condition during which invariant properties or event responses apply. Do not turn every activity step into a state. Use state machines where history, mode, lifecycle, availability, or event legality matters.

Define events and guards explicitly. A transition labeled ‘error’ without source, detection logic, guard, action, and destination is not analysable.

System modes coordinate multiple performers. Model allowed combinations and transition responsibilities; independent subsystem state machines can create forbidden configurations, race conditions, or deadlocks.

Trace hazards and failure modes to detection, containment, degraded service, recovery, and safe-state behavior. Recovery without a restoration criterion is incomplete.

Cross-view consistency queries should compare scenario events, state transitions, activity actions, interface signals, and requirements. The goal is not identical diagrams but compatible semantics.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Develop and analyze the functional architecture from black-box behavior to allocated white-box functions**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Specify and evaluate the logical architecture and its responsibilities**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Behavior models add temporal constraints to static allocations: what states exist, when transitions occur and which exceptions are legal.

### Distinguishing related ideas

An activity diagram portrays flow, while a state machine preserves lifecycle memory; neither alone gives a complete assurance argument.

### Interpretation and boundary conditions

A stale command may be syntactically valid yet forbidden by the present operational mode, making guard semantics essential.

## Deeper theory: behavioral models are contracts about time and concurrency

### State semantics must survive translation between views

An activity model may show “check vehicle ready, then authorize boarding,” while a state machine shows `Stationary → BoardingEnabled`. These diagrams can look compatible while making different assumptions about timing, atomicity, or the meaning of ready. A model-based workflow should define the shared predicates and events: whether `Ready` is a measured condition, a message, or an approved decision; who owns its truth; and what transition invalidates it. Without those contracts, cross-view trace links may connect contradictory propositions.

A state-based model can be described as states and allowed transitions, but a system of systems rarely has one globally synchronized transition order. The vehicle, passenger application, and dispatch service observe events at different times. A model that imposes an idealized global clock may hide a real race. The design needs an explicit execution semantics for message receipt, delayed observations, duplicate requests, network partitions, and contradictory local beliefs. Sometimes the correct abstraction is nondeterministic: several event orders are possible and every permitted order must preserve a safety constraint.

### Temporal logic expresses more than nominal scenarios

A safety invariant might be “always, if boarding is authorized then vehicle motion is disabled.” In temporal notation this resembles `G(Authorized → ¬MotionEnabled)`. A liveness requirement might say “every accepted request eventually completes or reaches a reported terminal disposition,” resembling `G(Accepted → F(Completed ∨ ReportedException))`. The latter requires assumptions about fair scheduling, repair, user cooperation, and whether the environment can block progress indefinitely. Writing a temporal formula does not make an impossible guarantee attainable; it forces those assumptions into view.

Timed behavior needs more precision. If an authorization expires after `Δt` seconds, clocks and freshness definitions must be defined. A controller can satisfy an untimed safety invariant and still respond too slowly to prevent harm. Conversely, overly strong temporal constraints can make the model unrealizable under plausible communication failures. The obligation is to specify meaningful deadlines and exception modes, not to make every action instantaneous in the model.

### Verification depends on abstraction and environment

Model checking explores the traces of a formal representation to find violations of stated properties. A counterexample is often more educational than a success indication because it shows an unexpected event order or missing guard. But “property holds” means only that it holds in the represented state space and under declared assumptions. Omitting stale messages, limiting retries to one, or bounding the number of vehicles can make the checked model much easier than the intended deployment.

For Northstar, use the behavioral model as a shared semantic contract among controls, interfaces, hazards, and verification. When test evidence reveals a new event sequence, update both the model and the constraint it was intended to represent. A state diagram becomes genuinely authoritative when its rules agree with the relevant requirements, physical timing, message semantics, and abnormal operations—not merely when all its transitions are connected graphically.

## Worked engineering example from the course

During cold-weather charging, the vehicle can be in Available, Reserved, EnRoute, Charging, Degraded, Isolated, or Maintenance states. The charger can be Idle, Negotiating, Energizing, Paused, Faulted, or LockedOut. A simulation trace reveals that a network timeout moves the vehicle to Degraded while the charger remains Energizing and the dispatch service still marks the vehicle Available. The learner adds coordinated timeout events, ownership, invariant constraints, a safe isolation action, and a recovery verification case.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Let a request be in exactly one of {submitted, accepted, assigned, boarded, completed, cancelled}. If `cancelled → completed` has no transition, a log claiming both states requires either a new transition rule or a data-correction explanation. Temporal logic concerns allowable sequences, not just the names of states.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** If demand rises 30% from 20 to 26 requests/hour while modeled capacity is 24/hour, calculate the nominal capacity gap.

<details><summary>Show a reasoned solution</summary>

The gap is 26−24=2 requests/hour. This is an arithmetic screening calculation; burstiness and queue buildup require a dynamic model.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Activities are relabeled as states without state invariants or event semantics.
* Critical events have no owner or transition response.
* A hazardous state combination is possible and undispositioned.
* Recovery returns to operation without defined readiness criteria or verification.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What is a state invariant?
2. What is a guard?
3. What is an orthogonal region?
4. Why model system modes?

<details><summary>Explain the answers</summary>

**1. What is a state invariant?** A condition that must remain true while an element is in a state.

**2. What is a guard?** A Boolean condition that must be true for a triggered transition to occur.

**3. What is an orthogonal region?** A concurrent region of a state machine whose state evolves in parallel with other regions.

**4. Why model system modes?** They coordinate allowed behavior and configurations across multiple elements.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 4](../labs/lab-04-model-state-based-behavior-modes-exceptions-hazards-and-temporal-con.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[03 — Previous chapter](03-develop-and-analyze-the-functional-architecture-from-black-box-behav.md) · [05 — Next chapter](05-specify-and-evaluate-the-logical-architecture-and-its-responsibiliti.md) · [Book index](../README.md)
