## NS-GS4.1 extension — actionable traceability is configuration-specific

A connected requirements graph is not necessarily an actionable assurance argument. Every supporting record needs a valid type, configuration revision, evidence date, acceptance decision and owner. The synthetic case has four requirement-to-artifact paths, with a maximum instructional evidence age of 20 days. The case intentionally includes three distinct failures.

### Predicate for eligible evidence

For requirement \(r\), define \(A(r)=V(r)\land F(r)\land P(r)\), where \(V\) indicates exact revision match, \(F\) indicates age within 20 days, and \(P\) denotes an authorized approval of the evidence itself. The operational release decision must satisfy still more gates outside \(A\). This model permits exactly one actionable record: R-ACCESS. R-SAFETY is 22 days old and unapproved; R-INTEROP references interface revision 1.0 where revision 2.0 is required; R-PRIVACY is current and matching but unapproved.

Actionable coverage is therefore \(1/4=25\%\). The percentage is a **record coverage diagnostic**, not a service success fraction. Remediating R-INTEROP's revision alone would raise coverage to \(2/4\) if its evidence remained authorized and current. Rebuilding an index or running a link checker does not fix a stale experiment.

### Assumptions, adverse tests and operational limits

The case simplifies evidence validity to three predicates. Real assurance needs test environment, instrument calibration, requirements semantics, independence of reviewers, scope, chain of custody and retained negative results. Configuration mismatch should fail closed. An explicit negative test must reject an approval flag recorded as text (`"yes"`) rather than Boolean true; coercing strings into truth values would allow an authorization bypass.

### Worked exercise and explained solution

**Problem.** R-SAFETY has age 22 days and no approval. A new record is attached at age 4 days, but nobody signs it. Does it become actionable?

**Solution.** No. Updating freshness makes \(F=\mathrm{true}\), but \(P=\mathrm{false}\). By conjunction, \(A=\mathrm{false}\). The [integrated laboratory](../integrated/labs/INTEGRATED-CASE.html) asks students to identify all missing predicates before proposing the minimum new evidence.

**Canonical overlap.** The [software-intensive-architecture flagship](../../U/flagships/F05-software-intensive-architecture.html) describes software contracts; this extension concentrates on *version-specific claim eligibility*.

**Reproducibility record.** Re-run the [controlled executable model](../integrated/code/ns_gs_case.py) using the [shared case data](../integrated/data/ns-gs4.1-case.json), then compare with the [computed evidence record](../integrated/outputs/ns-gs4.1-results.json). The numerical outputs do not establish field validation or an authorized operating decision.
