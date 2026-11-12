# Optimization, preferences and value of information

*Textbook-depth conceptual sequence · EN.645.784 / EN.645.632 / EN.645.767 · Northstar engineering case*

**Prerequisites:** basic algebra, unit discipline, structured requirements and probability as appropriate. **Related books:** [Book 14](../../B14/OPEN-BOOK.html), [Book 9](../../B9/OPEN-BOOK.html), [Book 6](../../B6/OPEN-BOOK.html).

> **Learning outcome:** derive the central method, state its assumptions, evaluate a worked engineering claim, and explain where the conclusion would fail.

## A mathematically optimal answer can still be the wrong decision

Systems engineering uses models to choose among constrained alternatives, not just to maximize a convenient score. Start by stating the decision-maker, alternatives, consequences, feasible constraints, stakeholder preferences and uncertain states of the world. A weighted score is meaningful only after clarifying which attributes can compensate for others. Safety thresholds, legal requirements, accessibility commitments and minimum service levels often belong in the feasibility set, not in a weighted sum where poor performance can be bought off by low cost.

Let alternative x have cost \(C(x)\), mean wait \(W(x)\) and coverage \(G(x)\). A constrained decision might minimize \(C(x)+\lambda W(x)\) subject to \(G(x)\ge0.90\), battery feasibility and a maximum incident risk. Changing \(\lambda\) explores the value assigned to waiting, but does not relax the coverage threshold. Different stakeholders may disagree about the tradeoff parameter. Make that disagreement visible instead of hiding it inside an apparently neutral mathematical formula.

## Pareto dominance and value scales

An alternative is Pareto-dominated if another feasible alternative is no worse on every objective and strictly better on at least one. Dominated choices can generally be set aside for the specified attributes and feasible set. Nondominated choices require preferences or additional evidence. Normalizing cost and quality values to 0–1 does not magically make them commensurable. A score depends on anchor definitions, directionality, treatment of nonlinearity and chosen weights.

Consider two feasible designs A and B with normalized cost merit 0.8 versus 0.5, and service merit 0.6 versus 0.9. With cost weight w, their scores are \(U_A=0.8w+0.6(1-w)=0.6+0.2w\) and \(U_B=0.5w+0.9(1-w)=0.9-0.4w\). Setting them equal gives \(w=0.5\). A is preferred for \(w>0.5\), B for \(w<0.5\). This reversal threshold is often more informative than a single recommendation based on a 0.6 weight. It exposes where stakeholder discussion, not additional algebra, is needed.

## Uncertainty-sensitive and robust choices

Expected utility uses probabilities over uncertain states and a utility function reflecting stakeholder preferences and consequences. It is appropriate only when both probabilities and utilities are sufficiently justified. If scenario probabilities are poorly supported, sensitivity ranges, worst-case feasibility, minimax regret, or distributionally robust methods may be more credible. These methods answer different questions: minimizing worst-case loss can select a conservative alternative that is not highest expected-value. There is no universal numerical objective for all missions.

Suppose two configurations A and B have payoffs (in arbitrary benefit units) across normal and disrupted conditions: A = (100, 20), B = (75, 60). With probability of disruption p, \(E[A]=100-80p\), \(E[B]=75-15p\). Equality occurs at \(100-80p=75-15p\), or \(p=25/65\approx0.3846\). If the outage probability is uncertain between 0.2 and 0.5, the preferred expected-value alternative is not robust to that probability. That is a decision-relevant uncertainty to investigate.

## Value of information

Information is valuable only if it changes an action or reduces expected loss. With payoff matrix as above and disruption probability p=0.3, choose A without new information because \(E[A]=76\) and \(E[B]=70.5\). With perfect information before choosing, choose A in normal conditions (100 vs 75) and B in disrupted conditions (60 vs 20). Expected value under perfect information is \(0.7(100)+0.3(60)=88\). Thus \(EVPI=88-76=12\) benefit units. This is an upper bound on the expected net benefit of **any** information-gathering exercise under the specified model. A proposed test costing 15 units cannot be justified solely by this decision value; a test costing 5 might still be worthless if it rarely changes the decision. Real tests supply imperfect information and require likelihood models.

## Decisions are evidence chains

A defensible trade study records source versions, feasibility gates, scoring rules, uncertainty bounds, model validation status, the chosen alternative and why rejected alternatives failed. When a design changes, re-evaluate the trade; do not reuse a ranking from a prior requirement baseline. Prefer a documented decision under visible uncertainty to a polished optimization chart that cannot be reproduced.


## Further depth: decision trees and imperfect evidence

Perfect information is a theoretical benchmark. A real test emits noisy positive or negative signals. Let \(H\) denote a disrupted operating environment and \(Y\) a positive test signal. The test is characterized by sensitivity \(P(Y+\mid H)\) and specificity \(P(Y-\mid\neg H)\). Bayes' theorem gives \(P(H\mid Y+)=P(Y+\mid H)P(H)/P(Y+)\). After each possible test outcome, optimize the decision using the updated probability; then average the resulting best utilities over signals. The expected value of sample information (EVSI) is this expected post-test utility minus the best utility without testing. EVSI is nonnegative when testing is optional and has no cost, and it cannot exceed EVPI under the same coherent decision model.

A sensitivity test may be most valuable near a decision threshold. In the Northstar example, designs A and B switch preference at disruption probability about 0.385. If p is certainly near 0.05, almost any realistic test leaves A preferred, so information has little decision value. If p is plausibly near 0.38, even moderately accurate evidence could change the selected design. This is why engineering teams should concentrate measurements on **decision-sensitive** uncertainties instead of collecting whichever measurements are easiest.

Choice under multiple objectives is not equivalent to choosing a single score. Feasibility constraints can be uncertain, too. A chance constraint such as \(P(G(x,\omega)\ge0.9)\ge0.95\) specifies probabilistic compliance under an assumed scenario distribution. A robust constraint instead requires \(G(x,\omega)\ge0.9\) for every scenario in a declared uncertainty set. These are different commitments; neither is meaningful until the distribution or uncertainty set is justified.

### Critique exercise

A trade study ranks alternatives by a weighted utility score but silently excludes road failures from the scenario dataset. Explain how that omission changes the optimization question. Then propose one hard constraint, one uncertain objective, and one evidence collection activity with potential to reverse the preferred architecture. The expected answer is not a new score alone; it is a traceable decision model and a plan for learning.

## Problems — attempt first

1. Find the weight at which the two normalized design scores cross.
2. Find the disruption probability at which A and B have equal expected benefit.
3. Compute EVPI at disruption probability 0.3, and state a limitation.
4. Why should minimum accessibility be modeled as a constraint rather than a compensable score?

<details><summary>Worked answers and engineering interpretation</summary>

1. From \(0.6+0.2w=0.9-0.4w\), \(w=0.5\).
2. \(p=25/65\approx0.3846\).
3. Without information choose A at 76; perfect-information expected value 88; EVPI = 12. It is conditional on the stated payoffs, p, and optimal action selection, not a market price for any particular experiment.
4. A hard service obligation cannot legitimately be traded away merely because another design is cheaper; include it in feasibility and review subgroup performance explicitly.
</details>

## Practice laboratory and further learning

[Open the lab for this chapter](../labs/07-decisions.html) · [Download editable Markdown lab](../labs/07-decisions.md) · [Open the associated notebook](../notebooks/07-decisions.ipynb) · [Download the calculation source](../code/engineering_math.py)

**Authoritative follow-up reading:** [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/), [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook), and [Systems Engineering Body of Knowledge](https://www.incose.org/resources-publications/technical-publications/systems-engineering-body-of-knowledge/). These are independent references, not endorsements of the fictional cases.

[Return to the quantitative textbook collection](../INDEX.html)

<!-- STEP04-QUANTITATIVE-START -->
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
<!-- STEP04-QUANTITATIVE-END -->
