# Evidence-aware backlogs and the economics of learning

**Concept essay · EN.645.780 · Phase 4 companion**

*Illustrative calculations and scenarios use synthetic data; do not treat them as certified operational evidence.*

An agile engineering backlog is a portfolio of competing investments: operational capability, risk reduction, experimentation, architecture, verification, quality and maintenance. Comparing them using a single arbitrary point scale can hide genuinely different obligations. A safety-critical verification activity may be mandatory rather than a discretionary competitor to a feature.

Distinguish **hard constraints** (requirements that may not be traded away), **desired outcomes** (quantifiable benefits), **uncertainty reduction** (new information) and **capacity requirements** (scarce experts, test rigs, suppliers). Ranking is meaningful only after the hard constraints are enforced.

### Value of an experiment

A proposed design choice has two equally likely outcomes. If you commit immediately to Design A, expected loss is $70,000. A proposed experiment costs $12,000 and, in a simplified model, provides perfect information allowing an expected post-test loss of $35,000. The expected gross value of perfect information is $35,000 and the net value is $23,000. Real experiments provide imperfect information and require posterior decision analysis; never apply the perfect-information benefit automatically.

### Decision worksheet

For each proposed initiative record: objective; hypotheses; hard constraints; evidence gap; expected consequence of error; technical coupling; reversible commitment date; experiment cost; likely decision after observing outcome; and reason to act now rather than later. Use a Pareto view for conflicting outcomes instead of pretending all tradeoffs can be reduced to a unique scalar.

### Practical exercise

Draft a six-week plan with five engineering items but only one shared integration rig. Explain why a mandatory regression test enters the plan before a lower-risk new feature even if the feature's perceived value is higher. Then test how your choice changes if the rig becomes available only every fourth week.

---

[← Phase 4 contents](../README.md) · [Related course lessons](../README.html#en645780) · [Further reading](../RESOURCE-SHELF.md)
