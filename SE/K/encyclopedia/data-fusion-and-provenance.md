# Data fusion: weighting evidence without losing provenance

**Reference entry · Systems of systems and quantitative assurance · Worked technical treatment**

## Fusion begins before the arithmetic

**Data fusion** combines observations from multiple sources to estimate a state, infer an event, or support a decision. Sources can disagree because they measure different quantities, sample different populations, have time skew, share calibration error, or fail under the same conditions. Averaging first and asking about provenance afterward is unsafe. Each input needs an identity, timestamp, unit, coordinate/frame convention, uncertainty, calibration history, processing version and admissibility criteria.

Different fusion tasks require different models. Associating radar tracks is not the same problem as combining two temperature measurements; classifying an event is not equivalent to estimating a continuous quantity. Do not apply a Gaussian weighted-mean formula to category probabilities or data with unknown association errors.

## Worked independent-measurement fusion

Suppose two hypothetical sensors observe the same scalar state \(x\), with unbiased, independent normal errors: \(x_1=10\), standard uncertainty \(u_1=2\); \(x_2=14\), \(u_2=1\). The inverse-variance estimator is

\[
\widehat x=\frac{x_1/u_1^2+x_2/u_2^2}{1/u_1^2+1/u_2^2}
=\frac{10/4+14/1}{1/4+1}=13.2.
\]

Its standard uncertainty under those assumptions is

\[
u_{\widehat x}=\sqrt{\frac{1}{1/u_1^2+1/u_2^2}}=\sqrt{0.8}\approx0.8944.
\]

The more precise second observation receives greater weight. This *conditional* uncertainty is not valid if both sensors share a calibration bias or the two measurements are of different states. The individual readings disagree by four units; that discrepancy merits a consistency check before automatically trusting the weighted estimate.

## Correlation changes the answer

For a vector of observations \(y=\mathbf{1}x+\epsilon\) with known covariance \(\Sigma\), the generalized least-squares estimate is

\[
\widehat x=(\mathbf{1}^{\mathsf T}\Sigma^{-1}\mathbf{1})^{-1}\mathbf{1}^{\mathsf T}\Sigma^{-1}y,
\qquad
\operatorname{Var}(\widehat x)=(\mathbf{1}^{\mathsf T}\Sigma^{-1}\mathbf{1})^{-1}.
\]

This formulation assumes a correctly specified, invertible covariance matrix, a common measurand, and a valid linear observation model. More observations with common-mode error do not necessarily reduce uncertainty as fast as independent observations. A fusion system should surface disagreement, conflicts and bad-source status instead of always returning a single confident-looking number.

## Time, identity, and operational decisions

In a distributed emergency-response network, two position reports may refer to different objects or to the same object at different times. Even an exact weighted mean would then be operationally meaningless. First perform identification, synchronization, units conversion and quality gating; then apply an estimator matched to the data and decision. Store a lineage record: source IDs, transform versions, synchronization windows, fusion algorithm, threshold rules, output timestamp and downstream users.

When a source is excluded, preserve the reason rather than deleting it from history. Assess sensitivity by repeating the decision without each major source and under plausible shared-bias scenarios.

## Exercise and pitfalls

Reproduce the estimate 13.2 and uncertainty 0.8944. Next suppose a common sensor bias could be as large as 1.5 units. Explain why the original 0.8944 alone is not an adequate uncertainty statement. Add a stale timestamp to one record: should it remain eligible? Decide using a documented freshness rule, not intuition.

## Technical references and related concepts

- [NIST metrological traceability](https://www.nist.gov/metrology/metrological-traceability) — traceability, measurement result and calibration context.
- [NIST/SEMATECH Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) — statistical modeling and uncertainty.
- Related: [technical data lineage](technical-data-governance-and-lineage.md); [measurement uncertainty](measurement-traceability-and-calibration.md); [probability and dependence](probability-and-dependence.md); [model evidence](model-vv-and-credibility.md).

*Scope:* Numerical values are original, synthetic teaching examples; this does not validate a real sensor fusion stack.

**Reproducible companion:** [Step 02 worked examples (standard-library Python)](examples/step02_examples.py). Run `python3 step02_examples.py --case all` from the downloaded examples folder; the program prints the declared synthetic inputs and computed results.

## Step 02 deeper treatment: dependent sensors change optimal fusion

The familiar inverse-variance rule assumes unbiased estimates with independent errors. For two sensors with variances \(\sigma_1^2,\sigma_2^2\) and covariance \(c\), a linear unbiased estimator \(\hat x=w y_1+(1-w)y_2\) has variance

\[
V(w)=w^2\sigma_1^2+(1-w)^2\sigma_2^2+2w(1-w)c.
\]

Setting its derivative to zero yields \(w=(\sigma_2^2-c)/(\sigma_1^2+\sigma_2^2-2c)\), provided the covariance is valid and the denominator is positive. For two hypothetical sensors with \(\sigma_1^2=4\), \(\sigma_2^2=9\) and \(c=3\), the weight on sensor 1 is \((9-3)/(4+9-6)=6/7\approx0.857\). Under a false independence assumption it would instead be \(9/(4+9)\approx0.692\). The resulting uncertainty claim changes as well. If errors share calibration or environment, independent-sensor mathematics overstates the evidence gained by combining them.

**Exercise:** calculate the fused estimate for sensor observations 10 and 12 using \(w=6/7\). The result is \(10.2857\), not an automatic indication that either sensor is correct. Document timestamps, calibration, common reference, correlation provenance and the measurement quantity. If covariance is unknown, report a sensitivity range rather than silently setting \(c=0\). See the [NIST measurement and uncertainty guidance](https://www.itl.nist.gov/div898/handbook/); this example illustrates covariance effects, not a validated calibration procedure.
