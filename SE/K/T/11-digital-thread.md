# Digital threads, model credibility, and configuration provenance

*Core Concepts · Enterprise & complexity · T11*

> Make the connection between models, tests, and decisions trustworthy across tools and revisions.

**Recommended preparation:** [Model semantics, viewpoints, and digital traceability](04-model-semantics.md), [Requirements, traceability, and assurance arguments](02-requirements.md)

**Related course companions:** [Book 3](../B3/OPEN-BOOK.html), [Book 16](../B16/OPEN-BOOK.html), [Book 17](../B17/OPEN-BOOK.html)

## 1. A connected data environment is not automatically a trustworthy one
A digital thread connects engineering information over the lifecycle: stakeholder needs, requirements, architecture, analyses, builds, tests, changes, and operational observations. A hyperlink among documents is only the beginning. The thread needs stable identifiers, typed relations, revision information, validity rules, and permissions. An automated report should be able to explain what a link means and why it remains valid.

Consider a battery model updated from capacity 40 kWh to 36 kWh because of aging. That change potentially affects route feasibility, charging schedules, test baselines, maintenance instructions, and a safety margin argument. A thread that only tracks file versions will show that something changed; a semantic thread tells reviewers which claims are affected.

## 2. Define authoritative sources by information type
There need not be one master database for everything. The requirements tool may own the approved requirement text; the CAD system may own geometry; a test repository may own raw measurements; a configuration service may own build identities. Define ownership and synchronization rules. When two tools disagree, the answer should be a documented conflict and resolution process—not silent last-writer-wins behavior.

Every evidence record should include content or immutable reference, producing tool and version, configuration identity, timestamp, collection conditions, and approval status. Cryptographic hashes can help detect alteration, but a perfectly preserved file can still contain an invalid measurement or incorrect assumption.

## 3. Digital twins are bounded models connected to observations
A digital twin is not synonymous with a dashboard or a highly detailed 3-D model. The key is a maintained relationship between a modeled system and relevant physical observations, with a specified purpose. A predictive maintenance twin may update degradation parameters using telemetry; a dispatch twin may estimate fleet readiness. Define update frequency, data latency, calibration conditions, and what action is permitted when the model becomes stale.

An engineering rule might reject predictions when telemetry age \(a\) exceeds 15 minutes. This creates an explicit stale-state condition. Without it, a dashboard can display visually persuasive but obsolete information.

## 4. Measure the credibility of an information chain
Audit one claim end to end: “The fleet can sustain 90% request completion in degraded operation.” Locate the model assumptions, demand dataset, simulator code version, configuration, random seeds, run outputs, statistical analysis, and approval decision. If you cannot recreate the result or identify its applicability boundary, the claim is not yet suitably supported.

Credibility grows through traceable evidence, verification, validation, uncertainty characterization, and independent review. More links alone do not make it credible.

## 5. Audit an entire evidence chain
Start from an operational claim, not from a database. For each claim, ask which model output supports it, which simulation and dataset produced that output, which software/configuration versions were used, which requirements make it relevant, and who approved the conclusion. Export the chain as an auditable manifest. Include hashes or immutable IDs where available, but do not confuse file integrity with scientific validity.

A digital-twin forecast should have a **validity envelope**. A maintenance model trained on warm-weather bus routes cannot automatically be applied to an icy mountain deployment. Document environmental range, observation freshness, sensor quality, calibration date, and actions allowed when those conditions fail. If a twin is stale, a robust design may fall back to a conservative rule rather than present a precise but unjustified prediction.

For cross-tool traceability, distinguish a *link existence* check from a *semantic compatibility* check. A model element may exist in two repositories but refer to different revisions or unit conventions. The interface between engineering repositories requires versioned mappings, just like an interface between runtime components.

**Check your reasoning:** A hash proves the evidence artifact was not modified after hashing. Does it prove that the telemetry sensor was calibrated? No. Provenance integrity and measurement validity are separate parts of the assurance chain.

## Guided worked example

### Worked revision example
Requirement R17 at revision 4 sets a 15-second timeout. Test T09 was executed against R17 revision 3, which specified 10 seconds, with software build 2.8. The traceability graph can report a link, but not current verification. A correct audit flags evidence as stale pending re-analysis or re-test; it should not silently mark R17 as passed.

## Independent transfer exercise

Create a six-node digital-thread chain for one fleet availability claim. Add version IDs, evidence dates, authority for each source, and a validation rule that detects stale or mismatched configurations.

[Open the companion hypothetical lab](labs/11-digital-thread-workshop.md)

<details><summary><strong>What a defensible answer must contain</strong></summary>

Differentiate referential integrity from evidence applicability; provide one scenario where every link resolves but the final claim is still unsound.

</details>

## Next connections

Use the related books above to see how this concept becomes a course assignment. The lab provides a small, deliberately incomplete practice setting; it does not replace verification against real operational data.


<!-- STEP04-T1-START -->

## Step 04 T1 — Evidence-driven correction and worked transfer

### T1 audit finding: complete links are not sufficient evidence

The NS-T4.1 evidence register contains five uniquely identified requirement paths. A path is *actionable for the defined use* only if its state is **verified**, its route-interface revision equals the declared `route-3` baseline, and its intended-use field says `classroom capacity screening`. Exactly **two of five** paths meet all three predicates. The other records include stale revisions, unverified artifacts, or a different permitted use. Counting five hyperlinks would report 100% graph connectivity, but only 40% actionable evidence.

A reproducible closed-world query should return the failing paths and reasons, not just a score. Record source identity, revision, method of verification, status, review date, configuration, and authorized purpose. Even if all five records passed this syntactic screen, operational authorization would remain separate: in the fixture, only the road authority has approved; labor and privacy approvals remain absent.

**Practice and explained solution.** Change a `route-2` record to `route-3` without changing its `draft` status. It **still does not** become actionable. Then grant all permissions without changing missing technical evidence: the technical evidence gate still fails. These independent gates help prevent a digital thread from becoming a visual substitute for an assurance argument. [Inspect the JSON and checker](labs/T1-INTEGRATED-CASE.md).

<!-- STEP04-T1-END -->
