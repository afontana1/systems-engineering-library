# Chapter 10 — Integration readiness and sequencing

*Book 7: System Design and Integration · Week 10 — Plan system integration and conduct the Integration Readiness Review*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 10](../labs/lab-10-plan-system-integration-and-conduct-the-integration-rea.md) without looking at the solution → return to [Week 10 of the course guide](../../../C/P2/EN645768.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-768-w10.md) is optional review, not the primary reading.

## The engineering problem

The Northstar concept has now been conditionally selected. Engineering must turn it into interfaces, allocations and budgets that can be implemented and tested, without treating open assumptions as resolved. The governing question this week is **integration readiness and sequencing**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Integrate to retire architectural risk and learn about interfaces, not merely in order of delivery dates. Begin with safe surrogates, prove contracts, then exercise mission threads and degraded paths. Test environments, stubs and configuration control need maturity before hardware or human subjects are exposed.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Integration sequencing is an information strategy: resolve the most damaging interface uncertainties while changes are still reversible.

### Distinguishing related ideas

Joining components in assembly order is not always the best learning order; high-risk timing and fault-handling contracts may need early emulation.

### Interpretation and boundary conditions

An incremental integration plan should state what each build proves and what unresolved dependencies could still invalidate it.

## Deeper theory: integration order is a risk and information problem

### Integration dependencies form more than a build list

A product architecture can be represented as a graph whose vertices are hardware, software, data, operator procedures, and test environments, with edges representing interfaces or dependencies. A simple topological order works when the dependency graph is acyclic. Real systems often contain cycles: an autonomy controller needs sensor data while the sensor calibration process needs controller feedback. Cycles cannot be resolved by blindly applying a build order; they need temporary substitutes, emulators, shared test rigs, or explicit integration increments that cut the loop.

The optimal sequence is not always “integrate the easiest subsystem first.” Integrating a high-risk, poorly understood interface early may have more learning value than completing several low-risk demonstrations. Conversely, an early difficult test can waste resources if its prerequisites are immature. The decision weighs probability of exposing consequential defects, cost of the test setup, cost of rework avoided, and the consequences of delaying discovery.

### Interface maturity and product maturity are distinct

Two mature components can be incompatible. A vehicle controller may have passed qualification on its supplier's network, and a fleet scheduler may have passed software acceptance with a mock controller, yet their combined behavior can fail due to message ordering, unit interpretation, clock synchronization, or recovery assumptions. Integration readiness therefore needs interface evidence, not only component completion percentages.

A useful readiness claim identifies a specific interface version, test environment, input and output semantics, fault policy, timing tolerance, and available instrumentation. An “interface complete” declaration lacking these details is difficult to falsify and therefore weak as a control point. The goal is not a perfect document package but a sufficiently stable contract to make the next integration trial interpretable.

### Fault isolation depends on observability

When a test fails at system level, the team must separate initiating fault from propagated symptoms. A dropped command might originate in the radio, message broker, authentication service, scheduling algorithm, or actuator. Instrumentation should preserve correlated identifiers, synchronized time bases, configuration versions, and critical state transitions so competing hypotheses can be tested. Without this, repeated integration runs may reproduce failure without teaching the team anything about causation.

Observability itself has constraints. Logging can add load, alter timing, or expose sensitive information. Engineering teams should define what evidence must be available during each integration stage and how collection affects the system under test. A highly instrumented debug build and a final production build may require separate verification of equivalence.

### Early failures are valuable only if feedback changes the design

Suppose a prototype reveals that communications recovery takes 40 seconds rather than the allocated five. The discovery has value because the team can adjust network architecture, local autonomy, or system-level degraded-operation requirements before production. If a gate records the deviation but the program continues without deciding what changes, integration has produced information without control. The resulting unresolved inconsistency may become more expensive as downstream configurations diverge.

An integration plan should therefore connect evidence to decision rights and change rules. Evidence of readiness includes credible interface behavior, known limitations, fault recovery, representative operating cases, and reproducible configurations. Sequence, observability, and authority together determine whether integration is a controlled learning process or merely the late assembly of parts.

## Worked engineering case

Five components have ten possible pairwise relationships, but exercising every pair does not guarantee the mission thread Request→Eligibility→Plan→Dispatch→Notify works across timing and state boundaries.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

A successful happy-path demo cannot establish integration readiness for abnormal states. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Design for supportability, producibility, supply, sustainability, and disposal](09-design-for-supportability-producibility-supply-sustaina.md); the next connection is [Baseline verification, validation, customer evidence, and CDR readiness](11-baseline-verification-validation-customer-evidence-and-.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Order a safe integration sequence from simulator to hardware test article, and gate each step with entry evidence.

**Problem B — Adversarial review.** Which missing interface test blocks test-article exposure?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 10: Integration readiness and sequencing](../labs/lab-10-plan-system-integration-and-conduct-the-integration-rea.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 10 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
