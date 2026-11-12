# Chapter 5 — Functions independent of components

*Book 6: System Conceptual Design · Week 5 — Functional architecture and mission-to-function traceability*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 5](../labs/lab-05-functional-architecture-and-mission-to-function-traceab.md) without looking at the solution → return to [Week 5 of the course guide](../../../C/P2/EN645767.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-767-w05.md) is optional review, not the primary reading.

## The engineering problem

At this point the Northstar team is still free to select among competing mobility-service concepts. A proposed autonomous shuttle is one hypothesis, not the definition of the problem. The governing question this week is **functions independent of components**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Functional decomposition explains what transformations must occur—information, material, energy and control—without saying which component does them. Trace functions to scenarios and measures; later physical allocation is a separate design decision. Functions should be verb-object phrases and include failure handling.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

### Functional neutrality preserves the design space

A functional architecture should describe transformations the system must provide before committing to who or what performs them. “Detect an unsafe obstacle” remains meaningful whether sensing is performed by onboard lidar, roadside infrastructure, or an operator. But the function must still specify the inputs it depends on, the output it produces, and the latency or confidence that matters to the mission. Functionality without measurable operating conditions is too vague to constrain a concept.

Separating function from physical allocation has a second purpose: it exposes hidden dependencies. If the function “grant boarding authorization” depends on an external identity provider, that provider is part of the operational dependency graph even if it lies outside the equipment boundary. An alternative architecture may relocate that function, increasing local autonomy while requiring more onboard computing. This is exactly why functional neutrality is powerful: it allows a designer to compare where responsibilities could live without silently changing what success means.

## Deeper theory: functional architecture separates necessary transformation from selected technology

A function describes a transformation, decision or control needed for the system to achieve its purpose. A physical component is one possible agent that realizes that function. The distinction is foundational because a design team can otherwise confuse “the present equipment layout” with “what the mission requires.” A functional architecture should remain meaningful when the implementation changes. *Maintain safe passenger separation from traffic* is a function or operational capability; *use lidar unit X* is a proposed means. The latter can be replaced without removing the former.

Functional analysis begins with **inputs, outputs, triggering conditions and state assumptions**, not a list of components. Consider the function `AuthorizeDeparture`. Its inputs could include passenger-boarding status, route permission, vehicle health and operator authority. Its output is not merely a boolean; it is a decision with a reason, time validity and consequences for subsequent control. When decomposing this function, the engineer asks which subordinate transformations are necessary and which information dependencies arise. The decomposition should preserve the parent's observable contract under the intended conditions.

### Functional decomposition is not automatically hierarchical in time

A traditional tree can suggest that each parent function contains independent child functions executed in a fixed order. Real behavior can be concurrent, cyclic or tightly coupled. A battery-management system estimates available energy while route planning changes the expected demand; neither process is entirely upstream of the other. A functional hierarchy is a **view of responsibility and scope**, not a complete behavioral model. Activity and state models may be needed to express ordering, feedback, and repeated evaluation.

An important completeness question is whether each external demand or condition has a corresponding functional response. The campus shuttle must handle not only normal ride requests but also invalid coordinates, unavailable vehicles, interrupted charging, emergency overrides and human intervention. A functional model that decomposes only the successful mission trace is structurally tidy and operationally incomplete.

### Allocation is a decision that introduces new constraints

After defining functions, engineers allocate them to physical or software elements. Allocation introduces performance, ownership and communication requirements that were not necessarily present in the abstract function. Suppose route eligibility is evaluated centrally. That architecture requires connectivity and introduces a latency dependency. Allocating the function to the vehicle may improve local availability but require distributing authoritative map revisions and preserving consistency after reconnecting. **The function is stable; the architecture changes the failure modes**.

A useful way to reason about allocation is through **coupling**. Functions that share rapidly changing state may be cheaper or safer to co-locate; functions that require independent assurance or fail-safe isolation may need separation. Co-location reduces communication cost but can create common-cause failures. Separation supports independent development and fault containment but creates protocol, synchronization and integration obligations. There is no universally optimal level of modularity without a model of change rates, latency, hazards and organizational boundaries.

### Interfaces appear when a function is divided

Every allocation decision moves some interactions from internal implementation detail to an interface between responsible elements. If one team owns passenger authentication and another owns reservation commitment, the boundary needs a contract about identity freshness, authorization lifetime, failure responses and audit records. A functional flow diagram may show only an `authorized` signal, but the physical architecture must explain when that signal becomes stale and who may revoke it. **Functional completeness does not imply interface completeness**.

Quantitative budgets make the distinction concrete. If a system must respond within \(T_{\max}\) and the chosen architecture has processing stages with worst-case bounds \(t_i\), then a conservative serial budget requires \(\sum_i t_i\leq T_{\max}\), assuming the bounds are genuine and the stages are serial. If the numbers are percentiles rather than worst-case bounds, direct addition does not establish a percentile guarantee. Allocation must therefore specify both the target and the statistical or deterministic meaning of its budgets.

### Traceability is an argument about satisfaction

A relationship from function to component indicates a design intention; it does not prove the component correctly performs the function. The satisfaction claim needs evidence concerning the component's behavior under specified interfaces and environments. An apparently complete matrix with every function allocated may still omit degraded operations, human responsibilities, external infrastructure and end-to-end timing. The quality of allocation lies in the explanatory consistency of mission needs, functional contracts, components, interfaces and evidence.

Functional architecture thus serves as a stable **reasoning layer between mission and implementation**. Its purpose is to preserve the essential transformations while allowing alternatives to be compared and consequences of allocation choices to be made visible.

## Worked engineering case

“Vehicle sends GPS to cloud” encodes a vendor topology. “Estimate position,” “assess confidence,” “publish trusted location,” and “reject stale reports” can be allocated to several architectures.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

A single “dispatch” bubble hides safety-critical eligibility and notification decisions. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Conceptual requirements, use cases, gaps, and experiment planning](04-conceptual-requirements-use-cases-gaps-and-experiment-p.md); the next connection is [Timing, interfaces, allocations, and Functional Architecture Review](06-timing-interfaces-allocations-and-functional-architectu.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Build an eight-function chain from accessible-trip request to completion and add an exception path for missing location.

**Problem B — Adversarial review.** What functional responsibility remains if a cloud connection is absent?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 5: Functions independent of components](../labs/lab-05-functional-architecture-and-mission-to-function-traceab.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 5 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.


## Step 03 integrated reference: NS-CD6.1 — functional architecture without vehicle lock-in

The central discipline of functional design is to describe transformations that any viable concept must perform, before allocating them to hardware, software or people. The [controlled functional record](../case/functions.csv) identifies F01 Detect mobility need, F02 Make feasible offer, F03 Dispatch allocated capacity, F04 Monitor and recover, and F05 Record outcomes and evidence. A brokered service and a self-operated shuttle may implement these functions differently while being evaluated against the same mission.

### Trace transformations instead of repeating organization names

For each function, specify triggering conditions, inputs, outputs, control policy, state, failure output and observable result. F02 needs a booking request and a current service envelope; its valid outputs are an accessible offer **or a clearly recorded inability to serve**. Omitting the failure output produces a misleading coverage denominator because unserved requests disappear. F03 consumes an accepted offer and a capacity commitment; a proposed dispatch is not successful service until allocation is exclusive and executable.

A simple functional thread is `F01 → F02 → F03 → F04`, with F05 recording outcomes from every stage. This is a **causal dependency**, not a claim that the physical system is strictly sequential. Monitoring is concurrent with dispatch, and recovery can redirect the flow to an operator. Timing matters because an offer based on stale capacity can be invalid before a passenger ever boards.

### Quantify the consequence of allocation

Candidate C assigns a trunk route and feeder vehicles to the same mobility mission. The simple arithmetic offers 40 + 12.8 = 52.8 effective trips/h. The decomposition is valid only if the trunk and feeder capacities represent disjoint served demand or an explicitly modeled transfer flow. If every feeder passenger must transfer to the trunk, summing their capacities **overstates** system throughput: a serial chain's throughput is bounded by the slower stage, \(C_{\mathrm{system}}\le\min(C_{\mathrm{feeder}},C_{\mathrm{trunk}})\) for that passenger class. This alternative interpretation is a useful counterexample; the case assumes parallel service contributions pending scenario validation.

### Review questions and answer

**Exercise:** A design team maps the need “accessible trip offered” only to F03 Dispatch. What is missing? **Answer:** F01 must accept eligible requests, F02 must apply accessibility feasibility and refusals, F04 must handle degraded or missing paths, and F05 must make coverage independently observable. The dispatch function is necessary but insufficient. Cross-check every CD6 requirement against [the function record](../case/functions.csv) and decide whether a missing link is a design defect or an unsupported mission claim.

**Boundary:** A functional map is not a physical interface specification, a safety assurance case, or an interoperability demonstration. Its value is to make those later analyses traceable to the original mission.
