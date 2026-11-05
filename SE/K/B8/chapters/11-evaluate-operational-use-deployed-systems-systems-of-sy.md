# Chapter 11 — Operational and autonomy evaluation

*Book 8: System Test and Evaluation · Week 11 — Evaluate operational use, deployed systems, systems of systems, AI, and autonomy*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 11](../labs/lab-11-evaluate-operational-use-deployed-systems-systems-of-sy.md) without looking at the solution → return to [Week 11 of the course guide](../../../C/P2/EN645769.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-769-w11.md) is optional review, not the primary reading.

## The engineering problem

The Northstar design team has handed over an evidence claim and a product configuration. The evaluator is independent of the preferred design decision and must distinguish what is demonstrated from what remains assumed. The governing question this week is **operational and autonomy evaluation**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Operational effectiveness asks whether a mission is accomplished, while suitability includes sustainment, human operations, support, cyber resilience and life-cycle use. Autonomy adds distribution shift, human takeover, opaque decisions and monitoring challenges. A system of systems may change its environment or deny a promised dependency.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

### Operational evaluation is a study of the whole mission

Operational evaluation differs from subsystem qualification because it examines whether real roles, procedures, environments, and interactions produce the desired outcome. A service can pass an algorithmic throughput test but underperform when dispatchers face competing priorities, passengers behave unpredictably, or maintenance removes capacity during a peak period. These factors are not necessarily “noise”; they may be part of the system whose suitability is under assessment.

A meaningful operational test must anticipate learning effects, scenario selection, and unintended incentives. If operators know the planned failure scenario, their responses may not represent ordinary performance. If the evaluation counts only completed trips, it can conceal stranded demand. Use complementary measures and report uncertainty and missing populations. The conclusion should separate what was observed under the trial, what is inferred under additional assumptions, and what remains a policy or risk-acceptance decision.

## Worked engineering case

Eight of ten nominal trips may succeed, but a night-event accessible-trip failure can defeat the intended mission even when aggregate completion looks respectable.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Graduate synthesis: operational evaluation of an autonomous service

### Move from component success to mission effect

A sensor may meet accuracy specification, a planner may produce collision-free trajectories in simulation, and the vehicle may pass a track test, while the *service* still fails. Operational evaluation estimates whether the configured system, personnel, environment, and procedures deliver the intended mission. Its unit of analysis must therefore include dispatch, passenger experience, accessibility, incident response, and degraded operation, not only vehicle autonomy. This is the difference between a technical performance measure and a measure of operational effectiveness.

For Northstar, define service completion as a passenger reaching an intended destination within an agreed window and without violating safety constraints. The observed fraction `p_hat = successes / eligible demands` is interpretable only if the denominator includes relevant demand and the observation window represents actual service use. Counting only accepted bookings conceals customers denied service. Excluding rainy days may be appropriate for a restricted operating envelope, but the restriction must be explicit in both the claim and authorization.

### Reason about rare events without false reassurance

Safety-critical autonomy concerns often involve events too rare to observe reliably during a short field trial. Under a simplified Poisson model for hazardous events at constant exposure rate `λ`, observing zero events in exposure `T` gives an approximate one-sided 95% upper rate bound of `3/T`. If a test accumulates 100 vehicle-hours without such an event, it supports an upper bound near `0.03 events/hour`—not evidence that a very small target, such as one in a million hours, has been met. The assumptions of event independence, stable hazard intensity, and representative exposure matter as much as the arithmetic.

Consequently, autonomy assurance must combine complementary evidence: scenario coverage, hazard analysis, formal restrictions, independent simulation, fault injection, human response evaluation, and monitored trials. Simulation can generate hazardous cases efficiently but cannot by itself validate the real-world frequency or all physical consequences of those cases. The evaluator should distinguish confidence in the controller logic from confidence in the environment distribution and sensor realism.

### Evaluate adaptation, not only nominal behavior

A useful test campaign deliberately perturbs assumptions: vehicle unavailable during a class-change peak, GNSS degradation near buildings, a wheelchair boarding interaction extending dwell time, and intermittent communications. The essential question is whether the system transitions to a controlled degraded mode with acceptable service and safety consequences. Record both the initiating disturbance and *observable recovery trajectory*: detection delay, safe-state entry, passenger notification, restoration time, and secondary congestion effects.

Operational trials produce a sample of situations, not a proof of universal safety or effectiveness. State the represented population, route configuration, season, staffing pattern, and software build. A conditional recommendation—supervised daytime pilot on mapped routes, with a stop trigger for repeated localization faults—is scientifically stronger than a generic declaration that “the autonomous shuttle works.” The evaluator's independence includes the right to challenge the underlying mission metric and the adequacy of its denominator.

## Competing explanations and failure modes

Operational adequacy is not a single pooled percentage when mission-critical strata differ. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Analyze results, determine evidence sufficiency, and recommend remedial action](10-analyze-results-determine-evidence-sufficiency-and-reco.md); the next connection is [Conduct the final evidence review and make the operational-readiness recommendation](12-conduct-the-final-evidence-review-and-make-the-operatio.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Design a scenario portfolio with ordinary, surge, degraded, accessibility and adversarial cases; name the evidence type for each.

**Problem B — Adversarial review.** What new evidence is required after changing the operational zone?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>

## Practice before the assessed course work

[Hypothetical Laboratory 11: Operational and autonomy evaluation](../labs/lab-11-evaluate-operational-use-deployed-systems-systems-of-sy.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 11 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.
