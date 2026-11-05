# Interoperability contracts: syntax, semantics, time and permission

**Graduate companion concept essay · EN.645.771 · Phase 5**

*All case data are invented teaching examples; models and calculations are not approved operational or safety evidence.*

A passing API test proves that a test client can exchange a particular message under particular conditions. It does not show that actors understand the message the same way or may lawfully act on it. Engineering interoperability means defining **exchange semantics under an operational purpose**.

Consider a field named `available`. For a city bus fleet it may mean buses not in maintenance; for paratransit it may mean buses with certified accessible equipment and free operators. Numeric equality does not imply capability equivalence. A defensible contract specifies units, reference frames, service scope, observation time, update interval, confidence, source, authority to use the data, and a treatment for unknown values.

### Worked freshness calculation

One dispatch feed reports a vehicle at 12:00 and a decision occurs at 12:07. If the allowed age for time-critical assignment is 180 seconds, the age is `7×60=420 s` and the record must be rejected for that purpose. It might still be usable for hourly planning. Intended use determines acceptable age.

### A four-layer verification strategy

* **Wire:** can the two endpoints authenticate and exchange the stated schema?
* **Meaning:** do fields describe equivalent quantities and state transitions?
* **Workflow:** do ordering, retries, timeouts, authorization and exception handling work?
* **Mission:** can the participants use this information to produce a safe outcome in stressed scenarios?

Test disagreement and stale data deliberately. A good interface agreement includes a data owner, change-notice process, conformance fixtures, incident escalation and a degraded mode. These remain necessary when software adapters are used.

**Check.** Does using the same JSON schema mean two agencies are interoperable? No. Semantics, authority, timing and operational conditions remain open claims.

---

[← Phase 5 contents](../README.md) · [Concept pathways](../KNOWLEDGE-THREADS.md) · [Further reading](../RESOURCE-SHELF.md)
