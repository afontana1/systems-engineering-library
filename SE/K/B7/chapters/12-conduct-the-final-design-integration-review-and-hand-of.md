# Chapter 12 — Design baseline handoff

*Book 7: System Design and Integration · Week 12 — Conduct the Final Design & Integration Review and hand off to T&E*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 12](../labs/lab-12-conduct-the-final-design-integration-review-and-hand-of.md) without looking at the solution → return to [Week 12 of the course guide](../../../C/P2/EN645768.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-768-w12.md) is optional review, not the primary reading.

## The engineering problem

The Northstar concept has now been conditionally selected. Engineering must turn it into interfaces, allocations and budgets that can be implemented and tested, without treating open assumptions as resolved. The governing question this week is **design baseline handoff**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

A final design handoff includes interfaces, allocations, budgets, constraints, specialty analyses, outstanding hazards, integration sequence, verification methods and a trusted configuration manifest. If any major assumption changes, dependent evidence must be re-evaluated. Conditional acceptance is meaningful only with explicit owners and due gates.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

The design baseline handoff transfers a controlled set of claims, interfaces, test obligations and residual risks.

### Distinguishing related ideas

A signed design review is not evidence that every behavior will work in operations; it means a defined authority accepted specified remaining uncertainty.

### Interpretation and boundary conditions

The receiving team must know which configurations the design evidence covers and what change invalidates that coverage.

## Worked engineering case

The selected route controller was validated only against Map Revision 3; the test organization receives Revision 4. That is a change-impact issue, not a harmless housekeeping detail.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

A reproducible package can still be substantively wrong; independent challenge remains essential. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Baseline verification, validation, customer evidence, and CDR readiness](11-baseline-verification-validation-customer-evidence-and-.md); the next connection is the receiving team and next review phase. Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Write a design-handoff memo that distinguishes accepted claims, conditional claims and deferred evidence.

**Problem B — Adversarial review.** What must the receiving T&E team revalidate first?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>


## Graduate depth: design handoff as preservation of technical meaning
### Handoff errors are often semantic rather than clerical

When engineering moves from design into integration and testing, knowledge crosses organizational and tool boundaries. A requirement identifier may survive the transfer while its meaning changes; a wiring revision may be current while the related test fixture uses old pin assignments. The receiving team needs more than a document package. It needs the ability to reconstruct the configuration, operating assumptions, interface commitments, known deviations, and evidence logic on which the design decision depended.

A handoff can be modeled as an information-preservation problem. The source team holds knowledge `K_source`; the recipient receives artifacts `A` and must recover an operationally sufficient representation `K_receiver = interpret(A, context)`. Perfect transfer is unrealistic because knowledge includes tacit expertise, but critical obligations can be made explicit through structured contracts, executable checks, annotated decisions, and walkthroughs of failure cases. A well-formed handoff minimizes ambiguity in the decisions the recipient must make, not simply the number of unanswered questions.

### Configuration identity joins models to hardware and tests

A baseline identifier should correspond to an identifiable combination of hardware revisions, firmware and software builds, parameter sets, drawings, interface specifications, calibration state, and approved deviations. Versioning only a top-level PDF is insufficient. A physical unit might contain a replacement sensor with different calibration, making evidence from another unit inapplicable unless equivalence is justified. The trace `requirement → design element → as-built item → verification method → measured result` is most useful when each link has a version and a declared relation.

Consider Northstar's vehicle-control integration. The design team may have tested a brake controller using simulated wheel speeds. The receiving team must know the simulation time step, sensor failure modes included, controller firmware build, calibration constants, and the exact timing assumption. Without these details, repeating the test can produce a different result while apparently following the same procedure. An artifact's provenance is thus a technical property, not an administrative afterthought.

### Acceptance criteria make handoff an engineering gate

A receiving team should be able to locate every critical interface, identify current configuration, reproduce a representative analysis, describe known limitations, and execute at least one end-to-end test or test rehearsal. It should also know what remains unverified and which authorities may approve deviations. This resembles a contract: the sending team promises a defined package, and the receiving team demonstrates that the promise is actionable. A signature without such checks is evidence of attendance, not successful transfer.

The handoff should include negative information: discarded alternatives, fragile assumptions, unresolved disagreements, and conditions under which a previous test no longer applies. Suppressing these details makes later failures harder to diagnose. When change occurs, the transfer record provides a starting point for deciding which tests must be rerun and which claims remain valid. The central principle is continuity of engineering meaning across lifecycle transitions. A successful handoff is measured by the new team's ability to build, integrate, challenge, and verify the design without inventing missing rationale.

## Practice before the assessed course work

[Hypothetical Laboratory 12: Design baseline handoff](../labs/lab-12-conduct-the-final-design-integration-review-and-hand-of.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 12 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.

## Step 03 integrated technical reference: NS-DI7.1 — final design review and defensible handoff

### Produce a decision package, not a green dashboard

The NS-DI7.1 case closes with a conditional design decision. The combined gateway/dispatch alternative has a modeled 440-ms degraded command path and 60-ms absolute reserve, satisfying the **modeled** 10% reserve allocation. Per-shift energy is 26.3 kWh against 30 kWh. However, modeled eight-hour mission reliability including the shared hazard is 0.97863 against 0.98; logistics-adjusted availability is 0.98644 against 0.99. The accessibility test is unexecuted, the revised degraded-latency test is stale, and the baseline-level evidence reconciliation is missing. The proper operational conclusion is **HOLD**.

Separate the final decision into three outputs: **design maturation approved conditionally**, **integration authorized only with named controls**, and **operational release not approved**. None is automatically implied by the others. An acceptance authority may decide which residual risks are tolerable, but a course exercise must not forge that authority by changing a field in a spreadsheet.

### A defensible handoff includes dissent and falsifiers

Transmit the controlled [requirement register](../case/requirements.csv), [interface definitions](../case/interfaces.csv), [allocation matrix](../case/allocation.csv), [analysis baseline](../case/model-baseline.json), [test evidence](../case/evidence-register.csv), [experiment results](../case/doe-synthetic.csv), and unresolved risks. Include exact model versions and scripts, not merely printed headline results. The [reproducible checker](../tools/step03_book7_design_check.py) calculates numerical consequences and identifies structural mismatches, but it is not a certified integration tool or a qualification test.

Record clear *reversal criteria*: the mission failure model must meet the 0.98 target under credible shared-cause assumptions; downtime logistics must be redesigned or supported by different qualified evidence; degraded p99 timing must be remeasured on NS-DI7.1; accessible trials must include the intended user population. If any test overturns a favorable model, update the design and its dependent claims before restarting the gate.

A high-quality final technical review distinguishes **what is calculated**, **what is observed**, **what has been validated with stakeholders**, and **what remains a hypothesis**. This habit carries forward into test and evaluation, operations, and eventual change control.

**Exercise.** A sponsor asks for the earliest route to operational approval. Write a minimum closure list without erasing the present design failure.

<details><summary>Worked resolution</summary>

Require (1) an acceptable mitigation and retest/justified model for shared mission failures, (2) a support-chain plan and evidence addressing the 0.99 availability target, (3) controlled degraded p99 timing trials on the revised hardware/software baseline, (4) accessible-service trials, and (5) a complete, reviewed baseline-linked evidence register. A new review then determines readiness; none of these tasks alone constitutes release authorization.

</details>
