# Assurance cases: what evidence supports which engineering claim?

**Canonical reference · Safety and assurance · Expanded reference · Internal editorial review; independent peer review not performed**

## From evidence inventories to justified claims

An **assurance case** is a structured argument connecting a bounded engineering claim to the evidence and reasoning intended to justify it. It includes the **context** (system, operating conditions, standards or decision basis), **strategy** (why the evidence set addresses the claim), **evidence** (models, tests, analyses, inspection results and records), **assumptions**, **defeaters** (ways the argument could be wrong) and **decision authority**. A folder full of successful tests is not automatically an argument: the tests may address the wrong configuration, operating modes or failure mechanisms.

For a shuttle release, the top-level statement “safe to operate” is too broad unless it names the configuration, mission envelope, relevant risks and acceptance authority. A useful hierarchy might include claims that controlled stopping works under named conditions; that human intervention remains feasible; that harmful commands cannot bypass authorization; and that degraded modes remain bounded. Each subclaim must identify what observation would undermine it.

## Evidence has types and validity conditions

Testing provides observations about exercised systems and scenarios; formal proof establishes properties of a model under mathematical assumptions; analysis predicts behavior using a model; review checks documented consistency; field telemetry records outcomes in a particular population. These are not interchangeable. Multiple pieces of evidence improve assurance only if they close distinct gaps; three test reports using the same faulty harness may not be independent corroboration.

Track a claim-to-evidence graph with nodes for claims, requirements, hazards, controls, model versions, tests, build identifiers, results and approvals. Edges should be typed: “verified by,” “assumes,” “refined into,” “challenges,” or “applies to configuration.” A link is not enough unless its semantics and validity window are specified. Evidence can expire when interfaces change, environmental conditions broaden, or the test article differs from the released build.

## Worked reasoning: coverage is not confidence

Assume 12 release-relevant hazards have been identified, and nine have accepted, configuration-current control evidence. A simple closure ratio is `9/12 = 75%`. It is a **workflow indicator**, not a 75% probability that the system is safe. If one of the three unresolved hazards has catastrophic severity while the nine closed hazards have minor severity, the count conceals the decision's dominant risk. Even complete closure of the *identified* set cannot establish that no unrecognized hazards exist.

Now suppose a timing proof guarantees an emergency-stop signal is issued within 100 milliseconds in a simplified controller model. The physical brake test measures stopping distance under dry conditions. The two reports address different subclaims. The assurance argument must still connect command time to actuator response, friction, operating load, degraded sensing and the range of acceptable stopping distances. A counterexample, uncovered assumption or inconsistent interface can invalidate the combined claim.

## Defeaters, independence, and risk acceptance

Good assurance reviews actively search for reasons the proposed conclusion may not hold. Common defeaters include correlated test environments, incomplete fault injection, unvalidated model parameters, undocumented operator actions, stale software versions, and exposure outside the design basis. An independent reviewer can challenge whether the argument has omitted hazards or alternatives; that challenge is different from simply repeating the originating team's calculation.

The release decision should include unresolved hazards, limitations of operation, compensating controls, residual-risk ownership and monitoring triggers. Evidence acceptance by a technical reviewer and risk acceptance by a designated organizational authority are different acts. A statement that a process was followed does not imply that the product meets its mission or protection needs.

## Decision-ready argument outline

1. **Claim:** explicit system configuration, target outcome and operating envelope.
2. **Context:** requirements, stakeholder risk tolerances, interfaces, and authoritative baselines.
3. **Strategy:** how subclaims cover the relevant causes and failure paths without gaps.
4. **Evidence:** cited model/test/review artifacts with reproducible versions and limitations.
5. **Defeaters:** unresolved contradictions, untested scenarios, common-mode and model uncertainty.
6. **Disposition:** reviewer judgment, qualified restrictions, acceptance authority and follow-up triggers.

Treat the assurance case as a maintained engineering model that evolves with the system, not as a certification slide generated at project closeout.

## Selected source-to-claim references

- **A1 · Verification, validation and technical reviews form complementary evidence:** [NASA Systems Engineering Handbook, section 2.0 — distinction between product verification and validation](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/).
- **A2 · Lifecycle software assurance and IV&V:** [NASA-STD-8739.8B — scope of software assurance and software safety](https://standards.nasa.gov/standard/nasa/nasa-std-87398).
- **A3 · Trustworthiness requires evidence, including appropriate requirements:** [NIST SP 800-160 Volume 1 Revision 1 — engineering trustworthy secure systems](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final).

## Follow the knowledge

- **Prerequisites:** [Traceability graph](traceability-graph.md), [Verification and validation](v-and-v.md).
- **Related concepts:** [System safety and hazards](system-safety-and-hazards.md), [Statistical acceptance](statistical-acceptance-and-confidence.md), [Digital thread and provenance](digital-thread-and-twin.md).
- **Go deeper:** [Book 1, Chapter 11 — Realization and evidence](../B1/chapters/11-realization-and-evidence.md); [Book 8, Chapter 10 — Sufficiency of test evidence](../B8/chapters/10-analyze-results-determine-evidence-sufficiency-and-reco.md).
