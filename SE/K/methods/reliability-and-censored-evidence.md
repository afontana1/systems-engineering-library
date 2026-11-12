# Reliability analysis with censored failure evidence

*Technical method guide · Survival, hazard, repair, field exposure, and uncertainty · Phase 2 expansion*

**What this guide enables.** Distinguish mission reliability from operational availability, organize censored life-test observations, calculate an exponential failure-rate estimate, construct a Kaplan–Meier product-limit curve, and identify where architecture dependence invalidates a naïve reliability prediction. All numerical observations are hypothetical.

**Prerequisites:** [Reliability, availability and maintainability](../encyclopedia/reliability-availability-maintainability.md); [probability and dependence](../encyclopedia/probability-and-dependence.md); [statistical acceptance](../encyclopedia/statistical-acceptance-and-confidence.md).

## 1. Reliability claims must specify a function and time horizon

For a nonrepairable item, let the random variable \(T\) be time to a specified failure under a specified set of conditions. Its survival or reliability function is \(R(t)=P(T>t)\). The cumulative distribution is \(F(t)=1-R(t)\), and the hazard rate is

\[
h(t)=\lim_{\Delta t\downarrow0}\frac{P(t\le T<t+\Delta t\mid T\ge t)}{\Delta t}=\frac{f(t)}{R(t)}.
\]

For a constant hazard \(\lambda\), solve \(dR/dt=-\lambda R\) with \(R(0)=1\):

\[
R(t)=e^{-\lambda t},\qquad E[T]=\frac1\lambda.
\]

The exponential model is a hypothesis, not a universal physical law. Wear-out mechanisms can produce increasing hazards; defective early units may produce decreasing hazards. A Weibull model with shape \(\beta\) and scale \(\eta\) has \(R(t)=\exp[-(t/\eta)^\beta]\). Here \(\beta=1\) reduces to exponential, \(\beta>1\) has increasing hazard, and \(\beta<1\) decreasing hazard. Do not choose a distribution merely because it gives a comfortable mission-success estimate.

**Repairable-system availability is different.** In a simplified alternating up/down process, the long-run intrinsic availability can be \(A\approx MTBF/(MTBF+MTTR)\) under the stated steady operating assumptions. Delays for logistics, support personnel, planned maintenance, and shared infrastructure require additional modeling. An availability estimate cannot replace the probability of surviving an uninterrupted 50-hour mission.

## 2. Right censoring is observed information, not a discarded unit

Suppose eight independent prototype power modules are observed for at most 100 operating hours. Three fail at **20, 50, and 80 hours**; five are still working at 100 hours. A right-censored unit contributes the information **"survived at least 100 hours"** even though its exact failure time is unknown. Dropping these five would bias a failure-rate estimate dramatically upward. Treating them as failures at 100 hours would instead fabricate events.

The corresponding [synthetic CSV](data/module-life-test.csv) has one row per module with `hours` and `failed` (1 for a failure, 0 for right censoring). Its units have not been repaired or returned for repeated exposure. The assumptions are independent units, accurately recorded failure/censor times, and *noninformative censoring*: the censoring mechanism does not itself disclose extra information about failure propensity beyond what the model includes.

| Unit group | Recorded time (h) | Observation | Contribution to total observed exposure (h) |
|---|---:|---|---:|
| Three failed modules | 20, 50, 80 | Observed failure | 150 |
| Five surviving modules | 100 each | Right censored | 500 |
| **Combined** | | **3 failures; 5 censors** | **650** |

## 3. Derive the exponential maximum-likelihood estimate

For a constant-hazard exponential model, the contribution of a failure at time \(t_i\) to the likelihood is the density \(f(t_i)=\lambda e^{-\lambda t_i}\); the contribution of a censored observation is the survival function \(R(t_i)=e^{-\lambda t_i}\). Using event indicator \(d_i\in\{0,1\}\),

\[
L(\lambda)=\prod_i[\lambda e^{-\lambda t_i}]^{d_i}[e^{-\lambda t_i}]^{1-d_i}
=\lambda^d\exp\!\left(-\lambda\sum_i t_i\right),\quad d=\sum_i d_i.
\]

Thus \(\ell(\lambda)=d\ln\lambda-\lambda T_\mathrm{exposure}\). Differentiating and setting the score to zero gives

\[
\widehat\lambda=\frac{d}{T_\mathrm{exposure}}=\frac{3}{650}=0.00461538\;\mathrm{h}^{-1}.
\]

For the specified exponential model, the estimated mission survival at 50 hours is

\[
\widehat R(50)=\exp(-50\times3/650)\approx0.7939.
\]

The estimate \(1/\widehat\lambda\approx216.7\) hours is a model-based mean lifetime, not a measured mean of the eight final failure times. With only three observed failures, the uncertainty about the hazard shape and rate is substantial. A point estimate alone should not justify a high-consequence acceptance decision.

The [standard-library reliability analyzer](code/censored_reliability.py) reads the CSV, validates event flags, computes exposure and the exponential estimate, and constructs a nonparametric Kaplan–Meier curve. It explicitly refuses to estimate an exponential rate when no failures have occurred, rather than pretending that a rate of zero is established.

## 4. A Kaplan–Meier curve makes fewer distributional commitments

At each unique observed failure time \(t_j\), with \(n_j\) units at risk immediately beforehand and \(d_j\) failures, the product-limit estimate is

\[
\widehat S(t)=\prod_{t_j\le t}\left(1-\frac{d_j}{n_j}\right).
\]

For the example there are initially eight units at risk. The survival estimate falls to \(7/8=0.875\) at 20 hours, \((7/8)(6/7)=0.75\) at 50 hours, and \((7/8)(6/7)(5/6)=0.625\) at 80 hours. The five units censored at 100 hours are removed from the risk set **after** the last failure but do not themselves cause another survival drop. The resulting \(\widehat S(50)=0.75\) differs from the exponential model's 0.7939: this is informative, not a contradiction.

The nonparametric curve still assumes appropriate censoring and independent observations. It cannot identify survival beyond the last informative observation. With only eight units, it is a demonstration of mechanics, not a dependable reliability assurance bound. A large test population with many censors may also require a formal interval estimate and a review of censor patterns.

## 5. Series systems, redundancy, and dependence

For two components that must *both* survive a mission, independent component lifetimes imply \(R_\mathrm{series}(t)=R_1(t)R_2(t)\). For a one-out-of-two parallel structure with independent failures, \(R_\mathrm{parallel}(t)=1-[1-R_1(t)][1-R_2(t)]\). These formulas fail as written for components that share a power supply, cooling, controller, manufacturing defect, or triggering hazard.

Example: two channels each have a nominal 0.90 mission survival. Independence would suggest \(R_\mathrm{parallel}=0.99\). Suppose instead that a **common-cause shock** occurs with probability 0.05 and disables both channels, while the independent 0.90 survival assumptions apply *conditional on no shock*. Then

\[
R_\mathrm{parallel,CC}=(1-0.05)[1-(1-0.90)^2]=0.9405.
\]

The change from 0.99 to 0.9405 is material. This hypothetical mixture model is intentionally simple; realistic common-cause analysis needs mechanism-specific evidence and can require explicit fault trees or dependency models. The inference is not that redundancy is useless, but that its value cannot be calculated without modeling shared causes.

**Degradation** creates another failure of a binary operational model. Capacity can decay continuously before the threshold is crossed. Monitoring a wear measure, calibration drift, or battery health requires measurement/process models tied to the definition of unacceptable performance. A mission may be degraded even if no component reports a terminal failure.

## 6. From life-test evidence to a governed decision

A defensible analysis record contains the item population and selection method; failure definition; start/stop and censor rules; exposure units; environmental profile; repairs, replacements and software changes; data exclusions; assumed lifetime family; diagnostic checks; point and interval estimates; common-cause mechanisms; intended service time; and the authority responsible for accepting residual risk.

Do not interpret censoring as missing-at-random automatically: modules can be withdrawn for overheating or suspicious deterioration, making censoring *informative*. Do not use a pooled failure rate when prototypes have significantly different stresses or versions unless the model justifies it. A constant failure rate over 100-hour laboratory exposures does not establish wear-out performance over years. Under repeated field repairs, distinguish first-failure lifetime from a repairable recurrent-event process.

## 7. Uncertainty is especially consequential when few failures are observed

For the exponential likelihood, it is tempting to report only \(\widehat\lambda=3/650\) and \(\widehat R(50)\approx0.794\). The estimate does not tell the reviewer how much the inferred rate could move. A useful *approximate* likelihood-ratio construction compares each candidate \(\lambda\) with the maximum:

\[
D(\lambda)=2[\ell(\widehat\lambda)-\ell(\lambda)]
=2\left[d\ln\left(\frac{\widehat\lambda}{\lambda}\right)
+T(\lambda-\widehat\lambda)\right].
\]

An asymptotic 95% **profile-likelihood** interval uses candidates with \(D(\lambda)\le\chi^2_{1,0.95}\approx3.84146\). The [reliability analyzer](code/censored_reliability.py) solves the two endpoints numerically by bisection and then transforms them to a corresponding range of mission-survival values. Here the approximate rate endpoints are about \(0.001148\) and \(0.011968\;\mathrm{h}^{-1}\), corresponding to model-based survival at 50 hours ranging roughly from \(0.550\) to \(0.944\). That is a *model-conditional approximate interval*, **not an exact 95% finite-sample guarantee**, especially with only three failures. A formal acceptance demonstration may need a different interval construction or a validated reliability plan. If censoring is informative, if failure mechanisms differ, or if the exponential hazard model is wrong, neither the point estimate nor this interval is trustworthy.

Confidence bounds should be treated as part of the interpretation, not a decorative statistic. In particular, a small number of failures may fit more than one failure mechanism. Compare exponential, Weibull and physical degradation explanations where the data and sample size support that work. With only three failures here, a free two-parameter Weibull fit would likely be too unstable for a strong decision. The sensible conclusion may be **obtain longer or more varied exposure** rather than force a precise wear-out estimate.

## 8. Repairable data require a different sample space

If a field module fails, is repaired, and returns to service, its next failure may involve a changed component, human intervention or accumulated degradation. A dataset of *time to first failure* is no longer a complete description of repeated events. A **repairable-system recurrent-event analysis** uses a timeline of failures, repair actions, exposure, operating conditions and potentially changing intensity. In a homogeneous Poisson-process approximation, the expected number of events over cumulative exposure \(t\) is \(\lambda t\); a trend in event intensity would contradict that stationary assumption.

A practical data dictionary should distinguish `asset_id`, `hardware_rev`, `software_build`, `failure_code`, `event_start`, `event_end`, `active_runtime`, `repair_action`, `parts_wait`, `sensor_quality`, and the censoring/end-of-observation reason. Maintenance-induced configuration changes are new covariates, not innocuous annotations.

This distinction matters for reliability **growth**. A falling observed failure rate might reflect genuinely improved design, reduced load, reporting changes, or selective replacement of bad units. An analysis that discards retired or unobserved units can make reliability look better even when field risk has not improved. Trace the fleet population and exposure source before crediting an intervention.

## 9. Derive a mechanism-based verification question

Suppose engineering proposes the common-cause shock probability of 5%. The illustrative redundant-system calculation gives 0.9405 mission survival, but the number 5% needs a physical basis. Ask which mechanisms—power outage, common firmware deadlock, environmental flooding, erroneous operator command—can disable both channels. Develop an independent fault-tree or stress/incident model, then connect each quantitative assumption to actual failure evidence and mitigation. If common causes are not adequately bounded, the architecture may not justify redundancy credit.

A strong reliability argument combines mechanism, architecture, test exposure, uncertainty and configuration. Its conclusion should state *the mission duration, expected environment and precisely which failure definition it supports*. It must not label 0.9405 as a verified field success rate based on eight artificial modules and an invented shock probability.


### Sources and curriculum connections

- [NIST/SEMATECH Engineering Statistics Handbook, Chapter 8 — Reliability](https://www.nist.gov/publications/nistsematech-engineering-statistics-handbook-chapter-8-reliability) explains survival, lifetime distributions, test design and censoring.
- [NIST, estimation from censored data](https://www.itl.nist.gov/div898/handbook/apr/section4/apr41.htm) discusses model fitting and its limitations.
- [Book 10, Chapter 8 — Reliability evidence](../B10/chapters/08-analyze-reliability-availability-maintainability-degradation-and-cen.md), [Book 7, Chapter 7 — RAM design](../B7/chapters/07-design-for-reliability-availability-and-maintainability.md), [Book 8, Chapter 8 — Reliability testing](../B8/chapters/08-plan-environmental-quality-reliability-maintainability-.md).
- **Curriculum:** EN.645.756, week 8; EN.645.768, reliability-informed design; EN.645.769, evidence sufficiency; EN.645.757, stochastic-model assumptions.

**Exercise:** recompute the estimate if one formerly censored unit fails at 90 hours. Update both \(d\) and total exposure, calculate \(R(50)\), and state which distributional and censor assumptions remain untested.
