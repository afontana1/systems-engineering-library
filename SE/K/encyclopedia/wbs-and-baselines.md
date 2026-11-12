# Work breakdown structures and technical baselines

**Reference entry · Foundations and management · Expanded reference**

## Definition and diagnostic distinction

A **work breakdown structure (WBS)** organizes the total authorized work by deliverable and decomposition level. It is a control structure for scope, responsibility, estimation, and earned progress—not a chronological task list. A **technical baseline** is a versioned agreement about approved requirements, interfaces, models, designs, and associated decision evidence. A cost or schedule baseline describes planned resources and timing; changing one without reconciling the others creates a project that appears controlled only on paper.

## Theory: decomposition, conservation, and change propagation

A well-formed WBS obeys a **100-percent rule** at every decomposition: children collectively cover their parent deliverable without double counting. Each control account joins scope to a responsible organization and measurable progress rules. For a work package `i`, planned value `PV_i`, earned value `EV_i`, and actual cost `AC_i` are distinct variables. At a review point, `CPI = sum(EV_i) / sum(AC_i)` and `SPI = sum(EV_i) / sum(PV_i)`. These ratios describe performance against a particular baseline; they do not measure technical adequacy or automatically predict physical completion.

Technical change propagation is a directed dependency problem. A battery capacity increase may change mass, cooling, packaging, maintainability, software thresholds, test equipment, and certification evidence. An approved change should carry an impact set `I(change)` with affected requirements, interfaces, configuration items, work packages, and verification records. Without configuration identifiers, two cost reports can be internally accurate yet refer to different designs.

## Worked example: a misleading recovery report

Suppose by week 12 a project has `PV = $400k`, `EV = $320k`, and `AC = $360k`. Then `CPI = 0.889` and `SPI = 0.80`. A simplistic estimate at completion for a `$900k` budget is `EAC = BAC / CPI = $1.0125M`, **if** future cost efficiency remains similar and the budgeted scope is unchanged. If the team deletes difficult verification work from the baseline, both ratios may improve while mission readiness worsens. A recovery proposal must show the revised work scope, evidence obligations, and schedule logic before comparing new metrics.

## Engineering use and evidence

Define WBS elements by verifiable product or service outcomes. For each control account, record acceptance rules, owner, measurement method, baseline version, risks, and upstream/downstream dependencies. Establish a change board that can approve, reject, defer, or condition a change—and that records impacts on the integrated baseline. Use physical percent-complete rules or weighted milestones only where achievement can be observed; hours spent are not equivalent to value earned.

## Limitations and connections

A precise WBS can still encode the wrong product, and earned-value indices become unstable for small packages or after frequent rebaselining. Schedule compression may increase rework and quality risk. Link the WBS to **requirements**, **risk and issues**, **traceability**, **integration readiness**, and **technical assurance** so that progress reflects delivered evidence, not administrative closure.

## Technical analysis: distinguish delivered scope from measured cost

A work breakdown structure (WBS) organizes the product-oriented scope of work; it is not identical to the organization chart or a schedule. A baseline binds agreed product scope, requirements, design configuration, and planned cost/schedule at a specific revision. Earned-value calculations may diagnose control performance but cannot substitute for independent evidence that the delivered product satisfies requirements.

Suppose a work package has budget at completion `BAC = $500k`, earned value `EV = $200k`, and actual cost `AC = $250k`. Its cost performance index is `CPI = EV/AC = 0.8`. Under the **specific** forecast assumption that future work continues at that CPI, estimated cost at completion is `EAC = BAC/CPI = $625k`. The implied overrun is **$125k**. A different completion strategy, scope revision, or nonrepresentative early cost profile can invalidate this extrapolation.

**Evidence boundary.** Identify the revision of each baseline, authorized change, remaining technical risk, and basis for percent-complete judgments. Treat forecast figures as conditional signals for management action, not definitive estimates of final affordability or technical quality.

## Claim-specific sources

The following **selected methodological claims** are tied to identifiable sections or abstracts, not merely generic reading lists. Source scope is stated for each link. Numerical scenarios and computations in this article are **original illustrative examples**, not data, calculations, or endorsements supplied by the linked publishers. Links require internet access; the explanation remains readable offline.

- **C1:** Technical planning organizes scope, resources and schedule according to product work breakdown and milestones. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §6.1 Technical Planning](https://www.nasa.gov/reference/6-1-technical-planning/) · *direct guidance*.
- **C2:** Configuration management defines and controls the technical baseline and its revisions. **Evidence:** [NASA — NASA Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2, §6.5 Configuration Management](https://www.nasa.gov/reference/6-5-configuration-management/) · *direct guidance*.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NASA · Systems Engineering Handbook, NASA/SP-2016-6105 Rev 2 (2016/2017)](https://www.nasa.gov/reference/systems-engineering-handbook/) — Lifecycle engineering, technical management, requirements, verification and validation.
- [INCOSE · Systems Engineering Handbook, 5th ed. (2023)](https://www.incose.org/resource/incose-systems-engineering-handbook-a-guide-for-system-life-cycle-processes-and-activities-5th-edition/) — Published practitioner reference; full text may require access.



## Step 02 review studio — a baseline change that looks like recovery

A team reports planned value (PV) 400, earned value (EV) 320, and actual cost (AC) 360, all in thousands of budget units. Compute `CPI = EV/AC = 0.8889` and `SPI = EV/PV = 0.80`. Now the program manager proposes removing a difficult safety-test work package from the WBS so the indicators improve. Is that schedule recovery or scope change? **Answer:** it is a scope change. It may be legitimate only after the product obligations and residual risks are reviewed by the authorized decision maker; the deleted task cannot make its safety evidence unnecessary. Update the *product baseline, WBS, cost/schedule baseline, and verification plan together*.

**Review exercise (solved):** a test work package has been earned at 100% because 40 test runs completed, yet none used the approved current interface schema. Should the package be recorded as complete? **Not without a justified acceptance rule and configuration applicability.** Output counts are not equivalent to accepted deliverables. A defensible earning rule would require an approved test report applicable to the controlled configuration, not merely executed test hours. Forecast indices also depend on the estimation and earning rules; they cannot certify product performance.

## Follow the knowledge

**Related concepts**

- [Risk, issue, uncertainty, and opportunity](risk-vs-issue.md)
- [Requirements traceability: a typed graph of engineering claims](traceability-graph.md)
- [Requirements: precise obligations, not persuasive sentences](good-requirements.md)
- [Integration build-up and readiness evidence](integration-strategy.md)

**Go deeper in the 240-chapter textbooks**

- [Book 2, Chapter 03: Chapter 3 · Scope Becomes Controllable Through Products](../B2/chapters/03-wbs-and-work-authorization.md)
- [Book 2, Chapter 06: Chapter 6 · A Baseline Is a Defensible Agreement](../B2/chapters/06-integrated-baseline-review.md)
- [Book 7, Chapter 12: Book 7 · Chapter 12: Design baseline handoff](../B7/chapters/12-conduct-the-final-design-integration-review-and-hand-of.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.
