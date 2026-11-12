
---

## Step 04 advanced integration — finite-state safety, liveness, and counterexamples (NS-AA4.1)

### A1. State and transition semantics

Let the dispatcher decision state be \(x=(s,a,u)\), where \(s\in\{\mathrm{OPEN},\mathrm{CLOSED},\mathrm{UNKNOWN}\}\) is the reported route status, \(a\ge0\) is the age in minutes of that report, and \(u\in\{0,1\}\) denotes operator authorization. The intended issuance guard is

\[
G(x)=(s=\mathrm{OPEN})\land(a\le5)\land(u=1).
\]

The *safety property* is \(\Box(\mathrm{DispatchIssued}\Rightarrow G(x))\): whenever a dispatch is issued, the recorded authorization, status, and freshness preconditions must hold at that decision instant. The box operator is a temporal-logic convention meaning *always*. This property is weaker than “the route is physically safe at arrival,” which requires a model of report accuracy, update delay, and actual road state.

A deliberately defective implementation uses \(G_{bad}(x)=(s=\mathrm{OPEN})\lor(u=1)\). Consider \(x=(\mathrm{CLOSED},0,1)\): the defective guard issues a dispatch because authorization exists, even though the road is closed. Or consider \(x=(\mathrm{OPEN},6,0)\): it dispatches despite stale information and missing authorization. The distinction between OR and AND is therefore a system hazard, not a style preference.

### A2. Exhaust the finite abstraction and interpret the result

The [testable checker](../code/advanced_case.py) enumerates all three statuses, ages \(\{0,5,6\}\) minutes, and both authorization values: 18 abstract decision states. For each it compares the defective guard with the desired conjunction, returning the states in which unsafe dispatch is permitted. This is an **exhaustive proof only for the 18-state abstraction**, not a model check of the real dispatcher, arbitrary time, concurrent message delivery, or an actual SysML model. A code review must still confirm that the implemented transition is the one being checked.

The abstraction intentionally includes the boundary \(a=5\) and the just-stale value \(a=6\). Boundary testing matters because the faulty expression can appear correct under a narrow nominal dataset. Add a case where a report is fresh during route selection and becomes stale before dispatch issuance: the invariant requires the guard to be reevaluated at the actual decision point. Time-of-check/time-of-use races cannot be ruled out by a single atomic Boolean evaluation if the real system has concurrent components.

### A3. Safety is not enough: explain a conditional liveness claim

A system that **never dispatches** satisfies the dispatch safety invariant vacuously. To reason about service, add a liveness statement such as \(\Box[(\mathrm{Eligible}\land\mathrm{ResourcesAvailable}\land\mathrm{FairScheduling})\Rightarrow\Diamond\mathrm{Resolved}]\). The diamond denotes *eventually*. Without assumptions about eventually available capacity, fair scheduling, reliable communications, and bounded outages, such a guarantee may be false. Moreover, “resolved” must distinguish completed service, authorized cancellation, and refusal: otherwise a system can game liveness by immediately rejecting every request.

A proper review therefore checks safety conditions and service obligations separately, with bounded scenarios and explicit environmental fairness premises. This is also why formal truth tables cannot replace tests using physical route providers and human operators.

**Exercise.** Evaluate \(G\) and \(G_{bad}\) for `(OPEN, 6, True)`. **Worked solution:** \(G=0\) because the age exceeds five minutes; \(G_{bad}=1\) because either an open status or authorization is sufficient. That is a counterexample despite the apparently reassuring open status. Propose a remedial guard requiring fresh status and a final, atomic authorization check.

**Reproduce:** `unsafe_dispatch_counterexamples(5)` in the [case code](../code/advanced_case.py). The next chapter treats the quantitative interfaces that can invalidate even a logically correct guard: [budgets and dependent reliability](04-budgets.html).
