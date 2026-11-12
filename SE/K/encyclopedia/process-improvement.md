# Process capability and continuous improvement

**Reference entry · Agile, digital and process engineering · Expanded reference**

## Definition and diagnostic distinction

**Process improvement** changes how work is performed to improve outcomes such as quality, lead time, safety, affordability, or learning. It is not synonymous with stricter procedure compliance or higher maturity ratings. A process can be highly standardized and still generate the wrong service. Credible improvement requires a causal hypothesis, a measurement system, a comparison strategy, and monitoring for adverse consequences.

## Theory: variation, causality, and capability

A measured process outcome `Y` varies due to operating conditions, inputs, people, equipment, sampling, and measurement error. Statistical process control distinguishes signals of possible process change from expected within-process variation; control limits characterize observed stability and should not be confused with customer specification limits. Traditional capability ratios such as `Cpk = min[(USL-μ)/(3σ), (μ-LSL)/(3σ)]` presume a meaningfully stable process and an appropriate distributional model. A nonstationary or heavily censored process makes naive capability numbers untrustworthy.

Before-and-after improvement claims are vulnerable to demand shifts, regression to the mean, and simultaneous initiatives. Randomized pilot assignment, phased rollout, matched comparison groups, or interrupted time-series analysis may provide stronger evidence depending on what is feasible. The chosen approach must account for spillovers: improving one group's handoffs can alter the control group's workload.

## Worked example: an apparent improvement driven by easier cases

A verification group reduces average closure time from 12 days to 8 days after introducing automated templates. However, the pre-change month contained 60% complex safety cases, while the post-change month contained only 20%. Stratified analysis shows safety cases still take 18 days and routine cases fall from 7 to 6. The unadjusted four-day gain overstates what the intervention achieved. A credible report presents case-mix-adjusted results, quality of closed evidence, escaped defects, and impact on downstream reviewers.

## Engineering use and evidence

Define the process boundary and stakeholder-valued outcome, map current flow, validate measurement, distinguish common and special causes, and identify the proposed mechanism of change. Pilot the intervention with acceptance and stop criteria. Record workload composition, implementation fidelity, resource cost, employee burden, and service outcomes. Institutionalize improvements only after observing sustained effects and a credible process-control response to future drift.

## Limitations and connections

Metric improvements may simply move delay or defects across an organizational boundary. A process with high conformance can be ineffective when the mission changes. Connect process improvement to **flow and queues**, **DOE**, **measurement hierarchies**, **intervention learning**, and **enterprise systems**.

## Technical analysis: separate improved work from easier work

Suppose an inspection process reports a pass rate rising from 80% to 90%. Initially it handles 80 easy cases (95% pass) and 20 hard cases (20% pass), yielding `0.8(0.95)+0.2(0.20)=0.80`. After a change, it handles 95 easy cases and 5 hard cases, with *unchanged conditional success rates*: the apparent pass rate becomes `0.95(0.95)+0.05(0.20)=0.9125` (91.25%). Overall improvement is therefore compatible with **zero improvement in the within-class processes**. This is case-mix confounding, not proof of a beneficial change.

Before endorsing the intervention, stratify by relevant workload, operator, environment, and severity; predefine the process boundary and outcome; and examine variation over time rather than comparing only two averages. For a difference-in-differences analysis, untreated and treated groups must have plausible parallel trends in the absence of intervention—an assumption requiring argument and diagnostic evidence. Control charts can distinguish stable from special-cause variation, but they cannot by themselves establish causality or show that the measured outcome is valuable to stakeholders.

## Verified source pointers

These sources establish authoritative terminology or methods in their own published scope. They have **not** reviewed or endorsed this entry.

- [NIST · NIST/SEMATECH e-Handbook of Statistical Methods (2002; online guidance)](https://www.nist.gov/publications/handbook-151-nistsematech-e-handbook-statistical-methods) — Statistical methods, experiments, reliability, and process assessment.
- [INCOSE · Systems Engineering Handbook, 5th ed. (2023)](https://www.incose.org/resource/incose-systems-engineering-handbook-a-guide-for-system-life-cycle-processes-and-activities-5th-edition/) — Published practitioner reference; full text may require access.

## Follow the knowledge

**Related concepts**

- [Measures of effectiveness and performance](metrics-hierarchy.md)
- [Design of experiments and sensitivity](design-of-experiments.md)
- [Flow, work in process, and bottlenecks](flow-wip-and-queues.md)
- [Interventions, policy resistance, and learning loops](intervention-and-learning.md)

**Go deeper in the 240-chapter textbooks**

- [Book 17, Chapter 05: Week 05 · Systems Engineering Process Improvement · Book chapter: Measurement system, variation, and baseline performance](../B17/chapters/05.md)
- [Book 17, Chapter 06: Week 06 · Systems Engineering Process Improvement · Book chapter: Process capability assessment, root causes, and midcourse exam](../B17/chapters/06.md)
- [Book 17, Chapter 09: Week 09 · Systems Engineering Process Improvement · Book chapter: Pilot experiments, implementation, and adoption](../B17/chapters/09.md)

**Further reference context**

- [NASA Systems Engineering Handbook](https://www.nasa.gov/reference/systems-engineering-handbook/) — General lifecycle and technical-management perspective.
- [Guide to the Systems Engineering Body of Knowledge](https://sebokwiki.org/wiki/Main_Page) — Broad terminology and disciplinary context.

**Editorial scope:** Examples and numerical values are illustrative. This is a reconstructed teaching reference, not a peer-reviewed compliance finding. Verify primary-source requirements and current publication versions before use on a regulated or high-consequence project.

## Step 02 deeper treatment: separate process changes from common-cause variation

A faster average is not necessarily an improved, stable process. Start by choosing the unit of analysis, a sampling interval and an operationally meaningful response measure. To illustrate, suppose a hypothetical review service measures ten consecutive weekly closure counts: 8, 11, 9, 12, 10, 9, 11, 10, 10 and 10. Their mean is 10 cases/week, but that number does not describe arrival rate, work size, reopened defects or queued inventory. A management dashboard showing “10 completed” cannot justify a conclusion that the backlog is stable unless arrivals and departures share the same boundary and time window.

A naive before/after comparison is vulnerable to regression to the mean and changing case mix. Prefer a documented intervention date, predeclared response measure, run-chart or suitable statistical process-control method, and evidence about special causes. Control limits are estimated from process data according to chart assumptions; they are **not** management targets or requirement limits. An experiment might split standardized work into smaller batches, then compare blocked time, defect escapes, and accepted throughput rather than only counting tickets.

**Exercise:** If 12 new cases arrive each week while 10 are accepted, calculate the six-week backlog increase: \((12-10)6=12\) cases, assuming no cancellations or rework. Identify a possible unintended consequence if the team maximizes closure count by skipping independent review. See [NIST/SEMATECH engineering statistics](https://www.itl.nist.gov/div898/handbook/) for design and statistical process techniques.
