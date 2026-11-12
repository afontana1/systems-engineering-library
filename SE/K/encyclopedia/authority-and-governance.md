# Authority, governance, and coordination

**Reference entry · Systems of systems, enterprises and complexity · Expanded reference**

## Definition and diagnostic distinction

**Authority** is the legitimate capacity to commit resources, set constraints, approve changes, or accept defined risk. **Governance** specifies how such decisions are made, reviewed, recorded, and challenged across institutional boundaries. Coordination is the practical alignment of actions among participants who may not share a single command chain. A system-of-systems engineer cannot assume that all constituent owners will obey a technically optimal architecture plan.

## Theory: decision rights are part of system behavior

For each consequential decision, identify the proposer, technical reviewer, affected stakeholders, approving authority, implementer, and independent challenger. An accountable role must have the information and jurisdiction needed for the decision. A responsibility matrix without escalation rules can leave cross-boundary risks orphaned. In federated arrangements, interface agreements and incentive-compatible benefits often matter more than hierarchical instructions.

Risk acceptance is a distinct act from technical verification. A test team can report that an objective criterion was met while an authorized mission owner decides whether residual uncertainty is acceptable. Conflicts also occur between compliance, affordability, mission urgency, and public legitimacy. Good governance preserves dissent and documents whose harms, rights, and needs are considered rather than turning a weighted score into a substitute for judgment.

## Worked example: a capability that has no single owner

An emergency mobility plan requires transit operations, campus security, a cloud vendor, and the city transport authority to share location data. The software team can meet its API throughput target, yet the mission fails if the city cannot legally disclose required records or if the vendor can suspend the interface during an incident. A governance map assigns authority for data-sharing terms, privacy review, operational activation, contingency procedures, funding, and residual risk. The integration gate requires signed operational agreements and exercised degraded-mode drills, not just successful API calls.

## Engineering use and evidence

Create a decision-rights register, constituent agreement map, conflict-escalation route, and risk-acceptance log. For every critical interface, verify ownership during normal service, emergency response, updates, and retirement. Test governance with scenario walkthroughs: what happens when two owners reject a change or a supplier withdraws service? Measure decision latency, unresolved exceptions, and effectiveness of independent challenge.

## Limitations and connections

Formal authority does not guarantee practical influence or stakeholder legitimacy. Governance can also become so slow that it creates operational risk. Connect this topic to **systems-of-systems autonomy**, **enterprise transformation**, **interface contracts**, **risk**, and **critical systems thinking**.

## Technical analysis: decision rights as a bounded control system

A governance system should specify who may **propose**, **evaluate**, **approve**, **veto**, and **operate** a change. These verbs are different. Technical authority can require evidence even when budget authority approves funding; a local team may implement a change but lack the authority to alter the certified operating envelope. Model a decision record as `(proposal, affected baselines, evidence, dissent, approvers, conditions, expiry)`.

Consider an illustrative change with an expected one-time benefit of **$120k**, implementation expense **$60k**, and an assumed **20%** chance of an additional **$100k** requalification expense. Its simplified expected net value is `$120k − $60k − 0.20($100k) = $40k`. That calculation does **not** license the change: if a mandatory separation-of-duties rule or safety constraint is breached, expected value cannot override the constraint. Even the economic result depends on consequence coverage, dependence, delay, and whose benefits count.

**Evidence boundary.** Set threshold-based escalation rules and identify the independent reviewers for high-consequence hazards. Record unresolved dissent and post-release decision outcomes; otherwise centralization can hide local signals while decentralization can hide cross-team coupling. This example describes a governance calculation, not an agency-wide decision rule or a documented NASA threshold.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** Decision analysis documents criteria, assumptions, uncertainties, recommendation and final decision authority. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §6.8 Decision Analysis](https://www.nasa.gov/reference/6-8-decision-analysis/) · *direct guidance*.
- **C2:** Technical baselines and approved changes require controlled configuration governance. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §6.5 Configuration Management](https://www.nasa.gov/reference/6-5-configuration-management/) · *direct guidance*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [INCOSE · Systems Engineering Handbook, 5th ed. (2023)](https://www.incose.org/resource/incose-systems-engineering-handbook-a-guide-for-system-life-cycle-processes-and-activities-5th-edition/) — Published practitioner reference; full text may require access.
- [NIST · SP 800-37 Rev. 2, Risk Management Framework (2018)](https://csrc.nist.gov/pubs/sp/800/37/r2/final) — Risk governance and continuous monitoring in the system life cycle.



## Step 02 review studio — who can accept which risk?

A campus steering committee approves project budget, an operations manager owns passenger-service procedures, a design authority controls interfaces, and a safety authority may separately assess hazards. None of those roles is automatically entitled to substitute a high weighted trade-score for a mandatory safety control. A good governance model declares both decision rights and escalation paths.

**Solved exercise:** an architecture board prefers option A because it scores 82 versus 79, but A violates a mandatory accessible-boarding constraint. Can the board approve A by increasing the affordability weight? **No.** A mandatory constraint is noncompensable under the stated decision rules. Approval requires correcting the design, changing the authorized constraint through an appropriate process, or rejecting the option—not hiding noncompliance in the scoring model.

**Failure test:** trace one change through proposer, evidence owner, reviewer, approver, implementation owner, and verifier of closure. If two actors can independently approve contradictory baselines, the authority model contains a race condition. The remedy is a uniquely controlled decision record with configuration identity and a documented dispute-resolution route, not more meeting participants.

## Follow the knowledge

**Related concepts**

- [Systems of systems: constituent autonomy and emergent mission performance](sos-characteristics.md)
- [The enterprise as a system](enterprise-as-system.md)
- [Risk, issue, uncertainty, and opportunity](risk-vs-issue.md)
- [Stakeholders, needs, and value: translating plural interests into engineering decisions](stakeholders-and-needs.md)

**Go deeper in the 240-chapter textbooks**

- [Book 18, Chapter 02: Week 02 · System of Systems Engineering · Chapter 02 — Managing SoS development, governance, acquisition, fielding, and evolution](../B18/chapters/02.md)
- [Book 19, Chapter 02: Week 02 · Enterprise Systems Engineering · Chapter 02 — Actors, authority, objectives, legitimacy, and governance](../B19/chapters/02.md)
- [Book 20, Chapter 08: Week 08 · Management of Complex Systems · Chapter 08 — Type F — coercive complexity: Team Syntegrity and Critical Systems Heuristics](../B20/chapters/08.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
