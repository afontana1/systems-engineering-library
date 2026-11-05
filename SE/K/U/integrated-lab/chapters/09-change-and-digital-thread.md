# L09 · Configuration, change impact, and the digital evidence thread

**Learning time:** 3–5 hours. **Gate:** Baseline and change-control review. **Prior reading:** [F01](../../flagships/F01-requirements-to-assurance.md), [digital provenance](../../derivations/12-digital-provenance-and-assurance.md).

## Version is part of every claim

A system test is a claim about **this code, these inputs, this configuration, under these conditions**. If any of them change, some evidence must be reconsidered. The lab therefore writes [input-hashes.json](../outputs/input-hashes.json), containing SHA-256 digests for key CSV and JSON files. These hashes are reproducibility breadcrumbs, not cryptographic proof of independently witnessed provenance: a person who controls both inputs and outputs can recompute them.

Traceability should connect *need → requirement → architecture element → interface → test → result → review disposition* along with the configuration state. In Northstar, `CR-001` requests support for two-person bookings. That change affects the request parser, resource scheduling model, possibly boarding time and fleet capacity, `REQ-07`, interface IF-01 and tests T-07. Simply changing the `passengers` validation from `==1` to `>=1` would pass input parsing while leaving the allocator unable to represent seat capacity. This is a classic partial change that appears harmless locally but violates system-level meaning.

## Change-impact reasoning

Start with a proposed change; find every directly allocated component; follow requirements and interface contracts to tests and hazards; identify dependent decisions and evidence. Then compare a new baseline with an immutable reference. The teaching artifact uses a [configuration index](../data/configuration-index.csv) and [change requests](../data/change-requests.csv). They are incomplete by design—your job is to test whether you can find missing affected objects.

The second proposed change, `CR-002`, introduces intermittent network delivery. That would invalidate single-process idempotency assurance because repeated messages may cross process restarts. You would need a persistent event store, a retry and reconciliation protocol, deterministic ordering rules, security controls and possibly a new acceptance architecture. It is unsound to declare the original T-01 sufficient for this changed system.

## Engineering activity

1. Change a noncritical parameter in `config.json`, rerun the lab and compare input hashes and results. Restore the reference fixture afterward.
2. For CR-001, write a change-impact matrix listing affected requirements, interfaces, algorithms, unit tests, hazards, risks, and review approvals.
3. Name at least two ways a provenance chain can appear intact even though the evidence is untrustworthy.
4. Draft a release-note statement that precisely identifies what this version verifies and what remains open.

## Knowledge check and explained answer

**Question.** Can an unchanged source-code hash show that an earlier performance test still applies after fleet size changes from two to one?

<details><summary>Show explanation</summary>

No. Test claims are configuration-dependent. The executable code can remain byte-for-byte identical while changing fleet size alters the performance outcome. A credible evidence chain must identify inputs, environment, configuration and relevant dependencies in addition to code.

</details>

**Gate evidence:** before-and-after hash comparison, impact analysis, controlled change proposal, and an evidence-currency table.
