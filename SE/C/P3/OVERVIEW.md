# Phase 3 — Quantitative analysis and model-driven decision support

Phase 3 develops the quantitative evidence needed to support systems-engineering decisions under variability, uncertainty, incomplete information, and competing objectives. The phase moves from foundational modeling-and-simulation practice through decision analysis, systems dynamics, stochastic performance modeling, MBSE-connected analytics, and advanced multi-domain simulation.

This is not a collection of disconnected mathematics courses. Every course must answer four questions:

1. **What decision or claim does the analysis support?**
2. **What model, data, assumptions, and uncertainty produce the result?**
3. **How credible is the result for the intended use?**
4. **What would cause the recommendation to change?**

[Back to program README](OVERVIEW.md)

---

## 1. Recommended sequence

1. [**EN.645.757 — Foundations of Modeling and Simulation in Systems Engineering**](EN645757.md)
2. [**EN.645.784 — Decision Science & Analytics in Systems Engineering**](EN645784.md)
3. [**EN.645.781 — Systems Thinking and Systems Dynamics**](EN645781.md)
4. [**EN.645.756 — Metrics, Modeling, and Simulation for Systems Engineering**](EN645756.md)
5. [**EN.645.632 — Applied Analytics for Model Based Systems Engineering**](EN645632.md)
6. [**EN.645.758 — Advanced Systems Modeling and Simulation**](EN645758.md)

After completing EN.645.757 and EN.645.784, EN.645.781 and EN.645.756 may be studied in either order. EN.645.632 may begin after EN.645.631, but it is more valuable after the learner has foundational simulation and decision-analysis experience. EN.645.758 remains last because it assumes stronger statistics, experimentation, multi-domain modeling, and model-credibility judgment.

## 2. Phase entry gate

Before beginning Phase 3, the learner should be able to:

* define a decision, stakeholder, system boundary, lifecycle phase, and evidence need;
* write or evaluate a measurable requirement, MOE, MOP, and verification criterion;
* use a spreadsheet with formulas, charts, and scenario tables;
* write a small Python, R, MATLAB, Julia, or equivalent script;
* interpret mean, median, variance, standard deviation, percentile, probability, confidence interval, and correlation;
* distinguish verification, validation, and decision acceptance;
* maintain versioned source, data, assumptions, results, and decision records.

A learner who cannot yet meet these outcomes should complete the quantitative/computational bridge in Phase 0 before continuing.

## 3. Shared phase case

### Autonomous Campus Mobility 2030 — Analytic Evidence Program

Phase 3 uses the concept, design, integration, and T&E artifacts from Phase 2 as a controlled input. The learner becomes the analytic lead for a campus mobility program that must decide how to improve service while controlling cost, safety risk, accessibility, congestion, energy use, and operational disruption.

The program provides a common context, but each course asks a different class of question:

| Course | Primary analytic question |
|---|---|
| EN.645.757 | Which model form and simulation process can credibly support a lifecycle decision? |
| EN.645.784 | How should objectives, preferences, evidence, risk, and uncertainty be combined into a decision? |
| EN.645.781 | What feedback structures and delays create observed long-term behavior? |
| EN.645.756 | How do stochastic performance measures change with use, environment, and design? |
| EN.645.632 | How can analytic models, queries, and results be connected to the authoritative MBSE baseline? |
| EN.645.758 | How can multiple advanced models be composed, calibrated, experimented with, and assessed? |

The Phase 2 recommendation is not automatically accepted as correct. Analytic evidence may confirm it, constrain it, or reopen it.

## 4. Phase-wide model and data rules

Every model must have:

* a named decision owner and intended use;
* a bounded system, environment, time horizon, and level of resolution;
* explicit assumptions, simplifications, exclusions, and known limitations;
* input-data provenance and quality assessment;
* versioned source and executable instructions;
* verification evidence that the implementation matches the conceptual and computational specification;
* validation evidence appropriate to the intended use;
* uncertainty and sensitivity treatment proportional to decision consequence;
* a result-to-decision trace and a statement of conditions under which the result should not be used.

Screenshots, plots, and dashboards are communication products, not substitutes for source, data, logic, or provenance.

## 5. Computational reproducibility policy

Maintain a common repository structure:

* `/00-governance-and-decisions`
* `/01-problem-and-conceptual-model`
* `/02-data-and-input-models`
* `/03-model-source`
* `/04-verification-and-tests`
* `/05-experiments`
* `/06-results-and-uncertainty`
* `/07-vva-and-credibility`
* `/08-reviews-and-handoffs`

Each executable result must record:

* software and package versions;
* random-number seed policy;
* input file identifiers and hashes where practical;
* configuration and parameter set;
* run length, warm-up, replications, and stopping conditions;
* analysis script version;
* output file and figure generation steps.

## 6. Phase review gates

| Gate | Purpose | Minimum evidence |
|---|---|---|
| Modeling Purpose Review | Confirm decision, intended use, model class, scope, and credibility needs | Decision statement, conceptual model, candidate method comparison, data plan |
| Model Readiness Review | Confirm implementation, input models, verification, and experiment readiness | Tests, traces, input analysis, run controls, unresolved defects |
| Analysis and Decision Review | Confirm output analysis, uncertainty, sensitivity, and interpretation | Reproducible runs, intervals, diagnostics, scenario/sensitivity results |
| Credibility/Use Review | Decide whether the model is acceptable for the stated use | V&V evidence, limitations, risk, accreditation/use recommendation |
| Phase Portfolio Review | Demonstrate progression across model forms and decisions | Controlled models, notebooks, reports, review records, oral defense |

## 7. Relationship among Phase 3 courses

Repeated topics must become more advanced rather than merely repeated:

* **EN.645.757** introduces intended use, conceptual modeling, discrete-event simulation, inputs, outputs, experiments, and credibility.
* **EN.645.784** deepens decision framing, value models, influence diagrams, Bayesian reasoning, multiobjective selection, and robustness.
* **EN.645.781** shifts from event/process behavior to feedback, accumulation, delays, nonlinear dynamics, policy resistance, and leverage.
* **EN.645.756** deepens stochastic characterization, DOE, statistical inference, performance surfaces, uncertainty, and lifecycle metrics.
* **EN.645.632** makes the analytics queryable and traceable inside an MBSE/digital-thread environment.
* **EN.645.758** integrates continuous, discrete, physical, real-time, interoperable, and composable simulations with advanced experimentation.

## 8. Workload and pacing

Fully expanded courses target approximately 10–12 hours per week. Quantitative work often takes longer when code, data, or models fail. Plan additional recovery time for:

* tool installation and environment management;
* debugging and verification;
* data cleaning and input-model analysis;
* long simulation runs;
* review and revision after credibility challenges.

Do not proceed merely because a model runs. Progress requires the weekly mastery gate and a reviewable evidence package.

## 9. Current development status

| Course | Status | Next action |
|---|---|---|
| EN.645.757 Foundations of Modeling and Simulation | Fully expanded | Complete and pilot the course |
| EN.645.784 Decision Science & Analytics | Fully expanded | Complete and pilot the course |
| EN.645.781 Systems Thinking and Systems Dynamics | Fully expanded | Complete and pilot the course |
| EN.645.756 Metrics, Modeling, and Simulation | Fully expanded | Complete and pilot the course |
| EN.645.632 Applied Analytics for MBSE | Fully expanded | Complete and pilot the course |
| EN.645.758 Advanced Systems Modeling and Simulation | Fully expanded | Complete and pilot the course |

All six Phase 3 courses are fully expanded. The remaining work is controlled piloting, workload calibration, tool-path verification, and maintenance of external references.

## 10. Phase exit criteria

Phase 3 is complete when the learner can:

* select and defend a model form based on a decision and intended use;
* construct conceptual, computational, and executable models with traceability;
* characterize stochastic inputs and outputs without substituting averages for distributions;
* design and analyze simulation experiments;
* perform uncertainty, sensitivity, robustness, and error analyses;
* verify implementations and validate model behavior against appropriate referents;
* distinguish model correctness, model validity, credibility, and authorization for a specific use;
* connect analytic evidence to requirements, architecture, risk, and decisions;
* communicate what the model supports, what it does not support, and what would change the conclusion.

---

## Course files

- [EN.645.757 — Foundations of Modeling and Simulation in Systems Engineering](EN645757.md)
- [EN.645.784 — Decision Science & Analytics in Systems Engineering](EN645784.md)
- [EN.645.781 — Systems Thinking and Systems Dynamics](EN645781.md)
- [EN.645.756 — Metrics, Modeling, and Simulation for Systems Engineering](EN645756.md)
- [EN.645.632 — Applied Analytics for Model Based Systems Engineering](EN645632.md)
- [EN.645.758 — Advanced Systems Modeling and Simulation](EN645758.md)

[Back to program README](OVERVIEW.md)
