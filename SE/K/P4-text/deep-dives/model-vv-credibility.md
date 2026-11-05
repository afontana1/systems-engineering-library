# Model credibility is scoped to a decision

**Concept essay · EN.645.782 · Phase 4 companion**

*Illustrative calculations and scenarios use synthetic data; do not treat them as certified operational evidence.*

Engineers routinely conflate model correctness with model usefulness. A model's **implementation verification** checks its consistency with the conceptual specification; **validation** compares its behavior with available reference evidence for an intended use; **credibility assessment** combines these with data pedigree, sensitivity, uncertainty, expert review, and consequence. None makes a model universally trustworthy.

### Example: evacuation operations

A queue model predicts that 95% of riders can board within 9 minutes. Model code passes internal checks and scenario replay. However, its input sample underrepresents mobility-device users and its demand data exclude a major event. Validation evidence is insufficient for the inclusive-service decision even though the model is computationally correct.

Define a credibility record with:

1. Decision, audience and harm from wrong inference.
2. Model scope, excluded physics/behaviors and assumptions.
3. Input sources, units, dates and sample coverage.
4. Code verification and numerical checks.
5. Validation comparisons and observed discrepancies.
6. Sensitivity to uncertain inputs, model-form uncertainty and limitations.
7. Approval scope, review date and change triggers.

### Scenario stress test

Vary accessible-boarding fraction from 5% to 25%, demand peaks from 1x to 2x and telemetry outage from 0% to 10%. A conclusion that holds only in nominal demand should not be advertised as resilient mission performance. Results can support additional experiments rather than immediate fleet-level commitment.

**Check.** Why is one successful trial insufficient to validate a mission simulator? Because it represents only a narrow combination of conditions and may hide structural model errors.

---

[← Phase 4 contents](../README.md) · [Related course lessons](../README.html#en645782) · [Further reading](../RESOURCE-SHELF.md)
