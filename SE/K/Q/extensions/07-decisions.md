## Step 04 integrated case — constrained preferences are not feasibility evidence

The NS-QSE4.1 dispatch decisions compare four policies using conditional queue outputs and **declared hypothetical costs**. Status quo has two servers and a ten-minute service time; capacity adds a server for $90/day; process reduces service duration to eight minutes for $45/day; combined does both for $130/day. These costs do not represent procurement quotes or operational budgets. The case assigns scenario weights of 0.55 clear, 0.30 storm, and 0.15 compound. They are **decision weights chosen for an illustrative expected-value calculation**, not estimated scenario frequencies.

### Derive an expected disutility rather than hide a value judgment

For policy \(a\) in scenario \(s\), let \(\bar W_{as}\) be **request-weighted mean queue wait in minutes**, \(\bar N_s\) the mean number of requests per intake window, and \(c=\$12/(\text{request}\cdot\text{minute})\) an illustrative delay penalty. Let \(C_a\) be the synthetic added daily policy cost. The chosen score is

\[
J(a)=C_a+\sum_{s\in\{c,s,x\}}p_s\,c\,\bar N_s\,\bar W_{as}.
\]

This formula keeps units in dollars per compared window, but translating a daily cost into a single-window comparison assumes one such window per day. It also ignores displacement, service quality, access, working conditions, and tail-risk externalities; a low score cannot erase those omissions. The reproducible values are approximately **$2,631.23** status quo, **$988.19** capacity, **$1,638.63** process, and **$552.68** combined. Thus combined minimizes **this** synthetic expected score.

### Apply hard constraints *before* recommending a design

The controlled case separately requires at least **90% of requests to wait no more than 12 minutes in every scenario**. Under compound stress, timely fractions are approximately 23.48% status quo, 56.82% capacity, 37.50% process, and **82.95% combined**. None clears the rule. Therefore the lowest expected-cost score yields **no eligible deployment option**. The correct output is an infeasibility or HOLD decision with a revised design/evidence plan, not automatic adoption of the numerical winner.

A Pareto analysis would retain alternatives not dominated on relevant dimensions such as added cost, wait, overtime, accessible completion, and operator workload. The current example has no modeled accessibility discipline or labor-quality measure, so a formal Pareto frontier over those real objectives cannot be claimed. Optimizing solely against \(J\) would imply unapproved trade-offs; stakeholder acceptance, privacy, safety and operational authority are explicit evidence gates.

### Uncertainty and value of information

Before valuing new measurements, identify decisions that could change when a parameter is updated. The storm-weight assumption is a strong candidate: a change in scenario prevalence changes the expected disutility, but the hard compound-screen failure remains. Value of information is upper-bounded by the difference between the best expected decision with perfect scenario knowledge and the current best expected decision **within the same feasible alternative set**. Here the operational feasible set is empty, so a numerical perfect-information computation over the unconstrained four-policy set would not solve the actual readiness problem. Investment in missing field evidence, accessible-service design and safety approval may be more valuable than refining the queue mean.

<details><summary>Worked exercises and interpretation</summary>

1. **Feasibility.** Combined has an approximately 82.95% timely fraction under compound stress; the target is 90%. The shortfall is **7.05 percentage points**, not 7.05% relative, and a good weighted score cannot cancel it.
2. **Simple value calculation.** For two hypothetical options, A costs $100 and incurs 20 request-minutes at $12 each; B costs $180 and incurs 10 request-minutes. Then \(J_A=100+240=\$340\) and \(J_B=180+120=\$300\), so B wins *if* those are the only objectives and both are eligible.
3. **Sensitivity.** Increasing the compound scenario weight without renormalizing the remaining weights is invalid. Reallocate weight and recompute the score. Hard screening still rejects a policy that misses the compound threshold, regardless of the assigned weight.

</details>

**Decision memorandum rule:** State the objective, units, weights, hard constraints, missing stakeholder values, alternative configurations, and whether evidence authorizes the selected use. The release's disposition is **HOLD**, not procurement guidance.
