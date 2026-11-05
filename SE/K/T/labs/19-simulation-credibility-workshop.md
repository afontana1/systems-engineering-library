# Practice Lab T19 — Simulation credibility: verification, validation, and decision relevance

## Scenario
A scheduler simulator claims 95% service completion but its report contains inconsistent counts, and the validation dataset includes only served passengers.

## Investigation
1. Use [model-audit.csv](model-audit.csv) to check the arrivals/completed/rejected/pending invariant for every run.
2. Implement two additional model invariants: no negative queue lengths and no duplicate completed request IDs.
3. Create a validation matrix distinguishing implemented behavior, observed real-world behavior, parameter fit, and model-use restrictions.
4. Compare results under three hypothetical demand distributions. Which conclusions are robust and which are dependent on assumptions?
5. Write a one-paragraph model-credibility statement suitable for an architecture review board.

## Deliverable
Submit the failed audit rows, a discrepancy report with disposition, a reproducibility manifest, and a bounded decision claim. A high simulation sample size does not excuse invalid accounting.

[Return to the textbook chapter](../19-simulation-credibility.md)
