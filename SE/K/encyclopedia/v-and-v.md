# Verification, validation, and acceptance: the three different decisions

**Reference entry · Assurance and test · Expanded reference**

## Core distinctions

**Verification** asks whether a defined artifact, subsystem, or system satisfies specified requirements. **Validation** asks whether the right solution has been created for the intended operational use and stakeholder need. **Acceptance** is an authorized decision to take delivery or assume responsibility under specified contractual, regulatory, safety, and operational conditions. A verified system may not be valid; a technically valid system may still be unacceptable because essential evidence, obligations, or authority is missing.

These terms apply throughout a lifecycle, not only at its end. Model verification, requirement validation, design verification, integrated test, operational demonstration, and service acceptance involve different claim boundaries and evidence. They must not be merged into a single green status.

## The claim–argument–evidence structure

A defensible assurance case begins with a **claim** (“the dispatch service meets its response-time requirement under specified load”), an **argument** explaining why evidence supports it, and **evidence** with provenance and applicability. Evidence is conditional on product version, configuration, environment, test population, instrumentation, assumptions, and the acceptance rule.

A verification cross-reference matrix maps requirements to methods—inspection, analysis, demonstration, or test—and to their resulting records. Coverage is necessary but insufficient: a row labeled “passed” does not reveal whether the measurement system was calibrated, the test environment was relevant, a fault was masked, or the tested build is the delivered build.

Independence matters especially for consequential claims. If development, test data generation, scoring, and acceptance all reuse the same unexamined assumption, apparent agreement is not independent corroboration.

## Worked example: evidence for a rare failure rate

Suppose a system requirement limits an independent per-demand failure probability to 1%. Zero failures in 30 independent representative demands is **not** persuasive evidence that the rate is below 1%. Under the Bernoulli model, the probability of seeing zero failures when the true failure rate is 1% equals **(0.99)³⁰ ≈ 0.740**; the outcome would be common even at the disallowed boundary.

For a one-sided 95% upper confidence limit after **n** independent demands with zero failures, solve **(1 − p)ⁿ = 0.05**, giving **p_upper = 1 − 0.05^(1/n)**. To make this upper bound at most 0.01 requires approximately **299 zero-failure demands**. Even then the inference depends on independence, representativeness, failure detection, and stable configuration; clustered common-cause failures may destroy the Bernoulli assumption. A production readiness decision may require additional operational evidence rather than only this test statistic.

## Evidence design

1. Identify each claim's subject and intended operating envelope.
2. Choose verification methods according to what can actually demonstrate the property.
3. Design representative and adverse scenarios, including failures and degraded modes.
4. Define measurement uncertainty, calibration, sample design, and decision thresholds in advance.
5. Preserve test procedure, build identity, configuration, raw results, anomalies, and adjudication.
6. Evaluate validity against real mission outcomes and affected stakeholder populations.
7. Separate the technical assessment from the **acceptance authority's** decision and recorded residual risk.

## Failure modes and limitations

A passed unit test is not equivalent to system verification; formal proof under abstract assumptions is not proof that the physical environment meets those assumptions. Testing the happy path can miss rare-event and interface failures. A simulator can support test planning but does not automatically replace the missing physical evidence. Statistical confidence pertains to a model of the sampling process, not a universal guarantee.

## Connections

This topic depends on requirements quality, operational scenarios, traceability, instrumentation, model credibility, and human decision authority. The same principle applies to agile continuous assurance: evidence must remain attached to the exact versions and intended uses it supports.

## Reference shelf retained from the earlier primer

These links are supplied for deeper reading. Confirm current publication versions before relying on them for compliance.

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — Reference chapters for lifecycle, needs, requirements, design, technical management, integration and V&V.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Breadth-first conceptual encyclopedia and pointers to further references.

**Expanded tutorial:** [From stakeholder need to verification evidence](../deep-dives/02-requirements-to-verification.md)


## Technical analysis: prove exactly which statistical claim is warranted

The zero-failure calculation above can be independently checked: `n ≥ ln(0.05)/ln(0.99) ≈ 298.07`, so the minimum integer is **299** independent representative demands. The bound is *one-sided frequentist confidence*, not “a 95% chance that this fixed rate is below 1%.” The confidence statement concerns the coverage of the procedure across hypothetical repeated studies. It assumes a fixed Bernoulli failure probability, complete failure detection, identical configuration, and representative independent trials.

At `n=299`, `p_upper = 1−0.05^(1/299) ≈ 0.00997`. If the demands share a battery defect or operator training effect, their failures may be correlated; 299 nominal requests are no longer equivalent to 299 independent trials. If some outcomes were unobservable, zero *recorded* failures is not zero true failures. A reliability qualification should therefore name the demand population, stress envelope, censoring criteria, configuration lineage, and admissible statistical procedure **before** execution.

Also distinguish **product verification** (against specified requirements) from **model verification** (implementation against a conceptual or mathematical specification) and from **operational validation** (fitness for intended use). These are different claims that can use overlapping evidence without becoming interchangeable. Acceptance authority may conditionally accept residual risk; acceptance does not change whether a technical requirement was actually demonstrated.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · Distinctions between product verification and validation](https://www.nasa.gov/reference/2-4-distinctions-between-product-verification-and-product-validation/) — Separate conformity to specifications from fitness for intended use.
- [NASA · Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 (2016/2017)](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle engineering, technical management, requirements, verification and validation.
- [NIST · NIST/SEMATECH e-Handbook of Statistical Methods (2002; online guidance)](https://www.nist.gov/publications/handbook-151-nistsematech-e-handbook-statistical-methods) — Statistical methods, experiments, reliability, and process assessment.



## Step 02 review studio — a verified wrong requirement is still a failure

**Verification** asks whether the engineered system conforms to specified requirements for a defined configuration and test domain. **Validation** asks whether the system satisfies its intended use and stakeholder needs. A requirement saying “the app shall show an acknowledgment within 8 seconds” may be verified while the service delivers phantom reservations or unusable pickup instructions.

**Solved exercise:** NS-R-01 passes a synthetic 8-second response test, but in representative user trials riders confuse “request received” with “vehicle reserved.” Has the stakeholder need for dependable booking been validated? **No.** The test may support a timing verification claim; it does not establish correct semantic confirmation or user understanding. Revise the ConOps and requirement hierarchy, then test the actual rider outcome.

**Evidence rule:** state the intended use, configuration, population and acceptance method. Testing a component in a simulator may provide valid lower-level evidence while leaving operational use unvalidated. Do not substitute the words verification and validation for each other in safety or release decisions.

## Follow the knowledge

**Related concepts**

- [Requirements and acceptance criteria](good-requirements.md)
- [Verification cross-reference matrices and test design](verification-matrix.md)
- [Simulation verification, validation, and credibility](model-vv-and-credibility.md)
- [Integration build-up and readiness evidence](integration-strategy.md)

**Explore in the 240-chapter textbooks**

- [Book 1, Chapter 11: Chapter 11 — From a Plausible Concept to Reviewable Evidence](../B1/chapters/11-realization-and-evidence.md)
- [Book 8, Chapter 1: Book 8 · Chapter 1: T&E strategy and acceptance authority](../B8/chapters/01-receive-the-design-baseline-and-create-the-integrated-t.md)
- [Book 8, Chapter 10: Book 8 · Chapter 10: Evidence sufficiency and decision statistics](../B8/chapters/10-analyze-results-determine-evidence-sufficiency-and-reco.md)

**Use this reference responsibly:** examples use hypothetical engineering data; the mathematical results rely on the assumptions stated in each passage. Recheck those assumptions for any real project.

