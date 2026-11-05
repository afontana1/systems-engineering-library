# Chapter 5 — Integration and SIL/HIL paths

*Book 8: System Test and Evaluation · Week 5 — Construct the integration test approach, SIL/HIL paths, and informal tests*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 5](../labs/lab-05-construct-the-integration-test-approach-sil-hil-paths-a.md) without looking at the solution → return to [Week 5 of the course guide](../../../C/P2/EN645769.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-769-w05.md) is optional review, not the primary reading.

## The engineering problem

The Northstar design team has handed over an evidence claim and a product configuration. The evaluator is independent of the preferred design decision and must distinguish what is demonstrated from what remains assumed. The governing question this week is **integration and sil/hil paths**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Component and interface tests answer different questions. Integration aims at state consistency, message semantics, recovery and timing under realistic compositions. Surrogates and automation expand coverage but only if their limitations are documented and abnormal conditions are deliberately introduced.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

### Test fidelity is purposeful similarity, not cosmetic realism

A simulation-in-the-loop or hardware-in-the-loop environment can reproduce some causal mechanisms while omitting others. A faithful visual scene may omit sensor latency; an unattractive bench model may reproduce the relevant timing and fault transitions accurately. Fidelity is therefore multidimensional and **relative to intended use**. A test environment suitable for evaluating a booking algorithm may not be suitable for proving emergency-stop performance under electrical interference.

Integration testing examines the assumptions at component boundaries: message schema, timing, ownership, resource contention, reset behavior, and failure propagation. A passing result in one environment supports only the mechanisms represented there. Transferring the result to a different environment requires an argument about what remained invariant and what changed. A traceable test strategy deliberately chooses which uncertainty each fidelity level can address and where physical or operational evidence is still necessary.

## Deeper theory: simulation-based integration and the limits of fidelity

System integration is not merely the act of connecting subsystems and observing that messages pass. It is the progressive discovery of whether independently developed elements preserve their intended contracts **when interacting through real interfaces and shared resources**. Simulation-based integration changes the setting in which those contracts are exercised, but it does not remove the need to reason about the conditions under which the evidence transfers to the assembled system.

Software-in-the-loop (SIL) testing typically exercises software logic in a simulated or representative execution environment. Hardware-in-the-loop (HIL) testing incorporates physical controllers or other hardware interacting with a simulated plant or environment. These categories are useful, but neither is a uniform certificate of realism. A SIL environment may accurately reproduce messaging and failure recovery yet poorly approximate vehicle dynamics. A HIL rig may accurately exercise controller timing while simplifying network congestion and human intervention. **Fidelity must be expressed in relation to the property being assessed.**

### Integration reveals emergent timing

Suppose sensing requires 40 ms, networking 25 ms, decision computation 60 ms and actuation 70 ms under a particular nominal case. The sum is 195 ms, but an operational requirement of 250 ms does not automatically have 55 ms of guaranteed margin. The quoted values may be averages, percentiles or conditional measurements; the stages may also run concurrently, block each other, or compete for CPU and network resources. A meaningful end-to-end timing claim requires a model of scheduling, dependencies and joint variability, plus evidence that the model holds under the relevant workload.

If the stages have genuine upper bounds \(T_1,\ldots,T_k\) and occur in series, then \(T_{\mathrm{end}}\leq \sum_i T_i\). When stages overlap, the bound may instead involve maxima or a task-graph critical path. If each stage has only a percentile bound, the percentile of the sum cannot generally be found by adding those percentiles. Dependence among stages matters: a common overload can slow sensing, messaging and control simultaneously.

### Fault injection tests assumptions, not only components

An integration environment is especially valuable when it can induce controlled abnormal conditions: message duplication, stale timestamps, power interruption, sensor disagreement, delayed acknowledgments and partial connectivity. These faults make hidden assumptions observable. A vehicle controller might correctly reject an invalid route command when tested alone but accept a command that becomes invalid during a multistep handshake. The failure exists in **the composition of states and timing**, not in a single locally incorrect function.

Fault injection should also have an explicit causal hypothesis. Inducing packet loss without recording what correctness property the system should preserve can yield many logs but little understanding. A sharper hypothesis is that *repeated booking commands must not allocate duplicate capacity when acknowledgments are lost*. The experiment then checks the state before and after retries and evaluates how the result depends on database failure and recovery.

### The model itself requires validation

A simulated vehicle may match speed and route behavior during nominal operation while failing to model the physical constraints that matter for emergency braking. HIL evidence can be strong for controller integration but limited for tire-road friction, sensor occlusion or passenger movement. Independent analytical bounds, component tests, measured field data and sensitivity studies can help establish where the simulated environment is credible. Agreement on one calibration trace should not be confused with validation over a broad operating domain.

This creates a **test pyramid with different inference targets**. Unit tests expose local errors; SIL tests examine software compositions; HIL tests reveal timing and device interactions; field tests observe the physical and operational system. Higher fidelity is not automatically better for every question. Some unusual failure modes are safer and easier to explore in simulation, while some human and environmental phenomena cannot be responsibly inferred from synthetic data alone.

### An integration result is an evidence object

The outcome must be linked to exact hardware, firmware, software, model, data and procedure revisions. A pass/fail label detached from these dependencies loses much of its meaning. If a timing test fails, the finding should record which interface assumption was violated and whether the design, test environment, instrumentation or expectation was at fault. Closing the issue requires evidence on the corrected configuration rather than an assertion that the component owner made a fix.

The intellectual purpose of SIL and HIL is to examine the **gap between models of independent parts and behavior of the interacting whole**. Well-designed integration testing makes that gap visible early and states carefully which real-world conclusions can and cannot be drawn from the simulated environment.

## Worked engineering case

The reservation service suppresses duplicate IDs, but a timeout and retry can reorder cancellation and dispatch acknowledgements. A unit test of each service misses the cross-service race.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

Passing every individual unit test says little about emergent interaction faults. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Apply measurement science, statistics, DOE, and sample rationale](04-apply-measurement-science-statistics-doe-and-sample-rat.md); the next connection is [Write formal qualification procedures and conduct the Test Readiness Review](06-write-formal-qualification-procedures-and-conduct-the-t.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Create a six-case interface matrix including reorder, duplicate, timeout, malformed input, stale state and recovery.

**Problem B — Adversarial review.** Which fault can be injected safely in SIL but not initially on vehicles?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 5: Integration and SIL/HIL paths](../labs/lab-05-construct-the-integration-test-approach-sil-hil-paths-a.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 5 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
