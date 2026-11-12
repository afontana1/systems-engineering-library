
---

## Step 04 advanced integration — bounded claims and measurement error (NS-AA4.1)

### A1. Define the target population before inspecting the results

The [controlled case inputs](../data/advanced-case.json) and [individual request outcomes](../data/advanced-requests.csv) describe **50 invented eligible requests**: 12 accessible and 38 standard. The population is declared before scoring, and two standard requests are unserved. Let \(I_i\) indicate that request \(i\) has a confirmed pickup and let \(W_i\) denote its measured wait when a pickup exists. For a wait ceiling \(\tau=20\) minutes, define the all-request timely fulfillment estimator

\[
\widehat F(\tau)=\frac{1}{N}\sum_{i=1}^{N}I_i\,\mathbf{1}(W_i\le\tau).
\]

An unserved request contributes zero, **not a deleted observation**. A separate completion estimator is \(\widehat C=N^{-1}\sum I_i\). The denominators remain \(N\), even when an outcome is missing. This specification prevents the erroneous calculation \(46/48=95.83\%\) from being reported as the mission fulfillment rate. The case yields \(48/50=96\%\) completion but only \(46/50=92\%\) measured timely fulfillment. The accessible subgroup yields \(11/12=91.67\%\) measured timely fulfillment.

These are descriptive proportions from a purposely constructed list, **not estimates of a representative population**. Confidence intervals, hypothesis tests, and probability guarantees require an explicit sampling or operational data-generating model. A simulated file with fifty rows does not become fifty statistically independent experimental replications merely because it has fifty IDs.

### A2. Convert timing uncertainty into a conservative compliance rule

Suppose each endpoint timestamp has bounded absolute error \(\epsilon=0.4\) minutes. A measured duration \(\widehat W=t_p^{obs}-t_r^{obs}\) has worst-case error \(|W-\widehat W|\le2\epsilon=0.8\) minutes. To **guarantee** a pickup occurred by \(\tau\) within this deterministic error envelope, require \(\widehat W+0.8\le20\). Hence the observed threshold becomes \(19.2\) minutes, not \(20\).

The case includes one accessible request at 19.6 minutes and two standard requests at 19.5 minutes. All three count as timely in the unguarded report, but none is guaranteed timely under the stated bound. The guarded count is therefore \(43/50=86\%\); accessible is \(10/12=83.33\%\). The illustrative requirements are 90% all-request timely fulfillment and 85% accessible timely fulfillment, so **both fail** after guard-banding, even though both unguarded summaries pass.

This is a *bounding exercise*, not a statement that actual clock errors always attain their worst-case signs. It is intentionally more conservative than a probabilistic measurement model. If errors are random, a separate calibration and dependence study could support a different adjudication rule, but must be approved before data inspection.

### A3. Show the boundary of a service claim

Meeting a threshold in one listed scenario cannot establish mission validation. Requests are invented; there is no evidence of neighborhood representativeness, disability-access consultation, clock calibration, dispatch safety, or demand surges. Nor does an observed subgroup proportion establish parity or fairness: service outcomes may differ in ways a two-group split does not reveal. An authorized stakeholder review must determine which disparities are relevant and what outcomes matter.

**Exercise.** If the endpoint bound were 0.1 minutes instead of 0.4, what would the guarded threshold be? Would the three borderline requests count? **Worked solution:** the total guard is \(0.2\) minutes, so the observed cutoff is \(19.8\). All three (19.5, 19.5, 19.6) would be included: guarded all-request fulfillment would be \(46/50=92\%\), accessible \(11/12=91.67\%\). This only changes a *measurement premise*; it does not validate that a 0.1-minute bound is real.

**Reproduce:** `python3 SE/K/A/code/advanced_case.py` from the repository root. The [case analysis source](../code/advanced_case.py) explicitly rejects duplicate requests, missing pickup times, and malformed groups. Continue with the [typed-evidence model in Part II](02-models.html).
