# Chapter 12 — Readiness recommendations and dissent

*Book 8: System Test and Evaluation · Week 12 — Conduct the final evidence review and make the operational-readiness recommendation*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 12](../labs/lab-12-conduct-the-final-evidence-review-and-make-the-operatio.md) without looking at the solution → return to [Week 12 of the course guide](../../../C/P2/EN645769.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-769-w12.md) is optional review, not the primary reading.

## The engineering problem

The Northstar design team has handed over an evidence claim and a product configuration. The evaluator is independent of the preferred design decision and must distinguish what is demonstrated from what remains assumed. The governing question this week is **readiness recommendations and dissent**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Separate compliance, mission validation, operational effectiveness, suitability, residual risk and configuration maturity. The final recommendation may be conditional, limited, deferred or rejected; give an exact operating envelope and named closure evidence. Preserve dissent when reasonable experts interpret sparse evidence differently.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

## The mechanism beneath the method

Operational readiness is a bounded decision about a specified mission envelope and governance regime.

### Distinguishing related ideas

A pass/fail dashboard cannot replace interpretation of excluded scenarios, unresolved anomalies, confidence limits or stakeholder consequences.

### Interpretation and boundary conditions

A strong review identifies what would cause suspension or re-evaluation after deployment, not just why the present gate was passed.

## Worked engineering case

A service can meet its dispatch latency requirement while failing accessible-trip completion under telemetry outage. A qualified statement must reflect both claims and should not promote the first into a blanket readiness conclusion.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Graduate synthesis: readiness as a structured decision with residual uncertainty

### A readiness recommendation is not a probability alone

Technical reviews often collapse complicated evidence into a green, yellow, or red score. Color is a communication device, not an inference method. A defensible readiness argument specifies the planned use, configuration, supporting evidence, remaining risks, and the exact authority accepting those risks. The same Northstar vehicle may be ready for a supervised demonstration and not ready for unsupervised passenger operation. Readiness is therefore indexed by *mission envelope*, rather than attached permanently to a product.

One way to structure the decision is to separate mandatory constraints from expected benefit. Let `A` be the set of allowed actions and let `H(a)` express non-negotiable safety and legal requirements. Only actions satisfying `H(a)` belong to the feasible set; within that set, decision-makers may compare cost, reliability, accessibility, and schedule outcomes. A high weighted benefit must not silently trade away a mandatory hazard control. If evidence for a constraint is incomplete, define a limited test permission and monitoring condition, or withhold authorization; do not reinterpret a missing demonstration as a favorable measurement.

### Calibrate evidence strength to the claim

The board should distinguish **verification** of a specified feature, **validation** of fitness for intended use, **qualification** against an agreed standard or environment, and **operational acceptance** by the accountable authority. They may rely on overlapping tests but answer different questions. A temperature-chamber test may qualify hardware for an environment yet say little about peak-hour passenger flow. A successful trial with a human supervisor cannot directly establish unsupervised operation unless the supervisor's intervention role is measured and bounded.

Statistical evidence needs denominators and uncertainty. Suppose 94 of 100 trips meet a punctuality criterion. The observed rate is 94%, but the plausible underlying rate is uncertain, particularly if trips share correlated weather and staffing conditions. A confidence interval based on independent Bernoulli trials will understate uncertainty when entire days are good or bad together. Stratify the evidence by operational scenario or use clustered analysis; report coverage gaps rather than combining incompatible conditions into one impressive percentage.

### Dissent is a source of information

An independent reviewer may accept the data but disagree that it covers the intended operational domain. Another may challenge the harm model or the risk threshold. Preserve these as distinct concerns, not as vague minority objections. The readiness record should name each dissenting claim, its evidentiary basis, how management responded, the acceptance authority, and the measurement that would force reconsideration. Overruling dissent is a decision that requires accountability, not a technical finding that dissent was disproven.

Northstar's final board might authorize a 90-day supervised pilot, require weekly accessibility and incident summaries, and prohibit expansion to new routes until independent localization testing is completed. State measurable stop conditions: repeated safety fallback activation, sustained wait-time inequity, or an incident-reporting failure. The aim is **bounded learning with explicit decision rights**. The strongest concluding report makes future reversal or escalation easier because it preserves the assumptions under which permission was granted.

## Competing explanations and failure modes

A binary “pass” badge hides unresolved scope and the causal path to mission harm. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Evaluate operational use, deployed systems, systems of systems, AI, and autonomy](11-evaluate-operational-use-deployed-systems-systems-of-sy.md); the next connection is the receiving team and next review phase. Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Write a board memo with accepted, conditional, rejected and untested claims, plus a red-team dissent paragraph.

**Problem B — Adversarial review.** What operational boundary must not be crossed on current evidence?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 12: Readiness recommendations and dissent](../labs/lab-12-conduct-the-final-evidence-review-and-make-the-operatio.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 12 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
