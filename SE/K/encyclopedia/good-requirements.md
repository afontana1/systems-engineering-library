# Requirements: precise obligations, not persuasive sentences

**Reference entry · Foundations, design, and test · Expanded reference**

## Definition

A **requirement** states an obligation that can be assessed for a particular system, element, process, or delivered service under declared conditions. A useful requirement identifies the responsible subject, required behavior or constraint, operating condition, measurable criterion, and verification route. It must also be necessary, feasible, consistent with neighboring requirements, and linked to a legitimate need. Grammar alone cannot establish these properties.

A need expresses the desired outcome; a requirement makes a bounded technical commitment; a design describes one means of satisfying it; and a test provides evidence of a particular claim. Confusing those roles leads to overconstrained concepts and verification plans that merely repeat the specification.

## A semantic model

Represent a behavioral requirement as **(trigger, mode, subject, response, performance bound, exceptions, observation window)**. The phrase “when a valid boarding request is received” is an event condition. “The dispatcher shall issue an acknowledgement within 2.0 seconds” is a temporal obligation. “At least 99% of such requests over the specified peak-demand envelope” introduces a population-level statistical criterion; it is not interchangeable with a per-request guarantee.

In temporal logic, **G(request → F≤2s acknowledgement)** informally means every applicable request eventually receives an acknowledgement within two seconds. Such a universal requirement is stronger than a 99th-percentile target. The two may be appropriate to different safety or service needs and call for different evidence methods.

Requirements must also be **jointly realizable**. Two individually readable statements—“every request receives immediate acknowledgement” and “all network traffic stops during maintenance”—may conflict unless maintenance is explicitly outside the first requirement's operating mode. Model-based consistency checks should search for these contradictions before implementation.

## Worked example: an attractive but untestable requirement

Weak: “The campus shuttle shall provide fast, dependable service.” This does not identify a population, scenario, denominator, or criterion.

Stronger candidate: “During term-time weekdays from 07:30 to 09:30, under demand of up to 180 trip requests per hour and normal weather, the dispatch service shall provide a definitive accepted/rejected response within two seconds for at least 99% of valid requests, measured at the public API over 30 operating days.”

This is **not yet automatically sufficient**. The team must define a valid request, arrival-pattern assumptions, instrumentation, exclusion policy, whether repeated requests count, and a statistical acceptance rule. If 3,000 trials all pass, the observed rate is 100%, but that does not prove that the true rate is 100%; sampling uncertainty remains. For independence-sensitive statistical claims, the sampling design should account for peak-period clustering and correlated outages.

A separate requirement should address accessibility or offline operation rather than hiding those obligations inside the latency statement.

## Requirements quality workflow

1. Trace each candidate to an authorized stakeholder outcome or constraint.
2. Check its subject, mode, trigger, response, metric, units, and acceptance decision rule.
3. Separate mandatory constraints from design preferences and provisional assumptions.
4. Check for gaps, contradictions, duplicate obligations, and unintended implementation constraints.
5. Allocate ownership and identify derived interface or subsystem requirements.
6. Plan the verifying evidence **before** committing to the baseline; flag anything not credibly testable.
7. Apply versioned change control because later revisions can invalidate earlier tests and cost estimates.

## Verification versus validity of the requirement

A test may establish that the service meets a two-second interface latency target while the experience remains unacceptable because boarding takes ten minutes. That is a **validated-need gap**, not necessarily a failed latency test. Conversely, users may report satisfaction even when an explicit regulatory requirement is violated. Verification and validation ask different questions.

## Pitfalls and connections

Avoid compound “and” requirements that conceal multiple independent pass/fail criteria; avoid ambiguous quantifiers (“most,” “quickly,” “as needed”); avoid test cases that assume the intended implementation; and avoid numerical limits unsupported by stakeholder evidence or physical feasibility. Requirements link directly to scenario design, architecture allocation, traceability, verification matrices, interface contracts, and technical margins.

## Reference shelf retained from the earlier primer

These links are supplied for deeper reading. Confirm current publication versions before relying on them for compliance.

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Reference chapters for lifecycle, needs, requirements, design, technical management, integration and V&V.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Breadth-first conceptual encyclopedia and pointers to further references.

**Expanded tutorial:** [From stakeholder need to verification evidence](../deep-dives/02-requirements-to-verification.md)


## Technical analysis: write a verifiable requirement without confusing it with a valid one

An operational need such as “dispatch promptly” does not specify a testable engineering threshold. A candidate requirement might be: **“For accepted requests originating inside the defined service region, when the certified system is operating with no more than 30 concurrent active requests, the system shall issue an assignment decision within 2.0 seconds for at least 99% of requests over a predeclared representative 30-day operating sample.”** This sentence fixes the event boundaries, population, load, statistic, time interval, and configuration; it still requires an acceptance sampling plan and handling of rejected or timed-out requests.

The requirement can be **verified yet strategically invalid** if users care about vehicle arrival rather than assignment decision latency, or if excluding unaccepted requests hides service denial. Conversely, a stakeholder-approved need can be well-founded but lack a measurable and feasible product requirement. Always keep the two evidence chains separate: *requirement validation* asks whether the requirement accurately represents a genuine need; *product verification* asks whether the specified system meets the approved requirement. Do not equate a 99% sample proportion with 99% confidence; confidence depends on sample size, dependencies, and sampling design.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · Systems Engineering Handbook appendix (requirements and verification matrices)](https://www.nasa.gov/reference/system-engineering-handbook-appendix/) — Requirements review criteria and verification planning context.
- [NASA · Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 (2016/2017)](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle engineering, technical management, requirements, verification and validation.

## Follow the knowledge

**Related concepts**

- [Stakeholders, needs, and value](stakeholders-and-needs.md)
- [Verification cross-reference matrices and test design](verification-matrix.md)
- [Verification, validation, and acceptance](v-and-v.md)
- [Requirements traceability and impact analysis](traceability-graph.md)

**Explore in the 240-chapter textbooks**

- [Book 1, Chapter 4: Chapter 4 — Requirements are promises that must survive a test](../B1/chapters/04-requirements.md)
- [Book 7, Chapter 2: Book 7 · Chapter 2: Closing the system specification](../B7/chapters/02-close-the-system-specification.md)
- [Book 9, Chapter 7: Book 9 · Chapter 07 — Elicit, derive, validate, and query system requirements from the integrated analysis](../B9/chapters/07-elicit-derive-validate-and-query-system-requirements-from-the-integr.md)

**Use this reference responsibly:** examples use hypothetical engineering data; the mathematical results rely on the assumptions stated in each passage. Recheck those assumptions for any real project.

