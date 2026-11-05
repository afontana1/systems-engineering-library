# Chapter 11 — A Red Team Tries to Break the Commitment

*EN.645.667 · Week 11 · Compliance, affordability and review-board challenge · Preceded by [Chapter 10](10-integrated-recovery-control.md); continue with [Chapter 12](12-baseline-defense-and-retrospective.md).*

> **Study contract.** This chapter teaches the concepts behind Week 11; practice them in [Hypothetical Lab 11](../labs/lab-11-proposal-red-team.md), then complete the [original Week 11 coursework](../../../C/P0/EN645667.md). These fictional examples are not contractual or safety approvals.

## The management problem

A polished proposal can fail because its pages are internally incompatible. The executive summary promises delivery in 18 months; the resource-loaded critical path requires 20; the cost volume prices two vehicles while the technical plan needs three; and the verification plan has no funded accessibility demonstration. These are not writing errors. They are failures of the integrated contract the proposal asks the customer to accept.

A red team should approach the bid as a skeptical customer rather than as an editor hired to improve its prose. Review four kinds of truth: compliance with instructions, plausibility of technical performance, executable management planning, and affordability. A review finding should quote the precise claim, identify contradictory or missing evidence, assess consequence, and recommend a disposition. “Needs more detail” is too vague to support correction.

Separate **red** reviews (customer-centric challenge) from **gold/management** reviews (organizational commitment) and specialist technical assurance. A reviewer who only rechecks their own section may reproduce its assumptions rather than test them. Independence is a spectrum, so disclose when the same person authored and reviewed a calculation.

## Develop the method

Trace high-risk proposal statements horizontally. A sentence promising degraded-mode capability must connect to system requirement, WBS, resource estimate, critical-path activities, test procedure, acceptance criterion and risk allocation. Use a numeric-consistency ledger for repeated quantities: vehicle count, service hours, contract price, PMB, dates and staffing.

Prioritize findings according to consequence and ease of correction. A missing appendix label may be quickly fixable; a hidden unpriced safety function may require a new architecture and cost estimate. Document the difference. A credible red-team exit criteria is that material contradictions have an agreed disposition and every surviving major claim has an accountable evidence owner.

### A red team attacks the reasoning behind the commitment

Independent review has value because teams become attached to their own assumptions and narratives. A red team should not simply search for formatting errors or demand more slides. It should identify which assumptions are load-bearing: the promised throughput, the dependence on a supplier, the feasibility of the test environment, or the legal authority for a proposed waiver. A single invalid load-bearing assumption can undermine a beautiful project plan more than dozens of minor defects.

A useful challenge distinguishes **lack of evidence**, **contrary evidence**, and **disagreement about values**. The first calls for additional observation; the second may require redesign or a narrower claim; the third may require stakeholder decision rather than another calculation. This classification prevents the review from becoming a ritual in which every finding is addressed by producing another document. The goal is not to make the proposal unassailable but to expose where commitments are conditional and which governance body can accept or change those conditions.

## Worked Northstar project example

A draft claims $8.4M price, 18 months to acceptance, and a fault-tolerant pilot. The controlled cost sheet supports the price, but an integration schedule references a 20-month date and the fault-tolerance test is not in the WBS. Mark the proposal non-ready for submission, not because the price alone is wrong but because the plan does not substantiate the commitment. Closure requires a reconciled schedule and authorized degraded-mode scope and evidence, potentially changing the price or customer offer.

## A proposal is a graph of commitments, not a set of sections

Treat the proposal as a typed graph. The customer requests an accessible service; the technical volume proposes a boarding function; the WBS allocates design and validation; the schedule reserves an accessible-boarding demonstration; the cost volume funds personnel and equipment; the acceptance plan specifies measurable conditions. A reviewer can traverse these links. If a claim has no supporting node, the graph exposes an obligation without a credible execution path.

This approach also improves *consistency testing*. Suppose the cost volume allocates $100,000 to operator training and the WBS has training under project transition, but the schedule omits instructor availability. The numerical budget is not necessarily wrong; the missing time and resource coupling is. A red team should not “fix” this by deleting the training claim if the customer requires it. It should require a corrected integrated plan and renewed price/schedule assessment.

**Independent arithmetic challenge.** Use the original illustrative price structure: 7.2 + 0.6 + 0.6 = $8.4M, under a ceiling of $8.8M. Ask the cost reviewer to trace 7.2 through work packages and control accounts, the scheduler to map major packages to logic, and the technical reviewer to identify every acceptance-critical unbudgeted test. The price is only plausible if its underlying defined scope is compatible with the offer. An attractive margin below the ceiling can evaporate if the estimate omitted required work.

A review disposition should explicitly state whether the package is ready to submit, ready subject to material corrections, or blocked. Avoid euphemisms like “green with observations” when a major executable commitment remains unsupported.

## Graduate synthesis: adversarial review as a test of a coupled commitment

### Why independent challenge has economic value

A proposal is not merely a forecast: it is a decision under asymmetric information. The bidding organization knows its assumptions better than the customer, while the customer may impose penalties, reject acceptance, or discover omissions after award. A red team reduces this *information asymmetry* by testing whether claims in different volumes refer to the same scope, configuration, operating scenario, and confidence level. The value of the review lies in changing a consequential decision before a commitment becomes expensive to reverse, not in maximizing the number of comments.

Consider a claim that the Northstar shuttle can deliver 300 passenger trips per day. The architecture predicts that throughput, the schedule includes two operating vehicles, and the cost model funds maintenance for one. The review must ask whether all three calculations use the same definition of availability. A service metric might be modeled as `delivered trips = demanded trips × dispatch availability × boarding completion fraction`; multiplying point estimates is legitimate only when the conditional interpretations are explicit. If demand surges and availability declines together in bad weather, treating those terms as independent systematically overstates delivery. A credible commitment identifies the *joint scenario* rather than mixing convenient individual assumptions.

### Construct an evidence-cut across the proposal

Represent the proposal as a directed dependency graph `G = (V,E)`, where each vertex is a controlled claim or artifact, and a directed edge means that one claim depends on another. The minimum evidence cut for a promised capability contains at least a requirement, an architecture allocation, executable work, schedule logic, cost provision, test method, and authority for disposition. A reviewer searches for missing or incompatible edges. This is stronger than checking whether every section exists: complete-looking documents can still describe incompatible systems.

The red team's severity judgment should combine *consequence* and *epistemic status*, not simply a risk-score product. A high-consequence claim supported only by a vendor assertion deserves deeper scrutiny than a low-consequence arithmetic typo. Separate three findings: (1) **contradiction**, two controlled artifacts cannot both be true; (2) **unsupported claim**, the necessary evidence is absent; and (3) **preference dispute**, evidence is agreed but acceptable tradeoffs differ. They have different owners and remedies. Contradictions require reconciliation, unsupported claims require evidence or a narrowed offer, and preference disputes require an authorized stakeholder decision.

### Example: the apparently affordable bid

Suppose the submitted price is $8.4M against an $8.8M ceiling and the red team finds an omitted $0.6M verification campaign. The nominal headroom is `$8.8M − $8.4M = $0.4M`; the unsupported test cannot be added without exceeding the ceiling by $0.2M. Removing it is not an acceptable correction if the campaign supports mandatory acceptance. The available decisions are to revise the design, find evidenced savings, qualify the offer where permitted, or decline the commitment. A claim of “within budget” is only meaningful relative to a *complete* scope.

Red-team closure is therefore a governance transaction: preserve the original finding, root cause, revised baseline identifier, independent recheck, and named acceptance authority. Treat a previously disproven claim as unresolved until the actual underlying model changes. A review that produces unanimous enthusiasm by suppressing dissent creates confidence theater rather than assurance.

## Boundary of the method

Do not close a high-impact finding by changing narrative wording while leaving schedule, estimate or interface obligations inconsistent. Fix the source of truth.

## Retrieval questions and explained answers

1. **Question:** What is the core difference between a red team and copy editing?
   **Explanation:** A red team challenges claims, consistency and executability from a customer perspective.
2. **Question:** When is an attractive proposal still non-ready?
   **Explanation:** When material commitments lack consistent scope, resource, schedule, cost or verification support.
3. **Question:** How should repeated numbers be governed?
   **Explanation:** Use authoritative controlled sources and reconcile every occurrence before submission.

## Put this into practice

Work through [Lab 11: The Adversarial Proposal Review](../labs/lab-11-proposal-red-team.md), then write a short paragraph on how the laboratory simplifies the real-world management problem. Use the [existing short Week 11 primer](../../P0-text/lessons/645-667-w11.md) for a second explanation. The assessed deliverable is defined in the original course guide, not by the hypothetical lab.
