# Chapter 8 — Humans, safety and security

*Book 7: System Design and Integration · Week 8 — Design for human performance, safety, security, usability, and resilience*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 8](../labs/lab-08-design-for-human-performance-safety-security-usability-.md) without looking at the solution → return to [Week 8 of the course guide](../../../C/P2/EN645768.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-768-w08.md) is optional review, not the primary reading.

## The engineering problem

The Northstar concept has now been conditionally selected. Engineering must turn it into interfaces, allocations and budgets that can be implemented and tested, without treating open assumptions as resolved. The governing question this week is **humans, safety and security**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Safety and security constraints are architectural responsibilities, not late checklists. Analyze unsafe control actions involving a human operator as well as software. An intervention can improve security and simultaneously burden emergency access; explicitly check both effects.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

### Human, safety, and security constraints cannot be added at the end

A design's safety depends on how people, software, hardware, and external services interact in both normal and abnormal conditions. A human may be assigned responsibility for emergency intervention while receiving delayed or ambiguous information. That allocation is not a safety control unless the operator can perceive the condition, understand the available action, and act before the hazard develops. Similarly, a security control that requires an unavailable network service can undermine an emergency function.

Safety, human factors, and cybersecurity are related but not interchangeable. Safety examines unacceptable losses arising from system behavior; security examines intentional misuse and adversarial capabilities; human-systems integration examines performance, cognition, and work conditions. An engineering analysis must expose their common interfaces and competing demands. The relevant design object is often a **control loop**—sensing, interpretation, decision, actuation, feedback—not a single component that can simply be labeled safe or secure.

## Deeper theory: people, hazards, and adversaries belong in one control architecture

### Human performance emerges from task and context

Human-system integration is not a late ergonomic review of an otherwise finished machine. The architecture allocates perception, interpretation, decision authority, and physical action between humans and automation. An operator asked to approve a remote movement command must see enough trustworthy state to make that decision, understand the allowed operating envelope, and have time to act. A dashboard can be legible and still provide the wrong information for the task. Human error is therefore not well modeled as a constant component failure rate independent of workload, fatigue, alarm frequency, training, or interface design.

Automation introduces an additional challenge: the operator's mental model may differ from the actual control mode. In a partially automated shuttle, “manual override available” is inadequate unless the handoff event, authority transfer, feedback, and fallback behavior are explicit. If a warning arrives after the vehicle has crossed the point where stopping is possible, the human control is nominal rather than effective. Evaluate detection time, comprehension, decision time, action execution, and the physical deadline of the hazard together.

### Safety and cybersecurity intersect through control authority

Safety hazards involve unacceptable losses; security threats involve adversarial intentions and capabilities. The same unsafe state can arise from a software defect, compromised credential, misleading sensor, or operator misunderstanding, but the causal models and defenses differ. A remote command channel may need authentication to resist malicious control and local interlocks to resist authorized but unsafe commands. Security does not substitute for safety merely because a message is cryptographically valid. Conversely, a safety mechanism reachable over an unauthenticated interface can become an attack surface.

Consider a network partition. A safe degraded mode might reject new boarding authorization while finishing a controlled maneuver using local state. A security design that fails closed on every communication error may protect access control yet interrupt critical rescue functions. The requirements need to distinguish operations that must cease, those that may continue autonomously, and those that require independent human authority. This is a control-allocation tradeoff with mission, timing, and human consequences—not a choice between “safe” and “secure” in the abstract.

### Hazard constraints need observable enforcement

A causal safety claim such as “the shuttle shall not move with the boarding ramp deployed” implies a sensor model, an authorization rule, and an actuator constraint. Ask what occurs if ramp state is unknown, stale, or inconsistent across controllers. Physical interlocks, fault-tolerant sensing, commands with short validity windows, and independently tested stopping functions may provide layered defenses. However, common software, power, or maintenance errors can compromise several nominally separate controls. Independence has to be argued and tested, not inferred from block-diagram spacing.

Human-centered evidence includes workload and task analysis, representative users and accessibility needs, usability under adverse conditions, training retention, and operational feedback. Hazard and threat analysis supply complementary evidence about harms and malicious pathways. The Northstar design should connect both to the same controlled scenarios and interface definitions. The important output is a set of constraints on system behavior that remains meaningful when workload rises, communications degrade, an attacker acts, or the operating context changes. Designing for the “average operator” in the “normal scenario” alone does not establish safe operation.

## Worked engineering case

A remote dispatcher can override an automated route, but ambiguous displays may permit unsafe approval on stale telemetry. A two-person confirmation could help some hazards while increasing response delay in others.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

Training alone is not a substitute for a reliable interface or controlled authority. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Design for reliability, availability, and maintainability](07-design-for-reliability-availability-and-maintainability.md); the next connection is [Design for supportability, producibility, supply, sustainability, and disposal](09-design-for-supportability-producibility-supply-sustaina.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Draw a human-control loop and test four unsafe-action categories: not provided, provided incorrectly, mistimed and held too long.

**Problem B — Adversarial review.** Which safety constraint becomes invalid if communications lag?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 8: Humans, safety and security](../labs/lab-08-design-for-human-performance-safety-security-usability-.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 8 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
