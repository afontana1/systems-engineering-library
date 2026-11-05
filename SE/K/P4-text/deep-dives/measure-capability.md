# Capability, variation, and misleading averages

**Concept essay · EN.645.783 · Phase 4 companion**

*Illustrative calculations and scenarios use synthetic data; do not treat them as certified operational evidence.*

A process metric needs a definition, denominator, collection rule and decision. For lead time, specify the start and end events and how aborted and open cases are handled. For defects, specify detection windows and severity. For evidence completeness, specify the required fields by risk class. Combining incompatible case types can make a process appear better or worse without any actual improvement.

### Capability versus stability

A process may be statistically stable yet fail to meet customer expectations; conversely, it may pass most cases while exhibiting unpredictable special-cause failures. Control charts assess patterns in time-ordered variation under their assumptions. Capability indices such as Cp/Cpk were developed for continuous, suitably stable measurement processes with defined specification limits; applying them casually to discrete governance outcomes or heavy-tailed turnaround times can be misleading.

### Example with two subgroups

A dashboard reports mean lead time falling from 26 to 20 days. High-risk changes, however, rise from a median of 32 to 40 while low-risk cases drop from 19 to 12. If low-risk cases become more common, the aggregate trend could mask a real high-risk deterioration. Always display risk-class results and retain safety-evidence escapes as a separate guardrail.

### Establish a measurement system

Run a small agreement study: two independent reviewers classify 30 cases as requiring full safety review or streamlined review. Record where they disagree and revise decision criteria. Good precision in timestamps will not compensate for inconsistent risk classification.

**Exercise.** Draft a metric definition sheet including construct, event boundaries, owner, source, units, exclusions, expected direction, known bias and reaction rule.

---

[← Phase 4 contents](../README.md) · [Related course lessons](../README.html#en645783) · [Further reading](../RESOURCE-SHELF.md)
