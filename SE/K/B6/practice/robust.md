# Advanced Workshop · Robust Concepts, Regret, and Value of Information

*Book 6 · Week 9 · scenario uncertainty · expected loss · minimax regret · sensitivity analysis*

**Placement:** After the relevant chapter, use this workshop to extend the reasoning, then try [the corresponding hypothetical lab](lab-robust.md). The assessed course obligations remain in [the curriculum](../../../C/P2/EN645767.html).

## 1. Choose a decision rule before looking for a winner

Systems engineers often compare alternatives under uncertain demand, weather, operating policy and costs. Those conditions are not interchangeable: **aleatory variability** describes genuinely varying conditions, while **epistemic uncertainty** describes missing knowledge. If a decision cannot be reversed cheaply, it may be rational to prefer a design that performs acceptably across plausible scenarios rather than optimizing for a single forecast. But robustness is not a synonym for conservatism; its definition depends on the sponsor's risk posture and on which scenarios have legitimate credibility.

In the fictional Northstar concept study, three feasible design options A, B, and C face normal and stressed service conditions. The table reports a synthetic loss measure in consistent units where smaller is better. It can represent penalty points or a normalized cost, but must not be mislabeled dollars without calibration.

| Design | Normal loss | Stress loss |
|---|---:|---:|
| A | 25 | 75 |
| B | 38 | 45 |
| C | 40 | 40 |

A is best when normal operations dominate, C is best in the stress scenario, and B compromises. No single option dominates both scenarios. The trade is real rather than a failure of optimization.

## 2. Expected value depends on scenario probabilities

Let \(p\) be the probability of stress and assume mutually exclusive, exhaustive scenarios. The expected losses are

\[
L_A(p)=25+50p,\qquad L_B(p)=38+7p,\qquad L_C(p)=40.
\]

At \(p=0.25\), A has expected loss 37.5, B 39.75, and C 40; A is preferred by **minimum expected loss**. However, if the stress probability exceeds the A–B crossover \(p=13/43\approx0.3023\), B beats A. The design review should not claim “A is best” without naming this assumption. Decision weights or probabilities are part of the decision baseline and deserve version control like requirements.

## 3. Minimax regret answers a different question

Regret compares each alternative with the best alternative *for the scenario that actually occurs*. In normal operation the minimum loss is 25; in stress it is 40. Regrets are therefore A=(0,35), B=(13,5), C=(15,0). Maximum regrets are 35, 13, and 15. **Minimax regret selects B**, even though expected loss at p=0.25 selects A. Neither rule is inherently correct without stakeholder risk preferences. Regret is particularly useful when scenario probabilities are too weak to justify precise expected-value arithmetic, but the scenario set still matters enormously.

A robust optimization study should reveal if a decision changes under reasonable changes in scenario definition, loss normalization and constraints. If “stress” bundles unlike events into one number, the analysis can hide distinct failure modes. Build transparent scenario families, not one giant worst-case label that makes any preferred design look bad.

## 4. Value of information is not free certainty

Suppose an experiment could reveal whether the stress scenario is likely, but it is noisy and costly. The expected value of perfect information (EVPI) is the minimum expected loss *without* information minus the expected loss obtained when one could choose the best alternative separately after learning the true scenario. For p=0.25, the best expected loss is 37.5, while the perfect-information expected loss is \(0.75(25)+0.25(40)=28.75\). Thus EVPI is **8.75 loss units**. No imperfect information source can have greater expected value than perfect information under the same model and utility scale.

An experiment costing 12 loss units cannot be economically justified solely by the promised improvement in this decision model, even if perfect; an experiment costing two units might be worth exploring, but only if its expected information quality justifies it. A credible experiment design must estimate likelihoods of observed evidence under each scenario and update probabilities rather than assuming the test will produce omniscience.

## 5. A conditional decision memo

A sound review can report: “A minimizes expected loss at the stated stress probability, B minimizes maximum regret over the two considered scenarios, and the preference switches near p=.302. We recommend keeping both candidates open until an operations pilot improves the stress estimate or the sponsor explicitly selects a regret-based policy.” This is not indecision. It is a decision that remains scientifically honest about its dependence on values and uncertain evidence.

## Worked problem set — attempt before revealing solutions

### Problem 1

At stress probability p=.25, compute expected losses for A, B, C.

<details><summary>Show solution 1</summary>

A=37.5, B=39.75, C=40. Minimum expected loss chooses A under these assumptions.

</details>

### Problem 2

Find the A–B crossover probability.

<details><summary>Show solution 2</summary>

Solve 25+50p = 38+7p, giving p = 13/43 ≈ 0.3023.

</details>

### Problem 3

Compute minimax regret over the two scenarios.

<details><summary>Show solution 3</summary>

Scenario minima are 25 and 40; maximum regrets A=35, B=13, C=15. Minimax regret selects B.

</details>

### Problem 4

Compute EVPI at stress probability .25 in loss units.

<details><summary>Show solution 4</summary>

Current optimal expected loss 37.5; perfect-information loss .75×25 + .25×40 = 28.75. EVPI = 8.75 loss units.

</details>

## Independent transfer to the Northstar case

Load `book6-concepts.csv` and add two scenario-loss columns. Compare expected loss and minimax regret using `book6.py`. Sweep stress probability from 0 to 1, mark changes in the preferred alternative, and make one graph. Then introduce an explicitly priced experiment and decide whether its upper bound (EVPI) is large enough to warrant further study. Record what probability, evidence, or stakeholder preference could reverse your recommendation.

## Further reading and conventions

The worked numbers are synthetic instructional fixtures. Do not use them as empirical transportation predictions, certification evidence, or claims about a particular deployed product. Foundational references (external and optional):

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/)

- [SEBoK — Guide to Systems Engineering](https://sebokwiki.org/wiki/SEBoK_Introduction)

- [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final)

**Continue:** [Hypothetical application lab](lab-robust.md) · [Python source](book6.py) · [Experiment dataset](book6-concepts.csv) · [Interactive workbench](WORKBENCH.html).
