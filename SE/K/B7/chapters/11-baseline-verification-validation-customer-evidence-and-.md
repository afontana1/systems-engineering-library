# Chapter 11 — Verification, validation and CDR

*Book 7: System Design and Integration · Week 11 — Baseline verification, validation, customer evidence, and CDR readiness*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 11](../labs/lab-11-baseline-verification-validation-customer-evidence-and-.md) without looking at the solution → return to [Week 11 of the course guide](../../../C/P2/EN645768.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-768-w11.md) is optional review, not the primary reading.

## The engineering problem

The Northstar concept has now been conditionally selected. Engineering must turn it into interfaces, allocations and budgets that can be implemented and tested, without treating open assumptions as resolved. The governing question this week is **verification, validation and cdr**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Verification asks whether the design meets the controlled specification; validation asks whether users can accomplish their intended mission in its real context. Evidence must be tied to article configuration, method and acceptance threshold. A design review makes a readiness recommendation, not a historical proof that every deployment condition has been exercised.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

### Verification coverage is not equivalent to system adequacy

A requirement can have an assigned test and still lack meaningful verification. The test may use the wrong configuration, an unrealistic stimulus, insufficient instrumentation, or acceptance limits inherited from a flawed allocation. Coverage matrices answer whether relationships exist; assurance arguments ask whether the evidence actually bears on the claim. This is why test readiness and final acceptance should involve technical interpretation, not only document completion.

Integration also changes the evidence question. Component tests establish properties under controlled boundaries. Once components share clocks, networks, energy, thermal conditions, and operator interfaces, their assumptions may cease to hold. A well-designed verification strategy moves from local behavior to interfaces and mission scenarios while recording what each level cannot establish. Validation then returns to intended use: a fully verified design can remain unsuitable if the requirement set omitted the actual operational need.

## Worked engineering case

Eighteen passing tests out of twenty show only this fixture’s pass count; they neither prove 90% population reliability nor satisfy a requirement if one failure is safety-critical.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

Counting tests rather than decision-relevant coverage produces false confidence. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Plan system integration and conduct the Integration Readiness Review](10-plan-system-integration-and-conduct-the-integration-rea.md); the next connection is [Conduct the Final Design & Integration Review and hand off to T&E](12-conduct-the-final-design-integration-review-and-hand-of.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Create a claim–method–article–criterion–result matrix and mark gaps that prevent CDR.

**Problem B — Adversarial review.** Which stakeholder need is underrepresented by the planned evidence?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>


## Graduate depth: critical design review as a chain of realizability claims
### Design maturity is not the number of finished drawings

A critical design review should determine whether an implemented product can plausibly satisfy its specified requirements and whether the remaining uncertainty is compatible with the next commitment. Realizability depends on interfaces, tolerances, resource budgets, fault responses, verification access, and manufacturability acting together. A subsystem can be individually detailed but incompatible with adjacent subsystems; a wiring diagram can be complete while leaving test points inaccessible. Maturity therefore requires examining cross-discipline dependencies, not merely percentage completion of design documents.

A useful assurance structure distinguishes four claims: requirements have been interpreted and allocated consistently; the detailed architecture is physically and logically feasible; evidence is planned and obtainable; and unresolved risks are bounded by decision authority. Each claim needs configuration-specific supporting artifacts. For example, an interface control document provides a contract, tolerance analysis supports fit, an integration rehearsal supports assembly sequence, and a fault-tree or hazard analysis supports specific safety arguments. No single artifact proves the whole claim.

### Verification and validation fail in different ways

Verification asks whether a realized item satisfies a specified requirement. Validation asks whether the specified and realized system serves the intended use. Passing every test of an incomplete requirement set may still yield an unacceptable service. Conversely, users may like a prototype whose unsafe operating mode has never been exercised. The review must preserve both dimensions. A requirements trace matrix detects missing planned tests, but it cannot alone establish that the requirements express the correct stakeholder needs or that the tests can expose realistic failure conditions.

Measurement plans also have feasibility constraints. An intended requirement that specifies a 100-millisecond response limit is only testable if timestamps share a sufficiently accurate clock, the event boundaries are defined, and the instrumentation does not distort the behavior. Tolerances and uncertainty need to be considered before qualification, not discovered when evidence arrives. A design requiring inaccessible internal measurements may need diagnostic ports, telemetry, surrogate observables, or a revised verification strategy.

### Acceptance with open items is a bounded authorization

Suppose a prototype fleet demonstrates nominal service while thermal performance under repeated peak charging remains uncertain. The board might authorize limited environmental tests and manufacturing preparation but prohibit operational release. This is different from declaring the design broadly qualified. The open item should name the consequence of failure, evidence needed for closure, owner, permitted exposure, and re-review trigger. Quantifying schedule risk may be useful, but a probabilistic estimate cannot override a mandatory certification or safety condition.

The review decision should preserve a controlled design baseline: drawings and models, software build identifiers, requirement revisions, interface versions, analytical assumptions, verification methods, test constraints, nonconformances, and outstanding supplier dependencies. Subsequent changes need impact analysis across these linked artifacts. In this way, critical design review connects technical detail to project governance and test readiness. The legitimate conclusion is an evidence-bounded authorization for the next lifecycle activity, not a declaration that every operational behavior is already understood.

## Practice before the assessed course work

[Hypothetical Laboratory 11: Verification, validation and CDR](../labs/lab-11-baseline-verification-validation-customer-evidence-and-.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 11 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
