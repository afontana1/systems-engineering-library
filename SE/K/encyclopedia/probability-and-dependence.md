# Probability, dependence, and technical uncertainty

**Reference entry · Applied analytics · Expanded reference**

## Why engineering uncertainty is not a single error bar

Engineering predictions contain uncertainty from **inherent variability** (different demand, weather, manufacturing outcomes), **incomplete knowledge** (unknown parameters, mechanisms, or model structure), **measurement** (instrument accuracy and data processing), and **scenario choice** (future operating conditions). These sources require different actions: more data may reduce some knowledge uncertainty but cannot eliminate the variability of future arrivals.

A probability model is a conditional statement about a specified experiment, population, and assumptions. A single reported mean can be useful for planning but unfit for a threshold, safety, or tail-risk decision.

## Dependence changes system outcomes

For independent events A and B, **P(A ∩ B) = P(A)P(B)**. Without independence, the correct relationship is **P(A ∩ B) = P(A)P(B | A)**. Correlation is one form of dependence, and zero correlation does not prove independence. Shared infrastructure, weather, operating procedures, and cyber vulnerabilities create **common-cause dependencies** across ostensibly separate subsystems.

The law of total probability makes regime dependence explicit: **P(F) = Σ P(F | Eᵢ)P(Eᵢ)** over mutually exclusive, exhaustive environmental states. For example, high reliability during normal weather can coexist with unacceptable total mission reliability if severe conditions carry both substantial probability and high failure rates.

## Worked example: shared service risk

Suppose two dispatcher nodes have individual availability 0.99, and each could support the entire workload. The naive independent parallel estimate is **1 − 0.01² = 0.9999** (99.99%). But suppose a common authentication service is required and is available only 0.98 of the time, independently of the dispatcher nodes. Overall availability becomes **0.98 × 0.9999 ≈ 0.979902**, or about **97.99%**—well below either node's availability.

The correct architecture question is not “How reliable are the replicas?” but “What collection of conditions must be simultaneously true for the mission to succeed?” A fault tree or Bayesian network can represent these dependencies; fault correlation and conditional state changes need explicit evidence.

## Distributions, tails, and statistical evidence

A distribution should be chosen by its mechanism and observed support, not convenience. Service times may be right-skewed; counts may have overdispersion; component lifetime can depend on age and stress; recovery duration may have a heavy tail. The 99th percentile of response time is an operational claim about rare but important cases, and can be unstable when the sample contains few peak-load observations.

A Monte Carlo simulation estimates consequences by sampling uncertain inputs and propagating them through a model. To be credible, it must preserve physically meaningful dependencies—e.g., storm conditions may jointly increase demand, lower vehicle speed, and reduce battery performance. Independent sampling of these variables can underestimate service-failure probability. Sensitivity analysis should distinguish influential uncertain assumptions from influential controllable design decisions.

## A decision-centered workflow

1. Define the adverse event, population, scenario, and threshold.
2. Separate variability, parameter uncertainty, model uncertainty, and measurement error.
3. Identify shared causes and conditional relationships before fitting distributions.
4. Inspect data provenance, missingness, censoring, outliers, and sampling bias.
5. Select distributions and dependence models with physical and statistical justification.
6. Propagate uncertainty; report tail probabilities, intervals, assumptions, and simulation error.
7. Challenge conclusions under alternative plausible models and extreme scenarios.

## Mistakes and limits

Do not interpret a probability interval as if it automatically incorporates model misspecification. Do not treat the output of a precise spreadsheet as evidence of input accuracy. Do not estimate a one-in-a-million event rate from a few hundred ordinary test cases. Do not assume two failures are independent because separate teams own the components. Where data are sparse, make the decision conditional and plan evidence-gathering rather than inventing certainty.

## Connections

Dependence is central to reliability, cybersecurity, queueing, optimization, simulation credibility, test evidence, and systems-of-systems resilience. A technical margin without an uncertainty model can conceal a fragile design.

## Reference shelf retained from the earlier primer

These links are supplied for deeper reading. Confirm current publication versions before relying on them for compliance.

- [NIST/SEMATECH Engineering Statistics Handbook](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook) — Statistical explanation, worked methods, measurement and design of experiments.
- [NASA-STD-7009B: Standard for Models and Simulations](https://standards.nasa.gov/node/263) — Modeling intended use, V&V, qualification, credibility and limitations.


## Technical analysis: correlation changes the architecture's failure rate

Consider two supposedly redundant independent power supplies, each with per-mission failure probability `p=0.02`. If the system fails only when **both** supplies fail and failures really are independent, joint failure is `p² = 0.0004` (0.04%). Independence is a causal assumption, not a benefit conferred by a two-box diagram. Now suppose a shared bus failure has probability `q=0.01`, independent of each supply's private failure mode, and any shared-bus failure disables both. Then system failure is `q + (1−q)p² = 0.01 + 0.99(0.0004) = 0.010396` (1.0396%). The common cause makes the two-supply architecture roughly **26 times** more failure-prone than the simplistic independent estimate.

This example treats private failures as independent *conditional on no common-bus failure*. A real assessment must also examine software common mode, maintenance practices, environmental exposure, and imperfect switching. For data-derived dependence, an observed correlation coefficient does not by itself determine tail co-occurrence; scenarios or a justified joint distribution are needed. Report the system failure definition, mission duration, and dependency model along with any single reported reliability number.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NIST · NIST/SEMATECH e-Handbook of Statistical Methods (2002; online guidance)](https://www.nist.gov/publications/handbook-151-nistsematech-e-handbook-statistical-methods) — Statistical methods, experiments, reliability, and process assessment.
- [NIST · Technical Note 1297, Reporting Measurement Uncertainty (1993)](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty) — Standard and expanded uncertainty, coverage factors, and reporting conditions.

## Phase 3 technical reference: A covariance term can change a deadline decision

For uncertain travel time \(T=D/V\), mean \(D=120\) m, \(V=12\) m/s, standard deviations 6 m and 1.2 m/s, and assumed correlation \(\rho=-0.6\), the delta-method propagation yields
\[
u_T^2\approx (6/12)^2+(120\cdot1.2/12^2)^2-2(120/12^3)\operatorname{Cov}(D,V)=1.85\;\mathrm{s}^2.
\]
Dropping covariance would give only \(1.25\;\mathrm{s}^2\), a 32% smaller variance, and could conceal mission risk. In the worked synthetic Monte Carlo model, \(P(D/V>12\text{ s})\) is about 9.7% with negative correlation versus 6.2% under an uncorrelated assumption. These are conditional model predictions, not field estimates. The [full propagation guide](../methods/correlated-uncertainty-propagation.md) derives the gradient, input construction and separation of simulation error from input/model uncertainty.



## Step 02 review studio — quantify dependence before multiplying risks

Let `A` represent loss of a status feed with probability 0.10 and `B` loss of a second feed with probability 0.20. Suppose observed or defensibly modeled joint probability is `P(A∩B)=0.08`. Independence would instead imply `0.10×0.20=0.02`, a fourfold underestimate of the **joint** event. The probability of at least one loss is `P(A∪B)=0.10+0.20−0.08=0.22`, not the independent-assumption value 0.28.

**Solved exercise:** can we conclude that one feed causes the other to fail? **No.** Dependence may arise from a shared power supply, environmental stress, correlated operation, or selection bias; association alone does not identify the mechanism. To predict the benefit of redundancy, investigate common causes and conditional dependence rather than multiply marginal failure rates automatically.

**Engineering boundary:** distinguish per-demand events, time-indexed availability, and hazard exposure populations. Their probabilities have different units and sampling assumptions; a plausible-looking number cannot be ported between them without a model.

## Follow the knowledge

**Related concepts**

- [Design of experiments and sensitivity](design-of-experiments.md)
- [Simulation verification, validation, and credibility](model-vv-and-credibility.md)
- [Resilience, robustness, and graceful degradation](resilience-adaptability.md)
- [Trade studies, constraints, and sensitivity](engineering-trades.md)

**Explore in the 240-chapter textbooks**

- [Book 10, Chapter 2: Book 10 · Chapter 02 — Characterize probability distributions, tails, dependence, and stochastic performance](../B10/chapters/02-characterize-probability-distributions-tails-dependence-and-stochast.md)
- [Book 10, Chapter 9: Book 10 · Chapter 09 — Propagate uncertainty with analytic Monte Carlo simulation and sensitivity analysis](../B10/chapters/09-propagate-uncertainty-with-analytic-monte-carlo-simulation-and-sensi.md)
- [Book 18, Chapter 9: Week 09 · System of Systems Engineering · Chapter 09 — Cascading risk, cyber resilience, safety, and mission assurance](../B18/chapters/09.md)

**Use this reference responsibly:** examples use hypothetical engineering data; the mathematical results rely on the assumptions stated in each passage. Recheck those assumptions for any real project.

