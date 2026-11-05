# 02 · Requirements, traceability, and evidence arguments

**Concept dossier · Foundations / MBSE / integration and test**  
**Prerequisites:** operational outcomes and scenarios; difference between verification and validation.

## Separate five things that are often conflated

A stakeholder **need** describes a valued outcome. A system **requirement** constrains required behavior or performance. An **architecture element** offers a design response. A **test** is a procedure that collects evidence. An **acceptance decision** interprets that evidence under an agreed rule. Conflating these creates false assurance: a green test can establish only what it actually measured, not that the original need is satisfied.

For a fictional accessible shuttle service:

- Need N-01: riders can board safely and predictably in the designated operating area.
- Requirement R-07: under a defined boarding scenario, the deployed service shall display the boarding-point change to the user within 15 seconds of dispatch approval.
- Architecture A-12: dispatch event broker and rider-notification interface.
- Test T-19: inject approved curb-change events and measure notification latency with synchronized clocks.
- Evidence E-19: raw timestamps, configuration, sample inclusion decisions and test report.
- Claim C-01: R-07 is satisfied for the specified configuration and tested conditions, subject to the pre-agreed acceptance rule.

The 15-second figure is **illustrative**, not an externally validated safety threshold.

## Traceability is a typed graph

Represent the thread as a directed graph `G=(V,E)` with **typed** nodes: need, requirement, architecture, interface, test, evidence, claim, risk and change. Typed edges include *derives*, *allocated_to*, *verified_by*, *produced*, *supports* and *changes*. A simplistic spreadsheet containing identical IDs in two columns may miss wrong edge semantics or invalid versions.

Useful automated checks:

1. Every in-scope approved requirement has at least one parent rationale or explicitly justified origin.
2. Every verifiable requirement has a linked verification method and an evidence-producing activity.
3. Evidence configurations match the claim: test of software v2.1 does not necessarily support release v2.3.
4. Changes propagate by traversing dependency edges in the relevant direction; reviewers distinguish affected items from definitely invalidated items.
5. Every critical claim identifies an owner, scope, conditions, uncertainties and acceptance authority.

A requirement is not “verified” by having a test link. It is supported by **suitable evidence evaluated against criteria**.

## Why pass/fail is more subtle than it looks

Suppose the requirement is “latency no more than 15 seconds for at least 99% of eligible events.” A single timing run below 15 seconds proves almost nothing about a 99th-percentile population claim. A procedure must define the sampling frame, event mix, timing accuracy, exclusions, dependence between trials, confidence criterion, software and hardware versions and what happens to discrepancies. A 95% confidence statement is not equivalent to a 95% performance requirement.

If 0 failures appear in `n` independent Bernoulli trials with common failure probability `p`, a **one-sided** 95% confidence upper bound for `p` is `1 - 0.05^(1/n)`. For `n=100`, this is about 2.95%; zero observed failures would not support a claim that `p` is below 1%. Real tests may violate independent-identically-distributed assumptions and require a different analysis.

## An evidence argument, not a paperwork chain

An assurance-style argument states:

> **Claim:** A declared configuration meets the user-notification latency requirement in the specified operating envelope.

**Reasoning:** Requirements map to observable event timestamps; clocks are calibrated; sampling adequately covers intended events; discrepancies are resolved according to approved rules.

**Evidence:** Controlled test logs, procedure version, sample description, calibration records, independent review and an approved deviation register.

**Limitations:** Storm-related radio outages and untested device configurations are outside the claim, unless explicitly included and supported.

The reasoning can be challenged: Is the event definition biased? Are trials correlated? Can the test harness understate real-world latency? An argument is a structured way to expose such vulnerabilities rather than conceal them.

## Change-impact worked example

Change request CR-06 replaces the push-notification vendor. Trace from interface IF-04 to architecture A-12, requirement R-07, test T-19, security controls and associated evidence. Old results may remain useful for other unchanged subsystems, but E-19 may no longer support R-07. The response is targeted impact analysis, not reflexively rerunning every test or blindly accepting the old report.

## Practice with solutions

**A.** Why is “shall be user-friendly” weak? **Answer:** no observable behavior, target population, operational condition or success criterion is defined. Elicit the intended user outcome before choosing a measurable substitute.

**B.** What does 100% requirement-to-test link coverage establish? **Answer:** only that links exist under the coverage query. It does not establish test adequacy, result validity, correct versions or validation of stakeholder needs.

**C.** A successful bench test uses v1.4 but the field system uses v1.5. Can it be cited? **Answer:** only after configuration-impact analysis justifies what remains applicable; do not silently claim identical evidence.

**Transfer artifact:** a five-requirement trace graph with two alternative failure paths, a test-case table, a change-impact query and a one-page evidence argument.

## Connections

[System boundaries and needs](01-outcomes-boundaries.md) · [Architectures and state models](03-architecture-states.md) · [Experiments and confidence](07-experimental-evidence.md) · [Digital provenance](11-digital-thread.md).  
**Legacy primers:** [Verification matrix](../../encyclopedia/verification-matrix.md), [V&V](../../encyclopedia/v-and-v.md).
