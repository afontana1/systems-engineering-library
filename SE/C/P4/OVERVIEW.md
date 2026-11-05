# Phase 4 — Agile, digital, mission, and process-centered engineering

Phase 4 changes the unit of analysis from a single technical baseline to the **engineering operating system** that creates, connects, learns from, and improves that baseline. The learner has already practiced lifecycle engineering, software-intensive design, integration and T&E, modeling and simulation, uncertainty analysis, and model-based analytics. This phase asks how those capabilities should operate when knowledge is incomplete, environments change, evidence arrives continuously, organizations cross boundaries, and engineering processes themselves must evolve.

The phase retains three distinct courses:

1. [**EN.645.780 — Agile Systems Engineering**](EN645780.md)
2. [**EN.645.782 — Foundations of Digital and Mission Engineering**](EN645782.md)
3. [**EN.645.783 — Systems Engineering Process Improvement**](EN645783.md)

Agile Systems Engineering develops an evidence-driven learning and delivery operating model. Digital and Mission Engineering connects mission questions, authoritative models, data, digital threads, digital twins, and collaborative environments. Process Improvement assesses the current engineering system and governs a measurable future-state redesign.

[Back to program README](OVERVIEW.md)

---

## 1. Recommended sequence

1. **EN.645.780 — Agile Systems Engineering**
2. **EN.645.782 — Foundations of Digital and Mission Engineering**
3. **EN.645.783 — Systems Engineering Process Improvement**

EN.645.780 and EN.645.782 may be swapped when a learner already has substantial agile product-development experience but limited digital-engineering experience. EN.645.783 should remain last because credible process redesign requires direct experience with the lifecycle, analytic, agile, and digital practices being assessed.

## 2. Phase entry gate

Before beginning Phase 4, the learner should be able to:

* maintain a controlled requirements, architecture, interface, integration, V&V, risk, and decision baseline;
* explain the difference among lifecycle phase, development cadence, release, increment, iteration, experiment, and operational deployment;
* construct and query a basic MBSE repository and connect descriptive models to analytic evidence;
* interpret uncertainty, sensitivity, and model-credibility evidence without presenting a point estimate as certainty;
* use version control, issue tracking, executable notebooks or scripts, and reproducible test evidence;
* conduct a technical review, disposition findings, and distinguish evidence from opinion;
* identify safety, cybersecurity, regulatory, supplier, human, and operational constraints that cannot be wished away by adopting a faster cadence.

A learner missing these capabilities should complete the relevant Phase 1–3 remediation before continuing.

## 3. Shared phase case

### Autonomous Campus Mobility 2030 — Engineering Transformation and Mission Evolution

The Phase 4 case begins after the Phase 2 concept-to-test program and the Phase 3 analytic evidence program. A fictional organization, **Northstar Mobility Systems (NMS)**, has been selected to mature and scale the campus mobility capability. The technical baseline is promising, but the organizational and delivery system is not keeping pace with changing conditions.

The controlled transformation brief includes:

* the planned operational pilot has been shortened from 18 months to 12 months;
* a supplier autonomy component has a newly disclosed cybersecurity weakness;
* a battery supplier now quotes a 24-week lead time;
* accessibility stakeholders require a revised boarding and assistance concept;
* two campus locations have different operating, labor, privacy, and safety constraints;
* Phase 3 evidence shows that mean performance is acceptable but tail wait-time and recovery performance are not;
* senior leadership wants demonstrable learning every 30–60 days without relaxing safety or mission evidence;
* the organization relies on disconnected requirements, model, code, test, maintenance, and operational-data repositories;
* the board wants a credible pathway from one pilot to a reusable family of mobility services.

Each Phase 4 course treats a different transformation question:

| Course | Transformation question |
|---|---|
| EN.645.780 | How should NMS organize teams, architecture, flow, learning intervals, quality, and technical governance to become more responsive without losing rigor? |
| EN.645.782 | How should mission threads, models, data, digital threads, digital twins, and collaborative environments be organized to create trusted lifecycle evidence? |
| EN.645.783 | Which engineering processes are actually limiting outcomes, and how should a measurable future-state process be implemented and sustained? |

## 4. Phase-wide operating principles

All Phase 4 work must observe these principles:

1. **Agility is an outcome, not a ceremony count.** Responsiveness, learning speed, decision quality, and affordable change matter more than whether a named framework is used.
2. **Architecture and process co-determine agility.** A tightly coupled product cannot be made agile solely by changing meetings, and a modular product can still be slowed by dysfunctional governance.
3. **Safety, security, quality, and compliance are continuous evidence obligations.** They are not final hardening phases.
4. **Models and data are governed engineering assets.** A dashboard or digital twin without provenance, authority, validation, and intended use is not trusted evidence.
5. **Flow is measured end to end.** Local utilization, velocity, or output can improve while system lead time and mission value worsen.
6. **Teams need bounded authority.** Self-management requires mission, interfaces, decision rights, escalation paths, and feedback—not management abandonment.
7. **Every change is a hypothesis.** A process, architecture, tool, or policy intervention must state expected outcomes, measures, risks, and reversal conditions.
8. **Transformation must preserve the right controls and remove the wrong ones.** The goal is not indiscriminate deregulation or automation.

## 5. Common Phase 4 repository

Use a shared controlled repository:

* `/00-transformation-governance`
* `/01-mission-and-stakeholders`
* `/02-learning-and-delivery-operating-model`
* `/03-architecture-and-models`
* `/04-digital-thread-and-data`
* `/05-pipelines-integration-and-evidence`
* `/06-process-measures-and-experiments`
* `/07-reviews-decisions-and-risks`
* `/08-handoffs-and-portfolio`

Every significant artifact must record owner, version, status, source, assumptions, dependencies, review state, and change rationale.

## 6. Shared evidence chain

The phase should maintain an end-to-end chain:

> mission outcome → stakeholder or operational need → learning question → technical or process hypothesis → architecture/process change → executable work → verification or analytic evidence → operational observation → decision → baseline/process update

A broken chain is treated as a transformation risk. It is not repaired by adding a presentation slide.

## 7. Phase review gates

| Gate | Course | Purpose | Minimum evidence |
|---|---|---|---|
| Agile Suitability and Tailoring Review | EN.645.780 | Decide where agile/Lean approaches fit and where stronger lifecycle controls remain necessary | Context assessment, uncertainty map, constraints, tailoring rationale |
| Learning and Flow Review | EN.645.780 | Confirm learning intervals, value flow, team model, architecture enablers, and evidence plan | Roadmap, value-stream analysis, backlog, architecture and assurance strategy |
| Agile Engineering Operating Model Review | EN.645.780 | Approve the integrated team, architecture, pipeline, governance, and scale recommendation | CEO recommendation, measures, risks, transition plan, oral defense |
| Digital Engineering Strategy Review | EN.645.782 | Confirm mission questions, authoritative sources, model/data strategy, and digital environment | Mission threads, information architecture, governance and use cases |
| Digital Thread/Twin Credibility Review | EN.645.782 | Decide whether connected digital evidence is trustworthy for stated uses | Trace/query evidence, provenance, validation, security, limitations |
| Current-State Process Assessment | EN.645.783 | Establish evidence for process performance, causes, variation, and constraints | Process model, measures, stakeholder evidence, root-cause analysis |
| Future-State Process Readiness Review | EN.645.783 | Approve an implementable process redesign and controlled experiment | Future-state model, controls, roles, pilot, measures, risks |
| Phase Portfolio Defense | All | Demonstrate an integrated, evidence-driven transformation system | Controlled repository, review records, results, reflections, defense |

## 8. Relationship among the courses

Repeated topics must increase in scope rather than restart:

* EN.645.780 uses models, digital threads, and pipelines to shorten learning and integrate evidence; it does not attempt to teach the full digital-engineering discipline.
* EN.645.782 makes mission questions, authoritative data, model semantics, interoperability, digital-thread queries, and digital-twin credibility the primary subject.
* EN.645.783 treats the agile and digital practices themselves as candidate process elements to be measured, diagnosed, redesigned, piloted, and governed.

## 9. Phase workload and pacing

Fully expanded courses target **10–13 hours per week**, consistent with graduate-level technical study and the source Agile Systems Engineering syllabus. Allow additional time for:

* cross-disciplinary coordination or role simulation;
* data and repository cleanup;
* pipeline, model, and traceability debugging;
* review preparation and corrective action;
* process observation, stakeholder interviews, or retrospective evidence;
* revision after red-team findings.

Do not compress learning intervals by skipping feedback, integration, or evidence. That reproduces the behavior this phase is intended to correct.

## 10. Current development status

| Course | Status | Next action |
|---|---|---|
| EN.645.780 Agile Systems Engineering | Fully expanded | Complete and pilot the course |
| EN.645.782 Foundations of Digital and Mission Engineering | Fully expanded | Complete and pilot the course |
| EN.645.783 Systems Engineering Process Improvement | Fully expanded | Complete and pilot the course |

All three Phase 4 courses are fully expanded. The phase is ready for controlled piloting and workload calibration.

## 11. Phase exit criteria

Phase 4 is complete when the learner can:

* assess whether, where, and how agile and Lean approaches fit a specific systems context;
* design deliberate learning intervals with hypotheses, evidence, and decision criteria;
* improve end-to-end flow while respecting long-lead hardware, suppliers, assurance, and integration constraints;
* define team boundaries, technical leadership, decision rights, and cross-team coordination;
* design architectures, model practices, and pipelines that enable affordable change and continuous evidence;
* define and govern authoritative digital threads and fit-for-use digital-twin concepts;
* assess an engineering process using data and stakeholder evidence rather than fashion;
* design, pilot, measure, control, and sustain a future-state process;
* defend a transformation recommendation, its expected benefits, risks, limits, and reversal conditions.

---

## Course files

- [EN.645.780 — Agile Systems Engineering](EN645780.md)
- [EN.645.782 — Foundations of Digital and Mission Engineering](EN645782.md)
- [EN.645.783 — Systems Engineering Process Improvement](EN645783.md)

[Back to program README](OVERVIEW.md)
