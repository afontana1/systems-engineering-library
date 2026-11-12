# Pareto search, scenario regret, and robust design decisions

*Technical method guide · Multiobjective optimization, constraints, sensitivity, and decision policy · Phase 2 expansion*

**What this guide enables.** Distinguish feasible design sets from Pareto-efficient candidates, calculate scenario losses and regret, compare expected-loss and minimax-regret decisions, and test whether the selected engineering alternative remains defensible when assumptions change. All candidate designs and monetary equivalents are synthetic.

**Prerequisites:** [Engineering trades](../encyclopedia/engineering-trades.md), [Pareto analysis](../encyclopedia/pareto-and-value.md), [robust optimization and margins](../encyclopedia/robust-optimization-and-margins.md), and [Bayesian decisions](bayesian-decision-handbook.md).

## 1. Start with constraints; do not hide them inside arbitrary weights

Let the design vector be \(x\in X\), where \(X\) contains actual implementable configurations, not diagrams of nonexistent alternatives. A conventional single-objective formulation is

\[
\min_{x\in X} f(x)\quad\text{subject to}\quad g_i(x)\le 0,\;h_j(x)=0.
\]

In systems engineering, \(g_i\) may encode response-time limits, energy budgets, minimum coverage, regulatory constraints, or an architecture policy. A candidate that violates a binding safety requirement must not be made acceptable simply by multiplying safety by a low weight. First distinguish **hard constraints**, negotiable preferences, and uncertain requirements. Record any exception authority and the verification evidence for each constraint.

For multiple objectives, \(f(x)=(f_1(x),\dots,f_m(x))\), there is generally no single natural best vector. A design \(x\) **dominates** \(y\) for minimization if every objective for \(x\) is no worse and at least one is strictly better:

\[
\left[\forall j,\;f_j(x)\le f_j(y)\right]\land
\left[\exists j,\;f_j(x)< f_j(y)\right].
\]

The **Pareto set** is the collection not dominated by another evaluated feasible candidate. Pareto efficiency is not proof that a design is affordable, good, or stakeholder-approved. It only says there is no currently evaluated alternative that improves at least one selected objective without worsening another.

## 2. A six-design engineering trade with three operating scenarios

The Northstar team compares six hypothetical shuttle dispatch designs. Capitalized expenditure is represented as cost \(C\) in **thousands of dollars**, energy use as kWh per mission, and mean dispatch delay under three scenarios in **seconds**. Lower is preferred for all three, but cost and energy measure different consequences from delay. The expected-delay model assigns probabilities 0.6, 0.3 and 0.1 to nominal, peak, and disruption conditions; these are *planning assumptions*, not measured frequencies.

| Design | Cost ($k) | Energy (kWh) | Nominal delay (s) | Peak delay (s) | Disruption delay (s) |
|---|---:|---:|---:|---:|---:|
| A | 120 | 65 | 5.5 | 7.0 | 9.0 |
| B | 135 | 58 | 4.8 | 6.0 | 7.5 |
| C | 142 | 54 | 4.6 | 5.9 | 7.2 |
| D | 115 | 73 | 5.8 | 7.4 | 10.2 |
| E | 150 | 52 | 4.2 | 5.7 | 6.9 |
| F | 155 | 60 | 5.1 | 6.5 | 8.1 |

Define objective vector \(f(x)=[C(x),E(x),\max_s D(x,s)]\): capital cost, energy and worst-scenario delay. Design **F is dominated** by B, C and E; for example B costs less (135 versus 155), uses less energy (58 versus 60) and has a better worst delay (7.5 versus 8.1). Designs A–E are mutually nondominated in this *evaluated candidate set*. They constitute a sampled trade frontier, not necessarily the globally optimal frontier over all possible designs.

An engineering owner might impose \(\max_s D(x,s)\le 8.0\) seconds. Then A, D and F are **infeasible**; B, C and E remain. This is a robust, *all three modeled scenarios* constraint. It does not certify the design for unmodeled disruptions or measurement uncertainty. The [candidate dataset](data/design-trade-scenarios.csv) and [analysis program](code/robust_trade.py) calculate dominance and feasibility explicitly.

## 3. Expected value and regret can prefer different designs

To illustrate a *decision* rather than merely an optimization vector, assume a stakeholder-endorsed monetization of **$10,000-equivalent loss per second of mean delay**. Define for each scenario \(s\)

\[
L(x,s)=C(x)+10D(x,s)\quad[\$\text{ thousands equivalent}],
\]

where \(C\) is also in thousands of dollars. This coefficient is a **hypothetical preference or consequence model**: it is not a financial law. Energy remains a separately reported objective and possible constraint; omitting it from \(L\) must be an explicit decision, not an unnoticed disappearance of value.

The expected loss given the assumed scenario probabilities is

\[
E[L(x,S)]=\sum_s p_s L(x,s).
\]

For D, the expected delay is \(0.6(5.8)+0.3(7.4)+0.1(10.2)=6.72\) seconds, so \(E[L(D,S)]=115+10(6.72)=182.2\) thousand-equivalent units. For A the expected loss is \(120+10[0.6(5.5)+0.3(7.0)+0.1(9.0)]=183.0\). D therefore has the lowest expected loss *among all six options* under these probabilities, despite its poor disruption performance.

Regret instead compares a decision to the best that **could have been chosen if the scenario were known**:

\[
R(x,s)=L(x,s)-\min_{y\in X}L(y,s).
\]

Using all six candidates as the comparator set, D has losses \([173,189,217]\), while A has \([175,190,210]\). The scenario-by-scenario best losses are \([173,189,210]\), giving **D regrets \([0,0,7]\)** and **A regrets \([2,1,0]\)**. The minimax-regret policy

\[
\min_x\max_s R(x,s)
\]

chooses **A** (maximum regret 2), while expected-loss minimization chooses **D** (expected loss 182.2). Neither method is inherently universally correct: they implement *different decision principles*. If the 8-second hard constraint is applied, both A and D leave the feasible set, and the comparison must be recomputed **within B, C, E**, not treated as if the original recommendation survived unchanged.

## 4. Robust optimization is more than taking a worst row of a table

Robust optimization makes uncertainty part of the design formulation:

\[
\min_{x\in X}\max_{u\in\mathcal U} L(x,u)
\quad\text{subject to}\quad g_i(x,u)\le0\ \forall u\in\mathcal U.
\]

Here \(\mathcal U\) is an explicitly justified **uncertainty set**: scenarios, uncertain physical parameters, bounded coefficients, or structured disturbances. A very wide set can make solutions prohibitively conservative; a narrow set can conceal credible failures. A probability-based alternative is a chance constraint such as \(P(g(x,U)\le0)\ge 0.99\), but that requires a defensible probability model. A scenario list alone cannot justify a 99% chance-constrained guarantee.

Optimization reports should name (a) the candidate generator, (b) the feasibility checks, (c) the evaluation model and its validity region, (d) uncertainty representation, (e) scaling/normalization of objectives, and (f) search stopping and approximation error. For computational optimization, store seeds, executable version, constraints, input units and solver tolerance. Use an independent re-evaluation of a selected candidate rather than trusting only the surrogate that found it.

**Sensitivity is a decision test.** The expected-loss ranking here depends on the assumed probabilities and $10k/s consequence conversion. Increasing the disruption probability from 0.1 to 0.3 while reducing the nominal probability from 0.6 to 0.4 raises D's expected loss more than A's because D is particularly poor under disruption. Examine the point at which the choice changes; a policy based on a knife-edge assumption should be escalated for more information or better architecture design.

## 5. When a weighted sum does and does not help

A weighted objective \(J(x)=\sum_j w_j\tilde f_j(x)\) can be useful after selecting **units, normalization, decision scales and weights**. A raw addition of milliseconds, kWh and dollars is meaningless. Even with proper normalization, choosing weights after observing which candidate wins can mask advocacy as analysis. Weighted sums can fail to reveal nonconvex parts of a continuous Pareto frontier; alternatives such as epsilon-constraint search or reference-point methods may be preferable.

A design trade should separate *facts about alternatives* from *stakeholder preferences*. Measured cost, energy and latency with uncertainty are engineering claims. Their relative desirability depends on value elicitation, affordability, mission needs and accountable decision authority. A Pareto chart can simplify conversation, but it cannot replace that conversation.

## 6. Evidence, limitations, and exercises

The small program [robust_trade.py](code/robust_trade.py) computes the full Pareto set, scenario losses, expected loss, maximum regret, and robust feasibility. It uses ordinary Python and no optimization library. It is exhaustive over the six given designs; it **does not search continuous architecture space** or guarantee a globally efficient solution.

For review, ask whether scenarios span plausible threats; whether constraints are actually verified; whether model outputs have uncertainty intervals; whether correlated failures were considered; whether the preferred design changes under reasonable probability or weight perturbations; whether all stakeholders accepted the loss conversion; and whether the actual implemented design preserves modeled properties.

**Exercise A:** impose \(\max_s D(x,s)\le 8.0\) and compute expected loss and maximum regret using only B, C and E; explain why the original expected-loss winner is no longer eligible.

**Exercise B:** increase disruption probability to 0.3 and reduce nominal to 0.4; recompute expected losses. State which assumptions require evidence before any project decision.

## 7. Derive the decision-switching threshold

The expected-loss comparison between A and D is close enough that uncertainty about operating conditions matters. Let disruption probability be \(q\), hold peak probability at 0.3, and allocate the remainder \(0.7-q\) to the normal scenario, with \(0\le q\le0.7\). The loss difference between D and A is

\[
\begin{aligned}
E[L(D,S)-L(A,S)]
&=(115-120)+10[(0.7-q)(5.8-5.5)\\
&\qquad+0.3(7.4-7.0)+q(10.2-9.0)]\\
&=-5+10(0.33+0.9q)=-1.7+9q.
\end{aligned}
\]

The switch occurs at \(q^*=1.7/9\approx0.1889\). For \(q<q^*\), D has lower assumed expected loss; for \(q>q^*\), A does. At the original \(q=0.1\), the difference is \(-0.8\) thousand-equivalent units. Increasing disruption to \(q=0.3\) while reducing normal operation to 0.4 changes that difference to \(+1.0\). The selected design flips without a single engineering performance estimate changing—only the scenario probabilities changed.

This is the purpose of **switching-value analysis**: identify the input assumption at which the recommendation reverses. The threshold is not itself evidence that the scenario probabilities are correct. It tells the team what operational data would be valuable to collect and what assumptions deserve management review. If the hard worst-scenario delay constraint is binding, both A and D are infeasible regardless of this threshold, so the switching analysis is a *conditional comparison* rather than the final choice.

## 8. Distinguish empirical dominance from robust dominance

Suppose predicted peak delay has a credible interval or range rather than one exact point. Point-estimate dominance may disappear when the estimates overlap and each design is evaluated under the same adverse conditions. A **robust dominance** claim needs a clearly defined uncertainty set and must hold for every included state or parameter realization. If \(f_j(x,u)\) varies with \(u\), checking \(f_j(x,u_0)\le f_j(y,u_0)\) only at nominal \(u_0\) does not establish robust dominance.

A physically grounded study may use a model of demand, sensor outages, or battery degradation to generate common scenarios for each design. Keeping *common random numbers* across simulated alternatives can reduce the variance of pairwise differences; however, it must be recorded as paired simulation evidence, not misrepresented as independent observations. For expensive multiobjective simulations, surrogate prediction errors should be measured on withheld designs, with promising candidates reevaluated using the original high-fidelity model.

**Stakeholder values and risk attitude are distinct from the design data.** An alternative can be Pareto-efficient and still undesirable because it has poor risk concentration, difficult maintenance, unquantified compliance burden, or weak provenance. Extend the objective vector only when a property is genuinely decision-relevant and operationally measurable. Otherwise present it as a qualitative constraint or review issue, not a made-up weighted numerical score.

## 9. A decision record suitable for later audit

A final trade report should preserve: the purpose and authority of the decision; design and performance assumptions; input units; data or model versions; scenario probabilities and their source; constraint thresholds and margins; which designs are infeasible or dominated and why; the preferred decision principle; the switching values; and a dissent/uncertainty log. If downstream requirements change, this record enables a fresh trade without reconstructing the original rationale from presentation slides.

The static [trade evaluator](code/robust_trade.py) supplies a small reference implementation. Modify its probability arguments and feasible-set constraint, then compare results against the algebra above. Real architecture optimization requires an appropriate solver and independent technical review; the program intentionally makes no claims of general solver optimality.


### Sources and curriculum connections

- [NIST Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook) for experiment design, response surfaces and uncertainty interpretation.
- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) for technical trades, decision rationale and lifecycle evidence practice.
- [Book 14, Chapter 4 — Constraints and Pareto](../B14/chapters/04-apply-constraints-dominance-and-pareto-analysis-to-the-selection-pro.md), [Chapter 8 — Multiobjective search](../B14/chapters/08-formulate-parametric-design-and-conduct-multiobjective-search.md), [Chapter 11 — Uncertainty and regret](../B14/chapters/11-analyze-uncertainty-sensitivity-robustness-regret-and-value-of-infor.md).
- **Curriculum:** EN.645.784 (weeks 4, 8 and 11), EN.645.767 (concept trades), EN.645.756 (sensitivity and technical margin).
