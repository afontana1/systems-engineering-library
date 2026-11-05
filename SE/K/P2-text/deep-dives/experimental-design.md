# A small factorial experiment, explained from first principles

*Phase 2 concept library deep dive · Independent instructional synthesis*

## Contrast rather than guess
In a two-factor design, factors A and B each have low (`−1`) and high (`+1`) settings. Running all four combinations gives average responses `y--`, `y+-`, `y-+`, `y++` using the first sign for A. A **main effect** is the average outcome at the high level minus that at the low level, averaging over the other factor. The **interaction** describes how one factor's effect changes depending on the other.

Define A = fleet size (2 versus 3), B = dispatch (fixed versus dynamic), with waiting time in minutes as the lower-is-better response. Our illustrative deterministic outputs are `y-- = 15`, `y+- = 10`, `y-+ = 12`, `y++ = 7`. Effect A = `(10 + 7)/2 - (15 + 12)/2 = −5` minutes. Effect B = `(12 + 7)/2 - (15 + 10)/2 = −3` minutes. The difference-of-differences, `[(7 − 10) − (12 − 15)] = 0`, shows no interaction under these four sample values. That does not imply no interaction in reality.

A different set, `15, 11, 12, 5`, makes the dispatch improvement 3 minutes for a two-vehicle fleet and 6 minutes for a three-vehicle fleet. The difference-of-differences is `−3` minutes. This might make a combined design attractive even if each factor alone looked modest.

## What experiment design must control
Randomize run order when physical drift or operator learning might matter. If using simulation, employ repeated demand seeds and consider common random numbers for direct comparisons. Define response units, observation window and inclusion rules. Replicate each cell to estimate run-to-run noise; a four-number table without replication describes a deterministic scenario, not a hypothesis test with uncertainty. Report confounding, failure to randomize, model applicability and missing factors.

## From experiments to decisions
Imagine a design review requires mean wait below 9 minutes without violating accessibility or cost limits. A four-cell table may suggest only the three-vehicle dynamic concept clears the wait target. But a robust decision also checks distribution tails, rider demand composition, budget and sensitivity to demand surges. Experiments inform the design argument; they do not decide the stakeholder objective for you.

## Practice with a solution
**Question:** The four results are `14, 9, 11, 5` in `(A−B−, A+B−, A−B+, A+B+)` order. Compute A and B main effects and difference-of-differences. **Answer:** A = `(9+5)/2 − (14+11)/2 = −5.5`. B = `(11+5)/2 − (14+9)/2 = −3.5`. Interaction difference-of-differences = `(5−9) − (11−14) = −1`. Report results in minutes and note the need for replications.

[Back to Phase 2 companion index](../README.md)
