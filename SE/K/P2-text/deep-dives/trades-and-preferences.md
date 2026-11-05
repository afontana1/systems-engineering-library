# Trade studies: feasibility, preference and uncertainty are different axes

*Phase 2 concept library deep dive · Independent instructional synthesis*

## The four gates in a defensible decision
A decision analysis starts with a reason to decide, not a weighting spreadsheet. First identify the objective and authority: what will the choice enable, who owns it, and what downstream commitments does it entail? Second screen **mandatory feasibility constraints**. A concept lacking an approved safe operating mode cannot be rescued by cheap acquisition cost. Third compare **value among the feasible choices** through well-defined attributes and preference functions. Finally, examine uncertainty, model defects and decision reversibility.

In additive multiattribute evaluation, a score `V(x) = Σ w_i v_i(x_i)` can be practical, but only if weights and value scales have coherent interpretation. Values `v_i` must map raw attribute levels to stakeholder preference over clearly defined ranges; weights compare the value of moving from the low to high anchor of each attribute. A 0.9 "availability value" does not directly mean 90% probability of availability. A weight of 0.6 is not necessarily a statement that one criterion is morally 60% important.

## A transparent ranking reversal
Consider two *feasible* dispatch service concepts. A has normalized availability 0.9 and affordability 0.4; B has values 0.7 and 0.8. With availability weight `w`, A = `0.9w + 0.4(1-w) = 0.4 + 0.5w`. B = `0.7w + 0.8(1-w) = 0.8 - 0.1w`. They tie when `0.4 + 0.5w = 0.8 - 0.1w`, hence `w = 2/3`. Below two-thirds, B wins; above two-thirds, A wins. A scoring tool that only outputs "B wins" at `w = 0.6` hides the central result: this decision is preference-sensitive.

If performance estimates are uncertain, sensitivity is wider still. Analyze optimistic/pessimistic data and seek a decision-relevant experiment where new observations could change the choice. The relevant output may be a decision to keep both options alive, not a false winner.

## Common mistakes
Raw weights applied directly to unlike units; combining safety gate violations with compensating scores; ignoring correlated attributes; turning one stakeholder's preferences into organizational consensus; and reporting three significant digits from a few interviews. A Pareto screen can remove dominated alternatives before preference modeling, but only after all relevant costs/benefits and constraints are represented.

## Exercise
Recalculate the A/B ranking at `w = 0.5, 0.6, 0.7, 0.8`. Then shift B's availability value from 0.7 to 0.65. Determine the new tie weight. **Answer:** `0.4 + 0.5w = 0.8 - 0.15w`, so `w = 0.4/0.65 ≈ 0.6154`. The choice becomes more favorable to A as B's estimated availability declines.

[Back to Phase 2 companion index](../README.md)
