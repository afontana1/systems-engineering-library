# Mission effectiveness is not subsystem performance

**Concept essay · EN.645.782 · Phase 4 companion**

*Illustrative calculations and scenarios use synthetic data; do not treat them as certified operational evidence.*

A mission is an outcome-oriented activity across systems, people, policies, and environment. A subsystem can satisfy all its technical specifications while the mission fails due to unavailable operators, inaccessible facilities or conflicting priorities. Mission engineering starts with scenarios and measures of **effectiveness** (MOEs) before translating needs into system performance measures (MOPs) and technical performance measures (TPMs).

### Three measures

| Level | Example | What it does not prove |
|---|---|---|
| MOE | Fraction of affected riders evacuated safely within the required window | Why success/failure occurred |
| MOP | Percentage of dispatch messages delivered within 3 s | Accessibility or evacuation success |
| TPM | Radio link margin at design operating distance | Mission reliability in crowd and weather |

### A simple multiplicative chain

For an illustration, suppose mission success requires independent events A, B and C, each with probability 0.95. Then `P(success) = 0.95³ ≈ 0.8574`. The independence assumption is often inappropriate: a single power outage could affect all three. More accurate models represent common-cause conditions, sequential dependence and conditional adaptation.

### Intervention comparison

Northstar has funding for either one more shuttle, better operator communications or improved accessible staging. Model at least three operational scenarios, including crowded peak, power outage and high-accessibility demand. The option with best vehicle throughput is not necessarily the option with best mission evacuation performance. Present outcome distributions and operational constraints before recommending.

**Exercise.** Draw the boundary of a night-time evacuation mission. Explicitly include a human decision, a facility dependency and a communications dependency that the shuttle product architecture omits.

---

[← Phase 4 contents](../README.md) · [Related course lessons](../README.html#en645782) · [Further reading](../RESOURCE-SHELF.md)
