# Design of experiments and sensitivity

**Reference entry · Analytics, modeling, simulation and decisions · Expanded reference**

## Definition and diagnostic distinction

**Design of experiments (DOE)** plans observations so competing explanations and design choices can be distinguished efficiently. It is more than running a collection of scenarios and drawing a response curve. Controlled factors, nuisance variables, randomization, replication, and a predeclared response measure determine whether an observed effect is attributable to a change rather than drift, selection, or chance.

## Theory: effects, interactions, and identifiable claims

In a two-factor coded design with factors `x_A, x_B ∈ {-1,+1}`, a basic response model is `y = β0 + βA x_A + βB x_B + βAB x_A x_B + ε`. The interaction coefficient captures how the effect of A changes with B. A one-factor-at-a-time study cannot identify this interaction cleanly. Randomization protects against unmeasured time trends; blocking handles known nuisance groupings; replication estimates variation; repeated measurements without independently assigned experimental units are not independent replicates.

Statistical significance does not guarantee engineering significance. Confidence intervals and a predeclared practical threshold matter more than a bare p-value. Multiple testing increases false discoveries unless managed through a planned analysis strategy. Computational DOE also needs surrogate-model validation: a smooth fitted surface may be wrong near a boundary, discontinuity, or untested environment.

## Worked example: a hidden interaction

Suppose a dispatch algorithm is tested with low/high vehicle supply (A) and low/high demand (B), with mean waiting times of 4, 8, 5, and 19 minutes for `(low supply, low demand)`, `(low supply, high demand)`, `(high supply, low demand)`, and `(high supply, high demand)` respectively. This illustrative table is deliberately unusual: adding vehicles slightly worsens low-demand waiting time but strongly worsens high-demand waiting time, suggesting an implementation or coordination problem. The simple difference-in-differences is `(19 - 8) - (5 - 4) = 10 minutes`, an interaction requiring explanation before adoption. Replicates and blocked randomized runs are needed to tell whether this pattern persists beyond noise.

## Engineering use and evidence

Specify the decision, experimental units, factors and ranges, response definition, expected variability, safety constraints, run order, and analysis before collecting results. Preserve raw data and random seeds. Fit candidate models, examine residuals and interactions, and confirm promising settings using new observations. For physical experimentation, document calibration and environmental conditions; for simulation, document code version and stochastic input models.

## Limitations and connections

A factorial result is local to its chosen levels and may not generalize to deployment. Correlated uncontrolled factors can defeat naive causal interpretation. Connect DOE to **probability**, **simulation credibility**, **process improvement**, **surrogate optimization**, and **value of information**.

## Technical analysis: a factorial interaction that a one-factor study misses

Consider two controllable choices: software batching (`A = −1` off; `+1` on) and cache capacity (`B = −1` small; `+1` large). Suppose measured average completion times (minutes) for the four treatments are `y(−,−)=14`, `y(+,−)=10`, `y(−,+)=12`, and `y(+,+)=4`. Under a balanced `2²` factorial design, the average effect of A is `(10+4)/2 − (14+12)/2 = −6` minutes; the effect of B is `(12+4)/2 − (14+10)/2 = −4` minutes. The **interaction contrast** is `14 − 10 − 12 + 4 = −4`, corresponding to an interaction *effect* of `−2` minutes and a coded-regression interaction coefficient `βAB = −1` minute. Define the convention explicitly: effect, contrast, and coefficient are not interchangeable.

The interaction matters: batching saves four minutes with the small cache but **eight** with the large cache. An experiment changing only batching at the small-cache baseline would understate the potential joint benefit. Randomize experimental order to reduce drift bias; replicate to estimate noise; block by load regime if service demand changes over time. A design with one observation per cell has **no pure-error degrees of freedom**, so it cannot support a significance claim about the interaction without additional assumptions or replications.

Document the response definition, treatment levels, operating envelope, randomization unit, and missing-run handling. Statistical significance is not a substitute for mission relevance or operational replication.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NIST · NIST/SEMATECH e-Handbook of Statistical Methods (2002; online guidance)](https://www.nist.gov/publications/handbook-151-nistsematech-e-handbook-statistical-methods) — Statistical methods, experiments, reliability, and process assessment.
- [NASA · NASA-STD-7009B, Standard for Models and Simulations (2024)](https://standards.nasa.gov/node/263) — Credibility practices for modeling and simulation used in decisions.

## Factorial effects are contrasts, not labels

A balanced two-factor experiment is more informative than changing A while holding B fixed because it estimates the interaction. For treatment means \(\bar Y_{--}=10.55\), \(\bar Y_{+-}=8.975\), \(\bar Y_{-+}=7.95\), and \(\bar Y_{++}=6.75\) ms, the main effect of A is \((8.975+6.75-10.55-7.95)/2=-1.3875\) ms. The AB interaction effect is \((10.55+6.75-8.975-7.95)/2=+0.1875\) ms. A positive interaction here means the combined latency reduction is somewhat smaller than the sum of the two separate reductions on this response scale. It is not a statement about all other load conditions.

Why does this matter? With only an A-only comparison, the analyst has no estimate of whether replication B changes scheduler effectiveness. Each factor combination also needs genuine independently randomized experimental replications. Thousands of requests from a single unaltered run are not equivalent to independently applied treatment settings. See [the full statistical and factorial treatment](../methods/statistical-inference-and-experiments.md), with synthetic data and independent residual calculations.



## Step 02 review studio — calculate effects before interpreting causality

A hypothetical two-factor, two-level dispatch experiment has response times (minutes): `A−,B−=20`; `A+,B−=16`; `A−,B+=14`; `A+,B+=8`. The estimated **A main effect** is the high-A mean minus low-A mean: `(16+8)/2−(20+14)/2 = −5` minutes. The **B effect** is `(14+8)/2−(20+16)/2 = −7` minutes. The two-factor interaction contrast is `(20+8−16−14)/2=−1` minute (under this conventional contrast scaling).

**Solved exercise:** can we declare either factor statistically significant from these four observations? **No.** With one observation per treatment combination, a saturated two-factor interaction model has no residual degrees of freedom to estimate random error. Replicate, randomize order, record run conditions, and check model assumptions before constructing intervals or significance claims. The estimated contrasts are still useful *descriptive* results for this synthetic experiment.

**Evidence boundary:** factor interactions are decision-relevant; a one-factor-at-a-time experiment could miss them. Correlated noise, uncontrolled demand drift, and nonrepresentative experiments can still invalidate a clean factorial table.

## Follow the knowledge

**Related concepts**

- [Probability, dependence, and technical uncertainty](probability-and-dependence.md)
- [Simulation verification, validation, and credibility](model-vv-and-credibility.md)
- [Process capability and continuous improvement](process-improvement.md)
- [Decision uncertainty and value of information](bayesian-value-of-information.md)

**Go deeper in the 240-chapter textbooks**

- [Book 10, Chapter 05: Book 10 · Chapter 05 — Design efficient experiments with factors, responses, noise, power, randomization, and blocking](../B10/chapters/05-design-efficient-experiments-with-factors-responses-noise-power-rand.md)
- [Book 10, Chapter 06: Book 10 · Chapter 06 — Analyze factorial experiments, interactions, diagnostics, and confirmation evidence](../B10/chapters/06-analyze-factorial-experiments-interactions-diagnostics-and-confirmat.md)
- [Book 14, Chapter 09: Book 14 · Chapter 09 — Design computational experiments to learn efficiently from the design space](../B14/chapters/09-design-computational-experiments-to-learn-efficiently-from-the-desig.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
