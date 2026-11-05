# Measurement traceability and calibration: accuracy is a chain of evidence

**Canonical reference · Expanded reference · Internal editorial and worked-example checks; independent external peer review not performed**

## A calibration sticker is not a measurement argument

**Metrological traceability** is a property of a measurement *result*, established through a documented unbroken calibration chain to specified references, with each link contributing uncertainty. It is not a permanent status conferred on an instrument by one visit to a calibration lab. NIST emphasizes that traceability alone does not establish fitness for purpose: a correctly traceable result can still be too uncertain for a demanding threshold decision.

For a system performance test, distinguish the measurand (the quantity actually intended to be measured), the measuring system, its reference standards, its environment, and the computation used to produce the reported number. A motor temperature reading might be biased by sensor location, mounting, time response, channel electronics or an unrecorded firmware conversion even when the thermometer is calibrated. Calibration is one control within a larger measurement assurance system.

## Build an uncertainty budget

Suppose a dimensionally consistent measured result is `y = x + b`, with independent standard uncertainties `u_x` and `u_b` and negligible model nonlinearity. The combined standard uncertainty is `u_c = sqrt(u_x² + u_b²)`. In a **hypothetical** pressure measurement, `u_x = 0.20 kPa` and `u_b = 0.30 kPa`, so `u_c = sqrt(0.04+0.09) = 0.3606 kPa`. With coverage factor `k=2`, expanded uncertainty is approximately `0.7211 kPa`. Calling this a "95% interval" requires distribution and effective-degrees-of-freedom justification; `k=2` is only a common approximation under suitable conditions.

If errors are correlated, the general first-order form is `u_y² = sum_i sum_j (∂f/∂x_i)(∂f/∂x_j) cov(x_i,x_j)`. Dropping covariance terms without evidence can understate or overstate uncertainty. The model can also include quantization, drift, spatial gradients, repeated-observation variation, reference uncertainty, environmental influence and processing bias. Distinguish random variability of the process under test from uncertainty of the measuring instrument: they affect different decisions.

## Guard bands in acceptance decisions

Suppose a component is required not to exceed 10.0 kPa and the reported measurement is 9.6 kPa with expanded uncertainty 0.72 kPa. The nominal value passes, but the upper edge of the illustrative interval is 10.32 kPa. Under the conservative decision rule `accept only if measured value + U ≤ limit`, the unit is not accepted. That does **not** logically prove that it fails the specification; the outcome is inconclusive under the stated rule. A different decision rule requires explicit treatment of false acceptance, false rejection and coverage assumptions.

## Stable processes and calibration intervals

A one-day calibration result does not show that the measurement process was in control throughout a six-month test campaign. Track check standards, instrument drift, maintenance, channel substitutions, environmental shifts, and calibration interval evidence. When an instrument is found out of tolerance, assess the affected historical test population and potential decision reversals; merely recalibrating today does not repair yesterday's evidence. Repeatability and reproducibility studies help distinguish variation within an operator/instrument setup from variation across setups, but study design matters.

## A review-ready measurement statement

Report the measurand, result, units, uncertainty and coverage rationale, instrument and reference identifiers, calibration history, sensor position, operating state, conversion software revision, sampling plan, and applicable decision rule. A quality score or dashboard should never substitute for this evidence. Common errors include adding standard uncertainties arithmetically when independence applies, treating correlated measurements as independent, calling all uncertainty "measurement error," and using unguarded pass/fail thresholds with no risk allocation.

## Selected source-to-claim references

- **M1 · Measurement-result traceability, uncertainty and fitness-for-purpose distinction.:** [NIST metrological traceability policy and FAQ](https://www.nist.gov/metrology/metrological-traceability). Measurement-result traceability, uncertainty and fitness-for-purpose distinction.
- **M2 · Calibration, repeatability, reproducibility and stability of measurement processes.:** [NIST/SEMATECH Engineering Statistics Handbook, Measurement Process Characterization](https://www.nist.gov/publications/nistsematech-engineering-statistics-handbook-chapter-2-measurement-process). Calibration, repeatability, reproducibility and stability of measurement processes.

## Follow the knowledge

- **Prerequisites:** [Probability, dependence, and technical uncertainty](probability-and-dependence.md), [Measures of effectiveness and performance](metrics-hierarchy.md).
- **Related concepts:** [Environmental qualification: test severity is not operational realism](environmental-qualification-and-test-levels.md), [Statistical acceptance: sampling decisions are not proofs of perfection](statistical-acceptance-and-confidence.md), [Technical data governance: lineage, meaning, and controlled reuse](technical-data-governance-and-lineage.md).
- **Go deeper:** [Book 8 · Chapter 4: Measurement and statistical confidence](../B8/chapters/04-apply-measurement-science-statistics-doe-and-sample-rat.md), [Book 10 · Chapter 03 — Establish data provenance, sampling validity, exploratory analysis, and measurement uncertainty](../B10/chapters/03-establish-data-provenance-sampling-validity-exploratory-analysis-and.md), [Week 05 · Systems Engineering Process Improvement · Book chapter: Measurement system, variation, and baseline performance](../B17/chapters/05.md).
