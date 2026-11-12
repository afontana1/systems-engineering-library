# L02 · Convert needs into requirements and traceable claims

**Learning time:** 4–6 hours. **Gate:** Requirements baseline. **Prior reading:** [F01](../../flagships/F01-requirements-to-assurance.md) and [requirements derivation](../../derivations/01-from-need-to-verification.md).

## Requirements are testable propositions

A requirement states a condition to be satisfied by a defined system under defined circumstances. Its grammatical clarity matters, but more important are the *test oracle* and *application boundary*: how would an independent reviewer know it had been met? The [eight baseline requirements](../data/requirements.csv) intentionally distinguish behavior (`REQ-01` idempotency), invariant (`REQ-02` non-overlap), metric (`REQ-03` fixed-fixture completion), statistical convention (`REQ-04` nearest-rank p90), assurance completeness (`REQ-05` links), degradation study (`REQ-06`), and error handling (`REQ-07`, `REQ-08`).

A requirement is not necessarily a product feature. `REQ-05` is a process/evidence requirement; it has a different verification method and cannot prove the tested behavior is correct. Use the requirement fields to capture **source**, priority, allocation, verification method, acceptance rule, and configuration. A weak wording such as “minimal wait” hides who chooses the limit. Here we choose a 20-minute p90 *only for the fictional fixture*, and state the method explicitly: order the completed-request waits, select position `ceil(0.9n)`.

## Worked trace example

`NEED-03 → REQ-01 → RequestLedger → T-01 → tests/test_lab.py`. The stakeholder wants a coherent audit record; the requirement narrows it to exact repeated event deliveries; the component owns the behavior; the test creates duplicates; the code checks there are 12 unique requests from 13 events. Another link `H-02 → T-01` says that the duplicate-event hazard is mitigated by evidence about this narrow model. That is not a complete safety argument: concurrency, network partitions, malicious replay, and persistent storage are absent.

The [traceability audit](../src/assurance.py) checks whether links point to *existing identifiers* and whether every declared requirement and hazard has test links. Link coverage of 100% is structural integrity. A meaningless test can satisfy a link, so reviewers must also judge relevance, independence, reproducibility, and acceptance thresholds.

## Boundary conditions to challenge

A system receives a second event with the same `request_id` but different destination. Silently discarding it hides a data-integrity conflict. Processing it as a new request violates at-most-once semantics. The toy ledger raises `ValueError`, making the conflict visible. The requested policy is intentionally different for an *exact* duplicate, which is ignored. A realistic service would need a durable, atomic idempotency store and identity/security design; this in-memory version is not sufficient.

## Engineering activity

1. In [requirements.csv](../data/requirements.csv), highlight every phrase that specifies measurable conditions. For each requirement, explain the test oracle without relying on the author's intent.
2. Run `python -m src.run_lab`; read `outputs/results.json` and identify which fields support `REQ-01` through `REQ-06`.
3. Create a proposed `REQ-09` for supported boarding assistance. Do **not** mark it verified by the existing tests. Add a pending acceptance test and a new hazard review action.
4. Break `REQ-04` deliberately by changing `target_p90_wait_min` from 20 to 15. Explain why this changes the acceptance verdict without changing the underlying schedule.

## Knowledge check and explained answer

**Question.** If the graph reports 8/8 requirements linked to tests, can a release board conclude 8/8 verified?

<details><summary>Show explanation</summary>

**No.** A link is not a passing test and a passing test is not necessarily valid evidence for the operational claim. Coverage requires further scrutiny of method, independence, version, test results, environmental representativeness and residual uncertainty. The trace auditor itself says that it checks links only.

</details>

**Gate evidence:** a requirements-to-test matrix, a written treatment of the conflict-id case, and one justified requirement change with an explicit verification impact.

## U2 cross-lab credibility challenge — NS-U2.1

**Focus: A trace link is not a verified requirement.** This adds a controlled cross-version analysis to the original learning stage, which remains unchanged.

Traceability has at least two independent tests: **referential integrity**, where every declared identifier resolves, and **claim adequacy**, where the test actually probes the requirement. Both lab runners report intact declared links, but that is a graph property rather than a guarantee of coverage, independence or field relevance. An experiment can be perfectly referenced and still omit an accessibility subgroup.

**Worked reconciliation:** v11 reports eight linked requirements in its own matrix; v12 reports six linked requirements in a different verification plan. The arithmetic `8/8 = 100%` and `6/6 = 100%` does **not** mean that fourteen distinct real mission obligations have been discharged. Requirements may overlap, and the two sets have different scopes and acceptance language.

**Exercise and explained answer:** A test is linked to “loss observable to dispatch” but only checks a simulator's omniscient truth ledger. Does the link close the claim? **No.** It demonstrates that simulated loss appears in a developer-accessible record. A real intake system must separately show receipt acknowledgments, end-to-end reconciliation, and alert latency. Write a new verification procedure for those mechanisms before claiming operational observability.

**Reproduce:** [Cross-lab lab guide](../../lab-credibility-u2/README.md) · [Evidence gates](../../lab-credibility-u2/data/gates.json) · [Computed results](../../lab-credibility-u2/outputs/u2-cross-lab-results.json).
