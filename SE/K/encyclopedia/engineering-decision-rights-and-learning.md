# Engineering decision rights and learning cadences

**Reference entry · Agile systems engineering, team architecture and technical governance**

## Design teams as decision-making systems

Technical leadership is not a synonym for command hierarchy. A common-mission team needs clear authority over interface choices, hazard decisions, verification evidence and tradeoffs, while preserving enough local autonomy to learn quickly. Ambiguous approval boundaries create queueing delay, hidden work and inconsistent safety decisions. Separate **decision-maker**, **technical advisor**, **accountable owner**, **independent reviewer** and **affected stakeholder**. A RACI table alone does not specify how disagreement is resolved or when escalation is mandatory.

Make each decision record explicit: problem and operating context; options; evidence and uncertainty; reversibility; interfaces affected; delegated decision authority; independent signoff if required; expiration/revisit trigger; and affected configuration. An experiment can be delegated if its risk is bounded; acceptance of a safety-critical residual risk may need organizational approval independent of the implementing team.

## Worked queue and cadence illustration

Suppose 12 interface decisions enter a review queue every two weeks and the review board closes 10 per two weeks. The arrival rate is 6/week and the average completion rate is 5/week, so unresolved inventory grows by roughly one decision per week under constant rates. A monthly review cadence alone cannot stabilize the system. Rather than adding status meetings, redesign the decision architecture: delegate reversible, low-risk choices; batch interface decisions only when justified; reserve independent review for defined classes; and measure age of blocked dependencies. Do **not** infer an exact lead time from the rates while inventory is increasing: Little's law's stationary assumptions do not hold.

A learning interval should be based on an unresolved claim and a decision deadline. Example: “the revised allocation algorithm reduces stale-data assignments without increasing 95th-percentile wait beyond the agreed margin.” Specify the test envelope, stopping condition, success and harm thresholds, data provenance and responsible reviewer before implementation. At the interval's end, choose **continue, revise, limit scope, reverse or seek more evidence**; do not equate activity completion with learning.

## Governance under scale

When multiple teams share a common physical interface, define an interface owner, semantic version policy and contract tests. Suppliers and regulators may have distinct authority. Capture contested assumptions in a decision log. Rotate implementation responsibility when useful, but preserve ownership of controlled baselines, safety cases and operational incidents. A “self-managing” team without a clear emergency stop authority is not self-governing in a defensible engineering sense.

## Exercise with answer direction

A team delegates a wiring-harness revision to a software lead because it seems “minor.” The change invalidates environmental qualification evidence. Design a decision-rights rule that would have flagged the cross-domain impact; identify required technical reviewers and evidence owners. Then compute the queue accumulation over six weeks under the illustrative 6/week arrival and 5/week closure assumption: **six additional open decisions**, absent cancellations or rate changes. Formally, \(\Delta B=(6-5)\times6=6\). Propose a measurable improvement experiment and a safety-independent stop rule.

## Boundaries and sources

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — technical planning, management, decisions and configuration control.
- [SEBoK](https://sebokwiki.org/wiki/Main_Page) — systems management and enterprise decision frameworks.

Related: [authority and governance](authority-and-governance.md), [agile tailoring](agile-tailoring.md), [flow and bottlenecks](flow-wip-and-queues.md), [architecture review](architecture-review-and-evidence.md). Organizational examples are illustrative; real approval rules depend on contractual and safety obligations.
