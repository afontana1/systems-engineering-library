# Technical data governance: lineage, meaning, and controlled reuse

**Canonical reference · Expanded reference · Internal editorial and worked-example checks; independent external peer review not performed**

## Data is an engineering claim in a particular context

**Technical data governance** assigns responsibility for identifying, interpreting, protecting, retaining, finding, and changing information used in engineering decisions. The aim is not merely to create a data lake. Data becomes useful evidence only if its meaning, origin, version, units, quality, access rights, and permitted uses are known. NASA technical data management guidance places identification, protection, metadata, access, use and long-term value within crosscutting systems engineering and distinguishes routine data management from the stricter change process for configuration-controlled records.

A shuttle telemetry record labelled `speed=12` is ambiguous: metres per second or miles per hour, wheel speed or ground speed, which vehicle, which timestamp clock, which calibration, and what missing-value convention? Combining two systems without resolving these questions can create a plausible yet wrong performance graph. Data interoperability requires agreement on semantics, not only file format or API transport.

## Build lineage as a versioned dependency graph

For every decision-relevant dataset, capture source system, producer, collection context, transformation sequence, software version, schema version, validation rules, time basis, access authorization, retention disposition, and decision outputs that depended on it. A lineage edge may mean `measured-by`, `cleaned-with`, `joined-to`, `estimated-from`, or `approved-for`. Different edge types imply different obligations. A future schema migration should identify which derived metrics, dashboards, models and acceptance results may change.

Data-quality criteria need operational meaning: completeness, validity, accuracy, consistency, timeliness, uniqueness, and representativeness are not interchangeable. Completeness can be measured by non-null records, but a complete dataset can still suffer severe selection bias. A synchronized timestamp can still be wrong if the wrong clock domain was used. Protection includes availability and integrity as well as confidentiality; keeping inaccessible but perfectly encrypted records can defeat a safety review.

## Worked example: a convincing wrong uptime rate

Suppose 600 service requests were made, 18 were dropped before the telemetry collector recorded them, and 570 of the remaining 582 were served successfully. The dashboard reports `570/582 = 97.94%` if it measures success only among recorded requests. The mission-level success rate is `570/600 = 95.00%`. This is not a small rounding error: the denominator changed. If the lost requests correlate with degraded communications, the omission is *informative missingness*. Adding more data from normally functioning periods will not remove that bias.

A record contract should therefore include the count of attempted requests at the authoritative source, how rejects and timeouts are represented, and how discrepancies across systems are reconciled. A metric owner should reject a seemingly precise estimate that cannot recover the relevant population.

## Reproducibility and rights

To reproduce a decision, preserve snapshot identifiers, data extraction queries, units, time windows, transformation logic, model parameter files, random seeds where relevant, and final result checksums. Versioning alone is inadequate if the input dataset is mutable in place or externally hosted and later replaced. Where personal or security-sensitive data appears, provide role-based access, retention controls, auditability and purpose-limited disclosure rather than distributing unrestricted copies. Sensitive data may need de-identification, but de-identification has reidentification risks and should not be equated with anonymous truth.

## Governance failure modes and review boundary

Beware orphaned data products, undocumented manual spreadsheet changes, semantic drift behind a stable field name, hidden timezone shifts, incomplete migration backfills, and dashboards without denominator ownership. An effective data release answers: Who produced this record? What exactly does it mean? Which configuration and operating conditions generated it? Which transformations altered it? Who can correct it? Which decisions would change if it were wrong?

## Selected source-to-claim references

- **D1 · Technical data access, protection, metadata, retention, coordination with configuration management.:** [NASA Systems Engineering Handbook, 6.6 Technical Data Management](https://www.nasa.gov/reference/6-6-technical-data-management/). Technical data access, protection, metadata, retention, coordination with configuration management.
- **D2 · Access control and audit-accountability context:** [NIST SP 800-53 Rev. 5, Security and Privacy Controls for Information Systems and Organizations](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final). Access control and audit-accountability context; local governance policies remain necessary.

## Follow the knowledge

- **Prerequisites:** [Digital thread and digital twin: preserving engineering meaning across time](digital-thread-and-twin.md), [Requirements traceability: a typed graph of engineering claims](traceability-graph.md).
- **Related concepts:** [Configuration assurance: proving that the tested design is the delivered design](configuration-assurance-and-change-control.md), [Simulation verification, validation, and credibility](model-vv-and-credibility.md), [Measurement traceability and calibration: accuracy is a chain of evidence](measurement-traceability-and-calibration.md).
- **Go deeper:** [Book 10 · Chapter 03 — Establish data provenance, sampling validity, exploratory analysis, and measurement uncertainty](../B10/chapters/03-establish-data-provenance-sampling-validity-exploratory-analysis-and.md), [Book 9 · Chapter 08 — Build executable parametric models with units, provenance, constraints, and linked analytics](../B9/chapters/08-build-executable-parametric-models-with-units-provenance-constraints.md), [Week 06 · System of Systems Engineering · Chapter 06 — Information fusion, provenance, confidence, and data quality](../B18/chapters/06.md).
