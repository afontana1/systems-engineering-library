# Authority, provenance, and a federated digital thread

**Concept essay · EN.645.782 · Phase 4 companion**

*Illustrative calculations and scenarios use synthetic data; do not treat them as certified operational evidence.*

A digital thread is not a special file type. It is a set of **typed, time-aware relationships** between engineering objects whose owners and configurations are known. In a federated system, requirements, model definitions, source code, test runs and field measurements may live in different tools. The question is not which tool “owns everything”; it is which is authoritative for a specific claim at a specific lifecycle stage.

A minimal evidence node should have an identifier, object type, creator/owner, version, effective dates, access classification, checksum or immutable reference where appropriate, and a declared intended use. An edge should name its semantics—e.g., `satisfies`, `tests`, `derived_from`, `applies_to_configuration`—and often needs its own approval status.

### Example graph failure

Requirement R-07 states the deployed system must detect obstructed boarding. Design D-09 satisfies R-07. Test case T-14 tests D-09. Result E-203 reports pass. The problem: E-203 was run against controller v2, while release candidate is v3. An ordinary reachability query declares R-07 covered. A configuration-consistent closure query correctly declares the release unsupported.

### A useful set of invariant checks

* Every active safety claim has at least one approved, applicable test result.
* No approved result references an unknown configuration.
* Every changed interface has an identified downstream owner.
* Archived evidence can be reproduced or its limits are recorded.
* A deletion or replacement operation has an auditable lineage.

### Exercise

Take five columns of an ordinary trace matrix and redesign it as a node/edge model. Add `tested_version` and `release_version`. Explain a failure that the five-column matrix would miss.

---

[← Phase 4 contents](../README.md) · [Related course lessons](../README.html#en645782) · [Further reading](../RESOURCE-SHELF.md)
