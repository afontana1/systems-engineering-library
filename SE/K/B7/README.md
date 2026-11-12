# Book 7 — System Design and Integration

EN.645-768 · Phase 2 · Twelve connected chapters and twelve fictional labs

**How to study:** Start with the updated [course guide](../../C/P2/EN645768.md), then read the chapter and work the lab before the graded deliverable. The website is `OPEN-BOOK.html`; the Markdown remains fully editable.

- **Week 12:** [Chapter — Conduct the Final Design & Integration Review and hand off to T&E](chapters/12-conduct-the-final-design-integration-review-and-hand-of.md) · [Lab](labs/lab-12-conduct-the-final-design-integration-review-and-hand-of.md)
- **Week 11:** [Chapter — Baseline verification, validation, customer evidence, and CDR readiness](chapters/11-baseline-verification-validation-customer-evidence-and-.md) · [Lab](labs/lab-11-baseline-verification-validation-customer-evidence-and-.md)
- **Week 10:** [Chapter — Plan system integration and conduct the Integration Readiness Review](chapters/10-plan-system-integration-and-conduct-the-integration-rea.md) · [Lab](labs/lab-10-plan-system-integration-and-conduct-the-integration-rea.md)
- **Week 9:** [Chapter — Design for supportability, producibility, supply, sustainability, and disposal](chapters/09-design-for-supportability-producibility-supply-sustaina.md) · [Lab](labs/lab-09-design-for-supportability-producibility-supply-sustaina.md)
- **Week 8:** [Chapter — Design for human performance, safety, security, usability, and resilience](chapters/08-design-for-human-performance-safety-security-usability-.md) · [Lab](labs/lab-08-design-for-human-performance-safety-security-usability-.md)
- **Week 7:** [Chapter — Design for reliability, availability, and maintainability](chapters/07-design-for-reliability-availability-and-maintainability.md) · [Lab](labs/lab-07-design-for-reliability-availability-and-maintainability.md)
- **Week 6:** [Chapter — Integrate multidisciplinary design and conduct the PDR-style review](chapters/06-integrate-multidisciplinary-design-and-conduct-the-pdr-.md) · [Lab](labs/lab-06-integrate-multidisciplinary-design-and-conduct-the-pdr-.md)
- **Week 5:** [Chapter — Use prototypes and experiments to retire technology and design risk](chapters/05-use-prototypes-and-experiments-to-retire-technology-and.md) · [Lab](labs/lab-05-use-prototypes-and-experiments-to-retire-technology-and.md)
- **Week 4:** [Chapter — Mature the physical architecture, interfaces, and performance budgets](chapters/04-mature-the-physical-architecture-interfaces-and-perform.md) · [Lab](labs/lab-04-mature-the-physical-architecture-interfaces-and-perform.md)
- **Week 3:** [Chapter — Allocate requirements and define component functions](chapters/03-allocate-requirements-and-define-component-functions.md) · [Lab](labs/lab-03-allocate-requirements-and-define-component-functions.md)
- **Week 2:** [Chapter — Close the system specification](chapters/02-close-the-system-specification.md) · [Lab](labs/lab-02-close-the-system-specification.md)
- **Week 1:** [Chapter — Receive the concept baseline and plan design maturation](chapters/01-receive-the-concept-baseline-and-plan-design-maturation.md) · [Lab](labs/lab-01-receive-the-concept-baseline-and-plan-design-maturation.md)

## NS-DI7.1 integrated design-and-integration case

All twelve chapters use [one controlled design case](case/INDEX.html) with [requirements](case/requirements.csv), [functional allocations](case/allocation.csv), [interface contracts](case/interfaces.csv), [architecture](case/architecture.svg), [synthetic factorial experiment](case/doe-synthetic.csv), [evidence register](case/evidence-register.csv), and [Python calculation and consistency checker](tools/step03_book7_design_check.py). The example separates modeled timing feasibility from failed mission reliability, availability shortfalls, and stale/unexecuted evidence. **Operational release remains on HOLD.**

## Applied resources

- [`datasets/`](datasets/) contains toy input and evidence sheets.
- [`notebooks/`](notebooks/) contains executable guided calculations.
- [`diagrams/`](diagrams/) contains editable system/evidence maps.

*The fictional Northstar case is illustrative, not an approved or independently qualified design.*


## Deeper concept readings

- [Safety engineering: from hazards to enforceable constraints](../T/13-safety-constraints.md)
- [Reliability, availability, and maintenance are different claims](../T/17-reliability-maintenance.md)
