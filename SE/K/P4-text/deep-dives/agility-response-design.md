# Engineering an agility response requirement

**Concept essay · EN.645.780 · Phase 4 companion**

*Illustrative calculations and scenarios use synthetic data; do not treat them as certified operational evidence.*

An agility claim needs the same rigor as any nonfunctional requirement. “Be more agile” is not testable. Instead, describe the **stimulus**, **observer**, **operating condition**, **authorized response**, **response-time bound**, **cost bound**, and **evidence**. For example: “When a field cybersecurity advisory identifies an exploitable fault in the dispatch gateway, the program shall place affected fleet configurations in an approved mitigated state within 72 hours, without disabling emergency-stop or violating configuration control.” The response clock must include detection, diagnosis, patch construction, verification, risk authorization and deployment.

### Why end-to-end response time matters

Suppose the median workflow is detection 8 hours, triage 8, development 24, integration testing 32, risk authorization 24, and staged deployment 8. Its median summed time is 104 hours **if these activities are serial**. Some can overlap; others are strict dependencies. Estimate the critical path from actual event logs rather than automatically summing averages (the average of the maximum is not generally the maximum of averages). Even if code development drops from 24 hours to 12, the system still misses 72 hours without changes elsewhere.

### Design dimensions

| Dimension | Engineering question | Example evidence |
|---|---|---|
| Awareness | How is change detected and classified? | Alarm detection and false-alert studies |
| Response architecture | Which modules can change independently? | Dependency graph and contract tests |
| Authorization | Who accepts residual consequences? | Signed decision record |
| Recovery | Can the system revert to a safe approved state? | Fault-injection and restoration test |
| Sustainment | Can adaptability be maintained economically? | Change cost and technical debt trend |

Different classes of change need different envelopes. An operational dispatch policy may be reversible in minutes. A battery-pack replacement can require procurement, certification and maintenance visits. Do not impose one organization-wide response SLA on unlike changes.

### Worked decision

Two interventions are proposed: A reduces average coding time by 12 hours at a cost of $40,000; B reduces assurance queue time by 20 hours at $65,000. If coding was not on the critical path because certification can begin from an earlier controlled build, A could offer little end-to-end benefit. Map dependencies and test before choosing. A valid experiment records the baseline distribution and guardrails, then compares end-to-end results and not only a team metric.

### Practice with an answer

**Question.** Why is “deploy changes in seven days” an unsafe requirement for a safety-critical fleet? **Answer.** It does not identify change class, safety constraints, baseline, verification evidence, decision authority or what “deploy” means. A safer requirement defines a bounded class and requires authorized, verified operational response.

---

[← Phase 4 contents](../README.md) · [Related course lessons](../README.html#en645780) · [Further reading](../RESOURCE-SHELF.md)
