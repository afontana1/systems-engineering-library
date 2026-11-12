# Chapter 8 — Resources and optimization

*Book 6: System Conceptual Design · Week 8 — Resource, affordability, schedule, feasibility, and optimization models*

> **Reading route:** Study this chapter → attempt [Hypothetical Laboratory 8](../labs/lab-08-resource-affordability-schedule-feasibility-and-optimiz.md) without looking at the solution → return to [Week 8 of the course guide](../../../C/P2/EN645767.md) for the independent assignment and rubric. The [short Phase 2 primer](../../P2-text/lessons/645-767-w08.md) is optional review, not the primary reading.

## The engineering problem

At this point the Northstar team is still free to select among competing mobility-service concepts. A proposed autonomous shuttle is one hypothesis, not the definition of the problem. The governing question this week is **resources and optimization**. Decisions in this course are cumulative: an assumption made now will reappear as an allocation, a test condition, or a readiness limitation later. Always preserve the exact scenario, configuration and affected stakeholder when making a claim.

One of the most useful distinctions in systems engineering is the difference between a *claim*, a *model*, and *evidence*. A claim says what must or does hold. A model explains or predicts behavior under named conditions. Evidence is a measured or inspected outcome from a known configuration. Moving among these three without recording assumptions produces false confidence even when all calculations are correct.

## Build the intuition

Resource models put physical units and time windows around a concept. A mathematical optimum is meaningful only inside its constraints and assumed operating regime. Separate energy feasibility from charger simultaneity, electrical peaks, workforce needs, and schedule risk.

There are two levels of reasoning. At the local level, ask whether the calculation, drawing, allocation, or test is internally correct. At the mission level, ask whether that local statement actually changes the stakeholder's decision. The distinction prevents a common mistake: optimizing a subsystem characteristic while harming the system-level outcome. In this case, an apparently efficient dispatch plan can be unacceptable if it systematically excludes accessible requests during event surges.

A second discipline is to make the operating envelope visible. State the load, timing, participants, environmental assumptions, failure modes and decision authority. If the result depends on a parameter you have not measured, classify it as *conditional*. An uncertainty is not automatically a defect, but unexplained certainty is one.

### Resource feasibility precedes attractive optimization

Optimization is meaningful only after the decision variables, constraints, and objective are expressed in compatible terms. A fleet size may be an integer, charger capacity a continuous power limit, and passenger wait a random outcome dependent on a demand process. Treating all three as interchangeable scores obscures feasibility. A concept that cannot recharge during its actual duty window is infeasible regardless of its aesthetic appeal or nominal operating cost.

The mathematical model is a deliberately simplified picture of a coupled system. A constraint like energy demand less than usable stored energy is necessary but may omit charging contention, aging, cold-weather losses, and reserve policy. Enlarging a constraint set is not automatically better: overly conservative bounds can eliminate useful options. The engineer should make each exclusion traceable to a physical limit, contractual obligation, or explicitly stated uncertainty policy. Only then do objective functions and sensitivity studies answer a meaningful concept-selection question.

## Worked engineering case

Thirty-two vehicles × 60 kWh = 1,920 kWh recharge. At 1,200 kW the ideal energy-only window is 1.6 h; at 75% usable charging capacity it becomes about 2.13 h, still excluding individual charge limits and scheduling.

**Reason through the case in this order:**

1. **Frame the decision.** What is the mission claim being evaluated? State who accepts or rejects the conclusion.
2. **List supplied information.** Label each number or statement as requirement, observation, assumption, or estimate; name the units.
3. **Check structure and arithmetic.** Show the formula, interfaces, event chain, or causal link; verify that numerator, denominator, configuration and time window agree.
4. **Challenge the favorable interpretation.** Identify a plausible failure or operating condition that could reverse it. If a case includes a conditional probability or a percentile, do not promote it into a universal guarantee.
5. **Select the next evidence.** Write a measurement or review criterion that could change your decision, rather than an activity with no pass/fail interpretation.

These steps do not automatically prove the design. They prevent a correct local calculation from being offered as a conclusion about unmeasured system behavior. When assumptions are uncertain, calculate sensitivity or state the required experiment instead of inventing precision.

## Competing explanations and failure modes

A correct energy total is not proof of grid, charger, or operational feasibility. This is why reviewers must distinguish *unknown* from *failed*, and *not applicable* from *not tested*. A robust decision record preserves an alternative hypothesis, the evidence needed to discriminate it, and the owner of that next investigation. Ask what would happen if the controlling requirement changed, a data feed became stale, or an operational context moved outside the model boundary.

## How this connects to the next part of the lifecycle

In the **concept** stage, design freedom is preserved and choices are screened against needs and feasibility. In **design and integration**, provisional choices become owned interfaces and controlled budgets. In **test and evaluation**, those statements become hypotheses tested against configurations and populations. Keeping this chain visible matters more than using the same document format across teams.

Your prior connection is [Generate physical concept families with morphological and set-based methods](07-generate-physical-concept-families-with-morphological-a.md); the next connection is [Objectives, value functions, and multiattribute evaluation](09-objectives-value-functions-and-multiattribute-evaluatio.md). Treat this chapter as a bridge between them, not a standalone checklist. In the final review, someone must be able to reconstruct how a stakeholder need became a claim, why an option was chosen, what was actually implemented and which evidence supports operation.

## Try the reasoning yourself

**Problem A — Construct the decision.** Create energy, charger-count and staffing constraints for two fleet concepts; label every idealization.

**Problem B — Adversarial review.** Which bottleneck appears when vehicles arrive at chargers together?

**Problem C — Evidence and limitation.** Propose one test or analysis with an acceptance criterion, a configuration identifier, a limit on generalization and a named decision owner. Explain what you would do if the result were borderline.

<details><summary>Worked answer guidance (look only after trying)</summary>

For **A**, produce the requested artifact with stable identifiers, explicit scenario assumptions and at least one exceptional condition. The answer is acceptable only if someone else could reconstruct the logic; plausible words alone are insufficient.

For **B**, evaluate the question against the actual mission, not just the subsystem metric. An answer must name the stakeholder affected and a plausible mechanism by which the current interpretation could fail.

For **C**, use a controlled artifact and a predeclared decision rule. A measured result can support only the specified configuration, environment and sampling conditions. Where that evidence does not yet exist, mark the claim *open* and assign a closure action rather than marking it *pass*.

</details>


## Graduate depth: resource feasibility as constrained optimization
### An attractive concept can lie outside the feasible set

Concept selection should begin by separating hard constraints from preferences. Define design variables `x`, resource use `r(x)`, and required performance `g(x)`. A generic feasibility problem seeks an `x` satisfying constraints such as `r_k(x) <= B_k` and `g_j(x) >= threshold_j`, where the functions may be nonlinear and uncertain. Only feasible concepts should then be compared for value. A weighted score can rank alternatives, but it cannot make an architecture feasible when a mandatory power, cost, safety, or timing limit is violated.

Resources are not all fungible. Money cannot directly replace charging capacity during a constrained operating window; adding engineers does not substitute for a limited environmental test chamber; additional batteries may exceed axle-load or thermal limits. Resource models should therefore preserve units, concurrency, replenishment rates, shared bottlenecks, and time profiles. A scalar total energy budget is insufficient when peak power, charging turnaround, and duty cycle determine whether a mission can be performed.

### Optimization is only as credible as its constraints

In a hypothetical Northstar concept comparison, let `x` describe fleet size, battery capacity, charge locations, and operating policy. The objective might minimize expected annual cost subject to response-time and availability targets. A simple expression, `min_x C_capital(x) + E[C_operating(x,omega)]`, hides scenarios `omega` for demand, weather, equipment failure, and energy price. If the selected plan meets requirements only for average demand, the optimization has not addressed its true operational risk.

Shadow prices can clarify tradeoffs in continuous constrained models. If a resource constraint is binding, its associated Lagrange multiplier roughly measures how much the optimum objective would improve from a small relaxation, under regularity and local sensitivity assumptions. This is useful for asking whether another charging bay or additional network capacity would have high marginal value. It is not a reliable global value when decisions are discrete, feasibility changes abruptly, or constraints are nonconvex.

### Robustness and learning are separate design objectives

A deterministic optimum often sits close to a boundary because unused margin looks expensive. Under uncertainty, a small modeling error may make that solution unacceptable. Chance constraints such as `P(g_j(x,omega) >= threshold_j) >= 1 - alpha` express tolerance for violation risk, but they require defensible distributions and an agreement about whether rare severe outcomes can be averaged. For safety-critical constraints, worst-case or scenario-bounded reasoning may be more appropriate than choosing an arbitrary small `alpha`.

Sensitivity analysis changes one or more assumptions to see whether the preferred concept survives. However, extreme-scenario testing differs from assigning probabilities to scenarios; stakeholders should not confuse the two. When an expensive technology uncertainty dominates the decision, the engineering value may lie in a small prototype that reveals real efficiency before committing to an architecture. The conceptual baseline should preserve the feasible set explored, constraint definitions, exclusion rationales, key uncertainty drivers, and the evidence needed for down-selection. This turns optimization into a transparent decision process rather than a black-box answer.

## Practice before the assessed course work

[Hypothetical Laboratory 8: Resources and optimization](../labs/lab-08-resource-affordability-schedule-feasibility-and-optimiz.md) provides a fictional rehearsal distinct from the assessed course project. Complete its decision memo and peer-review checklist first, then return to the actual guide's Week 8 deliverable and mastery gate. The course guide also retains its authoritative reading and source references; the companion does not replace those references or claim to be an independently validated technical standard.


## Step 03 integrated reference: NS-CD6.1 — affordability, schedule and constraint-first optimization

Concept evaluation often fails when a cheap alternative is assigned a large weighted value despite violating nonnegotiable requirements. The NS-CD6.1 screen uses peak capacity at least 46.2 effective trips/h, p90 wait no more than 12 minutes, access coverage at least 95%, capital no more than $3.0M and annual operations no more than $1.2M. All five checks are required before computing a preference ranking. The [machine-readable baseline](../case/model-baseline.json) makes those rules executable.

### Nominal cost is not lifecycle affordability

Assume one acquisition payment at time zero, identical real end-of-year operating expense in each of five years, and a real discount rate of 5%. The present-value annuity factor is

\[F_5=\sum_{t=1}^{5}(1.05)^{-t}\approx4.32948,\qquad LCC=CAPEX+F_5(OPEX).\]

For the hybrid C, \(LCC_C=2.25+4.32948(0.98)=\$6.493\) million. For pooled B, \(LCC_B=2.70+4.32948(1.12)=\$7.549\) million. D's simpler acquisition produces a lower nominal five-year cost (approximately $5.812M) but **does not satisfy the declared service and affordability screens**. This comparison is intentionally limited: it excludes replacement cycles, taxes, inflation, salvage, externalities and quantified risk. A realistic cost model requires those terms and an uncertainty range.

### Schedule as a dependency network

The concept pilot has tasks A framing (2 weeks); B supplier engagement (3 weeks after A); C simulation and accessible-service design (4 weeks after A); D integrated review (2 weeks after B and C); and E pilot preparation (3 weeks after D). Earliest finishes are A=2, B=5, C=6, D=8, E=11 weeks. The critical path is A→C→D→E, totaling **11 weeks**. A one-week delay in B does not initially move E if B still finishes by week 6. A one-week delay in C directly moves E to week 12, absent recovery. This is deterministic precedence analysis; duration variability needs separate treatment.

### Exercise and solution

**Exercise:** Finance proposes dropping C in favor of D because D costs less over five years. What is the correct answer? **Answer:** D is infeasible under current hard requirements: 45 < 46.2 trips/h, 12.4 > 12 minutes p90 wait, and $1.25M > $1.20M annual OPEX. A weighted or discounted cost advantage cannot erase failed constraints. Instead request a revised supplier proposal or documented requirements change with stakeholder authority. Use [the concept table](../case/concepts.csv) to make every violation explicit.

**Boundary:** These are point-estimate financial and scheduling exercises. Procurement, stakeholder acceptance, cost contingency and schedule confidence require independently sourced inputs before any investment approval.
