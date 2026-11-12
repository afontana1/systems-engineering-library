# Surrogate models: approximation, validation, and decision risk

**Reference entry · Quantitative design and optimization · Worked technical treatment**

## What a surrogate is for

A **surrogate model** approximates a costly simulation, experiment, or mathematical evaluation with a cheaper predictor. It can accelerate design exploration, optimization, uncertainty propagation and sensitivity analysis. Its prediction error is a separate engineering uncertainty. A smooth plot, low training error, or impressive interpolation is not proof that the surrogate is trustworthy for a design decision.

Choose the intended-use domain first: inputs, ranges, constraints, outputs, operating modes, model version and decisions that will rely on predictions. Select training points and an independent validation design to expose behavior in regions that matter, including boundaries and likely optimization targets. Avoid choosing a train/test split that leaks near-duplicate data from the same simulation run or physical test.

## Fully worked interpolation trap

Suppose a hypothetical response is sampled at input values \(x=0,2,4\) and yields \(y=8,4,8\). A quadratic interpolant is

\[
\widehat f(x)=x^2-4x+8=(x-2)^2+4.
\]

It fits all three training points **exactly**. But imagine the reference model actually contains an omitted interaction:

\[
f(x)=(x-2)^2+4+0.05x(x-2)(x-4).
\]

The extra term vanishes at all three training points, so training error remains zero. At a held-out \(x=3\), however, \(\widehat f(3)=5.00\) while \(f(3)=4.85\), an error of \(+0.15\). At \(x=6\), outside the training domain, \(\widehat f(6)=20.0\) but \(f(6)=22.4\), an error of \(-2.4\). This constructed example is designed to show why interpolation quality does not establish extrapolation quality.

## Validation needs a decision metric

Define signed residual \(e_i=\widehat y_i-y_i\). Root-mean-square error is \(\mathrm{RMSE}=\sqrt{n^{-1}\sum e_i^2}\); maximum absolute error can be more important when a limit or threshold is at stake. Residual plots against each input help reveal bias, heteroscedasticity and missing regimes. The error model should represent numerical simulation error, physical measurement error, and surrogate approximation separately where possible.

Suppose a safety limit is \(y\leq5.0\) at \(x=3\). The surrogate gives \(5.00\), with no margin; the constructed reference gives \(4.85\). Neither justifies declaring the system safe without a validated error envelope and relevant physical evidence. Optimization is particularly dangerous because the optimizer actively seeks regions where model error may be most favorable.

## Training, validation and adaptive refinement

A practical workflow is to: (1) specify input ranges and feasible combinations; (2) choose a space-filling design and record random seeds; (3) fit a model appropriate to the anticipated smoothness and interactions; (4) test independent points including boundaries; (5) quantify prediction uncertainty or conservative error bounds; (6) verify candidate optima using the high-fidelity model; and (7) retrain when the physical architecture or model version changes. Nested cross-validation may help tune a family of candidate models, but its assumptions must match the source of data dependence.

Surrogates are particularly useful for multiobjective trade studies, but a surrogate Pareto front is provisional until enough reference evaluations confirm candidate dominance and feasibility.

## Exercise and cautions

Reproduce the training fit, calculate the two held-out residuals, and propose four additional samples that would reveal the cubic deviation. Would a random 80/20 split of exactly three samples be defensible? Explain why not. Distinguish interpolation from extrapolation, validation-domain evidence from system validation, and a predictive distribution from a guarantee of correctness.

## References and links

- [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) — regression diagnostics, experiment design and statistical model assessment.
- [NASA Models and Simulations Implementation Guide](https://standards.nasa.gov/standard/nasa/nasa-hdbk-7009) — intended use and credibility context.
- Related: [design of experiments](design-of-experiments.md); [robust optimization](robust-optimization-and-margins.md); [model V&V and credibility](model-vv-and-credibility.md).

*Scope:* The cubic perturbation and numerical results are intentionally synthetic; no physical system is represented.

**Reproducible companion:** [Step 02 worked examples (standard-library Python)](examples/step02_examples.py). Run `python3 step02_examples.py --case all` from the downloaded examples folder; the program prints the declared synthetic inputs and computed results.
