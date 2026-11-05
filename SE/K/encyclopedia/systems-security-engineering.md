# Systems security engineering: protect the mission, not just the network

**Canonical reference · Safety and assurance · Expanded reference · Internal editorial review; independent peer review not performed**

## Security as an engineered system property

**Systems security engineering (SSE)** integrates stakeholder protection needs, threat assumptions, authorized behavior, security constraints, architecture choices and evidence into systems engineering across the lifecycle. Security is not an after-the-fact checklist, a vulnerability scanner score, or a guarantee provided by encrypting the network. A system can implement strong cryptography yet be insecure because an operator can approve the wrong action, a recovery procedure bypasses authorization, or a valid but stale command causes a physical hazard. NIST SP 800-160 treats trustworthy security as a system-wide engineering concern and links it to architecture, assurance and operational risk.

Define assets and unacceptable losses first. In a campus shuttle operation, relevant assets include passenger safety, valid dispatch authority, location privacy, system availability and the integrity of emergency commands. Protecting confidentiality, integrity and availability may require conflicting design choices: a strict network isolation control can prevent remote attacks but also block emergency operations. The trade must preserve mission constraints and clarify who may accept residual risk.

## Threat models, trust boundaries and attack paths

A threat model states possible adversary capabilities, entry points, trust boundaries, assets, misuse cases, plausible failures, and conditions under which assumed controls operate. Identify every place that information or authority crosses between a person, application, device, supplier or network segment. Model also maintenance, provisioning, backup restoration and retirement. An architecture may contain a protected command API but an unprotected local maintenance connector with equivalent authority; focusing on the API alone gives false confidence.

Defensive layers should be diverse enough that one overlooked requirement does not bypass them all. Examples include authenticated commands, least privilege, input validation, signed configuration, separation of control domains, explicit recovery authority, logging and independent safety controls. Security monitoring creates evidence about observed events, not proof of absence of capable adversaries. Assess attacks against fail-operational and fail-safe modes, not just against confidentiality.

## Worked engineering reasoning: freshness is a control requirement

Suppose the shuttle accepts a route-clearance message signed by an authorized dispatcher, but the signature does not attest to its time validity. An attacker who replays a valid command from 45 seconds earlier may trigger a maneuver after road conditions have changed. If the safety analysis requires route clearance no older than 30 seconds, the necessary condition is `now − authenticated_command_time ≤ 30s` **with a trustworthy clock and replay defense**. A signature alone cannot establish that freshness property. If clocks are unsynchronized or the network is partitioned, the controller must have a defined degraded or safe response and explain its effect on user service.

The 45/30-second scenario is synthetic. The real engineering exercise is to identify what evidence attests that a command is fresh, authorized **for the current mode**, and delivered to the correct configuration. Replay prevention, monotonic sequence numbers, bounded clock skew and controller autonomy can interact; one technique cannot be selected without the operating assumptions.

## Assurance and life-cycle obligations

Trace each critical protection claim to trust-boundary analysis, requirements, implemented controls, adversarial and fault-injection tests, operational monitoring and an assigned decision authority. Track supplier updates, shared infrastructure, credential lifecycle and incident response. A successful penetration test is bounded by its time, scope, testers, scenarios and tested build; it does not prove all exploit classes absent. When external connectivity is lost, emergency operations, audit logging and recovery need deliberate design instead of ad hoc exceptions.

SSE and safety engineering overlap but are not interchangeable. Safety treats unacceptable losses including accidents; security adds intentional adversarial behavior, but malicious actions can trigger a safety hazard. Combining their arguments may reveal safety controls that themselves create exploitable interfaces.

## Failure modes and limits

- **Boundary error:** a supplier gateway is treated as trusted because it is inside the physical facility.
- **Property error:** a certified encryption algorithm is mistaken for end-to-end command integrity or freshness.
- **Evidence error:** a passed scanner and clean vulnerability report are treated as a complete adversarial assurance case.
- **Lifecycle error:** emergency access, expired credentials or configuration rollback can invalidate the released baseline.

A security case should state authorized outcomes, credible threats, countermeasures, test limits, residual uncertainty and the basis for revisiting the claim when the environment or adversary changes.

## Selected source-to-claim references

- **C1 · Security integrated in systems engineering and protection needs:** [NIST SP 800-160 Volume 1 Revision 1, Engineering Trustworthy Secure Systems — abstract and scope](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final).
- **C2 · Resilience against adverse cyber conditions:** [NIST SP 800-160 Volume 2 Revision 1, Developing Cyber-Resilient Systems — abstract](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final).

## Follow the knowledge

- **Prerequisites:** [System boundaries](system-of-interest.md), [Risk and issue distinction](risk-vs-issue.md).
- **Related concepts:** [System safety and hazards](system-safety-and-hazards.md), [Software quality attributes](software-quality-attributes.md), [Assurance cases](assurance-cases-and-evidence.md).
- **Go deeper:** [Book 5, Chapter 8 — Performance and security](../B5/chapters/08-specify-and-analyze-performance-networking-re.md); [Book 18, Chapter 9 — Cascading risk and cyber resilience](../B18/chapters/09.md).
