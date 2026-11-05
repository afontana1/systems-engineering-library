# CI/CD, configuration, and software assurance

**Reference entry · MBSE and software-intensive systems · Expanded reference**

## Definition and diagnostic distinction

A **software lifecycle evidence chain** connects intended behavior to requirements, architecture, source changes, executable builds, verification results, deployment configurations, and observed operation. Continuous integration and delivery automate transitions within that chain; they do not eliminate the need for controlled technical baselines. “All pipeline jobs passed” is an assertion about a particular workflow and build, not proof that a system is safe or suitable for its mission.

## Theory: evidence attaches to configuration identity

Represent a release as `R = (source revision, dependency lock, compiler/toolchain, build parameters, configuration, environment, evidence set)`. An artifact digest identifies bytes; provenance explains how those bytes were created and what tests were applied. An assurance claim should be traceable through a typed relation such as `testedBuild(test, digest)` and `deployedBuild(environment, digest)`. Passing tests against one executable and deploying another breaks the reasoning even if filenames match.

Continuous assurance combines static checks, unit and integration tests, architecture conformance, vulnerability assessment, scenario-level tests, and controlled exceptions. Tests provide coverage of chosen properties under chosen conditions. They cannot establish the absence of all defects. For safety-critical functions, review authority and hazard-based qualification may need to be independent from the sprint team. Faster iteration is valuable only when the evidence production process keeps pace with change.

## Worked example: a green pipeline with the wrong binary

A team tests source revision `a14` with dependency library 3.2 and produces artifact digest `H1`. The deployment rebuilds the same source but resolves library 3.3, producing digest `H2`. Unit results from `H1` do not automatically cover `H2`; new concurrency behavior may have entered through the dependency. The corrective control is to promote the **tested artifact** immutably, or rebuild under a reproducible environment and prove equivalence before approval. A rollback plan must identify compatible data schemas and operator procedures, not merely an older binary.

## Engineering use and evidence

Require stable identity for commits, dependencies, containers, test equipment, simulators, generated code, configuration, and deployed instances. Maintain bidirectional change links to risks and affected requirements. Put hazard-relevant tests in the release gate and retain exception approvals with expiration conditions. Use fault injection and operational telemetry to test claims that are inaccessible in isolated unit tests. After deployment, monitor leading indicators of failure and maintain a path for safe recovery.

## Limitations and connections

Automation can rapidly repeat a flawed test and make false confidence more reproducible. A reproducible build does not guarantee a correct specification. Connect software lifecycle evidence to **traceability**, **software quality attributes**, **verification matrices**, **digital-thread provenance**, and **risk acceptance**.

## Technical analysis: a passing pipeline is a versioned evidence claim

Continuous integration is an evidence-production system only if test outputs are linked to the exact source, dependencies, build environment, test configuration, and release artifact. A green status for a branch is not proof that a differently built binary has passed the same checks. Configuration management and software assurance must cover changing compilers, libraries, deployment policies, and controlled exceptions.

For example, a regression suite reports **480 passed tests** on build `B17`, but the deployed release `B18` contains a dependency update. The fraction `480/480 = 100%` is a result about the executed suite and B17, not a success probability or verification result for B18. An auditable release record should include immutable build identity, requirements-to-test coverage, security scan versions, outstanding anomalies, reviewer approval, and a rollback configuration; any transfer of evidence from B17 to B18 requires an explicit equivalence rationale.

**Evidence boundary.** Report tests **not run**, flaky outcomes, operational profiles, and defect escape rates; count only tests that bear on declared claims. A very high test count can coexist with weak requirements coverage or undocumented production configuration changes. NASA software assurance guidance is a procedural reference, not an endorsement of a particular tool or a guarantee of safety.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** NASA software engineering and assurance guidance connects implementation, verification, lifecycle and configuration responsibilities. **Evidence:** [NASA — NASA-HDBK-2203 Software Engineering and Assurance Handbook, Software planning, configuration, assurance and product evidence (see software lifecycle topics)](https://swehb.nasa.gov/) · *direct guidance*.
- **C2:** Configuration management maintains product identity and approved change status over time. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §6.5 Configuration Management](https://www.nasa.gov/reference/6-5-configuration-management/) · *direct guidance*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NIST · SP 800-160 Vol. 1 Rev. 1, Engineering Trustworthy Secure Systems (2022)](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final) — System-level security and trustworthiness engineering.
- [NASA · Distinctions between product verification and validation](https://www.nasa.gov/reference/2-4-distinctions-between-product-verification-and-product-validation/) — Separate conformity to specifications from fitness for intended use.

## Follow the knowledge

**Related concepts**

- [Requirements traceability: a typed graph of engineering claims](traceability-graph.md)
- [Verification, validation, and acceptance: the three different decisions](v-and-v.md)
- [Software quality attributes and architectural tactics](software-quality-attributes.md)
- [Digital thread and digital twin: preserving engineering meaning across time](digital-thread-and-twin.md)

**Go deeper in the 240-chapter textbooks**

- [Book 5, Chapter 05: Book V · Chapter 5: Iteration must still produce system evidence](../B5/chapters/05-integrate-agile-product-engineering-with-syst.md)
- [Book 5, Chapter 10: Book V · Chapter 10: The verification chain includes build identity](../B5/chapters/10-design-testing-ci-and-an-integrated-software-.md)
- [Book 15, Chapter 10: Week 10 · Agile Systems Engineering · Book chapter: Create a cyber-physical DevSecOps and continual-integration system, then red-team a failed increment](../B15/chapters/10.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
