# Verification cross-reference matrices and test design

**Reference entry · Concept, design, integration and test · Expanded reference**

## Definition and diagnostic distinction

A **verification cross-reference matrix (VCRM)** links each requirement or allocated technical obligation to a specific method, procedure, configuration, result, and disposition. It is an index to evidence, not evidence itself. A green status cell can hide an invalid procedure, an obsolete design version, or an acceptance rule that never measured the requirement.

## Theory: claims, configurations, and evidence sufficiency

Model a verification record as `V = (requirement version, test item, method, procedure, scenario, acceptance criterion, observation, uncertainty, disposition)`. Permissible methods include analysis, inspection, demonstration, and test, each with different limitations. Passing a component test does not automatically close a system-level requirement unless there is a justified composition argument. The relevant denominator is the number of *applicable, version-current obligations*, not whichever subset happens to have a completed record.

Statistical criteria must match the claim. For a pass/fail reliability test with zero failures in `n` independent Bernoulli trials, a one-sided 95% upper confidence bound on failure probability is `1 - 0.05^(1/n)`. At `n = 30`, this is approximately 9.5%: thirty clean tests do **not** demonstrate a failure probability below 1%. Stronger claims need a more extensive or differently structured evidence plan, and independence may be implausible under common-cause failure.

## Worked example: a test passes but cannot close the requirement

Requirement R42 states that emergency acknowledgement must occur within 200 ms for at least 99.9% of valid commands in a specified peak-load environment. The lab procedure sends 20 commands at idle load; all respond in 180 ms or less. The matrix marks R42 “Pass.” That is unjustified: the workload differs, the sample is too small for the percentile claim, and timestamp measurement uncertainty is undocumented. The correct status is **evidence incomplete**, with an approved plan for representative peak loading, clock synchronization, and statistical acceptance.

## Engineering use and evidence

Track each requirement's source, current version, priority, verification level, method, objective criterion, procedure, configuration hash, raw result, reviewer, and open exceptions. Flag missing links, duplicate closing evidence, stale tests, and waiver decisions. Distinguish verified requirement, validated operational need, and readiness authorization. Independent challenge should sample passing rows and attempt to reconstruct the claim from raw evidence.

## Limitations and connections

Coverage percentage is a bookkeeping measure and cannot by itself quantify system assurance. A matrix can be complete while the selected requirements are wrong. Connect verification planning to **requirements**, **test design**, **traceability**, **measurement uncertainty**, and **model credibility**.

## Technical analysis: a closed row needs a defensible claim boundary

A verification matrix row should identify a single versioned claim, its verification method, planned acceptance rule, data source, test configuration, result, discrepancy status, and reviewer authority. Suppose the requirement is “battery temperature shall stay below 60°C at continuous 2 kW output for 30 minutes in a 40°C ambient.” A test performed at 25°C ambient that records 55°C **does not close** that requirement, regardless of a green “pass” field. The result may support a partial argument, but the tested environment does not cover the stated environment.

For a measurement of `59.5°C` with expanded uncertainty `±1.2°C` at a specified coverage, an acceptance rule that requires the *upper uncertainty limit* below `60°C` does not pass; `59.5+1.2=60.7°C`. Some projects may use other contractually approved decision rules, but they must be stated **before** observing results. Record whether test uncertainty, manufacturing variation, and configuration equivalence have actually been considered. A matrix counts evidence relationships; it cannot automatically judge whether they are sufficient.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · Systems Engineering Handbook appendix (requirements and verification matrices)](https://www.nasa.gov/reference/system-engineering-handbook-appendix/) — Requirements review criteria and verification planning context.
- [NASA · Distinctions between product verification and validation](https://www.nasa.gov/reference/2-4-distinctions-between-product-verification-and-product-validation/) — Separate conformity to specifications from fitness for intended use.
- [NIST · Technical Note 1297, Reporting Measurement Uncertainty (1993)](https://www.nist.gov/pml/nist-technical-note-1297/nist-tn-1297-7-reporting-uncertainty) — Standard and expanded uncertainty, coverage factors, and reporting conditions.

## In-depth method: evaluating what a verification row really establishes

A VCRM is a control surface for an argument, not a tally of green hyperlinks. The [requirements-to-evidence guide](../methods/requirements-verification-handbook.md) includes a complete fictional test plan, raw rehearsal data, a statistical confidence calculation, and a cross-reference matrix that distinguishes planned evidence from accepted evidence.

### Represent each test result as a scoped proposition

A result should be read as: “Procedure T at revision P, applied to configured item B in scenario S, observed measurement M with instrument uncertainty U, and the approved rule produced disposition D.” If B or S does not match the current requirement, the result may still be useful background, but is not automatically closing evidence. A representative row needs at least **requirement ID/revision, method and procedure, test configuration, applicable conditions, objective criterion, result, discrepancies, reviewer, and disposition**.

A useful statistical boundary for a zero-failure demonstration with \(n\) independent binary trials is

\[
p_{f,U}=1-\alpha^{1/n}.
\]

At 95% one-sided confidence, 300 zero-failure observations yield a failure-probability upper bound of roughly 0.994%. That conclusion depends on the sampling model; 300 repeated requests in the same quiet minute may offer poor evidence for peak-load operation. Coverage reporting should therefore separate **requirement linkage**, **procedural completion**, **evidence applicability**, **statistical adequacy**, and **acceptance authority**.

**Review challenge.** A requirement says that 99% of peak-load requests shall finish within four seconds. One hundred idle-load requests all finish in under a second. The matrix has a passing test link. Which requirement has been verified? The answer is *not the stated peak-load population claim* unless the idle-load result has a formally justified relation to that claim.

## Phase 5 technical reading: Design a verification matrix that does not overclaim

The project's controlled VCRM maps `REQ-ACK` to synthetic `TEST-ACK-01`/`EV-ACK` and states the 2.0 s acceptance bound, recorded maximum 1.74 s, CM-B2 build and limited test load. A passing maximum observation does not establish a deadline-tail probability, and an injected command-gate test does not cover every hazard pathway. The [complete VCRM, ICD, hazard and change-impact package](../methods/campus-mobility-engineering-artifacts.md) demonstrates test provenance, accepted scope and explicit residual limitations. Version IDs allow independent configuration-currency checks instead of counting all green status labels as adequate evidence.



## Step 02 review studio — distinguish a populated matrix from a closed claim

A verification matrix should state requirement, method, configuration, procedure, measured result, acceptance rule, evidence location, review status and open findings. A check mark is the *conclusion* of a documented reasoning chain, not the evidence itself.

**Solved exercise:** in the fictional Northstar baseline, all four requirements have a linked verification procedure. Three reference current NS-B1 evidence; NS-R-04 refers to NS-B0. The trace matrix is **100% populated**, but only **75% has current-configuration evidence on its face**. Does that mean exactly 75% of the requirements are verified? **Not necessarily.** The other three procedures may be invalid or incomplete, and the fourth may be reusable if a formal impact analysis establishes equivalence. Treat 75% as a superficial currency indicator, not an assurance score.

**Next action:** document the evidence currency question, assign an owner, resolve by equivalence analysis or repeat test, and retain the original report and disposition. A controlled matrix preserves negative and inconclusive evidence rather than deleting rows to make progress look better.

## Follow the knowledge

**Related concepts**

- [Requirements: precise obligations, not persuasive sentences](good-requirements.md)
- [Verification, validation, and acceptance: the three different decisions](v-and-v.md)
- [Requirements traceability: a typed graph of engineering claims](traceability-graph.md)
- [Measures of effectiveness and performance](metrics-hierarchy.md)

**Go deeper in the 240-chapter textbooks**

- [Book 8, Chapter 02: Book 8 · Chapter 2: Requirements to critical test parameters](../B8/chapters/02-trace-requirements-and-stakeholder-expectations-to-obje.md)
- [Book 8, Chapter 10: Book 8 · Chapter 10: Evidence sufficiency and decision statistics](../B8/chapters/10-analyze-results-determine-evidence-sufficiency-and-reco.md)
- [Book 9, Chapter 12: Book 9 · Chapter 12 — Verify and validate the model, assess the design, respond to change, and defend the final baseline](../B9/chapters/12-verify-and-validate-the-model-assess-the-design-respond-to-change-an.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
