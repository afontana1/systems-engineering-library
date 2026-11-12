# Uncertainty propagation with dependent inputs

*Engineering method guide · Measurement models, covariance, Monte Carlo, tail probabilities and evidence limitations · Phase 3*

**Learning outcome.** Given a derived engineering quantity, write the model, propagate dependent input uncertainty analytically, compare the approximation to a Monte Carlo distribution, report sampling error separately from input-model uncertainty, and explain why correlation can reverse an engineering conclusion. All inputs and outcomes here are **synthetic**.

**Prerequisites:** [Probability and dependence](../encyclopedia/probability-and-dependence.md), [measurement traceability](../encyclopedia/measurement-traceability-and-calibration.md), [statistical inference](statistical-inference-and-experiments.md), and [robust design](pareto-and-robust-design.md).

## 1. Start from the measurement or prediction model

Suppose an engineered shuttle must travel a known segment, but its actual distance \(D\) and effective speed \(V\) vary under a declared operating regime. The time in seconds is

\[
T=f(D,V)=\frac{D}{V}.
\]

The equation alone is not a stochastic model. We must specify what observations or uncertainties \(D\) and \(V\) represent, their units, their joint distribution, and the relevant population. Here set \(E[D]=120\) m, \(\sigma_D=6\) m, \(E[V]=12\) m/s, \(\sigma_V=1.2\) m/s, and \(\rho_{DV}=-0.6\). This negative correlation is an intentionally assumed teaching mechanism: conditions that lengthen the effective path also tend to slow the vehicle. It is not field evidence.

Random input variation, calibration uncertainty, and uncertainty about the correct relationship \(T=f(D,V)\) are different categories. Sampling uncertain inputs through a flawed physical model does not account for model-form error. Document epistemic uncertainty in correlation and distribution choice separately from aleatory variation among operating cases.

## 2. Derive the first-order uncertainty result

For differentiable \(f\), linearize around the mean vector \(\boldsymbol\mu\). With gradient \(g=\nabla f(\boldsymbol\mu)\) and input covariance matrix \(\Sigma\), the first-order output variance is

\[
\operatorname{Var}(T)\approx g^\mathsf{T}\Sigma g.
\]

For the travel-time ratio,

\[
\frac{\partial T}{\partial D}=\frac{1}{\mu_V}, \qquad
\frac{\partial T}{\partial V}=-\frac{\mu_D}{\mu_V^2}.
\]

Therefore, writing \(c=\operatorname{Cov}(D,V)=\rho\sigma_D\sigma_V\),

\[
\begin{aligned}
u_T^2 &\approx \left(\frac{\sigma_D}{\mu_V}\right)^2
 +\left(\frac{\mu_D\sigma_V}{\mu_V^2}\right)^2
 -2\frac{\mu_D}{\mu_V^3}\,c.\\
 &= 0.25+1.00+0.60=1.85\ \mathrm{s}^2,\\
 u_T&\approx\sqrt{1.85}=1.360\ \mathrm{s}.
\end{aligned}
\]

The covariance is \(c=-0.6(6)(1.2)=-4.32\;\mathrm{m^2/s}\). Its term **increases** uncertainty because longer distance is associated with reduced speed. If an analyst incorrectly assumes independence, that term vanishes and the approximate standard deviation falls to \(\sqrt{1.25}=1.118\) seconds. A zero covariance *assumption* is not evidence that the system is independent.

The nominal output \(120/12=10\) seconds is **not necessarily** \(E[D/V]\) for nonlinear \(f\). The delta method is a local approximation: its neglected higher-order terms matter when uncertainties are large, input distributions skew, or the denominator approaches zero.

## 3. Propagate the joint distribution, not two unrelated marginals

The worked Monte Carlo model constructs correlated standard normals:

\[
Z_1,Z_2\stackrel{\text{iid}}{\sim}N(0,1),\qquad
D=120+6Z_1,\quad
V=12+1.2\bigl(\rho Z_1+\sqrt{1-\rho^2}Z_2\bigr).
\]

This construction has the stipulated marginal means and standard deviations and correlation \(\rho\). It is a **joint-input model**; independently sampling the two marginal distributions would implement a different physical hypothesis. Normally distributed speed can be nonpositive, which is physically impossible. The demonstration explicitly rejects nonphysical draws and counts them; with the given parameter values this tail is extremely remote, but a safety-critical model should use a properly justified bounded input distribution and re-evaluate its dependence structure.

Download or run the [standard-library Monte Carlo example](code/correlated_uncertainty.py). The fixed-seed results with 100,000 valid trials are:

| Result | \(\rho=-0.6\) assumed dependent inputs | \(\rho=0\) assumed uncorrelated inputs |
|---|---:|---:|
| First-order \(u_T\) | 1.360 s | 1.118 s |
| Monte Carlo mean \(T\) | 10.133 s | 10.104 s |
| Monte Carlo standard deviation | 1.411 s | 1.160 s |
| Empirical 95th percentile | 12.632 s | 12.161 s |
| \(\widehat P(T>12\ \mathrm{s})\) | 9.694% | 6.171% |
| Bernoulli Monte Carlo SE for the probability | 0.0936 percentage points | 0.0761 percentage points |

The Monte Carlo standard error quantifies **finite sampling precision conditional on this input model**. It does not quantify uncertainty in \(\rho\), measurement calibration, model form, nor whether Gaussian marginals hold. The large difference in estimated deadline exceedance is caused primarily by a changed dependency assumption, not Monte Carlo noise.

For an event indicator \(I_i=\mathbf{1}(T_i>12)\), conditional on independent Monte Carlo trials,

\[
\hat p=\frac{1}{N}\sum I_i,\qquad
SE_{MC}(\hat p)\approx\sqrt{\frac{\hat p(1-\hat p)}{N}}.
\]

The displayed standard error is *not* a credible interval for the real system's service-failure probability. Tail uncertainty should be challenged with alternative plausible joint distributions, stress conditions, and independent measurements.

## 4. Separate input uncertainty, stochastic noise, and model discrepancy

An uncertainty budget should identify at least five distinguishable layers:

1. **Natural variability:** different traffic, routes, loads and ambient conditions for future missions.
2. **Parameter estimation:** limited data supporting \(\mu_D,\mu_V,\sigma_D,\sigma_V,\rho\).
3. **Measurement error:** distance calibration, timing alignment, and sensor bias (possibly shared across observations).
4. **Model discrepancy:** the approximation \(D/V\) omits starts, stops, turns and driver behavior.
5. **Numerical/Monte Carlo error:** finite sampling and arithmetic approximation.

Adding Monte Carlo trials reduces mainly the last item. It does not transform unvalidated input correlations into accurate ones. If two sensors share a calibration offset, their measurement errors may correlate even when physical distances and speeds do not. Combining multiple uncertainty sources by root-sum-of-squares is justified for suitably modeled **uncorrelated standard uncertainties**, not as a universal rule.

The JCGM 101:2008 GUM supplement describes propagating probability distributions through a measurement model using Monte Carlo. It is a reference method, not a claim that every stochastic engineering model is automatically metrologically qualified.

## 5. From uncertainty to a technical margin decision

Suppose an engineering design permits a 12-second travel segment. An analyst might calculate nominal margin \(M=12-10=2\) s and report “pass.” That ignores the uncertain tail: the hypothetical correlated-input model assigns nearly one in ten runs above the limit. Whether this is tolerable depends on the **requirement type**: a hard bound on all operations, a specified percentile, a per-mission probability target, or only a planning average. An inferred percentile cannot substitute for an absolute bound; a sample-proportion confidence interval cannot establish a rare failure limit from too little evidence.

A decision-ready report provides an exceedance probability *under stated input assumptions*, sensitivity to correlation and tail shape, parameter confidence, operational envelope, and required test or instrumentation. If uncertainty prevents a decisive recommendation, identify which field measurement has the greatest potential value of information rather than report extra digits.

## 6. Replication and sensitivity exercises

1. Derive the gradient of \(D/V\) and reproduce the 1.85 \(\mathrm{s}^2\) variance expression by hand, tracking units.
2. Run the code under \(\rho=-0.6\), \(0\), and \(+0.6\). Plot or tabulate the exceedance probabilities; explain how the physical story changes.
3. Tighten the time requirement from 12 s to 11 s. Compare the change in \(\hat p\) with the change in its Monte Carlo standard error.
4. Change only the random seed; show that simulation precision changes but the input-model hypothesis does not.
5. List operational observations needed to estimate correlation **without** treating autocorrelated data points as independent replications.
6. Write a one-page uncertainty budget distinguishing aleatory, epistemic, measurement and numerical sources.

**Curriculum crosswalk:** [EN.645.756](../../C/P3/EN645756.md), [EN.645.758](../../C/P3/EN645758.md), [Book 10 ch 9](../B10/chapters/09-propagate-uncertainty-with-analytic-monte-carlo-simulation-and-sensi.md), [Book 12 ch 8](../B12/chapters/08-model-natural-and-man-made-environments-as-dynamic-correlated-scenar.md), and [Book 11 ch 3](../B11/chapters/03-characterize-data-quality-probability-dependence-and-stochastic-inpu.md).

## Primary technical references

- [BIPM / JCGM 101:2008, Propagation of distributions using a Monte Carlo method](https://www.bipm.org/en/doi/10.59161/jcgm101-2008). Method for propagating distributional uncertainty through a measurement model.
- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.nist.gov/programs-projects/nistsematech-engineering-statistics-handbook). Measurement, interval and statistical-model reasoning.
- [NASA-STD-7009B, Standard for Models and Simulations](https://standards.nasa.gov/node/263). Intended-use credibility of model-supported decisions.

*All numerical scenarios in this guide are instructional; field verification, model validation and decision authority remain separate.*
