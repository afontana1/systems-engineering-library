# Chapter 06 — Design interoperable HLA/FMI federations, LVC interfaces, and composable co-simulations

*Book 12 · EN.645.758 · Advanced Systems Modeling and Simulation · Week 6 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 6](../labs/lab-06-design-interoperable-hla-fmi-federations-lvc-interfaces-and-composab.md) → attempt the [original Week 6 assessment](../../../C/P3/EN645758.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-758-w06.md) remains available for a quick recap.

## The decision behind the theory

File compatibility is not simulation interoperability. Distributed and co-simulated components must agree about semantics, time, ownership, initialization, events, error handling, and validity at their interfaces.

**Essential question:** Can independently developed simulations compose into a credible integrated experiment?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the advanced systems modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

* HLA provides a federation architecture and services for object exchange, ownership, synchronization, time, and management. It does not make federates semantically compatible or valid.
* FMI packages a dynamic model as an FMU. Model Exchange relies on the importing environment’s solver; Co-Simulation includes a solver; Scheduled Execution exposes partitions for coordinated execution.
* Define a shared information model: variable meaning, units, coordinate frame, reference, rate, timestamp, valid range, quality, ownership, and event semantics.
* Time policy must address logical time, wall time, lookahead, step negotiation, rollback or lack thereof, real-time pacing, latency, and deterministic replay.
* Composability assessment asks whether assumptions, resolutions, domains, interfaces, and behaviors remain compatible when models interact. Run coupling-step and event-order sensitivity tests.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Link MBSE, XML metadata, collaborative environments, and reusable M&S assets**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Integrate the model baseline and design advanced simulation experiments**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

## The mechanism beneath the method

Co-simulation interoperability depends on agreement about time advance, state ownership, event semantics and numerical error.

### Distinguishing related ideas

Two tools exchanging valid files may still disagree about when a discontinuity occurs or whether a state is interpolated or extrapolated.

### Interpretation and boundary conditions

Loose coupling can become unstable when strongly interacting subsystems need tighter synchronization than the exchange interval provides.

## Deeper theory: co-simulation is a negotiation about time and meaning

A federated simulation joins models that may be developed by different teams, at different levels of fidelity, using different internal solvers. The difficulty is not merely file exchange. A federation must agree on **what information means**, **when a value applies**, **who owns the advancing time**, and **which dependencies can be evaluated without contradiction**. This is why a collection of individually correct models can become incorrect when coupled.

### Data contracts are necessary but not sufficient

Imagine a vehicle dynamics model providing acceleration to a dispatch simulator. The dispatch simulator updates planned arrival time from acceleration and returns an adjusted route; the vehicle model changes acceleration in response. The relation has a feedback loop. If both models evaluate their outputs using the other model's *current* outputs, they may form an algebraic loop requiring a simultaneous solution. If they instead exchange values once per communication step, the coupling introduces a delay that may alter the dynamics. Neither interpretation is automatically correct: the engineer must specify the intended causal and numerical semantics.

A federation contract includes field types and units, reference frames, timestamps, coordinate systems, update frequency, interpolation/extrapolation rules, and treatment of missing or late messages. For example, position expressed in latitude/longitude cannot be substituted blindly for a local Cartesian position, and a speed sample stamped at 10:00:00.000 is not necessarily valid for a state estimate at 10:00:00.500. Defining such contracts is an engineering task, not just an integration configuration.

### Communication-step error and coupled stability

In a simple explicit co-simulation, model A advances over a macro-step \(H\) using the last available input from model B, then the models exchange new values. This is a **sample-and-hold** assumption. Its error depends on how rapidly the coupled quantities change and how strong the feedback between models is. Reducing \(H\) often improves agreement but increases communication cost and does not necessarily solve all inconsistencies. Discontinuous events and algebraic coupling may require iteration within a macro-step, rollback support, or a coordinated solver.

The stability of each model in isolation does not guarantee stability of their co-simulation. A controller stable when receiving continuous feedback can oscillate after a communication delay is introduced. The source of the instability may be the coupling algorithm, not the underlying physical plant. This is why fidelity claims must identify not only component models and solver tolerances but also the federation step size and exchange policy.

### Different interoperability technologies solve different layers

The **Functional Mock-up Interface (FMI)** standard describes interoperable interfaces for exchanging or running dynamic models packaged as Functional Mock-up Units (FMUs). Depending on FMI version and supported interface mode, a unit may expose model-exchange equations, co-simulation stepping, or scheduled-execution features. FMI does not by itself establish that the coupled models represent compatible physical meanings. The **High Level Architecture (HLA)** family concerns federation services such as data exchange, object models, and time management among simulation participants. HLA can coordinate federates, but it cannot make contradictory constituent assumptions true. A live/virtual/constructive (LVC) exercise adds further issues: real participants, human operators, simulated agents, and network delays may operate on incompatible clocks or under different safety constraints.

An interface standard should therefore be understood as an **enabler of composition**, not proof of validity. Technical interoperability concerns whether messages can be exchanged. Semantic interoperability concerns whether both sides interpret them consistently. Behavioral interoperability concerns whether interactions occur with permissible ordering and timing. Evidence interoperability concerns whether the combined results can be traced to the constituent versions and test conditions that produced them.

### Credibility across a federation is conditional

Suppose a verified vehicle dynamics model is coupled to a route planner whose assumptions exclude flooding. A flooding scenario may be rendered vividly, yet a claim about emergency service is still limited by the planner's omitted road closures. The federation's credibility is not the sum of the credibility ratings of its components. It depends on coverage of interaction mechanisms and on whether the **coupled model** has been examined against relevant system-level observations.

A sound argument documents the constituent model versions, parameter baselines, interface semantics, clock strategy, coupling-step sensitivity, event handling, and known inconsistencies. It distinguishes numerical correctness from domain validity and explicitly bounds the intended use. The purpose of co-simulation is to discover cross-domain behavior, but that discovery is trustworthy only when the federation does not create dynamics through accidental timing or semantic choices.

## Worked engineering example from the course

The vehicle plant FMU publishes speed and battery temperature every 10 ms, while a fleet/environment federate updates grade and traffic every 1 s. A naive co-simulation holds grade constant and allows the controller to step past a sharp route transition, underestimating peak traction power by 9%. The corrected architecture exchanges route-segment events, aligns macro steps at discontinuities, records timestamps and quality, and tests 100 ms, 20 ms, and 10 ms coupling intervals.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Two federates may agree on data field names but violate causality if one uses a 1 s step and the other needs 20 ms feedback. Define causality, synchronization policy, rollback limits, and validity envelope. FMI/HLA connectivity does not guarantee numerical stability.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** At constant 12 m/s, deceleration of 2 m/s² gives what ideal stopping distance?

<details><summary>Show a reasoned solution</summary>

d=v²/(2a)=144/4=36 m, excluding delays, grade and friction uncertainty.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Interoperability is claimed from successful file import alone.
* Time or event semantics are undefined.
* Components exchange variables with ambiguous units or ownership.
* A federation is accepted without composability or intended-use evidence.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. What does HLA provide?
2. What are FMI’s principal modes?
3. What is composability?
4. Why test coupling step?

<details><summary>Explain the answers</summary>

**1. What does HLA provide?** A framework, rules, services, interfaces, and object-model structure for federations.

**2. What are FMI’s principal modes?** Model Exchange, Co-Simulation, and Scheduled Execution.

**3. What is composability?** The ability of model components to combine while preserving valid assumptions and behavior for the intended use.

**4. Why test coupling step?** Because macro-step and interpolation choices can change events, peaks, stability, and conclusions.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 6](../labs/lab-06-design-interoperable-hla-fmi-federations-lvc-interfaces-and-composab.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[05 — Previous chapter](05-link-mbse-xml-metadata-collaborative-environments-and-reusable-m-s-a.md) · [07 — Next chapter](07-integrate-the-model-baseline-and-design-advanced-simulation-experime.md) · [Book index](../README.md)

## Step 03 integrated NS-CPS12.1 case: co-simulation contracts and synchronization

### Why correct components can compose into a wrong system

A vehicle dynamics component, motor model, pack model and fleet dispatcher may be tested individually and still fail together if their boundary variables, signs, clocks or event ownership disagree. High Level Architecture (HLA) concerns federate participation, data publication/subscription and time management at a distributed simulation level; the Functional Mock-up Interface (FMI) governs portable model interfaces and execution modes for FMUs. They are not interchangeable and an illustrative JSON contract is **not** a conforming HLA FOM or FMI XML model description. A simulation architecture must say which model is authoritative for every state and who resolves conflicting commands.

The NS-CPS12.1 [diagram](../case/multidomain-evidence.svg) separates the speed regulator, plant and electrical-thermal model. The actual Python script executes them sequentially in one process. It **does not** implement an HLA federation, export an FMU or simulate network latency. The following design is a contract exercise, not a claim that interoperability tests ran.

### A minimal power-port and time contract

| Signal | Publisher → subscriber | Unit/sign | Update/effect |
|---|---|---|---|
| `wheel_speed` | plant → controller | m/s, nonnegative | sampled at controller instant |
| `wheel_force_command` | controller → plant | N, signed (negative braking) | held until next controller sample |
| `wheel_power` | plant → battery | W, positive traction demand | calculated from physical speed |
| `pack_soc` | battery → supervisor | fraction 0–1 | output after plant state update |
| `pack_temp` | thermal → supervisor | °C, state estimate | updated on thermal clock |
| `coolant_flow` | supervisor → thermal | kg/s | constrained by pump hardware |

The signed power direction is easy to get wrong. If a negative regenerative \(P_w\) is interpreted as positive consumption by a second component, energy will be deleted twice. Likewise, if two federates independently integrate the same energy state, no global conservation law survives. One owner should update each state; other models exchange inputs and readouts.

### Explicit co-simulation error analysis

Consider two coupled scalar models

\[
\dot x=-ax+by,\qquad \dot y=cx-dy.
\]

If the orchestrator uses explicit one-step exchange and no iteration, the discrete update is \(z_{n+1}=(I+hA)z_n\) with \(A=\begin{bmatrix}-a&b\\c&-d\end{bmatrix}\). Numerical stability demands \(\rho(I+hA)<1\), where \(\rho\) is spectral radius, even when the continuous physical system is stable. Set \(a=d=2\,s^{-1}\) and \(b=c=1\,s^{-1}\). The continuous eigenvalues are −1 and −3 s⁻¹. An exchange step \(h=0.8\) s yields amplification eigenvalues 0.2 and −1.4: one mode grows numerically. With \(h=0.2\) s, they become 0.8 and 0.4: stable. The instability is caused by coupling step size, not changed physics.

A true partitioned execution with delayed partner output, different step rates, interpolation and zero-crossing events can introduce **additional** error. A valid federation test should compare a monolithic reference with successively refined exchange intervals, characterize missed events and specify what happens if the partner is late. Algebraic feedback loops may require iteration, rollback support or a solver that treats the coupled equations together.

### Compose physical and operational models without category errors

Book 11's model allocates one request per vehicle and tests queue outcomes. Book 12 resolves one shuttle's power and thermal trajectory on a repeated route. A future joint model could pass a *validated* conditional distribution of trip times and charger needs from Book 12 into Book 11, while Book 11 supplies weather, occupancy and scheduling events. But the present Book 12 trip times have **no boarding, traffic interference or charge pauses**; they cannot replace Book 11's trip-time input without separately modeling those missing terms. The coupling itself would require scenario alignment and common exogenous conditions to prevent false precision.

### Practical handshake and fault handling

Before an exchange, agree on common epoch, frame, time units, declared sample intervals, acceptable latency, external-event timestamping, and state reset. On packet loss or missing FMU output: fail closed or hold last value only for a bounded, justified duration. On mismatched versions or unsupported units: reject connection. On HIL, timestamp skew and deadline misses become failure modes, not merely performance bugs.

### Exercises with solutions

**A.** For the scalar example above, is \(h=0.8\) s safe? **Solution.** No: \(|1+h(-3)|=|-1.4|>1\). At \(h=0.2\), both amplification magnitudes are below one. Stability alone does not guarantee acceptable accuracy.

**B.** Plant sends a 25 kW load, battery expects W. What numerical value must it consume? **Solution.** 25,000 W. If it takes 25, the load shrinks by 1000; an interface test must inject an explicit unit-conversion vector.

**C.** If two models each integrate 10 kWh consumption, what is the failure? **Solution.** Double ownership can subtract 20 kWh for a 10 kWh transfer. Define one energy-state integrator and monitor aggregate conservation.

**Deliverable:** a versioned interface table, causal diagram, temporal handshake protocol and conformance-test *plan* for an external HLA/FMI tool. Do not claim standard conformance without running an appropriate implementation and tool-specific tests.
