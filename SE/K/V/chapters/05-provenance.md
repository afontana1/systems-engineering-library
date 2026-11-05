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
