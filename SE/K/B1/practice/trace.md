# Workshop 1 · When does a requirement actually have evidence?

*Companion to Book I, Chapter 4 · Requirements engineering and verification planning*

## A claim is not the same thing as an evidence link

Northstar's engineering team maintains six requirements for a fictional autonomous campus shuttle. A dashboard shows six verification records and three green checkmarks. Its sponsor asks a seemingly simple question: “Are we ready to accept the requirements baseline?” A dashboard can answer how many records are labeled `PASS`; it cannot by itself answer whether those results apply to the **version of the system being accepted**. A test can pass for an obsolete requirement, a different vehicle configuration, or a scenario outside the operating domain.

Traceability is the controlled relationship among need, requirement, allocation, verification method, configuration, result, and acceptance claim. The chain is only as strong as its least defensible transition. If a test result is for revision 3 but the requirement is now revision 4, the result is historical evidence, not proof that revision 4 has been verified. Nor should a requirement be called satisfied because a test was executed: an executed and failed test gives *valid adverse evidence*.

## Build a claim–evidence ledger

For every requirement, record its identifier and approved revision; its verification method and test identifier; the **requirement revision evaluated**; the tested configuration; outcome; and any deviations. The phrase “requirement covered” must be decomposed into at least three different questions: (1) is a test assigned? (2) was an admissible test conducted? and (3) does the admissible test support the acceptance claim? These numbers need not agree.

An evidence record is **admissible for a particular claim** only when its revision and configuration match the claim, the result is applicable to the intended environment, and its provenance can be inspected. Admissibility does **not** imply that the requirement passed. Use this distinction in the laboratory dataset.

### Worked example: six candidate claims

The ledger contains R-01 through R-06. R-01 and R-02 have successful tests for their current revisions and accepted configuration `A`. R-03 has a successful result for revision 3, but revision 4 is current. R-04 has a correctly matched, *failed* test. R-05 passed on configuration `B` rather than the proposed release `A`. R-06 has no test result. A simplistic report might say “four tests passed”; a stronger review finds **three admissible records**, **two verified passes**, **one valid failure**, and **three unresolved or inapplicable claims**. The acceptance pass rate is therefore 2/6, not 4/6. A valid failure is evidence against release, not a paperwork gap to be hidden.

The metrics serve different purposes:

\[
\text{Admissible evidence fraction}=\frac{3}{6}=0.50,\qquad
\text{Supported-claim fraction}=\frac{2}{6}\approx0.333.
\]

Neither metric should be casually described as system reliability. They are fractions of requirements in a particular register. A safety-critical requirement may prevent acceptance even when every other requirement passes; aggregation cannot substitute for gate criteria.

## Configuration changes break apparently complete chains

Suppose software revision `SW-4` modifies the logic for stale route permissions. Even if an earlier test `T-03` demonstrated correct behavior for `SW-3`, the new release needs a change-impact argument: is the test still applicable without rerun, can analysis justify equivalence, or must the behavior be reverified? The answer depends on changed interfaces, dependencies and hazard controls—not on how expensive a rerun would be.

A practical traceability system therefore stores **directed, typed relationships** (satisfies, verifies, derived-from, depends-on) and revision-specific evidence. “There is a link” is much weaker than “this current configured item was verified by the stated method under the required conditions.”

## Review checklist

- Have you distinguished assigned tests, executed tests, admissible results, and supported claims?
- Are verification failures retained as negative evidence instead of disappearing from counts?
- Does every test record name the exact requirement revision and product configuration?
- Do requirements have an acceptance authority, not merely an engineering owner?
- Are unresolved safety constraints highlighted individually rather than averaged away?

## Worked problems

**Problem 1.** An auditor sees four successful executions, three current-revision records, and two successful admissible outcomes among six requirements. Which count belongs in a readiness recommendation?

<details><summary>Worked solution 1</summary>

Report all three quantities with their meanings. Four executions passed in some historical configuration, three records are admissible to the present claim, and two requirements have affirmative current evidence. Readiness must use the **two supported claims** plus the status of each remaining requirement—not the headline number four.
</details>

**Problem 2.** R-04 has a `FAIL` with matching configuration, revision, and environment. Should it be classified as “missing evidence”?

<details><summary>Worked solution 2</summary>

No. It has valid **negative evidence**. Classifying it as missing would hide an observed nonconformance. Open a discrepancy, assess operational impact, implement and verify a corrective change, and maintain a link to the original failure.
</details>

**Problem 3.** R-05 has a successful result on configuration B. The release candidate is configuration A. What additional argument could make the result usable?

<details><summary>Worked solution 3</summary>

A configuration-equivalence argument may be possible if the difference cannot affect the requirement and that claim is supported by a reviewed change-impact analysis. Without that analysis, the result is not admissible for A. A green status from a different build is not sufficient.
</details>

**Problem 4.** A team reports “95% verification coverage” but has 20 high-consequence requirements, one with no valid evidence. Can the sponsor infer readiness?

<details><summary>Worked solution 4</summary>

No. The fraction describes a register and hides consequence and criticality. Apply requirement-specific acceptance gates. A single unverified hazard control may preclude authorization, whereas a noncritical documentation issue may be treated differently by the authority.
</details>

## Transfer to engineering work

Run the supplied ledger checker, inspect every status and author a one-page requirement acceptance memorandum. Identify which failures are defects, which are evidence gaps, and which are configuration mismatches. Preserve your assumptions and a before/after traceability ledger. Then return to the original Chapter 4 requirements clinic and revise its verification plan with the distinction between “planned,” “observed,” and “accepted.”
