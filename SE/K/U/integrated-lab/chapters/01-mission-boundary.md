# L01 · Mission, stakeholders, and system boundary

**Learning time:** 3–5 hours. **Gate:** Mission review. **Prior reading:** [F01 — mission to assurance](../../flagships/F01-requirements-to-assurance.md).

## Engineering problem

A regional operator asks for “a dependable, equitable mobility dispatch system.” That sentence is not yet a system requirement. Dependable to whom, during which hour, and under which disruptions? In this teaching case, *Northstar* is a **software-only scheduling sandbox** for twelve synthetic rider requests among fictional stops A, B, and C. It does not drive vehicles, dispatch real people, authenticate users, or certify service safety. Keeping that boundary explicit is the first engineering act.

The system of interest (SOI) includes an input parser, an idempotent request ledger, a deterministic scheduler, a scenario generator, and an evidence reporter. The operating environment—actual road networks, driver instructions, vehicle maintenance, accessibility, networks, weather, human dispatchers—is outside the SOI. Those systems would be essential in deployment, which means the prototype cannot validate the real mission. An *interface* is a contractual exchange across a boundary; an *assumption* is a proposition the model uses without independently establishing it. Confusing them is one of the fastest routes to false assurance.

## Context and mission model

The operational concept is deliberately small: a synthetic event arrives → input is validated → repeated deliveries are deduplicated → a one-pass scheduler allocates the earliest available vehicle → each assignment is classified as completed within an 80-minute model horizon or unserved → metrics and an audit digest are recorded. A rider is represented by one request and one fixed-duration trip. Travel geography, boarding assistance, emergency priority, real concurrent message arrival, and service recovery are absent. These omissions are not minor implementation TODOs; some are *validity barriers*.

Three stakeholders have different interests. Rider representatives ask for reasonable access, the dispatcher asks for conflict-free assignments and visible degraded operation, and the assurance reviewer asks for independently inspectable claims and evidence. See [stakeholder needs](../data/stakeholder-needs.csv). The metrics `served_fraction` and `p90_wait_min` are **model measures of performance**, not validated measures of real passenger mobility or equity. A measure becomes useful only if its definition, population, observation window, and limitations are explicit.

## Worked reasoning

Suppose the case states “serve at least 95% of rider requests.” If the scope is the twelve unique rows in the fixed fixture, at least `ceil(0.95 × 12) = 12` must finish before the horizon; completing 11 is 91.7% and fails. If the scope changes to thousands of real travel requests across counties, nothing about a 12-row teaching fixture establishes this real-world claim. The *denominator*, not just the numerator, is part of the requirement.

**Why a fixed fixture?** It gives a deterministic regression case in which requirements and code can be linked. **Why an additional stochastic model?** It exposes sensitivity to arrival timing. Neither substitutes for observed data or human-centered validation.

## Engineering activity

1. Draw a context diagram showing actors, SOI, external systems, and input/output contracts. Use [the system diagram](../diagrams/northstar-context.svg) as a starting point, not a final authority.
2. For each included subsystem, name one responsibility and one explicitly excluded responsibility. Identify which external systems would become safety critical if integrated.
3. Rewrite “dependable mobility” as three distinct claims: a narrowly testable prototype claim, a mission-level claim requiring field evidence, and a claim that should not be made at all with this prototype.
4. Update [stakeholder needs](../data/stakeholder-needs.csv) to include an accessibility representative; define a meaningful measure without implying that current data measure it.

## Knowledge check and explained answer

**Question.** Does a 100% pass rate for the fixed dataset validate rider access in a real community?

<details><summary>Show explanation</summary>

**No.** It verifies a statement about a stated dataset and simplified software model. Validation would require evidence that the modeled workflow solves the *right problem* in the actual operating context, including accessibility, coverage, human decisions, changing demand, and failure responses. A higher percentage on a narrow fixture cannot compensate for a mismatch of system boundary.

</details>

**Gate evidence:** a one-page ConOps, a context diagram, three stakeholder measures, and a limitations list with at least five substantive exclusions. A reviewer should be able to identify the SOI without asking who drives the vehicles.
