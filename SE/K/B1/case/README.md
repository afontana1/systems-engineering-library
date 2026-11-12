# Northstar NS-B1 — Book 1 integrated engineering case

**Purpose.** This is a single, controlled *fictional* reference case used across all 12 chapters of **Book 1 — Introduction to Systems Engineering**. The case is not field data, a transport design approval, a safety certification, or a real campus operating proposal. Its small numbers are selected for transparent calculations and review discussions.

## Operating concept and boundary

The system of interest is a supervised four-stop campus shuttle **service**, not a vehicle alone. The owned engineering scope includes the rider application, dispatch service, status gateway, supervisor console, and allocation database. Vehicle behavior, cellular infrastructure, accessible boarding operations, and emergency response must still be represented as interacting external systems or separately controlled constituents. The purpose of the exercise is to show what becomes invisible when boundaries, assumptions, and evidence are not stated.

The editable [NS-B1 baseline](northstar-reference-baseline.json) contains three stakeholder needs, four candidate requirements, component responsibilities, a deterministic emergency-status timing allocation, a sample trade study, and a synthetic common-cause hazard model. The [traceability CSV](traceability.csv) ties each requirement to a component and verification procedure. One evidence row is **deliberately stale** (`NS-R-04`, test baseline NS-B0) so that a coverage audit must find a real objection instead of giving a perfect score.

## Thread through the book

| Week | Learning question | Inspect or reproduce |
|---:|---|---|
| 1 | What lies inside the system boundary? | [Chapter 1](../chapters/01-what-is-the-system.md): need and responsibility ledger |
| 2 | Which uncertainty should we test before commitment? | [Chapter 2](../chapters/02-lifecycle-evidence.md): expected cost and perfect-information bound |
| 3 | How do normal and degraded operations differ? | [Chapter 3](../chapters/03-needs-and-conops.md): retry, cancellation, human response scenarios |
| 4 | Is a requirement testable without overclaiming? | [Chapter 4](../chapters/04-requirements.md): timing allocation with 0.85-s nominal margin |
| 5 | Does the behavioral model preserve an invariant? | [Chapter 5](../chapters/05-functions-and-behavior.md): one active allocation per reservation |
| 6 | Can a review board rely on every piece of evidence? | [Chapter 6](../chapters/06-reviewing-the-functional-baseline.md): deliberately stale NS-R-04 evidence |
| 7 | Where do interface semantics become part of architecture? | [Chapter 7](../chapters/07-allocating-architecture-and-interfaces.md): status-message schema and clock assumptions |
| 8 | When does a trade-study preference reverse? | [Chapter 8](../chapters/08-trade-studies-and-sensitivity.md): score recomputation and a third-option counterexample |
| 9 | How does a change affect cost, scope, and test validity? | [Chapter 9](../chapters/09-managing-the-technical-baseline.md): CPI, SPI, evidence currency |
| 10 | Why can nominal redundancy fail? | [Chapter 10](../chapters/10-failures-and-controls.md): conditional common-cause top event |
| 11 | What does zero observed failures demonstrate? | [Chapter 11](../chapters/11-realization-and-evidence.md): independent Bernoulli confidence bound |
| 12 | What decision is evidence actually sufficient to support? | [Chapter 12](../chapters/12-synthesis-and-defense.md): restricted laboratory integration versus operational release |

## Reproduce numerical examples

The examples require only Python's standard library:

```bash
python3 SE/K/B1/tools/step03_case_check.py
```

Expected values, under the declared assumptions: allocation **1.65 s**, nominal timing margin **0.85 s**, scores **70.0 / 74.5 / 73.5**, pairwise switch at resilience weight **0.418182**, shared-cause top event **0.0031994 per demand**, and one-sided 95% bound after 300 independent zero-failure trials approximately **0.009936**. The script asserts the requirements/traceability structure and detects the single intentionally stale test row.

## What cannot be inferred from these checks

- The 1.65-s allocation is not a measured end-to-end percentile or a field latency guarantee.
- The score ranking expresses declared values and fictional performance judgments; a real design must first satisfy noncompensable constraints.
- Fault-tree numbers are *assumed event probabilities* and do not establish operational safety or risk acceptance.
- A zero-failure binomial bound is conditional on identical, independent, representative trials and a well-defined failure event.
- Structural trace links cannot establish correctness, model conformance, human usability, or evidence applicability.

For teaching references, see [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) and the connected methods under [Concepts](../../CONCEPTS.html). Verify edition-specific obligations, applicability, and interpretations with primary sources before using a method on a real program.
