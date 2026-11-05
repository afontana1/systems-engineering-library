# Requirements, traceability, and assurance arguments

*Core Concepts · Foundations · T02*

> Turn stakeholder needs into bounded, falsifiable obligations and credible evidence chains.

**Recommended preparation:** [System boundaries, outcomes, and emergence](01-boundaries.md)

**Related course companions:** [Book 1](../B1/OPEN-BOOK.html), [Book 7](../B7/OPEN-BOOK.html), [Book 8](../B8/OPEN-BOOK.html)

## 1. A requirement is an obligation, not an aspiration
“The service shall be safe and efficient” sounds persuasive because it allows incompatible interpretations. A requirement becomes useful when an independent reviewer can decide whether evidence satisfies it. A well-formed system requirement identifies a subject, required behavior or property, operating condition, numerical or categorical acceptance criterion, and where relevant a time or accuracy boundary. The requirement must also be necessary and feasible: testability alone does not justify building the wrong capability.

Contrast a stakeholder need—“A passenger using a mobility device can board without unsafe assistance”—with a system requirement: “Under the specified boarding-surface conditions, the vehicle shall deploy its boarding aid within 20 seconds of a valid request.” The second can be tested. It does not, by itself, guarantee the first, because geometry, user interaction, and surface conditions still matter. The distinction between **verification** (did the system meet its specification?) and **validation** (does the resulting system meet its intended use?) is not merely terminology; it defines different evidence obligations.

## 2. Build a directed evidence chain
A traceability matrix becomes meaningful only when its links have semantics. A stakeholder need may be *refined by* system requirements; a requirement may be *allocated to* components, *satisfied by* a design element, and *verified by* a test. A test report must identify the exact configuration, procedure version, conditions, observations, and disposition. A green cell without provenance is not a robust assurance claim.

A minimal chain is: **Need N → Requirement R → Architecture A → Test T → Evidence E → Decision D**. Ask six independent questions: Is the need complete? Is the requirement necessary? Can the architecture plausibly satisfy it? Is the test capable of discriminating pass from fail? Is the result attributable to the correct configuration? Is the resulting decision proportional to the strength of evidence?

### Changes propagate through meaning
If a dispatch timeout moves from 10 to 15 seconds, the software constant is only one change. Update the interface contract, latency budget, hazard analysis, test expectations, and possibly the operational concept. Change impact is a traversal of *typed links*, not a text search for the number 10. A requirement may be unchanged in wording while its validity is undermined by a new environment assumption.

## 3. Verification coverage is not test counting
Suppose five tests touch requirement R-17. That is not necessarily stronger evidence than one competent test. The key variables are distinct operating conditions, independence of failure modes, measurement validity, and acceptance criteria. Conversely, an automated test that runs one thousand times against the same narrow fixture may provide little evidence about unexpected interfaces.

A defensible coverage argument partitions the intended operational domain: nominal use, boundary conditions, degraded modes, and abuse cases. Record which partitions have evidence and what remains unknown. Traceability measures *completeness of the argument*; it does not automatically establish correctness.

## 4. Typical traps
A test that only confirms that code executed is not necessarily a verification. A passed component test cannot substitute for a system-level outcome measure. A requirement whose acceptance criterion changes after results arrive invites confirmation bias. An assurance case should state its limitations, not hide them in footnotes.

## 5. Develop an acceptance test before finalizing the statement
Draft a requirement, then reverse the usual workflow: ask a test engineer to describe precisely how the project would fail it. If the engineer cannot identify the stimulus, environment, observation method, and pass condition, the statement is incomplete. This is not an invitation to over-specify the design. “The service shall recover from a single dispatch-node failure within sixty seconds while preserving accepted trip assignments” allows several architectures, while providing an observable outcome.

Now check whether the requirement is **allocated at the right level**. An end-to-end service availability target should not be assigned in full to each software component; shared infrastructure and human operations matter. Decompose it into appropriate component responsibilities, but preserve the system-level measure. The decomposition is an argument that the pieces jointly achieve the top-level obligation, not an algebraic guarantee.

**A useful coverage review** has two axes. Rows are operating scenarios: nominal, peak demand, degraded connectivity, accessibility, and maintenance. Columns are forms of evidence: analysis, inspection, demonstration, and test. Empty cells are not automatically failures; they identify where reviewers must justify why a particular evidence type is unnecessary. Where a test covers multiple requirements, record the distinct assertions it makes about each.

**Check your reasoning:** A requirement says “The scheduler shall respond in less than 500 ms, on average.” A test reports a 300 ms mean but a 4 second maximum. Did it pass? Technically the mean criterion may be met, but the stated requirement may be inadequate for the intended operational task. The engineer should report compliance and the unresolved mission-risk issue separately, not retroactively change the criterion.

## Guided worked example

### Worked case: the false 100% coverage report
A project has 10 requirements, and each has at least one linked test: link coverage = 10/10 = 100%. However, two tests ran against an obsolete configuration and one lacks observed results. Evidence-current coverage is at most 7/10 = 70%, even before asking whether the test conditions are adequate. The two numbers answer different questions. Report both, and list the outstanding evidence gaps explicitly.

## Independent transfer exercise

Create a traceability table with five fictitious shuttle requirements, architecture owners, tests, evidence versions, and pass conditions. Change one interface timing limit and identify all links requiring review.

[Open the companion hypothetical lab](labs/02-requirements-workshop.md)

<details><summary><strong>What a defensible answer must contain</strong></summary>

Use typed relationships and version identifiers. At least one requirement should remain open because evidence is stale, even though a test link exists.

</details>

## Next connections

Use the related books above to see how this concept becomes a course assignment. The lab provides a small, deliberately incomplete practice setting; it does not replace verification against real operational data.
