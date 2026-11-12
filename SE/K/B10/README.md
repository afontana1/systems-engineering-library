# Book 10 — Metrics, Modeling and Simulation for Systems Engineering

*Phase 3: Quantitative systems engineering · Complete 12-week course-aligned book companion*

This book supplies long-form explanatory chapters, example reasoning, reproducible calculations and fictional laboratories for every week of the original **EN.645.756** guide. The original guide sets assessed requirements and rubrics; the chapters and labs prepare you to meet them. All Northstar data is synthetic.

**Start here:** [Open the offline book website](OPEN-BOOK.html) · [Course guide](../../C/P3/EN645756.md) · [Earlier concise companion](../P3-text/README.md)

## Reading sequence

- **Week 1:** [Define the lifecycle technical-measurement strategy and decision chain](chapters/01-define-the-lifecycle-technical-measurement-strategy-and-decision-cha.md) → [Hypothetical lab](labs/lab-01-define-the-lifecycle-technical-measurement-strategy-and-decision-cha.md)
- **Week 2:** [Characterize probability distributions, tails, dependence, and stochastic performance](chapters/02-characterize-probability-distributions-tails-dependence-and-stochast.md) → [Hypothetical lab](labs/lab-02-characterize-probability-distributions-tails-dependence-and-stochast.md)
- **Week 3:** [Establish data provenance, sampling validity, exploratory analysis, and measurement uncertainty](chapters/03-establish-data-provenance-sampling-validity-exploratory-analysis-and.md) → [Hypothetical lab](labs/lab-03-establish-data-provenance-sampling-validity-exploratory-analysis-and.md)
- **Week 4:** [Use estimation, confidence intervals, hypothesis, equivalence, and engineering significance](chapters/04-use-estimation-confidence-intervals-hypothesis-equivalence-and-engin.md) → [Hypothetical lab](labs/lab-04-use-estimation-confidence-intervals-hypothesis-equivalence-and-engin.md)
- **Week 5:** [Design efficient experiments with factors, responses, noise, power, randomization, and blocking](chapters/05-design-efficient-experiments-with-factors-responses-noise-power-rand.md) → [Hypothetical lab](labs/lab-05-design-efficient-experiments-with-factors-responses-noise-power-rand.md)
- **Week 6:** [Analyze factorial experiments, interactions, diagnostics, and confirmation evidence](chapters/06-analyze-factorial-experiments-interactions-diagnostics-and-confirmat.md) → [Hypothetical lab](labs/lab-06-analyze-factorial-experiments-interactions-diagnostics-and-confirmat.md)
- **Week 7:** [Build and validate performance response models across use and environment](chapters/07-build-and-validate-performance-response-models-across-use-and-enviro.md) → [Hypothetical lab](labs/lab-07-build-and-validate-performance-response-models-across-use-and-enviro.md)
- **Week 8:** [Analyze reliability, availability, maintainability, degradation, and censored evidence](chapters/08-analyze-reliability-availability-maintainability-degradation-and-cen.md) → [Hypothetical lab](labs/lab-08-analyze-reliability-availability-maintainability-degradation-and-cen.md)
- **Week 9:** [Propagate uncertainty with analytic Monte Carlo simulation and sensitivity analysis](chapters/09-propagate-uncertainty-with-analytic-monte-carlo-simulation-and-sensi.md) → [Hypothetical lab](labs/lab-09-propagate-uncertainty-with-analytic-monte-carlo-simulation-and-sensi.md)
- **Week 10:** [Quantify requirement compliance, technical margin, allocation risk, and design options](chapters/10-quantify-requirement-compliance-technical-margin-allocation-risk-and.md) → [Hypothetical lab](labs/lab-10-quantify-requirement-compliance-technical-margin-allocation-risk-and.md)
- **Week 11:** [Update lifecycle evidence and decide among upgrade, replacement, retirement, or more information](chapters/11-update-lifecycle-evidence-and-decide-among-upgrade-replacement-retir.md) → [Hypothetical lab](labs/lab-11-update-lifecycle-evidence-and-decide-among-upgrade-replacement-retir.md)
- **Week 12:** [Integrate, reproduce, challenge, and defend the lifecycle analytics decision](chapters/12-integrate-reproduce-challenge-and-defend-the-lifecycle-analytics-dec.md) → [Hypothetical lab](labs/lab-12-integrate-reproduce-challenge-and-defend-the-lifecycle-analytics-dec.md)

## NS-QA10.1 quantitative evidence case

All twelve chapters share [one winter quantitative evidence dossier](case/INDEX.html). It includes a [controlled requirements register](case/requirements.csv), [factorial trial data](case/factorial-trials.csv), [right-censored life data](case/reliability-life.csv), [declared statistical assumptions](case/model-assumptions.json), [verification evidence](case/evidence-register.csv), an [evidence-chain diagram](case/analytics-evidence-chain.svg), and a [reproducible Python checker](tools/step03_book10_quantitative_check.py). Its modeled latency, energy, reliability and lifecycle-cost results support a **HOLD**, not an operational acceptance claim. All data are synthetic.

## Engineering evidence discipline

Follow a traceable chain of **question → representation → assumption/data → computation or explanation → sensitivity → supported claim → owner and next evidence**. Validate mathematical examples for their assumptions, not simply arithmetic. Do not treat a hypothetical result as operational validation.

## Computational practice

See [Notebooks](notebooks/README.md), [Synthetic datasets](datasets/README.md), [Diagrams](diagrams/README.md), and [Calculation tools](tools/README.md). The notebooks provide reproducible exercises; the book text can be read offline with no software dependencies.


## Deeper concept readings

- [Experimental design: ask a question the evidence can answer](../T/16-experimental-design.md)
