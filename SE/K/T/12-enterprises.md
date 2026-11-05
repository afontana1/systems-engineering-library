# Systems of systems, enterprise governance, and complex adaptation

*Core Concepts · Enterprise & complexity · T12*

> Understand why mission outcomes depend on independently governed constituents and human incentives.

**Recommended preparation:** [System boundaries, outcomes, and emergence](01-boundaries.md), [Reliability, hazard controls, and resilience](09-assurance.md), [Multiobjective decisions, Pareto tradeoffs, and information value](10-decisions.md)

**Related course companions:** [Book 18](../B18/OPEN-BOOK.html), [Book 19](../B19/OPEN-BOOK.html), [Book 20](../B20/OPEN-BOOK.html)

## 1. Technical interoperability is not enough
A regional emergency-access service may depend on city dispatch, public transit, hospitals, utilities, and privately operated vehicles. These constituents can be useful independently and answer to different authorities. A common API does not create a common mission: participants may have incompatible funding, duty-of-care rules, service priorities, or incentives.

Treat a system of systems as a negotiated operational arrangement. Model not just interfaces and data formats but decision rights, escalation paths, service-level commitments, fallback authority, and who carries losses when a constituent withdraws. Technical coupling without governance can create brittle dependence.

## 2. Enterprise architecture includes incentives and change capacity
A capability map identifies what an organization must be able to do; a process map describes how it attempts to do it; a system architecture describes supporting technology. They overlap but are not interchangeable. An enterprise can own excellent software and still fail because procurement timing, training, labor rules, or budget incentives conflict with the intended transformation.

A realistic change plan has a transition architecture: what capabilities coexist, which interfaces are temporary, how data are migrated, and who can authorize rollback. Track adoption, not merely deployment. A completed software rollout is not proof that operational behavior changed.

## 3. Emergence can be harmful or beneficial
Suppose agencies optimize their own dispatch performance independently. They may unintentionally route demand toward the same scarce intersection, increasing regional delays. Alternatively, sharing capacity information may improve global recovery. Both effects depend on interaction rules, not simply local component quality. Use network and agent-based models as hypotheses about interactions, validated against meaningful observations where possible.

Complex systems cannot always be controlled by issuing one central instruction. Adaptation, workarounds, learning, and political response change the system as interventions unfold. Build monitoring and reversible experiments into the governance model.

## 4. Define who benefits and who bears the cost
Average response time may improve while a small rural population experiences worse access. Enterprise performance measures should be disaggregated by relevant users, locations, and failure conditions. A boundary dispute can be ethically important: a system owner may regard an externalized cost as “not our mission,” while affected residents view it as the central outcome.

A responsible intervention identifies contested values, uses multiple methods, provides meaningful review and appeal, and avoids portraying a simulation as a neutral social decision-maker. Model uncertainty and governance uncertainty belong in the same review packet, though they need not be quantified in the same way.

## 5. Conduct an intervention rehearsal
Before deploying a cross-agency initiative, stage a tabletop rehearsal in which each constituent acts according to its real incentives. The hospital protects emergency access; the transit operator protects scheduled service; the city protects pedestrian safety; the contractor protects cost and availability targets. A shared technical API may amplify rather than resolve disagreement if there is no agreed escalation authority.

Identify **control rights** versus **influence**. One agency may have authority to change a signal but not to prioritize one operator's passengers. Another may own a vehicle but have contractual obligations that limit emergency redeployment. A governance architecture should specify normal decision rights, incident decision rights, dispute resolution, and review after a contested decision.

Use multiple success measures. Regionwide mean response time, underserved-area access, incident safety, affordability, and public trust can move in different directions. Averages often conceal distributional harm. Treat disaggregated performance as core evidence, not a decorative appendix.

**Check your reasoning:** A simulation shows an 8% regionwide improvement but some communities experience a 20% deterioration. The engineering team may report those estimates and their uncertainty; it should not unilaterally conclude that the trade is acceptable. That judgment requires accountable governance and engagement with affected groups.

## Guided worked example

### Worked governance example
A proposed cross-agency scheduler cuts mean regional response time from 24 to 20 minutes, but increases one underserved district's mean from 30 to 38. The aggregate improvement is real under the fictional data; it is not sufficient to call the project a success. The governing body must determine acceptable distributional impacts, safeguards, monitoring, and appeal rights before approving a rollout.

## Independent transfer exercise

Map five autonomous agencies and draw an authority/technical-dependency matrix. Propose a phased pilot with an explicit stop rule and disaggregated outcome measures.

[Open the companion hypothetical lab](labs/12-enterprises-workshop.md)

<details><summary><strong>What a defensible answer must contain</strong></summary>

A strong proposal names both technical and institutional failure paths, specifies who authorizes changes, and acknowledges stakeholder disagreement instead of smoothing it into one score.

</details>

## Next connections

Use the related books above to see how this concept becomes a course assignment. The lab provides a small, deliberately incomplete practice setting; it does not replace verification against real operational data.
