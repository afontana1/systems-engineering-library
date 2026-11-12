# Chapter 1 — Receiving concept assumptions

*Book 7: System Design and Integration · Week 1 — Receive the concept baseline and plan design maturation*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 1](../labs/lab-01-receive-the-concept-baseline-and-plan-design-maturation.md) without looking at the solution → return to [Week 1 of the course guide](../../../C/P2/EN645768.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-768-w01.md) is optional review, not the primary reading.

## The engineering problem

The Northstar concept has now been conditionally selected. Engineering must turn it into interfaces, allocations and budgets that can be implemented and tested, without treating open assumptions as resolved. The governing question this week is **receiving concept assumptions**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

A design team inherits a chosen concept, not permission to stop questioning it. Receiving review partitions baselined facts, conditional decisions, references, unresolved issues and rejected materials; each needs authority, revision and acceptance rationale. The System Engineering Management Plan must name actual decision owners and closure procedures.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Receiving a concept baseline is an exercise in recovering its assumptions, not passively accepting a set of diagrams.

### Distinguishing related ideas

A concept estimate and a detailed allocated requirement may use the same number but refer to different configurations and environments.

### Interpretation and boundary conditions

Before decomposing, identify which inherited assumptions are demonstrated, which are contractual and which remain provisional.

## Worked engineering case

A concept claims 15-minute accessible service but lists vehicle location freshness as “TBD.” That parameter is an unresolved performance dependency, not a complete interface specification.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

Merely copying the incumbent concept into the design baseline can manufacture false maturity. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is the Phase 1 architecture and foundation books; the next connection is [Close the system specification](02-close-the-system-specification.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Classify 10 incoming artifacts and build an evidence-dependency path for the highest-risk missing one.

**Problem B — Adversarial review.** What would you refuse to accept at the receiving gate?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>


## Deeper theory: the concept-to-design transfer as an assumption contract

### A selected concept is not yet a buildable design

Conceptual design often chooses among alternatives using simplified performance estimates, cost models, mission scenarios, and preliminary allocations. Detailed design must turn the selection into verifiable requirements, controlled interfaces, tolerances, and manufacturable components. That transition creates a predictable risk: estimates that were acceptable for ranking concepts can become unacceptable as implementation commitments. The receiving design organization should not inherit an estimated value as though it were a validated physical limit. Each transferred fact needs a type: binding requirement, design assumption, preliminary estimate, unresolved trade, accepted risk, or supporting evidence.

A handoff is therefore a **contract about uncertainty**. It identifies what the design team may change, what must remain invariant, and which assumptions must be tested first. For Northstar, a concept might assume a 40-second average dwell time, a nominal charging cycle, and flawless connection to dispatch. The receiving team must ask whether the mission outcome depends on the average or on high-percentile dwell, whether charge time includes queueing and battery conditioning, and how communication loss changes safe operation. A concept gate that records these dependencies creates a roadmap for real engineering rather than a fiction of finished knowledge.

### Maturity should be assessed by risk retirement, not drawing detail

A detailed CAD assembly may contain impressive geometric resolution while retaining uncertain materials, fatigue loads, supply availability, thermal conditions, or control behavior. Conversely, a rough prototype can settle a decisive integration risk early. Technical maturation should prioritize uncertainties by their probability of undermining the mission, their consequence, and the time required to resolve them. Risk matrices can help prioritize, but ordinal risk scores should not be multiplied and treated as precise physical quantities without justification. A hazard with low estimated probability and catastrophic consequence may require a noncompensatory safety rule rather than a high average score.

Engineering margins can be represented as differences between predicted capability and required capability. If allowable energy per mission is 20 kWh and the current predicted requirement is 17 kWh, the nominal margin is 3 kWh, or 15% of the allowed budget. Its meaning depends on what uncertainties are included: temperature, battery aging, route changes, HVAC demand, and emergency reserve can each erode the available margin. A useful margin report distinguishes nominal estimate, uncertainty bound, reserved contingency, and who may spend the margin. Treating margin as an unowned pool encourages incompatible local optimizations.

### Design authority requires explicit interface and decision ownership

Interfaces frequently cross company or discipline boundaries. A timing requirement negotiated only by software engineers may contradict the physical actuator's response; a power budget negotiated by hardware specialists may ignore cybersecurity hardware overhead. The handoff should assign interface owners, change authority, data definitions, and procedures for resolving conflicts. A review board can authorize a deviation but should document which mission claim it compromises and what evidence justifies the decision. Configuration identity makes those decisions reproducible when suppliers change.

The transition is successful when the receiving team can state which claims are mature, which are conditional, and which upcoming tests could reverse the architecture decision. It is unsuccessful when the only deliverable is a preferred drawing with no explicit validity domain. Detailed design begins by **challenging the concept's conditional promises**, not by decorating them.

## Practice before the assessed course work

[Hypothetical Laboratory 1: Receiving concept assumptions](../labs/lab-01-receive-the-concept-baseline-and-plan-design-maturation.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 1 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.

## Step 03 integrated technical reference: NS-DI7.1 — controlled concept handoff

### From a preferred concept to a design obligation

A *concept recommendation* is not a component design specification. Book 6 preferred a hybrid mobility concept under an invented operating envelope, but left degraded response, accessibility evidence, and failure behavior open. Book 7 begins by receiving those conditions as **obligations**, not silently converting them into resolved facts. The editable [NS-DI7.1 design case](../case/INDEX.html) records its inheritance from NS-CD6.1; the [model baseline](../case/model-baseline.json) is an explicitly new design baseline, not a claim that an actual system has been built.

The controlled case defines a peak-service requirement of 46.2 trips/hour and a model capacity of 52.8 trips/hour. Their difference, 6.6 trips/hour, is **nominal modeled headroom**, not a statistically established probability of meeting demand. Capacity depends on duty cycle, disruptions, accessible pickup requirements, and fleet availability. A reviewer should ask whether the calculation covers the same demand population and shift as the requirement.

A transfer register should assign a decision to every inherited condition. For instance, "degraded dispatch timing" becomes requirement DI7-R02, allocated to the gateway, broker, dispatch and vehicle controller; "accessibility trial incomplete" becomes DI7-R07 and remains **planned**, not passed. The [requirements](../case/requirements.csv), [allocation matrix](../case/allocation.csv) and [evidence register](../case/evidence-register.csv) show the differences. Controlled identifiers matter because a reviewer must trace a change in a function to an interface, a test procedure, and a release decision.

### Test the handoff for completeness

A useful transfer is a directed graph: stakeholder claim → system requirement → assigned function → owned physical element → verification method → configuration-specific evidence. A missing edge is not evidence of failure, but it is evidence that the claim has not been fully justified. The corresponding audit must also check that a test assigned to NS-DI7.0 is **not** accepted for NS-DI7.1 without an applicability argument.

Treat these distinctions as separate axes: design feasibility (a calculation), model integrity (a linked and typed claim), and demonstrated performance (executed evidence). The first two do not imply the third. Concept reviews also hand forward retained alternatives and termination criteria so a risky design is not allowed to become inevitable merely because work has begun.

**Exercise.** A design team sees 52.8 trips/hour against a 46.2-trip/hour need and labels DI7-R01 "verified." Identify the invalid inference and the smallest legitimate next step.

<details><summary>Worked resolution</summary>

The numerical headroom is 6.6 trips/hour (about 14.3% of the requirement) *under the modeled assumptions*. It does not establish performance at a stated confidence or across the required service population. Record MODEL_ONLY and design a representative controlled fleet-load trial with measured throughput and explicit exclusion rules. Keep the concept decision conditional.

</details>
