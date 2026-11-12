# Engineering method guides

These guides give a full technical explanation of methods needed in the curriculum: the underlying model, assumptions, a worked engineering calculation or executable state model, interpretation, limitations, and a path to the course and textbook material. They supplement the canonical concept articles and course-aligned textbooks without displacing them.

## Foundations: first set

1. [Requirements engineering and verification evidence](requirements-verification-handbook.md) — requirement formulation, timing budgets, test design, statistical acceptance, and evidence sufficiency.
2. [Bayesian decisions and value of information](bayesian-decision-handbook.md) — posterior actions, EVPI/EVSI, sensitivity, and uncertainty.
3. [MBSE semantics and executable checks](mbse-semantic-modeling-handbook.md) — typed graph semantics, parametric feasibility, and evidence configuration.

## Expanded methods: second set

4. [Statistical inference and design of experiments](statistical-inference-and-experiments.md) — estimands, confidence intervals, factorial effects, interactions, and reproducible experiment analysis.
5. [Reliability analysis with censored failure evidence](reliability-and-censored-evidence.md) — hazard, exponential lifetime MLE, Kaplan–Meier, dependence, and repair-versus-survival interpretation.
6. [Pareto search, scenario regret, and robust design](pareto-and-robust-design.md) — dominance, constraints, scenario probabilities, regret, robust feasibility, and engineering preference models.
7. [MBSE behavioral contracts and bounded checking](mbse-behavioral-contracts.md) — transition relations, state invariants, idempotence, counterexample traces, and finite-model limitations.

## Simulation, uncertainty, and software contracts: third set

8. [Simulation output analysis and model credibility](simulation-output-and-credibility.md) — warm-up, independent replications, paired common random numbers, uncertainty intervals, verification versus validation, and NASA-style intended-use statements.
9. [Uncertainty propagation with dependent inputs](correlated-uncertainty-propagation.md) — covariance propagation, delta method, correlated Gaussian inputs, Monte Carlo tail estimates, and input-model limitations.
10. [UML and OCL software contracts](uml-ocl-software-contracts.md) — class-model invariants, preconditions and postconditions, snapshot counterexamples, and persistence/concurrency enforcement boundaries.

## Safety, evidence, and one connected engineering case: fourth set

11. [Safety engineering, fault trees and assurance](safety-fault-trees-and-assurance.md) — hazard/control distinction, minimal cut sets, common-cause dependencies, numeric sensitivity, and claim–evidence review.
12. [MBSE baselines and evidence currency](model-baselines-and-evidence.md) — typed graph constraints, stale evidence, change-impact queries, and precise limits on JSON versus actual SysML v2 validation.
13. [Campus Mobility: integrated engineering case](campus-mobility-engineering-case.md) — one synthetic case through needs, requirements, interfaces, architecture, hazard analysis, alternatives, acceptance evidence and release decision.

## Language validation, advanced simulation, transactional correctness and case artifacts: fifth set

14. [SysML v2 modeling and traceability](sysml-v2-modeling-and-traceability.md) — typed definitions and usages, trace semantics, explicit OMG pilot-parser validation procedure, and cross-document audit; the included illustration is *not* claimed as parser-validated SysML.
15. [Simulation calibration and rare-event analysis](simulation-calibration-and-rare-events.md) — Poisson likelihood and profile interval, withheld count challenge, normal-tail importance sampling and the distinction between numerical precision and physical credibility.
16. [Transactional concurrency and assurance](transactional-concurrency-and-assurance.md) — a reproducible check-then-act race, partial unique index, retries, local invariants and distributed boundaries.
17. [Campus Mobility controlled artifact package](campus-mobility-engineering-artifacts.md) — editable requirement set, interface control extract, VCRM, hazard/assurance register, baseline change-impact record and auditable cross-document identities.

Each guide has an editable Markdown source and a corresponding `.html` reader; the site uses its **local MathJax**, with no online math service. The reproducible programs use the Python standard library; Phases 4–5 add fault-tree, baseline-audit, document-crosswalk, calibration and transactional-concurrency programs with a controlled and a deliberately stale JSON fixture. All values are synthetic teaching examples and are not field measurements or guarantees.

## Course and textbook crosswalk

| Guide | Curriculum entry points | Core textbook starting points |
|---|---|---|
| Requirements and verification | EN.645.662; EN.645.769 | [Book 1 ch 4](../B1/chapters/04-requirements.md), [Book 8 ch 10](../B8/chapters/10-analyze-results-determine-evidence-sufficiency-and-reco.md) |
| Bayesian decision analysis | EN.645.784 | [Book 14 ch 11](../B14/chapters/11-analyze-uncertainty-sensitivity-robustness-regret-and-value-of-infor.md) |
| MBSE semantics | EN.645.631 | [Book 3 ch 4](../B3/chapters/04-requirements-modeling-relationship-semantics-.md), [ch 8](../B3/chapters/08-values-units-measures-constraints-parametrics.md) |
| Statistical inference and DOE | EN.645.756; EN.645.769; EN.645.757 | [Book 10 ch 4](../B10/chapters/04-use-estimation-confidence-intervals-hypothesis-equivalence-and-engin.md), [ch 5](../B10/chapters/05-design-efficient-experiments-with-factors-responses-noise-power-rand.md), [ch 6](../B10/chapters/06-analyze-factorial-experiments-interactions-diagnostics-and-confirmat.md), [Book 8 ch 4](../B8/chapters/04-apply-measurement-science-statistics-doe-and-sample-rat.md) |
| Reliability and censoring | EN.645.756; EN.645.769; EN.645.768 | [Book 10 ch 8](../B10/chapters/08-analyze-reliability-availability-maintainability-degradation-and-cen.md), [Book 7 ch 7](../B7/chapters/07-design-for-reliability-availability-and-maintainability.md) |
| Pareto and robust trades | EN.645.784; EN.645.767 | [Book 14 ch 4](../B14/chapters/04-apply-constraints-dominance-and-pareto-analysis-to-the-selection-pro.md), [ch 8](../B14/chapters/08-formulate-parametric-design-and-conduct-multiobjective-search.md) |
| MBSE behavior and model checking | EN.645.631; EN.645.632; EN.605.704 | [Book 3 ch 5](../B3/chapters/05-behavior-modeling-use-cases-activities-action.md), [ch 11](../B3/chapters/11-model-quality-queries-reports-change-impact-g.md) |

| Simulation output and credibility | EN.645.757; EN.645.758 | [Book 11 ch 8](../B11/chapters/08-analyze-transient-and-steady-state-output-with-defensible-run-contro.md), [ch 11](../B11/chapters/11-plan-and-evaluate-verification-validation-credibility-and-accreditat.md) |
| Correlated uncertainty propagation | EN.645.756; EN.645.758 | [Book 10 ch 9](../B10/chapters/09-propagate-uncertainty-with-analytic-monte-carlo-simulation-and-sensi.md), [Book 12 ch 8](../B12/chapters/08-model-natural-and-man-made-environments-as-dynamic-correlated-scenar.md) |
| UML/OCL software model contracts | EN.605.704; EN.645.631 | [Book 3 ch 11](../B3/chapters/11-model-quality-queries-reports-change-impact-g.md), [Book 9 ch 11](../B9/chapters/11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md) |

| Safety, fault trees and assurance | EN.645.764; EN.645.768; EN.645.769; EN.645.771 | [Book 1 ch 10](../B1/chapters/10-failures-and-controls.md), [Book 7 ch 7](../B7/chapters/07-design-for-reliability-availability-and-maintainability.md) |
| Model baselines and evidence currency | EN.645.631; EN.645.768; EN.645.769 | [Book 3 ch 11](../B3/chapters/11-model-quality-queries-reports-change-impact-g.md), [Book 9 ch 11](../B9/chapters/11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md) |
| Campus Mobility connected case | EN.645.662; EN.645.631; EN.645.768; EN.645.769; EN.645.784 | [Book 1 ch 11](../B1/chapters/11-realization-and-evidence.md), [Book 8 ch 8](../B8/chapters/08-plan-environmental-quality-reliability-maintainability-.md) |

| SysML v2 language and traceability | EN.645.631; EN.645.632; EN.645.768 | [Book 3 ch 4](../B3/chapters/04-requirements-modeling-relationship-semantics-.md), [Book 9 ch 11](../B9/chapters/11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md) |
| Simulation calibration and rare events | EN.645.757; EN.645.758; EN.645.756 | [Book 11 ch 8](../B11/chapters/08-analyze-transient-and-steady-state-output-with-defensible-run-contro.md), [ch 11](../B11/chapters/11-plan-and-evaluate-verification-validation-credibility-and-accreditat.md) |
| Concurrency and transactional assurance | EN.605.704; EN.645.764; EN.645.631 | [Book 3 ch 5](../B3/chapters/05-behavior-modeling-use-cases-activities-action.md), [Book 9 ch 11](../B9/chapters/11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md) |
| Campus Mobility controlled artifacts | EN.645.662; EN.645.768; EN.645.769; EN.645.764 | [Book 1 ch 4](../B1/chapters/04-requirements.md), [Book 8 ch 10](../B8/chapters/10-analyze-results-determine-evidence-sufficiency-and-reco.md) |

## How to study a method

Start with the problem and assumptions, work the example by hand, reproduce the executable results, change one assumption and predict how the conclusion will change, then return to the course assessment. A project decision still requires validation of the relevant data, operating context, and decision authority. These guides are reference instruction, not automatic verification or certification.
