# Chapter 05 — Implement discrete-event processes, resources, queues, priorities, and statistics

*Book 11 · EN.645.757 · Foundations of Modeling and Simulation · Week 5 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 5](../labs/lab-05-implement-discrete-event-processes-resources-queues-priorities-and-s.md) → attempt the [original Week 5 assessment](../../../C/P3/EN645757.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-757-w05.md) remains available for a quick recap.

## The decision behind the theory

Tool fluency matters only when it faithfully implements the approved conceptual model. **Essential question:** Can the learner translate state and event logic into a transparent, testable executable model?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the foundations of modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

Discrete-event simulation advances from event to event rather than through every clock tick. State changes at events; future events are scheduled by logic and sampled durations.

Use explicit units. Time, energy, distance, capacity, and probabilities should be named and checked; hidden unit conversions are common model defects.

Random streams should be controlled by purpose. Separate streams or generators can support paired comparisons and diagnose unintended coupling.

Instrumentation is part of design. Event traces, counters, state snapshots, queue histories, and assertions support verification and later analysis.

Keep experiment configuration external where practical so scenarios can be compared without modifying implementation logic.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Use M&S for needs, opportunity, current-state, and baseline analysis**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Model detailed operations and complete computational verification**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### A discrete-event model is a state machine with time

Discrete-event simulation advances the simulated clock from one consequential event to another, updating system state at those instants. Its core objects are events, resources, queues, and state-transition rules. In a mobility service, an arrival may enter a queue, an assignment may seize vehicle capacity, and a completion may release that capacity. These operations must obey invariants: no vehicle simultaneously serves two incompatible trips, and requests cannot depart before they arrive.

The event calendar also forces decisions about simultaneous events. Does a cancellation processed at exactly the same time as dispatch release capacity before or after allocation? Different event-priority policies can produce different results even with identical input streams. Random generators add variability, but **stochasticity does not eliminate the need for deterministic semantics**. A credible simulator states its event ordering, validates conservation and state bounds, and checks hand-computed simple cases before drawing conclusions from large batches of runs.

## Deeper theory: event systems, queueing limits, and state-dependent operations

### A discrete-event model is a transition system, not an animation

A discrete-event simulation can be specified by a state `x(t)`, an ordered set of future events, transition rules, and a statistical observation process. Between event times, its relevant state is held constant; at an event, `x(t+) = T(x(t-), e, u)` applies a transition based on the pre-event state, event `e`, and any policy input `u`. For a Northstar vehicle-dispatch example, state may include the number of waiting travelers, vehicle locations, free berths, crew availability, and the next appointment deadline. An arrival event increments a queue; a boarding-completion event releases a berth and may schedule a vehicle departure. This distinction makes the *semantics* of the model auditable. The graphical icon of a bus is incidental; the event ordering and rules determine what the bus can actually do.

Simultaneous events expose hidden assumptions. Suppose a berth-release event and an arrival event share a timestamp. Does the arriving vehicle claim the berth before a scheduled emergency departure? A simulator's arbitrary processing order may bias priority statistics even when all event times are correct. Define a tie-breaking rule based on the operating policy, and identify processes that must be atomic. For repeated experiments, record the initial state, random stream assignment, event-calendar rules, priority definition, and stopping condition. Reproducibility is a claim about a specified stochastic experiment, not simply about rerunning a file.

### Queueing identities constrain what a plausible model can claim

Let `λ` be the long-run arrival rate, `W` the mean time an entity spends in a stable system, and `L` the corresponding mean number of entities present. Under appropriate stability and averaging conditions, Little's law gives `L = λW`, independent of the detailed service-time distribution. If 24 passengers per hour enter a transfer system and mean time within its boundary is 15 minutes, the implied average work in process is `L = 24 × 0.25 = 6` passengers. This identity provides a valuable consistency test; it does not predict the waiting-time distribution or guarantee that transient observations satisfy the same relation.

For an idealized `M/M/1` server, with Poisson arrivals and exponential independent service times, utilization is `ρ = λ/μ` and mean time in the system is `W = 1/(μ−λ)` when `λ < μ`. As arrival rate approaches capacity, delay increases nonlinearly. At `λ = 8` and `μ = 10` vehicles/hour, `W = 0.5` hour; at `λ = 9.5` with unchanged capacity, it becomes two hours. This is not a forecast of Northstar's station: its passenger groups, scheduled departures, priority classes, finite waiting areas, and service variability violate the simple assumptions. It explains why a facility that is busy but apparently functioning can become brittle under a small demand increase.

### Priority rules transfer risk between populations

First-come-first-served, earliest-deadline-first, and emergency priority can all be internally rational while producing different mission outcomes. Giving emergency transfers priority reduces their conditional delay but can starve other requests when emergency arrivals are frequent. Preemptive priority also differs from nonpreemptive priority: interrupting an active boarding process may introduce safety and setup costs, whereas allowing it to finish may miss a critical response window. A model should calculate time in queue by class, deadline misses, abandonment, and utilization rather than reporting only an overall average that hides those transfers.

Service and arrival processes are often dependent. Bad weather simultaneously increases emergency demand, lengthens vehicle travel, and reduces available berths. Sampling three independent random numbers from empirical marginal distributions cannot reproduce that coupling. Where dependence is supported by evidence, sample a joint scenario or introduce shared state drivers, such as weather and road closures. When evidence is weak, vary the assumed dependence explicitly. A dispatch policy that works in independently generated worlds may fail when the same incident increases demand and destroys capacity.

### Model boundaries and verification are part of the result

In an event model, lost entities and impossible negative resources can arise from small bookkeeping errors. Conservation provides a test: `arrivals = completed + in_system + abandoned` over a run, after clearly defining boundary crossings. Resource capacity cannot be negative, a passenger cannot board two vehicles, and an incident response cannot finish before it starts. Instrument these as invariants rather than inspecting a few animation traces. At the conceptual level, ask what the model omits: traveler behavior, accessibility assistance, telecommunication outages, and human overrides may change the relative ranking of policies. The appropriate conclusion is conditional: an event model supports a choice only within its declared state structure, stochastic assumptions, and operational envelope.

## Worked engineering example from the course

A one-vehicle model is run with deterministic arrivals and service times. Hand calculation predicts completion times and maximum queue length. The executable trace matches until a request at the same timestamp as service completion exposes an event-priority rule; the conceptual model is updated and the rule is tested.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

For a single-server M/M/1 queue with λ=8/hour and μ=10/hour, utilization ρ=0.8 and expected system time W=1/(μ−λ)=0.5 hour. As λ approaches 10, W rises nonlinearly. These formulas are checks for specific assumptions, not general fleet results.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** For a theoretical M/M/1 queue λ=8/hour and μ=10/hour, calculate utilization and expected time in system.

<details><summary>Show a reasoned solution</summary>

ρ=8/10=0.8; W=1/(10−8)=0.5 hours=30 minutes. M/M/1 assumptions are restrictive.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* The model runs but has no deterministic verification case.
* Time or capacity units are implicit or inconsistent.
* Scenario changes require editing core logic without control.
* Random-number state cannot be reproduced.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What advances time in a discrete-event simulation?
2. Why use deterministic cases?
3. What is an invariant?
4. Why separate random streams?

<details><summary>Explain the answers</summary>

**1. What advances time in a discrete-event simulation?** The simulation clock jumps to the next scheduled event time.

**2. Why use deterministic cases?** They create predictable results for logic verification independent of stochastic noise.

**3. What is an invariant?** A property that must remain true throughout execution, such as nonnegative queue length or capacity limits.

**4. Why separate random streams?** To control stochastic sources, support paired comparisons, and avoid accidental dependence.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 5](../labs/lab-05-implement-discrete-event-processes-resources-queues-priorities-and-s.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[04 — Previous chapter](04-use-m-s-for-needs-opportunity-current-state-and-baseline-analysis.md) · [06 — Next chapter](06-model-detailed-operations-and-complete-computational-verification.md) · [Book index](../README.md)

## Step 03 integrated mobility simulation case: event scheduling and resource logic

### A discrete-event model is an executable set of transition rules

At simulated time \(t\), select the earliest record \((t_e,\mathrm{sequence},\mathrm{type},\mathrm{payload})\) from a min-heap and set \(t\leftarrow t_e\). A monotonically increasing sequence breaks exact-time ties reproducibly. Events generated by an active operation (trip or charging) are scheduled into the future; simulation time does not advance for each idle minute. The [standard-library simulator](../tools/step03_book11_mobility.py) uses `heapq`, `random.Random`, and explicit state updates, so its numerical outputs can be reconstructed offline.

A request is eligible for a vehicle if the vehicle is idle and either the trip is standard or the vehicle is marked accessible. The current dispatch algorithm scans waiting requests in order and allocates the first compatible free vehicle. This means a standard request may consume an accessible resource while an inaccessible vehicle sits idle, which can harm accessible waits. That outcome is an **exposed policy assumption**, not evidence that an accessibility-prioritized real dispatch system would behave identically.

Once assigned, \(t_{done}=t_{pickup}+t_{boarding}+t_{travel}\). Fractional SOC changes as \(SOC_i\leftarrow SOC_i-e\), with synthetic energy draw \(e\in[0.065,0.12]\) per trip. When SOC falls below 0.22 at trip completion, the vehicle queues for a charger. Charge time is Triangular(24,32,50) minutes, and completion returns SOC to one; while charging, a vehicle cannot dispatch. There are initially four chargers. The model does not include charger transit, staggered charging, failures, physical battery thermal behavior or route-specific kWh accounting.

### Verify the scheduling rules with a hand-computed trace

At \(t=0\) a request arrives and occupies the only compatible vehicle for 5 minutes. At \(t=1\), a second request joins the wait queue. At \(t=5\), completion makes the vehicle idle; the second request is picked up immediately. Wait times are \(0\) and \(4\) minutes. With the nearest-rank empirical p90 \(x_{(\lceil0.9(2)\rceil)}\), the index is 2 and p90 = **4 minutes**. An implementation that returns 2 minutes because it averages the waits has computed the *mean*, not p90. An implementation that assigns the second request at minute 1 has violated the one-request-per-vehicle resource constraint.

A second invariant checks that occupied, idle, waiting-to-charge and actively charging vehicles sum to fleet size. Further assertions bound charger concurrency, SOC, and the eventual equality of pickups and request count when the after-close cleanup events complete. Such assertions identify internal contradiction; they cannot identify missing traffic intersections or under-specified priorities.

### Queueing theory is a critic, not a substitute for the DES

For a stable *hypothetical* M/M/1 queue with rate \(\lambda<\mu\), \(\rho=\lambda/\mu\) and \(E[W_{system}]=1/(\mu-\lambda)\). At 8/hour demand and 10/hour service, the expectation is 0.5 hour. Here \(W_{system}\) includes service and must not be silently compared with the mobility model's **pickup** wait. M/M/1 assumptions of one server, steady state, exponential service and nonpriority customers do not match this fleet. Use it only to check dimensions and warn how waiting diverges as \(\rho\to1\).

**Exercise with solution.** Four vehicles are charging and a fifth is queued at a four-charger station. A coder starts charging the fifth immediately, but counts the fifth under “idle.” What is wrong? **Solution:** both charger capacity \(C\le4\) and vehicle state partitioning are violated. The correct transition leaves that fifth vehicle in the charge queue until a charger-completion event frees one resource; relabeling it does not create capacity.

**Reproduce:** run the checker `scripts/check_step03_book11.py` for deterministic and adversarial event cases, then inspect [the controlled model assumptions](../case/model-assumptions.json). [Chapter 6](06-model-detailed-operations-and-complete-computational-verification.md).
