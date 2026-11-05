# Chapter 3 — ConOps and mission measures

*Book 6: System Conceptual Design · Week 3 — Desired end state, ConOps, scenarios, and mission calculator v0.1*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 3](../labs/lab-03-desired-end-state-conops-scenarios-and-mission-calculat.md) without looking at the solution → return to [Week 3 of the course guide](../../../C/P2/EN645767.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-767-w03.md) is optional review, not the primary reading.

## The engineering problem

At this point the Northstar team is still free to select among competing mobility-service concepts. A proposed autonomous shuttle is one hypothesis, not the definition of the problem. The governing question this week is **conops and mission measures**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

A Concept of Operations describes actors, triggers, system states, normal and abnormal sequences, and the mission outcomes to be delivered. It is not a marketing narrative. Scenarios reveal hidden boundary conditions and supply the operating envelope used by early mission models.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

A Concept of Operations is a causal narrative connecting missions, actors, environments and modes of behavior.

### Distinguishing related ideas

A storyboard is not a validated performance model: it exposes who must coordinate and which assumptions need testing.

### Interpretation and boundary conditions

Use adverse scenarios to reveal the difference between a nominally available shuttle and a truly accessible trip under delay or dispatch failure.

## Deeper theory: a ConOps is a hypothesis about value in use

### Operational narratives are causal models

A concept of operations describes how capabilities, people, procedures, and environments combine to deliver an outcome. It is not a marketing story about what the new equipment will do. A strong ConOps makes a causal claim: under identified conditions, these interacting activities should produce this stakeholder benefit. For a campus shuttle, the claim might be that coordinated booking, accessible boarding, demand-responsive routing, and manual exception recovery reduce missed trips. Each link can fail for a different reason. The narrative is valuable because it exposes those links before the design becomes difficult to change.

Separate **inputs** (vehicles, staff, information), **activities** (accept, dispatch, board, transport), **outputs** (completed rides), and **outcomes** (reliable access to desired destinations). Increasing outputs does not always increase outcomes. If the service concentrates on easy short rides, trip totals may rise while wheelchair-accessible service deteriorates. A mission measure should therefore match the beneficiary's purpose, not just the contractor's throughput.

### Measure definition determines what “good” means

Consider on-time trip completion. A metric such as `on_time_completed / requested_trips` differs from `on_time_completed / accepted_trips`; the second can improve simply because an overloaded booking service rejects more requests. A third denominator, attempted bookings by eligible users, can reveal digital-access and admission barriers. The correct measure depends on the decision, but the choice must be explicit. Time windows, exceptional weather, canceled requests, and accessibility requirements need equally explicit treatment.

An aggregate average can conceal performance differences across demand periods or user groups. A design that improves the median waiting time while worsening the longest waits may violate the operational purpose. Quantiles, conditional service probabilities, and distributional comparisons are often more informative than a single mean. When certain outcomes are non-negotiable—safe boarding, for instance—they should be represented as constraints rather than small terms in a weighted score.

### Scenarios delimit the claim's operating domain

A ConOps should include nominal, peak-demand, degraded, emergency, transition, and recovery scenarios. These are not merely interesting stories; they expose changes in causal mechanisms and control authority. During normal operation a central dispatcher may assign vehicles. During communication loss, local controllers might complete already approved trips but refuse new ones. During evacuation, the relevant success criterion may shift from average wait time to safe evacuation of vulnerable passengers. A design evaluated only under nominal demand cannot support broad claims about resilience.

Transitions are especially important. “System operates manually” is not a complete degraded-mode concept unless it explains who detects the fault, how responsibility transfers, what information remains available, and when normal operation resumes. Many hazards emerge at the handoff between otherwise well-understood modes. This is where human factors, interface design, and system safety meet operational analysis.

### Concepts are hypotheses to be compared, not stories to be endorsed

Two candidate ConOps may deliver similar normal throughput but rely on different staffing, connectivity, or accessibility assumptions. A defensible comparison lists the causal assumptions that distinguish them and identifies observations that could refute each one. An operator interview may challenge an assumed recovery time; a field study may expose a demand peak; a simple queue model may show that a proposed fleet size cannot stabilize service. Such evidence revises the concept rather than merely decorating a preferred design.

This also connects early concept definition to lifecycle assurance. The ConOps supplies operational situations that later become requirements, architecture scenarios, test conditions, and acceptance measures. Its authority does not come from polished narrative language; it comes from traceable assumptions and its ability to predict meaningful outcomes within a declared operating domain.

## Worked engineering case

If requests arrive at 8/hour and an initial concept can serve only 6/hour, backlog grows at approximately 2 requests/hour under sustained demand. Averages hide event surges and inaccessible trips.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

A calculator that reports an average wait without measuring unserved requests can reward exclusion. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Stakeholder evidence and current-state analysis](02-stakeholder-evidence-and-current-state-analysis.md); the next connection is [Conceptual requirements, use cases, gaps, and experiment planning](04-conceptual-requirements-use-cases-gaps-and-experiment-p.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Write a five-step event-day scenario with one road closure and a wheelchair-accessible request, then identify the model inputs required.

**Problem B — Adversarial review.** How would an event-day mission scenario alter your service-capacity assumption?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 3: ConOps and mission measures](../labs/lab-03-desired-end-state-conops-scenarios-and-mission-calculat.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 3 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
