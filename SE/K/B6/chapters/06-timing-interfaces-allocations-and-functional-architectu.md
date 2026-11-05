# Chapter 6 — Timing and interface feasibility

*Book 6: System Conceptual Design · Week 6 — Timing, interfaces, allocations, and Functional Architecture Review*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 6](../labs/lab-06-timing-interfaces-allocations-and-functional-architectu.md) without looking at the solution → return to [Week 6 of the course guide](../../../C/P2/EN645767.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-767-w06.md) is optional review, not the primary reading.

## The engineering problem

At this point the Northstar team is still free to select among competing mobility-service concepts. A proposed autonomous shuttle is one hypothesis, not the definition of the problem. The governing question this week is **timing and interface feasibility**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Interface definitions allocate ownership, data meaning, timing, and degraded behavior. Summing deterministic step times gives only a budget illustration; realistic delay budgets require variability, concurrency, and percentile criteria. An architecture review should separate proven allocations from optimistic placeholders.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Timing and interface feasibility create a coupled constraint problem: communication delays, actuation, boarding, routing and recharge windows must coexist.

### Distinguishing related ideas

A design satisfying each average component budget may still violate its end-to-end deadline because latency tails and dependencies accumulate.

### Interpretation and boundary conditions

Treat slack as an explicit resource that can be consumed by variation, rather than as an unexplained difference between planned and nominal values.

## Worked engineering case

Request capture 0.2 s + eligibility 0.4 s + option generation 0.7 s + commitment 0.5 s + notification 0.2 s = 2.0 s. Under a 2.0 s deadline the nominal margin is zero; a 0.3 s network delay breaks it.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

Latency estimates at a single percentile cannot simply be added to prove an end-to-end percentile. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Functional architecture and mission-to-function traceability](05-functional-architecture-and-mission-to-function-traceab.md); the next connection is [Generate physical concept families with morphological and set-based methods](07-generate-physical-concept-families-with-morphological-a.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Build a latency budget with owners and an exception reserve, and identify one test that could disprove the budget.

**Problem B — Adversarial review.** Which timing assumption is most likely to invalidate the proposed service?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>


## Graduate depth: timing and interfaces as network feasibility constraints
### A functional architecture becomes physical when time matters

A function can be logically complete yet impossible to realize within a deadline. Timing converts abstract behavior into a resource-constrained engineering problem: computation takes time, communication competes for bandwidth, sensing adds delay and uncertainty, and human actions have variable response distributions. The end-to-end response time of a strictly sequential path is the sum of component execution, waiting, transport, and handoff times. Parallel paths that must all complete contribute a maximum over branch completion times. Omitted waiting and synchronization are common reasons a “sum of nominal latencies” looks acceptable while the real service misses its deadline.

For a real-time function, distinguish deadline, period, release jitter, worst-case execution time, and response time. A task with execution demand `C_i` and period `T_i` contributes nominal utilization `U_i = C_i/T_i`, but a low total utilization does not guarantee schedulability under arbitrary priorities, blocking, nonpreemptive sections, or shared resources. Response-time analysis may require equations such as `R_i = C_i + B_i + sum_{j in higher-priority} ceil(R_i/T_j) C_j`, with assumptions about fixed-priority preemptive scheduling and interference. The point is not to apply that equation indiscriminately, but to show how execution policy alters timing feasibility.

### Interface contracts must include uncertainty and failure behavior

An interface specification should capture more than a message schema. It includes units, range, freshness, semantic meaning, ordering, allowable duplicates, authentication, source authority, failure and retry behavior, and timing limits. A GPS update with a syntactically valid position may be operationally unsafe if it is stale. A dispatch message that arrives twice may be harmless if idempotent and catastrophic if it causes double allocation. Thus timing, information quality, and consistency are intertwined; an interface can meet a bandwidth budget and still violate the mission contract.

Consider Northstar's authorization path: a request enters the broker, an eligibility service checks state, a reservation is committed, and the rider receives confirmation. A budget that assigns 60 milliseconds to each component overlooks burst queueing and cross-service retry storms. A more defensible budget includes nominal and stressed loads, correlation among delays, tail metrics, and explicit degraded-mode rules. If an external network is down, the design might refuse new assignments rather than silently relaxing eligibility requirements.

### Allocation is a feasibility proof with margins

When functions are allocated to hardware, software, or operators, each decision consumes budgets: compute cycles, storage, energy, thermal headroom, interface capacity, and human attention. These budgets are coupled. Faster processing can increase energy and cooling demands; additional encryption may increase latency; redundant paths may increase fault tolerance while introducing more coordination. An allocation matrix is therefore a set of conditional feasibility claims, not just a responsibility chart.

Margins must state both sign and uncertainty. If a deadline is 500 milliseconds and the measured 99th percentile is 450 milliseconds in a limited lab test, the apparent 50-millisecond margin is not a demonstrated field guarantee. Confidence intervals, untested operating envelopes, and long-tail delays matter. The conceptual design should identify which interface and timing assumptions will be retired by analysis, prototype, or integration testing. This creates a direct bridge from functional architecture to physical design and system verification.

## Practice before the assessed course work

[Hypothetical Laboratory 6: Timing and interface feasibility](../labs/lab-06-timing-interfaces-allocations-and-functional-architectu.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 6 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.


## Advanced worked practice

- [Deep workshop — Concept Feasibility Before Scoring Alternatives](../practice/feasibility.md)
- [Corresponding independent laboratory](../practice/lab-feasibility.md)
- [Interactive workbench](../practice/WORKBENCH.html)
