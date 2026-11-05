# Configuration assurance: proving that the tested design is the delivered design

**Canonical reference · Expanded reference · Internal editorial and worked-example checks; independent external peer review not performed**

## The meaning of a controlled configuration

A **configuration baseline** identifies an agreed set of requirements, designs, interfaces, software, hardware items, supporting data, and verification evidence at a particular decision point. Configuration assurance asks whether the installed, tested, operated, and documented configurations actually correspond. A complete-looking requirements matrix is not enough: if the tested controller runs build R4 while the operational vehicle runs R5, the evidence may no longer apply to the deployed system.

The NASA configuration-management process distinguishes identification, change control, status accounting, and audits. These are related but not interchangeable. Identification specifies what is under control; change control makes decisions about proposed modifications; status accounting records the current state and its history; auditing compares stated baselines with actual products and evidence. The scope of control should include configuration-significant suppliers and enabling systems, not only top-level drawings.

## A typed change-impact graph

Represent configuration information as a directed graph `G=(V,E)` with typed nodes and edges. Nodes may be requirements, interface specifications, parts, firmware hashes, model versions, test procedures, results, and approved deviations. Typed edges include `satisfies`, `implemented-by`, `depends-on`, `verified-by`, and `released-with`. When a sensor model changes, traverse not only the direct hardware assembly but also calibration coefficients, sampling assumptions, timing constraints, software drivers, safety controls, and affected tests. A connection is a candidate impact, not proof that all linked elements must be redesigned.

A release condition can be expressed as a predicate: `ReleaseReady(c) = ApprovedChange(c) AND BaselineMatch(c) AND EvidenceCurrent(c) AND OpenWaiversAccepted(c)`. The terms require explicit rules. For instance, `EvidenceCurrent` may require test evidence on exactly the installed item, or on a demonstrably equivalent configuration under an approved equivalence argument. Graph reachability can reveal the review population; it cannot establish technical equivalence by itself.

## Worked example: the hidden incompatible pair

Suppose firmware F2 adds a higher-rate status stream, sensor S3 outputs a new packet format, and gateway G1 accepts only the old format. Each of the three items has its own passing component test. The combined configuration `F2/S3/G1` nevertheless fails the end-to-end data contract. If there are two independently selectable versions of each of three subsystems, a naive release space contains `2³ = 8` combinations; a single integration qualification covers at most one unless a justified family-of-configurations argument exists. A compatibility matrix with eight rows can show three explicitly permitted combinations and five blocked combinations. **Three approved combinations do not imply that three of eight random field upgrades are safe**, because version-selection probabilities and deployment rules were never specified.

A change package should identify originating need, alternatives, affected contracts, hazard and cybersecurity consequences, resource impact, review disposition, implementation owner, regression scope, and baseline-specific evidence. Retroactive documentation is inferior to controlling changes before units enter the field.

## Effectivity and as-built reconciliation

Effectivity expresses *which* serial numbers, locations, dates, and deployed software instances a particular change applies to. An engineering drawing can be correct while an old vehicle still contains an earlier replaceable assembly. Useful evidence includes installed part identifiers, software image hashes, calibration revisions, approved concessions, interface revisions, and time of installation. As-designed, as-built, as-tested, and as-maintained states should be traceable and differences explicitly reconciled.

The release authority must know whether a discrepancy is a harmless documentation defect, an incomplete test, or an unaccepted safety condition. A configuration audit is not a replacement for technical verification: matching the approved baseline establishes identity, whereas tests and analysis support the claim that the baseline meets its requirements.

## Common failures and review boundary

Watch for unreviewed supplier substitutions, undocumented firmware patches, stale test fixtures, data schemas changed without consumers, waived anomalies with no operating constraints, and uncontrolled field repairs. An immutable artifact hash helps detect change but does not prove artifact correctness or origin. A reliable release argument names the exact configuration, evidence population, exceptions, decision owners, and conditions requiring requalification.

## Selected source-to-claim references

- **C1 · Identification, control, status accounting and audits of baselines.:** [NASA Systems Engineering Handbook, 6.5 Configuration Management](https://www.nasa.gov/reference/6-5-configuration-management/). Identification, control, status accounting and audits of baselines.
- **C2 · Configuration integrity and recorded changes:** [NASA NPR 7123.1 Systems Engineering Procedural Requirements, configuration management process](https://nodis3.gsfc.nasa.gov/displayAll.cfm?Internal_ID=N_PR_7123_0001_&page_name=ALL). Configuration integrity and recorded changes; not the illustrative graph metrics.

## Follow the knowledge

- **Prerequisites:** [Work breakdown structures and technical baselines](wbs-and-baselines.md), [Requirements traceability: a typed graph of engineering claims](traceability-graph.md).
- **Related concepts:** [Interface control and integration contracts](interface-control.md), [CI/CD, configuration, and software assurance](software-lifecycle-evidence.md), [Supply-chain assurance: provenance, substitutions, and hidden dependencies](supply-chain-assurance-and-provenance.md).
- **Go deeper:** [Chapter 8 · Risk, Change, and Configuration Are Coupled](../B2/chapters/08-risk-change-and-quality.md), [Book 9 · Chapter 10 — Specify physical architectures, variants, configurations, instances, and lifecycle baselines](../B9/chapters/10-specify-physical-architectures-variants-configurations-instances-and.md), [Book 8 · Chapter 6: Qualification procedures and readiness](../B8/chapters/06-write-formal-qualification-procedures-and-conduct-the-t.md).
