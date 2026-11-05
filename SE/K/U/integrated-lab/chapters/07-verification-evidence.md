# L07 · Verification planning and an evidence-backed test report

**Learning time:** 5–7 hours. **Gate:** Test readiness and results review. **Prior reading:** [F03](../../flagships/F03-statistical-assurance.md), [F01](../../flagships/F01-requirements-to-assurance.md).

## What does an accepted test actually establish?

A test makes a bounded claim about a specified configuration, stimulus, expected observation, and outcome. The [verification matrix](../data/verification-matrix.csv) links tests to requirements and traces evidence to paths. The code [assurance.py](../src/assurance.py) catches missing or dangling identifiers. The [run report](../outputs/results.json) records actual output and an input-hash file identifies which fixtures were used. These are components of an evidence package, not an assurance argument by themselves.

To describe a test result properly, record **objective**, configuration, environment, procedure, acceptance oracle, actual observation, discrepancy, reviewer, and limitations. `T-03` measures 12/12 completed on the fixed fixture, while `T-06` demonstrates that 1/2 fleet capacity leads to a missed completion threshold. The latter can be a *passing test of degradation reporting* even though the degraded **system performance** fails its target. Conflating those two meanings of pass is a frequent source of misleading dashboards.

## Trace, coverage, and inference

Coverage counts how much of a declared artifact set is connected: the reference audit yields 8/8 requirements with at least one test link and 4/4 hazards with test links. But consider an absurd test that only checks that the program launches; linking it to all requirements makes graph coverage 100% without establishing requirements compliance. That is why evidence review must separate *syntactic integrity* from *semantic relevance and sufficiency*.

The final board should not be shown only a green list. It needs scenario results, test-code identification, input configuration hashes, residual risks, open findings, independent checks, and a constrained claim. The lab does not establish runtime behavior under network loss, physical vehicle failures, authentication breaches or human misuse. Such omissions are evidence gaps, not mere low-priority enhancements.

## Engineering activity

1. Inspect [verification-matrix.csv](../data/verification-matrix.csv) and [hazards.csv](../data/hazards.csv). Pick two links and explain whether the actual test code demonstrates the described acceptance outcome.
2. Temporarily remove one `test_id` from the hazard sheet. Re-run `audit_traceability` and explain which report fields flag the defect.
3. Create a discrepancy report for the one-vehicle scenario, including observed failure, reproducibility, impact, and disposition. Do not label the deliberate degradation as a software test failure.
4. Populate a review evidence index and mark each of these as verified, partly evidenced, or unsupported: idempotency under duplicates; real access equity; fleet safety; confidence in the stochastic model.

## Knowledge check and explained answer

**Question.** What is the difference between “test passed” and “operational claim substantiated”?

<details><summary>Show explanation</summary>

A test passes if its configured observation satisfies its stated oracle. An operational claim is substantiated only when those observations are applicable and sufficient for the real context, with known configuration, coverage, credible methods and uncertainty treatment. A passing test can be necessary without being remotely sufficient.

</details>

**Gate evidence:** executable test report, traceability audit, a discrepancy report, an evidence index, and an honest confidence/limitations statement.
