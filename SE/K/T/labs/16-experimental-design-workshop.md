# Practice Lab T16 — Experimental design: ask a question the evidence can answer

## Scenario
Compare two fleet sizes and two dispatch policies. Each row of the supplied file represents a complete independent synthetic demand day, not an individual passenger.

## Procedure
1. Inspect [factorial-results.csv](factorial-results.csv), which contains three replications per design cell.
2. Compute cell means, average main effects, and the difference-of-differences interaction by hand.
3. Run [factorial.py](../tools/factorial.py) and verify the calculations. Replace one observation to see how sensitive the conclusions are.
4. Rewrite the experiment to use paired demand streams. State what would be held constant and what the unit of randomization would be.
5. Add an explicit secondary condition: at least 90% service completion across each tested stratum. Describe how an otherwise favorable delay result could be rejected.

## Deliverable
Produce an experiment protocol and a one-page results memo with estimates, uncertainty limitations, decision rules, and a reproducibility appendix. Avoid concluding “no effect” solely from an inconclusive small sample.

[Return to the textbook chapter](../16-experimental-design.md)
