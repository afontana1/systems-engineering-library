# Human systems integration: people are part of the architecture

**Canonical reference · Human-centered systems engineering · Expanded reference · Internal editorial review; independent peer review not performed**

## Definition and system boundary

**Human systems integration (HSI)** considers operators, maintainers, users, training, workload, staffing, accessibility, health, safety, and organizational conditions together with hardware and software. A function assigned to a person is still a system function with capacity limits, error modes, environmental constraints, and evidence needs. HSI is therefore not the cosmetic improvement of user interfaces after the technical architecture is fixed; it is part of system requirements, allocation, trades, integration and validation. NASA's systems-engineering guidance identifies HSI as a cross-disciplinary concern and calls for a planned human-centered design process.

For an automated shuttle, the architecture may assign route selection to software, boarding verification to an operator, and emergency intervention to a remote supervisor. An interface diagram that shows only network messages obscures attention switching, confusing alerts, communication time, physical accessibility, and the risk that two people believe the other has control.

## Task analysis and function allocation

Start with representative tasks and contexts: who performs them, goals, cues, information, controls, physical effort, error opportunities, interruptions, required recovery, and time constraints. Use actual operational scenarios rather than abstract personas alone. Allocate tasks based on human and machine strengths, but also on *coordination costs*. Automation may reduce routine workload while increasing rare-event cognitive demand; a supervisor who has not actively controlled the system for hours may be expected to recover it in seconds.

Human factors design must consider populations rather than an average user: variations in vision, mobility, reach, language, age, fatigue, training, and assistive technology can determine whether the system provides acceptable service. A design that works for an experienced prototype team may fail with newly trained staff, temporary workers, visitors, or stressed operators. Include support and maintenance roles during early trade studies.

## Worked reasoning: when workload exceeds available attention

Assume a dispatcher must perform six distinct checks that each require **20 seconds of focused attention** in a 90-second transition. The nominal work demand is `6 × 20 = 120 seconds`, so the demanded utilization is `120/90 = 1.333`, or **133%** of one person's available attention even before interruptions or switching costs. Training cannot reliably make 120 seconds of nonoverlapping work fit into a 90-second window. Design responses could move checks earlier, automate with independent evidence, change role allocation, simplify the interaction, or extend the allowed transition where safety permits.

The figures are illustrative. Real work is not necessarily divisible into independent 20-second tasks; measurements may depend on priority, proficiency, stress, visual search, and parallel actions. The important inference is the *feasibility constraint*: an allocation requiring more serial attention than the operating window affords is not realizable without changing the tasks, timing or team.

## Validation evidence and disagreement with usability metrics

A usability survey can be positive even when rare emergency performance is unacceptable. Conversely, a formally correct safety process can have confusing labels that slow response. Appropriate HSI evidence may include task-completion distributions, missed-cue rates, recovery time, workload measures, situational awareness, ergonomic and accessibility checks, simulation exercises, and controlled human-in-the-loop trials across relevant participant groups and scenarios. Avoid inferring cause from a small before/after change when staffing and scenario difficulty changed simultaneously.

A human-in-the-loop study cannot establish universal human reliability. Reporting must identify sample composition, training, environmental context, task novelty, equipment configuration, simulation realism, and limitations. Ethics, privacy and informed procedures matter when observing staff or collecting sensitive human-performance data.

## Failure modes and design review questions

- **Automation surprise:** an operator cannot predict mode transitions or what control authority they have.
- **Capacity mismatch:** the architecture assumes continuous attention from a person assigned several simultaneous duties.
- **Exclusion by averages:** the design is optimized for a nominal operator and omits accessibility or anthropometric extremes.
- **Training as a substitute for design:** recurrent errors are attributed to personnel rather than interfaces and allocation.

An HSI review should ask which functions depend on humans, under what conditions, with what workload and authority, what evidence supports successful operation, and what happens when people err or cannot respond. These answers belong in the architecture baseline.

## Selected source-to-claim references

- **H1 · HSI in systems engineering:** [NASA Systems Engineering Handbook, section 2.6 Human Systems Integration](https://www.nasa.gov/reference/2-0-fundamentals-of-systems-engineering/).
- **H2 · Human-centered design process and integration:** [NASA Systems Engineering Processes, Volume 2 — HSI and HCD guidance](https://www.nasa.gov/reference/3-0-systems-engineering-processes-vol-2/).
- **H3 · Design data and rationale for human spaceflight:** [NASA Human Integration Design Handbook — scope and companion guidance](https://www.nasa.gov/organizations/ochmo/human-integration-design-handbook/). Spaceflight-specific design data are not universal thresholds for all domains.

## Follow the knowledge

- **Prerequisites:** [Stakeholder needs](stakeholders-and-needs.md), [Operational scenarios](conops-and-scenarios.md).
- **Related concepts:** [System safety and hazards](system-safety-and-hazards.md), [Architecture allocation](allocation-matrix.md), [Verification and validation](v-and-v.md).
- **Go deeper:** [Book 7, Chapter 8 — Human performance and safety](../B7/chapters/08-design-for-human-performance-safety-security-usability-.md); [Book 1, Chapter 3 — Human needs and operational concept](../B1/chapters/03-needs-and-conops.md).
