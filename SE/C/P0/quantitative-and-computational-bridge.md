# Optional bridge — Quantitative and computational readiness

[Back to Phase 0](OVERVIEW.md) · [Back to program README](OVERVIEW.md)

## Purpose

This bridge is for learners who do not yet meet the quantitative and computational gate required before the Phase 3 modeling, simulation, statistics, and analytics sequence. It is not a substitute for those courses. It establishes enough fluency to follow derivations, inspect data, write reproducible calculations, and recognize when a result is numerically or statistically indefensible.

## Tool path

Use:

- a spreadsheet with formulas, tables, and charts;
- Python with a notebook environment, or R, MATLAB, Julia, or an equivalent reproducible computational tool;
- Git or another version-control system;
- Markdown for assumptions, methods, and result interpretation.

## Exit gate

The bridge is complete when the learner can:

1. manipulate algebraic expressions, units, ratios, rates, and logarithms;
2. interpret functions, graphs, derivatives, accumulation, and simple differential relationships;
3. calculate and interpret probability, conditional probability, expectation, variance, and common distributions;
4. summarize data with appropriate descriptive statistics and visualizations;
5. construct and interpret a confidence interval and distinguish statistical from practical significance;
6. fit and diagnose a basic linear regression without treating correlation as causation;
7. build a transparent spreadsheet model with assumptions, checks, and sensitivity cases;
8. write a reproducible script or notebook that imports data, performs calculations, creates figures, and records versions and assumptions.

Recommended threshold: **80%**, with no critical error involving units, probability bounds, data provenance, reproducibility, or interpretation.

## Eight-week bridge

Plan on **7–10 hours per week**.

### Week 1 — Algebra, units, functions, and engineering estimates

- Rearrange equations and solve for unknowns.
- Work with proportions, percentages, dimensional analysis, and orders of magnitude.
- Plot linear, polynomial, exponential, and logarithmic relationships.
- Build a unit-checked shuttle energy and charging estimate.

**Deliverable:** calculation notebook and independent hand-check.

### Week 2 — Rates, derivatives, accumulation, and simple dynamic relationships

- Interpret slope as a rate of change and area as accumulation.
- Use finite differences and numerical integration on sampled data.
- Relate a simple differential equation to physical or operational behavior.
- Analyze vehicle energy use, queue growth, or inventory accumulation over time.

**Deliverable:** rate/accumulation analysis with plots and interpretation.

### Week 3 — Probability and conditional reasoning

- Use sample spaces, complements, unions, intersections, and conditional probability.
- Apply Bayes' rule to a bounded diagnostic problem.
- Calculate expectation and variance for discrete outcomes.
- Distinguish independence from lack of correlation.

**Deliverable:** reliability or diagnostic-evidence problem set with a probability-tree or table.

### Week 4 — Random variables and common distributions

- Interpret Bernoulli, binomial, Poisson, normal, exponential, and uniform distributions.
- Select candidate distributions based on mechanism and support.
- Compare mean behavior with tail behavior.
- Simulate samples with a fixed random-seed policy.

**Deliverable:** distribution comparison notebook and model-selection rationale.

### Week 5 — Descriptive statistics, data quality, and visualization

- Compute median, mean, variance, standard deviation, quantiles, and robust summaries.
- Detect missingness, duplicates, impossible values, censoring, and inconsistent units.
- Create honest histograms, boxplots, scatterplots, and time-series plots.
- Maintain a data dictionary and provenance note.

**Deliverable:** cleaned synthetic operations dataset, data-quality report, and figures.

### Week 6 — Sampling, confidence intervals, and practical significance

- Explain population, sample, estimator, sampling distribution, and standard error.
- Construct confidence intervals for a mean or proportion under stated assumptions.
- Distinguish a confidence interval from a probability statement about a fixed parameter.
- Evaluate whether an observed difference is operationally meaningful.

**Deliverable:** service-performance comparison with assumptions and limitations.

### Week 7 — Correlation, linear regression, and diagnostic limits

- Fit a simple and a multiple linear regression.
- Interpret coefficients conditionally rather than causally.
- Inspect residuals, leverage, nonlinearity, and extrapolation risk.
- Compare training fit with held-out or cross-validated performance at an introductory level.

**Deliverable:** regression notebook, diagnostic plots, and a non-claim statement.

### Week 8 — Reproducible engineering analysis capstone

Analyze a synthetic campus mobility dataset and answer a bounded question such as:

> Under what demand and operating conditions is the current service likely to violate a wait-time objective, and which input appears most decision-relevant?

Submit:

- raw and processed data;
- data dictionary and provenance record;
- spreadsheet cross-check;
- executable notebook or script;
- environment/package record;
- figures generated from source;
- uncertainty and sensitivity discussion;
- a two-page decision memo;
- a 5–8 minute recorded walkthrough.

## Critical failures

- inconsistent or missing units;
- probabilities below zero or above one;
- silent deletion or alteration of data;
- causal claims from correlation alone;
- reporting only an average when tails drive the decision;
- unreproducible figures or calculations;
- extrapolation beyond the evidence without a limitation statement;
- a numerical answer with no decision interpretation.

## Readiness-review questions

1. When is the median more informative than the mean?
2. What does a 95% confidence interval mean?
3. Why can two variables be correlated without one causing the other?
4. What information is lost by replacing a distribution with its average?
5. How do units help detect modeling errors?
6. Why must random-number seeds and package versions be recorded?
7. What residual pattern would make a linear model questionable?
8. What result would cause your capstone recommendation to change?

A learner who can reproduce the capstone from a clean checkout and defend these answers is ready for Phase 3.
