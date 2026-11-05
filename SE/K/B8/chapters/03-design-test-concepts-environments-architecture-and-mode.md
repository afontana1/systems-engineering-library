# Chapter 3 — Test architecture and fidelity

*Book 8: System Test and Evaluation · Week 3 — Design test concepts, environments, architecture, and model-based evidence*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 3](../labs/lab-03-design-test-concepts-environments-architecture-and-mode.md) without looking at the solution → return to [Week 3 of the course guide](../../../C/P2/EN645769.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-769-w03.md) is optional review, not the primary reading.

## The engineering problem

The Northstar design team has handed over an evidence claim and a product configuration. The evaluator is independent of the preferred design decision and must distinguish what is demonstrated from what remains assumed. The governing question this week is **test architecture and fidelity**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

A test environment reproduces only selected properties of operational reality; characterize timing, physical dynamics, workload, cybersecurity posture, human use and environmental stress separately. A simulation may support development decisions but needs an argument before it supports operational qualification.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Test architecture determines what is observable, controllable and realistically stressed in the experiment.

### Distinguishing related ideas

Fidelity is not visual similarity: it is similarity of the causal features that affect the claim under test.

### Interpretation and boundary conditions

A simulated communication link may be adequate for functional logic yet inadequate for a deadline whose tail latency depends on congestion.

## Deeper theory: test environments are representations with limited validity

### Fidelity is multidimensional, not a single percentage

A test environment can resemble the operational system in one way and differ radically in another. Relevant dimensions include physics, timing, network behavior, human interaction, environmental exposure, sensor error, software configuration, and operational workload. A high-resolution vehicle visualization might have excellent geometric fidelity yet omit packet delay and operator stress; a modest bench rig might reproduce the safety-critical control handshake precisely. The right fidelity is the fidelity needed to support a specific decision claim, not the most expensive simulation available.

The first question is what causal mechanism the test must exercise. If the claim concerns preventing unsafe boarding after a stale vehicle-state message, the environment needs credible timing, message-age semantics, controller behavior, and observation of the final authorization state. A perfect rendering of the shuttle body adds little. If the claim concerns ramp clearance under load, geometry, compliance, and mechanical dynamics become central. Test architecture follows the evidence claim and the potential failure pathways.

### Representativeness and controllability are competing test virtues

A laboratory permits repeatable fault injection and controlled factor changes, but its operating conditions may be unlike those in the field. Operational trials improve realism yet may provide poor coverage of rare hazards and make causal interpretation difficult. Software-in-the-loop tests expose algorithm and protocol behavior under simulated inputs; hardware-in-the-loop tests add physical interfaces, timing, and device faults, but still depend on the fidelity of the simulated surroundings. No rung in a nominal test ladder automatically validates every claim from the previous one.

A staged strategy can use models to explore broad scenarios, controlled rigs to isolate mechanisms, integrated tests to expose interaction, and operational trials to examine validity in intended use. The links between stages matter. A calibration finding that the field network's latency distribution is heavy-tailed should update the simulation input model. A failure in a bench test should prompt analysis of the corresponding operational hazard, not be filed away as a local laboratory exception.

### Measurement design is part of test design

Suppose two subsystems timestamp an event on unsynchronized clocks. Their recorded difference may not be a valid latency measurement. Timing tests need defined trigger points, clock synchronization or monotonic reference, sampling rates, instrumentation uncertainty, and records of dropped samples. If the desired upper-bound response is close to the instrument's uncertainty, passing the observed value may not support compliance. Similarly, a simulator that supplies perfect state information may fail to reveal behavior under noisy, biased, or unavailable sensors.

Coverage also needs a denominator: requirements, hazards, operating modes, interfaces, or equivalence classes of conditions. “All tests passed” is not informative when tests cover only nominal demand and fair-weather operation. The Northstar test architecture should map each claim to the environment's relevant fidelity dimensions, observable quantities, calibration evidence, limitations, and planned transfer to the next evidence source. A test is credible when its conditions support the decision being claimed, not merely because it runs successfully or looks realistic.

## Worked engineering case

A software-in-the-loop model reproduces route logic but assumes zero radio delay. It can detect algorithm errors while giving biased wait and recovery predictions during communication disruption.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

High visual realism can coexist with low behavioral or statistical fidelity. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Trace requirements and stakeholder expectations to objectives, methods, and critical test parameters](02-trace-requirements-and-stakeholder-expectations-to-obje.md); the next connection is [Apply measurement science, statistics, DOE, and sample rationale](04-apply-measurement-science-statistics-doe-and-sample-rat.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Draw a matrix of phenomena versus SIL, HIL, bench and field tests; mark gaps requiring transfer evidence.

**Problem B — Adversarial review.** What phenomenon does your cheapest environment systematically omit?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 3: Test architecture and fidelity](../labs/lab-03-design-test-concepts-environments-architecture-and-mode.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 3 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
