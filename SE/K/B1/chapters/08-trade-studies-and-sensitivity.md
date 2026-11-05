# Chapter 8 — A Trade Study Makes Judgment Inspectable

*EN.645.662 · Week 8. Builds on [Chapter 7](07-allocating-architecture-and-interfaces.md). Practice in [Hypothetical Lab 8](../labs/lab-08-decision-hearing.md).*

## There is no objectively best shuttle architecture

The Northstar sponsor asks for a recommendation: buy a turnkey integrated mobility system, integrate components from multiple suppliers, or build a small university-operated demonstrator. Every alternative has plausible advantages. A turnkey product may simplify initial integration but create dependence on one supplier; a multivendor design may strengthen substitutability but require more interface engineering; a local build may facilitate research but carry greater delivery uncertainty. A professional recommendation must reveal **whose objectives** are being optimized and which evidence supports each claim.

A **trade study** transforms an unstructured disagreement into an auditable decision process. It does not eliminate judgment. It makes assumptions, scales, criteria, uncertainties, and values open to scrutiny and sensitivity analysis.

## 8.1 Decide what is forbidden before deciding what is preferred

Separate **constraints** from **value criteria**. A demonstrator that cannot meet an explicitly required accessibility condition is not made feasible by scoring well on cost or flexibility. First eliminate or clearly identify infeasible alternatives. Then score remaining alternatives on agreed criteria, such as service coverage, implementation effort, reliability under defined failures, and lifecycle affordability. Constraints must have authority; otherwise a team can game the comparison by declaring its preferred architecture mandatory.

Each value scale should define what 0 and 100 mean, not simply assign attractive numbers to favorite designs. For example, “service under communication outage” might receive 0 if no defined service is possible and 100 if a particular approved subset of essential trips remains available with demonstrable safeguards. That scale depends on mission needs and evidence—it is not an objective physical constant.

## 8.2 Reproduce a weighted decision

Suppose three *feasible* teaching alternatives are scored on resilience (R), affordability (A), and maintainability (M). Proposed weights are 0.50, 0.30, and 0.20. Scores are illustrative, value-scaled judgments from 0 to 100:

| Concept | R | A | M | Weighted value |
|---|---:|---:|---:|---:|
| Central turnkey | 60 | 90 | 65 | 70.0 |
| Federated integration | 85 | 60 | 70 | 74.5 |
| Local demonstrator | 70 | 75 | 80 | 73.5 |

The simple additive calculation is \(V_j=0.50R_j+0.30A_j+0.20M_j\). For the federated concept, \(0.50(85)+0.30(60)+0.20(70)=74.5\). Under *these particular assumptions*, federated integration ranks first. That is a conditional conclusion, not proof that the design is universally best.

Weighted sums presume compensability and an appropriate interpretation of the scales. If the real decision has veto conditions or nonlinear value, this model may be misleading. Affordability and lifecycle cost also must not be counted twice under different labels.

## 8.3 Sensitivity: how fragile is first place?

To see when turnkey overtakes federated, hold maintainability weight at 0.20 while shifting weight between resilience and affordability. Let resilience weight be \(w\) and affordability weight \(0.80-w\). Then:

\[
V_F(w)=85w+60(0.80-w)+70(0.20)=62+25w,
\]
\[
V_T(w)=60w+90(0.80-w)+65(0.20)=85-30w.
\]

They tie at \(62+25w=85-30w\), giving \(w=23/55\approx0.4182\). For resilience weights below about 0.418, turnkey outranks federated; above the threshold, federated wins over turnkey. At the current \(w=0.50\), federated wins their pairwise comparison. **Important:** this is only a pairwise reversal threshold; a third candidate might rank higher at the same weight. Always rerank *all* candidates when testing sensitivity.

Now question the score evidence. If federated resilience has an uncertain score of 70–85 depending on integration maturity, its weighted total falls by as much as 7.5 points at the original weights. The apparently small 1-point advantage over the local demonstrator is then not robust. Report the uncertainty rather than concealing it behind decimal precision.

## 8.4 Pairwise comparisons and AHP are aids to judgment

An Analytic Hierarchy Process (AHP) exercise elicits relative importance through pairwise comparisons. If stakeholders say resilience is three times as important as affordability, affordability twice as important as maintainability, and resilience ten times as important as maintainability, the judgments are not perfectly multiplicatively consistent: 3×2 would suggest 6, not 10. AHP consistency calculations diagnose such tensions, but **consistency is not correctness**. A perfectly consistent set of values can still encode an ethically unacceptable preference or use poor evidence.

Record where weights came from, who participated, and what constituencies were absent. Consider the effect of stakeholder representation: operations staff may emphasize recoverability; riders may emphasize dependable accessible service; suppliers may emphasize cost and schedule. The engineering team must not pretend a single convenient weight vector came from nature.

## 8.5 What makes a decision record defensible?

A credible decision memo states: the exact choice to be authorized, the alternatives and exclusions, objective hierarchy, mandatory constraints, value scales, sources of performance estimates, uncertainties, weighting process, calculations, sensitivity thresholds, decision authority, dissent, and follow-up evidence needed. If the winner changes under plausible values, the proper decision may be to run a targeted experiment rather than force a premature commitment. A trade study can therefore recommend *what to learn next*, not only *what to buy*.

When the choice has safety, regulatory, or public-trust implications, avoid treating aggregate numerical utility as the sole authority. You may need separate assurance gates, noncompensable constraints, and explicit residual-risk acceptance.

## Deeper theory: decisions under value conflict and uncertain evidence

### Scores are measurements only when their scales mean something

A weighted trade study is a particular mathematical model of preference, not a neutral vote counter. Its familiar expression, `V(a) = Σ_i w_i v_i(a)`, combines the value of alternative `a` on criterion `i` with a declared tradeoff weight. The crucial distinction is between a *measure* such as stopping distance, a *value function* mapping that measure into desirability, and a *weight* expressing the importance of changing that desirability over a specified range. A weight of 0.3 does not mean safety contributes 30 percent of the system's physical performance. It means a particular swing on the defined safety-value scale receives 30 percent of the modeled preference weight. Unless the scale anchors and swing ranges are explicit, arithmetic precision is illusory.

Weighted addition also presumes a relevant form of preferential independence: tradeoffs on one criterion can be evaluated without their meaning changing fundamentally with the levels of the others. Consider Northstar alternatives scored separately for passenger waiting time and missed-connection rate. These may respond to the same capacity constraint, so counting them as unrelated benefits can double reward dispatch capacity. Correlation in *observed outcomes* is not alone proof of invalid preferences; the question is whether the criteria represent distinct consequences stakeholders care about. If “accessibility” is also a mandatory obligation, however, compensating a failure to serve wheelchair users with better average journey time is unacceptable. Apply feasibility and noncompensatory constraints before calculating compensatory scores.

### Robust choice is different from choosing the largest mean

Suppose two designs have normalized value estimates of 0.74 and 0.71. The apparent winner may reverse if one criterion's weight changes slightly, if the tested demand profile excludes an evening surge, or if a vendor's reliability claim is only a point estimate. Keep *value uncertainty* (what decision makers prefer) separate from *performance uncertainty* (what the alternatives will do). Denote uncertain parameters by `θ` and stakeholder weights by `w`. The result is not one magical score but a family `V(a; θ, w)`. A useful decision record states the region of plausible `(θ,w)` in which each option is preferred and identifies the assumptions responsible for reversals.

Dominance offers a stronger conclusion than a narrow score difference. If alternative A is no worse than B on every relevant criterion and strictly better on at least one, B is Pareto-dominated under monotonic preferences; no arbitrary weighting is required to discard it. Where alternatives cross, the Pareto frontier exposes real conflicts instead of concealing them inside one rank. Under uncertainty, a robust alternative may have slightly lower expected value yet avoid catastrophic shortfalls over credible operating conditions. Expected utility, worst-case analysis, regret, and chance constraints answer different questions; selecting one is itself a governed decision.

### Evidence can have more value than immediate commitment

A trade study is often conducted when the best action is to learn rather than buy. Imagine that two control architectures differ principally in whether the campus network can support a required emergency-status latency. A targeted network test may change the ranking; polishing weights will not. In decision-theoretic language, the *expected value of sample information* is the expected value of the best decision after observing test results, less the value of the best decision without that information. It is nonnegative before test costs under coherent assumptions, but the net gain may be negative once the experiment's cost and delay are included.

The value of a test depends on whether it could change the action. Measuring an easy, low-impact characteristic with great precision may create a strong-looking report without resolving the decisive uncertainty. Conversely, discovering that a candidate violates an absolute safety constraint can settle a decision despite wide uncertainty elsewhere. The Northstar decision record should therefore preserve the feasibility screen, value-scale definitions, sensitivity ranges, decisive evidence gaps, and authority to accept remaining risk. That makes a recommendation revisable when conditions change rather than a ranking frozen in a spreadsheet.

## 8.6 Practice with explained answers

**A. Calculate.** Central turnkey's score is \(0.5(60)+0.3(90)+0.2(65)\). **Answer:** 70.0.

**B. Interpret.** What does \(w\approx0.418\) mean? **Answer:** The pairwise federated-versus-turnkey ranking flips at that resilience weight with maintainability fixed at 0.20 and affordability taking the remaining weight; it is not a general optimum.

**C. Audit.** A proposed criterion is “technical quality,” weighted at 40%. What's wrong? **Answer:** It needs an operational definition and value scale; it likely overlaps resilience, service, and maintainability, encouraging double counting.

**D. Challenge.** An alternative fails a mandatory accessibility condition but gets the highest aggregate score. **Answer:** It is infeasible under the decision's approved constraints; do not compensate away the violation.

**E. Learn.** What experiment would reduce uncertainty in federated resilience? **Answer:** Define an interface-disruption scenario, representative assumptions, a measurable degraded-service metric, and a decision threshold before executing a prototype test.

## Read, rehearse, produce

Use [Hypothetical Lab 8](../labs/lab-08-decision-hearing.md) to defend a recommendation before a simulated board. Then prepare the full original Week 8 `662_W08_TradeStudy_v1.0`, including AHP consistency checking and multiple sensitivity methods. The book's toy numbers teach method, not the answer to the assessed assignment.

**Next:** [Chapter 9 — Technical management](09-managing-the-technical-baseline.md).


### A trade study is a model of preference, not a machine for truth

A weighted score appears objective because its arithmetic is reproducible, yet its result depends on judgments embedded in criteria, measurement scales, normalization, and weights. Weighting “safety” and “cost” is meaningful only after non-negotiable safety constraints are removed from the trade space. Otherwise the model can imply that sufficiently low cost compensates for an unacceptable hazard. Feasibility and desirability are logically distinct operations: first rule out alternatives that violate hard limits, then compare those that remain.

Weights also require an interpretation. A ten-point improvement in one criterion need not be commensurate with ten points in another. If the value functions are nonlinear, a raw weighted average can conceal diminishing returns or thresholds. The intellectually honest output of a trade study is therefore not only a winning concept but a map of **conditions under which that preference changes**. Sensitivity analysis examines those conditions. If a small, defensible change in a weight reverses the decision, the analysis has revealed a fragile preference, not failed to identify a unique answer.

## Extended worked problems and lab

Study the [worked problem workshop on architecture choice and reversal](../practice/trade.md), then complete the [extended laboratory](../practice/lab-trade.md). The exercises are separate from the original assessed coursework.
