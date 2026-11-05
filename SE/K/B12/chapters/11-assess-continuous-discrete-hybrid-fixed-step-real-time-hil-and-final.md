# Chapter 11 — Assess continuous, discrete, hybrid, fixed-step, real-time, HIL, and final credibility constraints

*Book 12 · EN.645.758 · Advanced Systems Modeling and Simulation · Week 11 of 12*

**Study sequence:** Read this chapter → complete [Hypothetical Lab 11](../labs/lab-11-assess-continuous-discrete-hybrid-fixed-step-real-time-hil-and-final.md) → attempt the [original Week 11 assessment](../../../C/P3/EN645758.md) using its complete rubric. The [earlier concise companion lesson](../../P3-text/lessons/645-758-w11.md) remains available for a quick recap.

## The decision behind the theory

A model that runs faster than real time on a workstation is not automatically suitable for real-time or HIL use. Determinism, fixed-step accuracy, overruns, I/O, sample rates, latency, jitter, scheduling, and failure behavior must be measured.

**Essential question:** What execution and credibility evidence supports offline analysis, software-in-the-loop, real-time, or hardware-in-the-loop use?

The fictional Northstar regional mobility project provides continuity across the six books. It is not a real deployment or validated transportation model. The same physical operations can be described using a system model, a sample of observations, an event simulation, coupled dynamics, feedback stocks, or a preference model; these are **different representations answering different questions**. This chapter examines what the advanced systems modeling and simulation perspective adds, which claims it supports, and which decisions require evidence from another discipline.

## Develop the fundamental ideas

* Classify every subsystem by continuous state, discrete state, event, sample time, and execution priority. Make rate transitions explicit.
* Fixed-step selection trades accuracy against computational deadline. Test step sizes with the same challenge scenarios used for decision results.
* Measure worst-case execution, not only average. Track deadline misses, jitter, I/O latency, logging overhead, initialization time, and recovery behavior.
* SIL executes production or representative software against a simulated plant; PIL executes on target-class processor; HIL includes real hardware and I/O. Each adds evidence and new failure modes.
* Finish credibility assessment by integrating verification, validation, data quality, uncertainty, sensitivity, numerical/timing evidence, peer review, limitations, and acceptance criteria.

### What to keep separate

A parameter is a model input or characteristic; an *observation* is data recorded with a defined process; a *claim* is an assertion to be tested; an *inference* extrapolates under assumptions; and a *decision* includes consequences and responsibility. These cannot be interchanged. For this topic, start from the named engineering question, write a minimally sufficient representation, state units and operating range, then identify a counterexample that could change the result. A model may be fully verified as software while still failing to represent its intended real-world use.

The prior connection is **Extend the model to population or biological dynamics and communicate behavior through visualization**. That prior work constrains the current boundary and data definitions; changing it silently breaks comparisons. The subsequent connection is **Reproduce, challenge, present, and defend the final complex-system simulation study**. Carry forward source identifiers, units, uncertainty and model versions rather than exporting a single attractive result.

### Hybrid simulation requires a contract between time and events

A hybrid system combines continuous dynamics with discrete changes in mode. A battery temperature evolves continuously, but a protective shutdown may occur when a threshold is crossed; a vehicle accelerates continuously, but a dispatch instruction changes its target. Numerically implementing these interactions requires agreement about event detection, solver step, reset rules, and which component owns state at the transition.

Co-simulation adds another challenge because different simulators may advance time with different methods and exchange delayed values. An apparently minor communication interval can change the stability or timing of a coupled loop. Fixed-step hardware-in-the-loop operation may satisfy real-time deadlines by reducing numerical detail, while an offline variable-step simulation may yield more accurate trajectories but fail real-time constraints. Neither is intrinsically better. The appropriate method follows the **phenomenon and decision**, and its timing contract must be part of the credibility argument.

## Deeper theory: real-time simulation is an execution contract

### Numerical time and wall-clock time are different resources

Offline simulation aims to approximate a mathematical trajectory to a desired error tolerance; real-time simulation must also deliver its outputs before the physical equipment requires them. A solver advancing simulated time by `h = 1 ms` must complete computation, input acquisition, and output delivery within the corresponding wall-clock deadline. A run averaging 0.2 ms per step is not real-time safe if occasional 3 ms overruns cause a connected controller to miss critical updates. Assess worst-case or high-percentile execution demand under representative loads, memory behavior, scheduling interference, and I/O, rather than relying on a desktop stopwatch.

Fixed-step integration creates an explicit tradeoff. For forward Euler, `x_(k+1) = x_k + h f(x_k,u_k)`, local truncation error is typically order `h²` and global error order `h` for sufficiently smooth, well-posed problems. Numerical stability can impose tighter limits than accuracy. Applied to the stable scalar mode `dx/dt = −a x`, Euler produces `x_(k+1) = (1−ah)x_k`; its amplification magnitude is below one only when `0 < ah < 2`. A physically decaying mode can therefore oscillate or diverge numerically when the step is too large. Faster hardware does not eliminate the need to analyze stiffness and discretization error.

### Hybrid behavior requires rules for crossing mode boundaries

A hybrid system combines continuous state evolution with discrete mode transitions. A shuttle may accelerate continuously, switch to a current-limited mode, detect a wheel-slip threshold, and apply a different control law. Mathematically, each mode has its own vector field `f_q(x,u)`, while guard conditions trigger transitions and reset maps may alter state. The event detection policy determines whether a threshold is found at its actual crossing or at the next fixed tick. In a safety controller, even a one-tick delay can matter when combined with actuation and communication delays.

Poorly defined guards can cause *chattering*: repeated switching around a threshold because of sensor noise or solver discretization. Hysteresis, minimum dwell times, and physically justified filters can help, but they change behavior and must be represented in the credibility argument. Events that happen almost simultaneously also require a deterministic ordering when the order affects state. A model cannot claim faithful safety logic while leaving the mode-transition semantics to whichever simulator happens to process an event first.

### Hardware-in-the-loop adds failure paths the software model never had

In hardware-in-the-loop (HIL), a real controller interacts with simulated plant dynamics through physical signals or communication interfaces. I/O quantization, sensor scaling, latency, jitter, packet loss, grounding, electrical isolation, and startup sequencing become elements of the experimental system. A physically stable control loop can be destabilized by added sampling delay. For a nominal loop phase margin, delay `τ` contributes frequency-dependent phase lag `−ωτ` radians, reducing stability margin near crossover. Treating delay as an unrecorded fixture property can make a controller appear safe in one laboratory and unstable in another.

A HIL test can validate real controller behavior against the interface and plant representation used; it cannot validate unmodeled terrain physics, human response, or the real vehicle's power stage. Fault injection requires containment: a test mode should not accidentally issue active commands to external equipment. Separate *plant fidelity* (the modeled physical process), *interface fidelity* (signals and timing), and *scenario fidelity* (the operating challenges). They may be high or low independently, and a use claim should name which matter.

### Evidence should cover accuracy and deadline reliability together

Record both a numerical error envelope against a suitable higher-fidelity or analytic reference and a deadline profile over relevant scenarios. Test normal and overloaded computation, rapid mode switching, maximum sensor traffic, startup, reset, and loss of input. Monitor missed deadlines, hold-last-value policies, numerical divergence, and the physical effect of fallbacks. A controller that correctly enters a safe state after one missed input may still be unsafe after a pattern of stale inputs. The final claim should distinguish successful offline analysis, software-in-the-loop execution, deterministic real-time operation, and HIL suitability; each requires its own evidence rather than inheriting credibility from the previous label.

## Worked engineering example from the course

The controller uses a 10-ms base rate and 100-ms thermal supervisor. At a 1-ms plant step the model is accurate but misses the 10-ms deadline on 3% of runs. A 5-ms fixed step meets timing but overestimates current peak by 4.8%; a multi-rate configuration with a 1-ms electrical partition and 10-ms mechanical/controller partition meets both accuracy and timing on the available target. The readiness claim is limited to SIL/timing-in-the-loop because no physical I/O hardware was tested.

The result above is best understood as a conditional argument: if the observations, configuration, model structure and decision thresholds are as stated, then the reported conclusion follows. **Never treat a worked teaching assumption as a field measurement.** Write a second interpretation in which at least one assumption fails and identify what additional measurement would discriminate the interpretations.

## A second example: work the method rather than memorize it

Forward Euler for x˙=−2x with step 0.75 gives x_{n+1}=(1−1.5)x_n=−0.5x_n, an oscillating discrete approximation to a strictly positive decaying continuous solution. Check numerical stability and physical bounds.

The useful questions are: *Which quantities are inputs? What are their units? Which relationship produces the output? What breaks if we change operating conditions?* Record the formula or structural constraint, not only the final answer. Where the method is qualitative, represent actors, directions of influence and competing causal explanations explicitly. Where it is numerical, check dimensions, plausible ranges, limiting cases and dependence.

### A computation you can reproduce

**Problem.** For x˙=−2x, x(0)=1 and Euler step h=0.2, calculate the first two numerical states.

<details><summary>Show a reasoned solution</summary>

x1=1+0.2(−2)=0.6 and x2=0.6+0.2(−1.2)=0.36. The exact states are e^(−0.4)≈0.6703 and e^(−0.8)≈0.4493.

A correct computed result is not automatically a system acceptance result; explain which additional sampling, validation or model checks are needed for that leap.

</details>

## Failure analysis and professional caution

This week's source guide flags the following unacceptable shortcuts. Treat them as adversarial tests of your own work:

* Real-time or HIL capability is claimed without measured deadline and I/O evidence.
* Only average execution time is reported.
* Fixed-step error is not compared with the accepted offline baseline.
* Credibility acceptance ignores unresolved critical timing, data, or validation findings.

For each failure, ask whether it results from a missing measurement, an unsupported assumption, an incorrect relationship, an unsuitable decision rule, or a governance failure. These classes require different remedies. A more complicated model will not repair a poorly framed mission question; more data will not rescue an incorrect formula; a perfect formula will not replace stakeholder authority.

## Check conceptual understanding

1. Why fixed step for real time?
2. What is jitter?
3. What is an overrun?
4. What distinguishes SIL from HIL?

<details><summary>Explain the answers</summary>

**1. Why fixed step for real time?** Execution must complete predictably on a wall-clock schedule.

**2. What is jitter?** Variation in execution or I/O timing around the intended schedule.

**3. What is an overrun?** A computation that fails to complete before its deadline.

**4. What distinguishes SIL from HIL?** SIL uses simulated hardware/plant interfaces; HIL includes real hardware and I/O interacting with the simulation.

</details>

## Apply the chapter to an engineering artifact

Using a controlled Northstar scenario, prepare a two-page analysis explaining (1) the stakeholder decision; (2) the representation and its boundaries; (3) source data and assumptions; (4) a reconstructable example or diagram; (5) an adverse scenario; and (6) what new evidence would alter the recommendation. Then use the fictional [Lab 11](../labs/lab-11-assess-continuous-discrete-hybrid-fixed-step-real-time-hil-and-final.md) to rehearse the technique and complete the original course's more demanding weekly deliverable.

The **course guide remains authoritative for assessment**. This book teaches and rehearses the underlying reasoning; it does not substitute its own checklist for that rubric.

[10 — Previous chapter](10-extend-the-model-to-population-or-biological-dynamics-and-communicat.md) · [12 — Next chapter](12-reproduce-challenge-present-and-defend-the-final-complex-system-simu.md) · [Book index](../README.md)
