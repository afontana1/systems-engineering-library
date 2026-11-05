# Agile increments with an evidence-based safety boundary

**Concept essay · EN.645.780 · Phase 4 companion**

*Illustrative calculations and scenarios use synthetic data; do not treat them as certified operational evidence.*

An increment is a changed system configuration. For regulated or safety-critical systems, integration and operational authorization are different events. One can integrate code frequently while authorizing use less frequently. The separation enables fast learning without silently exposing users to unassured behavior.

Build an increment-level evidence contract: configuration hash; changed requirement and interface IDs; applicable hazards; cybersecurity findings; automated test run IDs; independent review status; rollback constraints; and approved operational scope. The contract is *machine-queryable* where practical and reviewed by accountable authorities.

### Claim–argument–evidence reasoning

A claim such as “the vehicle will not depart while a passenger is boarding” is supported by a specific behavioral argument and evidence from sensor tests, controller logic tests, degraded-mode trials, and controlled operational observations. One thousand passing nominal tests cannot replace missing evidence for a hazardous abnormal state. An evidence graph should make negative findings and unknowns queryable as well as successful tests.

### Worked change

A new accessible-boarding sensor is integrated into the dispatcher. The software team's dashboard reports 100% pass on 60 scripted tests. However, five tests used the previous gateway configuration, two used a stale test harness, and no evidence covers sensor dropout. The correct decision is not “release” or “throw away all testing.” Instead, isolate applicable evidence, regenerate configuration-specific results and add fault-injection tests before the authorized scope is expanded.

### Define three gates

1. **Development integration:** builds and basic technical checks pass; no field use implied.
2. **System integration:** representative hardware, interfaces and failure modes have been tested in a controlled environment.
3. **Operational release:** residual risk, validation evidence, training and recovery are approved for a defined population and configuration.

Practice: write an explicit release-blocking rule for missing hazard evidence and a separate rule for low-severity cosmetic defects. Avoid treating all findings identically.

---

[← Phase 4 contents](../README.md) · [Related course lessons](../README.html#en645780) · [Further reading](../RESOURCE-SHELF.md)
