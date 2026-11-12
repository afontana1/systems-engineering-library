# Book 14 — Decision Science and Analytics in Systems Engineering

*Phase 3: Quantitative systems engineering · Complete 12-week course-aligned book companion*

This book supplies long-form explanatory chapters, example reasoning, reproducible calculations and fictional laboratories for every week of the original **EN.645.784** guide. The original guide sets assessed requirements and rubrics; the chapters and labs prepare you to meet them. All Northstar data is synthetic.

**Start here:** [Open the offline book website](OPEN-BOOK.html) · [Course guide](../../C/P3/EN645784.md) · [Earlier concise companion](../P3-text/README.md)

## Reading sequence

- **Week 1:** [Frame the decision, distinguish problem types, and expose decision-process risk](chapters/01-frame-the-decision-distinguish-problem-types-and-expose-decision-pro.md) → [Hypothetical lab](labs/lab-01-frame-the-decision-distinguish-problem-types-and-expose-decision-pro.md)
- **Week 2:** [Translate stakeholder values into objectives, measures, and value structure](chapters/02-translate-stakeholder-values-into-objectives-measures-and-value-stru.md) → [Hypothetical lab](labs/lab-02-translate-stakeholder-values-into-objectives-measures-and-value-stru.md)
- **Week 3:** [Model decisions, uncertainties, evidence, constraints, and alternatives](chapters/03-model-decisions-uncertainties-evidence-constraints-and-alternatives.md) → [Hypothetical lab](labs/lab-03-model-decisions-uncertainties-evidence-constraints-and-alternatives.md)
- **Week 4:** [Apply constraints, dominance, and Pareto analysis to the selection problem](chapters/04-apply-constraints-dominance-and-pareto-analysis-to-the-selection-pro.md) → [Hypothetical lab](labs/lab-04-apply-constraints-dominance-and-pareto-analysis-to-the-selection-pro.md)
- **Week 5:** [Converge on a preferred selection using transparent value and decision methods](chapters/05-converge-on-a-preferred-selection-using-transparent-value-and-decisi.md) → [Hypothetical lab](labs/lab-05-converge-on-a-preferred-selection-using-transparent-value-and-decisi.md)
- **Week 6:** [Visualize, communicate, and defend the pilot selection decision](chapters/06-visualize-communicate-and-defend-the-pilot-selection-decision.md) → [Hypothetical lab](labs/lab-06-visualize-communicate-and-defend-the-pilot-selection-decision.md)
- **Week 7:** [Reframe the engineering design problem and generate alternatives through morphology](chapters/07-reframe-the-engineering-design-problem-and-generate-alternatives-thr.md) → [Hypothetical lab](labs/lab-07-reframe-the-engineering-design-problem-and-generate-alternatives-thr.md)
- **Week 8:** [Formulate parametric design and conduct multiobjective search](chapters/08-formulate-parametric-design-and-conduct-multiobjective-search.md) → [Hypothetical lab](labs/lab-08-formulate-parametric-design-and-conduct-multiobjective-search.md)
- **Week 9:** [Design computational experiments to learn efficiently from the design space](chapters/09-design-computational-experiments-to-learn-efficiently-from-the-desig.md) → [Hypothetical lab](labs/lab-09-design-computational-experiments-to-learn-efficiently-from-the-desig.md)
- **Week 10:** [Build, validate, and use surrogate models without hiding approximation error](chapters/10-build-validate-and-use-surrogate-models-without-hiding-approximation.md) → [Hypothetical lab](labs/lab-10-build-validate-and-use-surrogate-models-without-hiding-approximation.md)
- **Week 11:** [Analyze uncertainty, sensitivity, robustness, regret, and value of information](chapters/11-analyze-uncertainty-sensitivity-robustness-regret-and-value-of-infor.md) → [Hypothetical lab](labs/lab-11-analyze-uncertainty-sensitivity-robustness-regret-and-value-of-infor.md)
- **Week 12:** [Integrate, communicate, and defend the engineering design decision](chapters/12-integrate-communicate-and-defend-the-engineering-design-decision.md) → [Hypothetical lab](labs/lab-12-integrate-communicate-and-defend-the-engineering-design-decision.md)

## NS-DA14.1 campus mobility decision-science laboratory

The twelve chapters share the [NS-DA14.1 controlled decision dossier](case/INDEX.html), including the [course-based six-alternative inputs and explicit teaching assumptions](case/decision-inputs.json), [reproducible standard-library analyzer](tools/step03_book14_decision.py), [pilot screening](case/pilot-screening.csv), [full design/rejection table](case/design-candidates.csv), [nondominated finite-grid designs](case/efficient-designs.csv), [factorial experiment](case/factorial-doe.csv), [surrogate holdout](case/surrogate-holdout.csv), [value-of-information computations](case/summary.json), [morphology register](case/morphology.csv) and [evidence/credibility register](case/evidence-register.csv). The six course pilot alternatives are preserved unchanged. All new thresholds, utility weights, design equations and likelihoods are explicitly synthetic; this case is **HOLD** for real decisions and does not supersede Book 11–13 validation boundaries.

## Engineering evidence discipline

Follow a traceable chain of **question → representation → assumption/data → computation or explanation → sensitivity → supported claim → owner and next evidence**. Validate mathematical examples for their assumptions, not simply arithmetic. Do not treat a hypothetical result as operational validation.

## Computational practice

See [Notebooks](notebooks/README.md), [Synthetic datasets](datasets/README.md), [Diagrams](diagrams/README.md), and [Calculation tools](tools/README.md). The notebooks provide reproducible exercises; the book text can be read offline with no software dependencies.


## Deeper concept readings

- [Robust optimization: feasibility before preference](../T/18-robust-optimization.md)
