# 5 · Digital engineering requires trustworthy evidence lineage

*Graduate methods companion · Digital and Mission Engineering (Book XVI)*

A digital thread is not merely a dashboard showing linked engineering documents. It is a governed chain of identities, revisions, transformations, claims, and evidence that permits an engineer to answer: **Which configured system does this conclusion describe, what observations support it, and what changed since the evidence was collected?** Without those answers, a beautifully connected dashboard can create more confidence than the underlying information warrants.

## 5.1 Identify artifacts and claims separately

Consider a requirement R-17: 'an authorized departure must use current route restrictions.' The model associates R-17 with dispatch service S-2, interface I-4, test T-9 and evidence file E-9. The existence of links is only structural coverage. It does not show that T-9 actually evaluates the current route-revision behavior, that E-9 was generated from the correct build, or that a passing status is still valid.

Represent the information model as a typed directed graph $G=(V,E,\tau_V,\tau_E)$ where nodes include requirements, models, interfaces, tests, evidence, decisions, and configurations. Allowed edge types might include `satisfies`, `verifies`, `generated_from`, `applies_to_revision`, and `supersedes`. A type checker can reject `evidence verifies component` if the metamodel requires evidence to verify a claim. Yet type correctness is not truth: even a perfectly typed `verifies` edge may point to a test that never exercised the relevant failure mode.

## 5.2 Configuration is part of the evidence claim

Suppose E-9 was produced by software build `build-21`, against route policy revision `route-5`, using data snapshot `data-8`. The current deployment is `build-22`, `route-6`, `data-8`. If the changed code or policy can influence the tested property, E-9 cannot be silently carried forward as proof of build 22. An impact analysis must determine which claims and tests require re-execution, re-analysis, or documented equivalence.

A practical evidence record should include artifact ID, artifact version, exact source hash, creation time, tool version, test configuration, environmental assumptions, result, responsible reviewer, and approval status. A content digest such as SHA-256 helps detect accidental modification. It does not authenticate who approved an artifact, establish semantic correctness, or guarantee that the correct test was run. Those require identity, authorization, governance and independent review.

## 5.3 Why 'green' dashboards are not assurance cases

Coverage dashboards often report a fraction of requirements linked to at least one test:

$$C_{\mathrm{struct}}=\frac{|\{r:\exists t,\ (r,t)\in E_{\mathrm{verifies}}\}|}{|R|}.$$

A score of 100% is compatible with every test being stale, inadequate, or executed against an obsolete configuration. A richer coverage definition might demand current configuration, approved test method, passing result, valid calibration, and unexpired evidence. Even then, coverage is not a complete probability of operational success; evidence may be correlated or omit unanticipated hazards.

For Northstar, imagine 10 requirements, each linked to a test, giving 100% structural coverage. Four tests refer to a retired interface revision, two have no recorded acceptance thresholds, and one relies on missing telemetry. Only three are currently actionable as acceptance evidence. The meaningful summary is not '100% verified'; it is a gap analysis identifying the seven unresolved claims, each with an owner and closure plan.

## 5.4 Provenance through transformations

Evidence frequently moves through scripts, spreadsheets, reports, and presentations. A data flow might be:

$$\text{raw event log}\to\text{filtered events}\to\text{performance metric}\to\text{test conclusion}\to\text{review decision}.$$

Every arrow is a transformation with assumptions. If a filter silently drops canceled requests, the reported average wait applies to a selected population. If a plotting script rounds timestamps before calculating a 600-ms deadline, the error may dominate the acceptance threshold. If a report copies a value without recording its upstream digest, future reviewers cannot determine which dataset it came from.

A reproducible transformation record includes input hashes, code revision, parameters, tool/runtime version, command, and output hash. This is similar to reproducible scientific computing, but the engineering requirement is stronger: the output must also be tied to system configuration, authorized requirements, and an intended-use claim.

## 5.5 Baseline changes require explicit change-impact reasoning

A change from route-status TTL 250 ms to 500 ms appears small, but it affects temporal contracts, interface acceptance tests, stale-data hazard analysis, operator indications, and possibly network loading. A useful impact procedure begins with the changed entity, traverses relevant dependency edges, then classifies each affected claim as unchanged by justification, reverified, revalidated, or unresolved.

Automated graph traversal is useful for finding candidates, not for making final engineering judgments. A missing edge in the model produces a false negative in impact analysis; a dense but low-quality graph can swamp reviewers with irrelevant candidates. Regular sampling audits and independent model reviews are therefore part of governance.

## 5.6 A bounded digital assurance argument

A review board can reasonably conclude: 'For configuration build-22 / route-6, under demand envelope X and interface contract Y, requirements R-01 through R-08 have current approved evidence; R-09 and R-10 remain unresolved.' This is more useful than a generic green light. Record counterevidence, unresolved anomalies, and the event that would invalidate the conclusion.

The purpose of the digital thread is not administrative traceability for its own sake. It is to make engineering change understandable and accountability reproducible across disciplinary and organizational boundaries.

## Worked problems with explained solutions

**A.** Ten requirements have test links; four tests are stale, two lack thresholds, and one has missing input evidence, with no overlap. What are structural and actionable coverage? **Solution:** 100% structural coverage and 3/10 = 30% actionable coverage.

**B.** Can a matching SHA-256 digest prove that an acceptance test was conceptually appropriate? **Solution:** No. It proves consistency with the hashed bytes under the digest assumptions, not the correctness of the test method or authority of approval.

**C.** A route TTL is extended from 250 to 500 ms. Name three potentially affected artifacts. **Solution:** Temporal interface contract, stale-data hazard argument, and qualification test procedure; operator notification and network timing models may also be affected.

**D.** Why is an automatically generated change-impact list not a substitute for a technical review? **Solution:** Its completeness depends on the completeness and correctness of the dependency graph; semantic impacts and missing edges still require judgment.

## Independent research question

Propose an evidence graph that distinguishes a requirement, its modeled behavior, the test oracle, the executed test result, and the configuration against which it applies. Specify which properties can be automatically validated and which require human evidence appraisal.

**Practice:** [Digital thread laboratory](../labs/05-provenance.html) · [Python provenance checker](../code/graduate_models.py) · [Notebook](../notebooks/05-provenance.ipynb).

## 5.7 Semantic change is harder than file change

A digest detects a change in bytes, but a semantically significant change can occur when the same artifact is interpreted under a new rule. If a unit convention changes from seconds to milliseconds while a schema remains nominally compatible, a data pipeline can process all files successfully and still be incorrect. Conversely, a harmless reformatted model can change its digest without invalidating prior verification. Change-impact analysis needs semantic typing, units, dependency metadata, and engineering review in addition to hashing.

Digital twins introduce a further obligation: freshness and representativeness. The twin's state is an estimate of a physical asset, not the physical asset itself. Document time synchronization, sensor uncertainty, update delay, state-estimation assumptions, and control authority. A current timestamp does not prove that the sampled sensor measures the property needed for the decision. A digital thread should also retain *negative evidence*: failed tests, anomalies, and overturned decisions—not only passing results.

## 5.8 Governance and cyber trust

Evidence is an organizational asset. Define who may originate a requirement, approve a test, sign an evidence record, change a baseline, and release a configuration. Separate duties where safety or financial consequences justify independent review. Digital signatures, access control, immutable logging, and secure build pipelines can support this governance, but none can determine whether an architecture concept is suitable. Treat the assurance argument as a combination of technical proof obligations and human accountability.

<!-- STEP04-CONNECTED-EVIDENCE-START -->
## Step 04 integrated case — NS-CE4.1: structured paths are not current evidence

A digital thread is valuable because it can reveal missing, stale, or contradictory arguments. It is dangerous when a link's mere existence is treated as proof. The synthetic NS-CE4.1 ledger has five connected **claim → requirement → artifact** paths. All five exist structurally; only one is currently actionable under a narrow, stated set of checks.

### Model an evidence path as a typed assertion

An actionable path needs more than a claim identifier. Let $e$ be an evidence record and let $r_b$ be the current release revision. A simple necessary screen is

$$A(e)=I[h(e)=h_{\rm recorded}]\,I[r_e=r_b]\,I[s_e=s_{\rm required}]\,I[\mathrm{status}(e)=\mathrm{PASS}],$$

where $h$ is a SHA-256 content digest over the example's **declared payload string**, $r_e$ is evidence revision, and $s_e$ is the tested scope. Each indicator is necessary for the local screen; their conjunction is **not** an accreditation of the test method, authenticity of signatures, or independence of reviewers. Real evidence systems also require immutable artifact storage, key management, credentialed review, meaningful semantic change control, and trust boundaries.

The controlled ledger reports:

| Claim | Artifact | Recorded problem | Actionable? |
|---|---|---|---|
| CL-CAP | EV-CAP | Tested nominal scope, but storm scope required | No |
| CL-WAIT | EV-WAIT | Revision 2.0, while build is 2.1 | No |
| CL-ACCESS | EV-ACCESS | Current revision, but recorded FAIL | No |
| CL-INT | EV-INT | Interface contract evidence revision 2.0 | No |
| CL-ENT | EV-ENT | Current, matching scope, PASS status | Yes for **narrow local path screen** |

Hence structural coverage is $5/5=100\%$ but actionable local coverage is $1/5=20\%$. The fifth path is **not** a validated causal enterprise claim; it only passes the explicitly simplified metadata checks. None of the required `safety_approval`, `accessibility_consultation`, `data_governance_approval`, and `operations_authorization` flags is granted in the case JSON. These omissions are separately disqualifying and cannot be made good by adding more evidence links.

### Change impact and provenance attack examples

Suppose an analyst copies `EV-WAIT` from release 2.0 into a 2.1 readiness dashboard. The link target exists, the status remains PASS, and the recorded content digest still matches. Yet the evidence is **stale** for 2.1 until a reviewed impact assessment or new verification establishes its applicability. Conversely, if an artifact's payload changes without updating the recorded digest, a digest check detects the mutation; updating both payload and digest can still conceal an unauthorized rewrite. A digest verifies content consistency relative to a trusted baseline, not authorship or professional approval.

To run the adversarial exercise, copy the JSON, alter an evidence payload without changing `sha256`, and rerun the checker in a temporary Python process. The affected path must gain `digest_mismatch`. If instead you update the revision string alone, it must still retain any unresolved status or scope failures. A real digital thread would also distinguish evidence generated for the same model from independent bench measurement; two paths based on one unverified simulation do not create two independent proofs.

### Granular assurance and defeaters

A defensible assurance argument states a bounded claim: 'The specified dispatch interface satisfied requirement REQ-INT under the listed test environment, revision, timestamp policy, and input class.' The *warrant* links a test result to that claim, and a *defeater* identifies conditions under which the warrant fails (such as clock drift, unseen demand regimes, or a producer schema revision). The path is re-evaluated when a defeater becomes plausible. A verified model trace and a signed operational release are distinct evidence types, with distinct authorized decision makers.

**Worked exercise 1 — coverage.** A dashboard reports 100% coverage because every requirement links to an artifact. Calculate actionability. **Solution:** One of five paths passes the local metadata screen, so actionable coverage = 20%. Even 100% actionability would not override missing authorizations.

**Worked exercise 2 — repaired revision.** Change `EV-WAIT` revision from 2.0 to 2.1 without changing its payload and without new validation. Does the record become credible? **Solution:** The toy checker may mark it actionable if all local fields match; this demonstrates the *limit* of the checker. Authentic release evidence requires a legitimate revision record, justified model applicability, and independent verification—not a string edit.

**Adverse case.** Duplicate a claim row in the ledger. The model must reject ambiguity rather than silently overwrite one evidence source. The six chapters' joint example deliberately ends with HOLD; the release decision remains outside the programmatic checker.
<!-- STEP04-CONNECTED-EVIDENCE-END -->
