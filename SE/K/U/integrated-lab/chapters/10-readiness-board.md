# L10 · Integrated design review and defensible release decision

**Learning time:** 5–8 hours. **Gate:** Final integrated technical review. **Prior reading:** [F09](../../flagships/F09-enterprise-systems-of-systems.md) and [F03](../../flagships/F03-statistical-assurance.md).

## A review board decides on a claim and a next action

The final objective is not to maximize the count of green checks. It is to present a credible argument to a skeptical review board, so it can decide whether to continue research, authorize a controlled field experiment, or stop. For the supplied Northstar case, the defensible recommendation is **continue sandbox research only**. The fixed fixture passes its illustrative thresholds, but the stochastic stress model is often less favorable and major real-world assumptions are unvalidated. High-consequence safety and equity questions remain open.

An integrated review package must carry different kinds of evidence separately: needs and ConOps, requirements and test coverage, architecture and interface contracts, software tests, experiment designs and numerical results, hazards and open findings, configuration/provenance, design alternatives, and a decision memo. Avoid the linguistic shortcut “system verified”: specify exactly which requirement, which configuration, which scenario and how the result was observed.

## Construct the assurance argument

**Claim C1:** In the fixed dataset and reference configuration, the toy scheduler meets REQ-01 through REQ-06's measured fixture outcomes. **Grounds:** passing unit tests and `results.json`, an audit digest, and an input-hash register. **Warrant:** these tests implement the narrow specified oracle for a deterministic single-process model. **Rebuttal/limitation:** that evidence does not establish real availability, accessible service, cyber resilience, concurrent correctness, human operational suitability or safe vehicle movements.

**Claim C2:** The reference design's service performance is sensitive to resource loss and demand assumptions. **Grounds:** one-vehicle degradation and independent synthetic arrival replications. **Warrant:** controlled factor changes show how the *model* responds. **Rebuttal:** the arrival distribution is invented and the model structure excludes key factors; this is a sensitivity warning, not a field reliability estimate.

## Review method

Ask three distinct reviewers to challenge the same package: a systems engineer checks trace completeness, a software reviewer checks invariants and reproducibility, and a community/human-factors reviewer checks the validity of the chosen outcome measures. The board should insist on open findings and ownership, not just a list of capabilities. Use the [review board packet](../review/REVIEW-BOARD.md) and [open findings](../data/review-findings.csv).

A useful board statement is: *“The simulated prototype demonstrates selected deterministic scheduling and traceability behaviors under synthetic conditions. It is not authorized for operational dispatch or safety-critical decisions. Further domain validation and independent assurance are required before any real pilot.”*

## Engineering activity

1. Produce a ten-slide equivalent technical review or written board memo, with each important conclusion linked to reproducible evidence.
2. Rerun the full code and test suite; include Python version, seed, fixture hash, and changed assumptions.
3. Classify every significant open finding by impact and explicitly assign closure evidence. Reject any attempt to convert an unknown likelihood into an unsubstantiated risk score.
4. Prepare an argument for **not** approving deployment even if every fixture test is green. Include stakeholder considerations and uncertainty in the causal model.

## Knowledge check and explained answer

**Question.** What is the correct disposition when software tests pass but the operational model lacks real-data and human-factors validation?

<details><summary>Show explanation</summary>

Do not approve real-world deployment from this package alone. A teaching prototype may be accepted for further study or controlled model development, but a real operational decision requires appropriate independent technical, safety, human-factors, privacy and domain evidence, with accountable authority.

</details>

**Gate evidence:** complete board packet, documented decision and limitations, an assigned open-findings register, and specific evidence needed to revisit the decision.
