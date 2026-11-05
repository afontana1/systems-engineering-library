# Pilot causal inference and unintended process consequences

**Concept essay · EN.645.783 · Phase 4 companion**

*Illustrative calculations and scenarios use synthetic data; do not treat them as certified operational evidence.*

Process improvements often arrive alongside staffing changes, demand spikes, case-mix shifts and new software. A before–after comparison cannot isolate the intervention automatically. Stronger pilot designs include matched concurrent comparison groups, randomization where ethically and operationally appropriate, predeclared outcome measures, and data-quality checks.

### A simplified difference-in-differences example

Pilot team's median lead time falls from 30 to 20 days, a change of −10. Comparison team falls from 28 to 25, a change of −3. A naïve difference-in-differences estimate is `−10 − (−3) = −7 days`. This arithmetic is illustrative: difference-in-differences is generally defined on **group means/expectations**, and medians do not automatically inherit its causal interpretation. Further, causal inference requires a credible parallel-trends assumption and no harmful spillovers. Do not present −7 days as a proven effect from these illustrative medians.

### Guardrails and mechanism tests

Track mandatory evidence escapes, later-discovered defects, reviewer workload, supplier rework and customer waiting. A checklist could reduce board rework but increase upstream preparation time. If that time lies outside the instrumented process boundary, the “gain” may be an accounting artifact. Work sampling and qualitative interviews are useful supplements.

### Decision rule

Go beyond “p < 0.05.” Specify the minimum meaningful improvement, acceptable guardrail change, exposure limit, expected cost and rollback triggers. If the pilot is underpowered, choose a measured extension rather than an unqualified scale-up.

**Exercise.** Design a two-team pilot and list at least five factors that could invalidate a causal conclusion. State which can be controlled, measured or only acknowledged.

---

[← Phase 4 contents](../README.md) · [Related course lessons](../README.html#en645783) · [Further reading](../RESOURCE-SHELF.md)
