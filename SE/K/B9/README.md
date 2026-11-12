# Book 9 — Applied Analytics for Model-Based Systems Engineering

*Phase 3: Quantitative systems engineering · Complete 12-week course-aligned book companion*

This book supplies long-form explanatory chapters, example reasoning, reproducible calculations and fictional laboratories for every week of the original **EN.645.632** guide. The original guide sets assessed requirements and rubrics; the chapters and labs prepare you to meet them. All Northstar data is synthetic.

**Start here:** [Open the offline book website](OPEN-BOOK.html) · [Course guide](../../C/P3/EN645632.md) · [Earlier concise companion](../P3-text/README.md)

## Reading sequence

- **Week 1:** [Receive the baseline, define intended use, and tailor the MBSE method and modeling plan](chapters/01-receive-the-baseline-define-intended-use-and-tailor-the-mbse-method-.md) → [Hypothetical lab](labs/lab-01-receive-the-baseline-define-intended-use-and-tailor-the-mbse-method-.md)
- **Week 2:** [Analyze stakeholders, mission, scenarios, outcomes, and measures in the authoritative model](chapters/02-analyze-stakeholders-mission-scenarios-outcomes-and-measures-in-the-.md) → [Hypothetical lab](labs/lab-02-analyze-stakeholders-mission-scenarios-outcomes-and-measures-in-the-.md)
- **Week 3:** [Develop and analyze the functional architecture from black-box behavior to allocated white-box functions](chapters/03-develop-and-analyze-the-functional-architecture-from-black-box-behav.md) → [Hypothetical lab](labs/lab-03-develop-and-analyze-the-functional-architecture-from-black-box-behav.md)
- **Week 4:** [Model state-based behavior, modes, exceptions, hazards, and temporal consistency](chapters/04-model-state-based-behavior-modes-exceptions-hazards-and-temporal-con.md) → [Hypothetical lab](labs/lab-04-model-state-based-behavior-modes-exceptions-hazards-and-temporal-con.md)
- **Week 5:** [Specify and evaluate the logical architecture and its responsibilities](chapters/05-specify-and-evaluate-the-logical-architecture-and-its-responsibiliti.md) → [Hypothetical lab](labs/lab-05-specify-and-evaluate-the-logical-architecture-and-its-responsibiliti.md)
- **Week 6:** [Specify interfaces, exchanges, allocations, ownership, and model-based change exposure](chapters/06-specify-interfaces-exchanges-allocations-ownership-and-model-based-c.md) → [Hypothetical lab](labs/lab-06-specify-interfaces-exchanges-allocations-ownership-and-model-based-c.md)
- **Week 7:** [Elicit, derive, validate, and query system requirements from the integrated analysis](chapters/07-elicit-derive-validate-and-query-system-requirements-from-the-integr.md) → [Hypothetical lab](labs/lab-07-elicit-derive-validate-and-query-system-requirements-from-the-integr.md)
- **Week 8:** [Build executable parametric models with units, provenance, constraints, and linked analytics](chapters/08-build-executable-parametric-models-with-units-provenance-constraints.md) → [Hypothetical lab](labs/lab-08-build-executable-parametric-models-with-units-provenance-constraints.md)
- **Week 9:** [Explore the trade space with alternatives, uncertainty, sensitivity, and model-based decision records](chapters/09-explore-the-trade-space-with-alternatives-uncertainty-sensitivity-an.md) → [Hypothetical lab](labs/lab-09-explore-the-trade-space-with-alternatives-uncertainty-sensitivity-an.md)
- **Week 10:** [Specify physical architectures, variants, configurations, instances, and lifecycle baselines](chapters/10-specify-physical-architectures-variants-configurations-instances-and.md) → [Hypothetical lab](labs/lab-10-specify-physical-architectures-variants-configurations-instances-and.md)
- **Week 11:** [Extend the modeling language and automate queries, validation rules, matrices, and generated products](chapters/11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md) → [Hypothetical lab](labs/lab-11-extend-the-modeling-language-and-automate-queries-validation-rules-m.md)
- **Week 12:** [Verify and validate the model, assess the design, respond to change, and defend the final baseline](chapters/12-verify-and-validate-the-model-assess-the-design-respond-to-change-an.md) → [Hypothetical lab](labs/lab-12-verify-and-validate-the-model-assess-the-design-respond-to-change-an.md)

## NS-MBA9.1 integrated model-analytics case

Every chapter now uses [one controlled model-analytics dossier](case/INDEX.html), with an [editable structured model](case/model.json), [six requirements](case/requirements.csv), [six verification-evidence statuses](case/evidence-register.csv), a [supplier change record](case/configuration-change.csv), a [typed evidence-chain diagram](case/model-evidence-flow.svg), and a [standard-library Python checker](tools/step03_book9_model_check.py). The case compares three fictional winter fleet variants, detects stale evidence, and propagates a charger interface change. **The design is suitable only for conditional study, not operational release.**

## Engineering evidence discipline

Follow a traceable chain of **question → representation → assumption/data → computation or explanation → sensitivity → supported claim → owner and next evidence**. Validate mathematical examples for their assumptions, not simply arithmetic. Do not treat a hypothetical result as operational validation.

## Computational practice

See [Notebooks](notebooks/README.md), [Synthetic datasets](datasets/README.md), [Diagrams](diagrams/README.md), and [Calculation tools](tools/README.md). The notebooks provide reproducible exercises; the book text can be read offline with no software dependencies.
