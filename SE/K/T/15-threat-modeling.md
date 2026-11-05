# Cybersecurity engineering: threats, trust boundaries, and recovery

*Core Concepts · Modeling & software · T15*

> Connect assets, adversary actions, architecture controls, detection, and test evidence.

**Recommended preparation:** [03 Architecture](03-architecture.md), [05 Software Contracts](05-software-contracts.md)

**Related companion books:** [Book 3](../B3/OPEN-BOOK.html), [Book 5](../B5/OPEN-BOOK.html), [Book 16](../B16/OPEN-BOOK.html)

## 1. Security is an engineering property of interactions
A system can use strong encryption and still make incorrect authorization decisions. For Northstar, a vehicle status message may be cryptographically protected but belong to the wrong fleet configuration; an authenticated operator may have expired authority to restart a closed route. Security engineering therefore begins with the mission, protected assets, authority relationships, and consequences of losing confidentiality, integrity, or availability.

Identify the actors: passenger, dispatcher, vehicle, fleet administrator, maintenance service, emergency agency, and third-party map provider. Then draw data flows and **trust boundaries**: where the system must make a new decision about identity, privilege, freshness, origin, or permissible action. A network segment is not automatically a trust boundary; one service account with global privileges can erase useful boundaries even across many networks.

## 2. Make threats testable
Threat modeling asks what an adversary might want, what capabilities they could obtain, and how the architecture exposes a pathway. Consider a replay of a previously valid *route-clearance* message after the road has been closed. Encryption alone does not prevent replay. A security claim must include message identity, nonces or sequence numbers, expiry, signed revision, and a bounded time source.

A useful threat record has: asset and mission effect; entry point; preconditions; adversary capability; attack path; existing preventive control; detection signal; response owner; and verification evidence. Avoid a list that says only “hackers may attack APIs.” Threats need a concrete path through an actual architecture.

## 3. Apply least privilege at operational boundaries
Suppose fleet operators may cancel a trip but only regional command may reopen a closed evacuation route. Implement authorization as a check of both subject authority and current resource state:

\[
\operatorname{permit}(u,a,r,t)=\operatorname{roleAllows}(u,a)\land\operatorname{stateAllows}(r,a,t).
\]

A role-only check is insufficient because the same action may be legitimate on an open route and prohibited on a closed one. Document how policy changes propagate, how stale tokens are rejected, and how services behave when the policy engine is unreachable. “Fail closed” is a good default for sensitive authorization, but the safety consequences of losing a control path must also be analyzed; security and availability are not separable by slogan.

## 4. Distinguish prevention, detection, and recovery
A signature check can reject altered data. It does not detect an authorized insider sending a dangerous but valid command. A replay detector can reject repeated sequence numbers. It does not detect a newly forged message from a compromised key. Controls must be layered and their independence justified.

Plan recovery at the architecture level: isolate compromised credentials, revoke trust, preserve forensic records, operate in a degraded mode, and re-establish provenance before resuming. A backup can restore software but not the public's confidence that mission state is trustworthy. Specify the criteria for safe re-entry: validated configuration, reconciled command history, verified route state, and an accountable release decision.

## 5. Quantify carefully
A security risk score is not an objective probability of attack. Threat actors adapt, knowledge of the system changes, and the observation process is biased. Quantitative risk models can aid sensitivity analysis when parameters are honestly labeled as assumptions. For example, suppose a threat pathway succeeds only when both a credential is compromised and a second authorization check is bypassed. The independent-product model would use

\[
P(\text{success})=P(C)P(B\mid C),
\]

not automatically $P(C)P(B)$; compromise may make bypass more likely. Present scenario ranges and control dependencies rather than fabricating precision from a spreadsheet.

## 6. Worked example: rejecting stale-but-signed clearance
The dispatcher accepts clearance only if the signature is valid, the route identifier matches, the issuer has current authority, the revision equals the authoritative latest revision, and the message age does not exceed four seconds. If a signed clearance has revision 18 but the system already knows revision 19 denotes closure, the message is rejected even though the signature remains valid. This is a clear example of why authenticity does not imply current correctness.

Test the contract with a table of cases: good clearance, wrong route, old revision, expired time, revoked issuer, and disconnected policy service. The negative cases matter at least as much as the positive. An application log should record enough information to reconstruct the decision without exposing private credentials or sensitive payloads.

## 7. Build an assurance argument, not a checklist
The claim “only authorized route releases are executed” requires evidence about identity provisioning, policy enforcement, freshness, error handling, deployment configuration, and ongoing monitoring. It also requires review of the boundary between software authorization and the physical vehicle's safety constraints. Passing one penetration test is a piece of evidence, not a proof of secure operation in all contexts.

## Practice questions
**A.** Identify four trust boundaries in the shuttle architecture and one control for each. **B.** Explain the difference between authentic, authorized, current, and safe. **C.** Propose a credential-compromise recovery test that includes operational effects and review evidence.

<details><summary>Instructor reasoning</summary>

An excellent answer treats authentication, authorization, freshness, and system safety as separate predicates; names both preventive and detective controls; and demonstrates degraded operation and recovery without assuming a network connection will always be available.

</details>

## Further connections
[Architecture and interfaces](03-architecture.md), [software contracts](05-software-contracts.md), and [safety constraints](13-safety-constraints.md) provide the foundations for specifying secure action boundaries.

## Guided laboratory

[Open the corresponding case-based lab](labs/15-threat-modeling-workshop.md)
