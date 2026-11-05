# Chapter 3 — Allocation and derived requirements

*Book 7: System Design and Integration · Week 3 — Allocate requirements and define component functions*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 3](../labs/lab-03-allocate-requirements-and-define-component-functions.md) without looking at the solution → return to [Week 3 of the course guide](../../../C/P2/EN645768.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-768-w03.md) is optional review, not the primary reading.

## The engineering problem

The Northstar concept has now been conditionally selected. Engineering must turn it into interfaces, allocations and budgets that can be implemented and tested, without treating open assumptions as resolved. The governing question this week is **allocation and derived requirements**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Allocation is not a bookkeeping exercise: it establishes the owner of performance, control, data quality and failure response. Derivation follows from the mathematical or logical need to satisfy a parent. Cross-check budgets to avoid individually plausible subsystem specifications that cannot satisfy the whole.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Requirement allocation turns system-level performance into coupled lower-level obligations and therefore creates interface agreements.

### Distinguishing related ideas

A system deadline cannot always be partitioned by independently assigning arbitrary budgets; queueing, concurrency and shared resources create dependencies.

### Interpretation and boundary conditions

Derived requirements should explain their derivation and assumptions so later component tests can be interpreted against whole-system claims.

## Worked engineering case

A two-second dispatch requirement might allocate 0.4 s to eligibility, 0.8 s to planning, 0.3 s to message delivery and 0.5 s to reserve. If the network alone needs 0.6 s, the design has a contradiction, not a reason to relax acceptance silently.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

Subsystem teams can all report “green” while the end-to-end chain fails. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Close the system specification](02-close-the-system-specification.md); the next connection is [Mature the physical architecture, interfaces, and performance budgets](04-mature-the-physical-architecture-interfaces-and-perform.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Create an allocation matrix including owners, margin, an abnormal-mode path and parent rationale.

**Problem B — Adversarial review.** Who owns the unallocated performance margin?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>


## Deeper theory: requirements allocation as a constrained consistency problem

### Allocation creates obligations across a hierarchy

A system-level requirement expresses behavior at an externally meaningful boundary. Subsystem allocation distributes the functions, limits, and evidence needed to realize it. A trace from system requirement to component does not prove correct allocation; engineers must show that the composed subsystem behavior implies the system obligation under declared assumptions. For sequential timing, an allocated system budget may satisfy `T_total = T_sensor + T_compute + T_network + T_actuator + T_wait`. All terms must use compatible definitions and units. If queuing or retransmission is omitted, the apparent sum is not the actual end-to-end delay.

A timing allocation of 0.2, 0.5, 0.3, and 0.8 seconds leaves 0.2 seconds from a two-second total budget when the four activities are sequential. The reserve may be inadequate if the 0.3-second network estimate is an average rather than a tail bound. For parallel activities, their completion time may be the maximum, not the sum; synchronization, resource sharing, or retries can change the result. Allocation mathematics is meaningful only when the behavior model matches the system's actual execution structure.

### A requirement can cross several ownership boundaries

Not every requirement has one owner or one verifying component. Safe boarding might need an actuator interlock, perception software, human-interface signaling, and operator procedure. The top-level claim is *jointly realized* even if one organization coordinates its evidence. A trace matrix should distinguish the accountable integrator, participating implementers, and independent acceptance authority. Otherwise a requirement linked to four subsystems may be assumed to be “covered” while each supplier believes another is responsible for integration-level failure modes.

Interface contracts close the allocation gap. They should define signal meaning, physical units, valid ranges, timing, fault response, version compatibility, and what counts as successful transfer of responsibility. For example, “brake active” might mean a command was sent, current was detected, or deceleration was measured. Those statements support different safety conclusions. A contract that leaves the semantics ambiguous creates an integration hazard even when the interface connector and data packet are fully specified.

### Trade studies must respect system coupling

Subsystem optimization can worsen system performance. Choosing the lowest-power communication module may increase transmission delay, causing longer vehicle idling and higher system energy consumption. A lighter mechanical design may require tighter software limits and more expensive maintenance. Allocations should therefore be tested against coupled system models and the mission measures they support. Sensitivity analysis identifies parameters that dominate the result; not every allocated detail deserves equal analytic effort.

An allocation review asks what happens when each child fails, exceeds its budget, or returns stale information. The team should be able to trace the consequence through interfaces to mission behavior, identify detection and containment mechanisms, and update both verification and operational constraints. Formal decomposition never eliminates uncertainty; it makes the assumptions that bind subsystem claims to system claims visible, challengeable, and governable.

## Practice before the assessed course work

[Hypothetical Laboratory 3: Allocation and derived requirements](../labs/lab-03-allocate-requirements-and-define-component-functions.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 3 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
