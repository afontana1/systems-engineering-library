# Queues, Little’s Law, and engineering work in process

**Concept essay · EN.645.780 · Phase 4 companion**

*Illustrative calculations and scenarios use synthetic data; do not treat them as certified operational evidence.*

Engineering workflows often have far more waiting than hands-on effort. To estimate their behavior distinguish **arrival rate**, **completion rate**, **number in process**, **service time**, **waiting time** and **rework**. For a stable system with consistent boundaries, Little's Law states:

**L = λW**.

If the long-run average work in process is 18 changes and completion throughput is 3 changes/week, average end-to-end flow time is 6 weeks. This is an identity across a stable observation window, not a guarantee that forcibly halving WIP halves flow time without affecting throughput or demand.

### Why utilization matters

In the idealized M/M/1 queue with Poisson arrivals (rate λ) and exponential service (rate μ), and λ < μ, the expected *system* time is **W = 1/(μ − λ)**. Suppose arrivals occur at 4/week and the reviewer completes an average of 5/week: W = 1 week. If arrivals rise to 4.8/week, expected time becomes 5 weeks—even though nominal reviewer capacity has not changed. Real processes need not meet M/M/1 assumptions; this example explains why operating near 100% utilization is risky under variability.

### A more defensible diagnosis

Collect timestamps for: submitted, valid intake, queued for review, review started, returned for correction, evidence accepted, approved, integrated and released. Plot median and 90th-percentile times by change risk, classify blocked reasons and separate first-pass from rework flow. The single bottleneck may migrate after an intervention; that is not failure, it is a predicted system response.

### Three interventions and their distinct mechanisms

* **WIP policy:** prevents starting new work while key evidence tasks are blocked; may expose constraints but can reduce completed throughput if incorrectly enforced.
* **Intake-quality check:** lowers rework probability; may initially increase intake handling time.
* **Dedicated specialist capacity:** increases service rate at a verified bottleneck; may create underutilized specialist time if demand shifts.

Run a small discrete-event model before allocating money. Test its output against real cycle-time quantiles and stress it at peak arrivals.

**Check.** A team completes more work this month but its average work item age grows. Can you conclude lead time improved? **No**; demand, WIP, case mix and window boundaries must be examined.

---

[← Phase 4 contents](../README.md) · [Related course lessons](../README.html#en645780) · [Further reading](../RESOURCE-SHELF.md)
