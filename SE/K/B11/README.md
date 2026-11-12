# Book 11 — Foundations of Modeling and Simulation

*Phase 3: Quantitative systems engineering · Complete 12-week course-aligned book companion*

This book supplies long-form explanatory chapters, example reasoning, reproducible calculations and fictional laboratories for every week of the original **EN.645.757** guide. The original guide sets assessed requirements and rubrics; the chapters and labs prepare you to meet them. All Northstar data is synthetic.

**Start here:** [Open the offline book website](OPEN-BOOK.html) · [Course guide](../../C/P3/EN645757.md) · [Earlier concise companion](../P3-text/README.md)

## Reading sequence

- **Week 1:** [Frame the M&S decision, intended use, terminology, and model-method trade space](chapters/01-frame-the-m-s-decision-intended-use-terminology-and-model-method-tra.md) → [Hypothetical lab](labs/lab-01-frame-the-m-s-decision-intended-use-terminology-and-model-method-tra.md)
- **Week 2:** [Develop the M&S plan and conceptual model before implementation](chapters/02-develop-the-m-s-plan-and-conceptual-model-before-implementation.md) → [Hypothetical lab](labs/lab-02-develop-the-m-s-plan-and-conceptual-model-before-implementation.md)
- **Week 3:** [Characterize data quality, probability, dependence, and stochastic input models](chapters/03-characterize-data-quality-probability-dependence-and-stochastic-inpu.md) → [Hypothetical lab](labs/lab-03-characterize-data-quality-probability-dependence-and-stochastic-inpu.md)
- **Week 4:** [Use M&S for needs, opportunity, current-state, and baseline analysis](chapters/04-use-m-s-for-needs-opportunity-current-state-and-baseline-analysis.md) → [Hypothetical lab](labs/lab-04-use-m-s-for-needs-opportunity-current-state-and-baseline-analysis.md)
- **Week 5:** [Implement discrete-event processes, resources, queues, priorities, and statistics](chapters/05-implement-discrete-event-processes-resources-queues-priorities-and-s.md) → [Hypothetical lab](labs/lab-05-implement-discrete-event-processes-resources-queues-priorities-and-s.md)
- **Week 6:** [Model detailed operations and complete computational verification](chapters/06-model-detailed-operations-and-complete-computational-verification.md) → [Hypothetical lab](labs/lab-06-model-detailed-operations-and-complete-computational-verification.md)
- **Week 7:** [Use simulation for concept exploration, alternatives, and scenario analysis](chapters/07-use-simulation-for-concept-exploration-alternatives-and-scenario-ana.md) → [Hypothetical lab](labs/lab-07-use-simulation-for-concept-exploration-alternatives-and-scenario-ana.md)
- **Week 8:** [Analyze transient and steady-state output with defensible run controls](chapters/08-analyze-transient-and-steady-state-output-with-defensible-run-contro.md) → [Hypothetical lab](labs/lab-08-analyze-transient-and-steady-state-output-with-defensible-run-contro.md)
- **Week 9:** [Apply simulation in design and development using selection, ranking, and design of experiments](chapters/09-apply-simulation-in-design-and-development-using-selection-ranking-a.md) → [Hypothetical lab](labs/lab-09-apply-simulation-in-design-and-development-using-selection-ranking-a.md)
- **Week 10:** [Use M&S to support integration, verification, validation, and test decisions](chapters/10-use-m-s-to-support-integration-verification-validation-and-test-deci.md) → [Hypothetical lab](labs/lab-10-use-m-s-to-support-integration-verification-validation-and-test-deci.md)
- **Week 11:** [Plan and evaluate verification, validation, credibility, and accreditation for intended use](chapters/11-plan-and-evaluate-verification-validation-credibility-and-accreditat.md) → [Hypothetical lab](labs/lab-11-plan-and-evaluate-verification-validation-credibility-and-accreditat.md)
- **Week 12:** [Apply M&S to production and sustainment, survey advanced methods, and defend the final baseline](chapters/12-apply-m-s-to-production-and-sustainment-survey-advanced-methods-and-.md) → [Hypothetical lab](labs/lab-12-apply-m-s-to-production-and-sustainment-survey-advanced-methods-and-.md)

## NS-MS11.1 integrated campus mobility case

All twelve chapters follow the [NS-MS11.1 decision and credibility dossier](case/INDEX.html), which includes controlled [model assumptions](case/model-assumptions.json), [requirements](case/requirements.csv), a [credibility register](case/credibility-register.csv), [simulation outputs](case/replication-output.csv), a [machine-readable summary](case/summary.json), a [process diagram](case/simulation-evidence-chain.svg) and a [reproducible Python simulator](tools/step03_book11_mobility.py). Using the course's synthetic 06:00–18:00 campus data, the current **single-request** mobility model supports a **HOLD**, not field or pilot qualification. Staffing, pooling, route travel and real-world validation are not established.

## Engineering evidence discipline

Follow a traceable chain of **question → representation → assumption/data → computation or explanation → sensitivity → supported claim → owner and next evidence**. Validate mathematical examples for their assumptions, not simply arithmetic. Do not treat a hypothetical result as operational validation.

## Computational practice

See [Notebooks](notebooks/README.md), [Synthetic datasets](datasets/README.md), [Diagrams](diagrams/README.md), and [Calculation tools](tools/README.md). The notebooks provide reproducible exercises; the book text can be read offline with no software dependencies.


## Deeper concept readings

- [Simulation credibility: verification, validation, and decision relevance](../T/19-simulation-credibility.md)
