# Chapter 4 — An Estimate Is an Argument About the Future

*EN.645.667 · Week 4 · Basis of estimate, uncertainty, budgets and price · Preceded by [Chapter 3](03-wbs-and-work-authorization.md); continue with [Chapter 5](05-schedule-networks-and-float.md).*

> **Study contract.** This chapter teaches the concepts behind Week 4; practice them in [Hypothetical Lab 4](../labs/lab-04-estimating-and-reserves.md), then complete the [original Week 4 coursework](../../../C/P0/EN645667.md). These fictional examples are not contractual or safety approvals.

## The management problem

Project estimates look like numbers, but they are really arguments about how work will unfold. “Vehicle integration will cost $1.1 million” silently assumes a technical baseline, supplier scope, labor productivity, quality standard, integration sequence, and contingency for unknowns. The critical management task is not merely computing a subtotal; it is making the causal assumptions auditable and updating them as evidence arrives.

Use several estimating methods for different maturity levels. An analogous estimate transfers historical observations with explicit adjustments; a parametric estimate multiplies quantities by rates validated for a relevant domain; a bottom-up estimate decomposes work packages and resource hours; expert judgment can fill gaps but should preserve the rationale. Independent cross-checks matter because two spreadsheet tabs built from the same optimistic assumption are not independent evidence.

Distinguish an estimate of expected work from a time-phased budget, a performance measurement baseline (PMB), management reserve, contingency for identified risks, fee, and quoted price. Organizations use these terms differently under different contracts and EVMS policies; document the particular conventions used. Under this course’s simplified fictional convention, $7.2M PMB + $0.6M management reserve + $0.6M fee = $8.4M proposed price.

## Develop the method

A defensible basis of estimate has units, quantities, labor rates or vendor quotes, escalation assumptions, schedule basis, exclusions, estimate date, and a method for each WBS element. To express uncertainty, use ranges and explicit drivers rather than adding an arbitrary percentage to every line. A three-point assessment may use optimistic, most-likely, and pessimistic values, but its output is only as credible as its assumptions about the distribution and correlation of risks.

Cost and schedule must be integrated: changing an interface can add not only engineering hours but additional test fixtures, supplier delays, and facility occupancy. Record causes, not just monetary adders. Management reserve should have a control procedure; it is not spendable performance credit that can erase a variance.

## The mechanism beneath the method

An estimate is a conditional forecast produced by assumptions about quantities, rates, learning, uncertainty and the scope being estimated.

### Distinguishing related ideas

Contingency handles modeled variability; management reserve addresses management-controlled uncertainty; neither repairs a missing scope item.

### Interpretation and boundary conditions

A labor estimate that assumes uninterrupted integration becomes implausible if interface defects repeatedly recycle the same test campaign.

## Deeper theory: estimation is a calibrated uncertainty model

### A point estimate hides the conditional structure of cost

An estimate is a prediction conditional on scope, performance, labor market, acquisition strategy, maturity, and calendar. A useful decomposition is `C_total = Σ_j Q_j R_j + C_integration + C_overhead`, where `Q_j` is work quantity and `R_j` is a unit rate. This decomposition is not unique; its value is that quantities, rates, and exclusions can be examined separately. Work packages also interact: a delayed interface specification may cause rework across software, hardware, and verification. The error from that coupling is not necessarily captured by adding an independent contingency percentage to each line.

Three-point estimates are summaries of judgment, not automatically probability distributions. A minimum, most-likely, and maximum value only define a distribution after a family and its interpretation are chosen. The often-used PERT-style mean `(a + 4m + b)/6` carries assumptions about shape and elicitation; it should not be mistaken for an empirical law. Early projects often have asymmetric downside: a favorable interface test saves limited money, while a failed architecture can cause expensive redesign. Reference-class estimates from genuinely comparable projects can expose such optimism, but only if size, novelty, scope, and reporting rules are normalized.

### Correlation changes the budget tail

For uncertain work-package costs `C_i`, the total variance is `Var(Σ C_i) = Σ Var(C_i) + 2Σ_{i<j} Cov(C_i,C_j)`. If integration and testing are both delayed by the same supplier, their covariance is positive; treating the costs as independent understates the width of the total-cost distribution. If two remediation options are mutually substitutable, their costs might instead be negatively related. The covariance structure must describe actual mechanisms, not be chosen to make a desired reserve look reasonable.

A P50 cost estimate is the median of a modeled distribution; a P80 is a cost not exceeded in 80 percent of outcomes *under that model*. Neither is a guaranteed funding amount, and neither includes unknown unknowns by definition. Distinguish estimate uncertainty from identified risk events, escalation, scope change, and deliberate managerial buffers. Contingency covers uncertainty within approved scope under specified rules, whereas management reserve is controlled separately for unforeseen work or changes according to the program's governance. Hiding one inside productivity factors erases learning about performance.

### Scheduling and cost prediction are coupled

Suppose a specialist team costs $40,000 per month while held on the project. A three-month delivery delay may increase time-related cost by $120,000 even if the original engineering work quantity does not change. Conversely, acceleration may require overtime and reduce productivity, so cost is not simply a linear function of duration. A joint cost-schedule model identifies the causal routes: longer queues, shared scarce resources, retesting after changes, supplier coordination, and contractual escalation. Simulating cost and schedule separately while sharing none of these drivers can produce reassuring but incoherent forecasts.

Calibration is the long-run test of an estimation method. If ten independently comparable P80 forecasts are routinely exceeded, the model, inputs, or interpretation needs revision; one forecast cannot by itself prove calibration. Track the original baseline, what was known at approval, actual outcomes, and categorized causes of deviations. For the fictional shuttle program, the proper product of estimation is not a number advertised as certainty but a controlled decision range, explicit assumptions, identified tail exposures, and a rule for updating the forecast as evidence arrives.

## Worked Northstar project example

A work package requires 1,800 engineer-hours at $140/hour and $90,000 of purchased items. Direct build-up cost is 1,800 × $140 + $90,000 = $342,000. If a supplier delay adds 240 hours, a scenario estimate becomes $375,600 before any additional delay-driven purchases. The $33,600 increase is **not** independently another “10% reserve” if the same risk was already costed in a risk allowance. Two independent estimating methods can disagree; the task is to reconcile scope and assumptions, not average incompatible numbers.

## Why uncertainty cannot be reduced to one reserve percentage

Estimating uncertainty has at least two dimensions: uncertainty *inside* the chosen scope and uncertainty about what the scope actually is. The former may be modeled with ranges on hours and quantities. The latter requires alternative technical scenarios or explicit assumptions. The shuttle program may estimate a dispatch interface at 2,000 hours with a 20% range, but if a new cybersecurity certification is required, adding a small generic allowance is unlikely to capture the discrete new work.

A useful sensitivity analysis changes one assumption at a time to reveal influence; a scenario analysis changes a set of mutually consistent assumptions together. Monte Carlo methods can combine specified distributions, but the resulting probability estimates only describe that model. Correlated failures and common schedule drivers matter: supplier lateness and overtime spending are not necessarily independent. If the same underlying late interface causes both, modeling their costs independently may understate tail outcomes.

**Worked sensitivity.** With 1,800 hours at $140 and $90,000 in purchases, total direct cost is $342,000. If labor rate rises 8%, total becomes 1,800 × $151.20 + $90,000 = $362,160, an increase of $20,160. If instead effort increases by 240 hours with the original rate, total becomes $375,600, an increase of $33,600. If both occur together, 2,040 × $151.20 + $90,000 = $398,448. This combined estimate is not the sum of individual rounded percentages; it must be computed from the underlying drivers.

The proposal price calculation has another boundary. A $0.6M reserve inside an $8.4M offer may protect the plan against certain overruns under a specific contract convention, but its existence does not guarantee that risks are covered. Reserve should have a documented rationale, authority and drawdown mechanism. To test an estimate, ask what technical event would make it obsolete.


## Reproduce and challenge the numbers

Run the [Week 4 calculation notebook](../notebooks/01-price-and-estimate.ipynb) against the [editable dataset](../data/project-budget.csv) in the Markdown source package. Change at least one assumption, recompute the result, and write down which conclusion changes. This exercise checks arithmetic and reasoning within a fictional model; it does not validate the real-world estimate or program.

## Boundary of the method

Quoting a point estimate to three significant figures without a maturity statement creates false precision. Neither a conservative budget nor a low bid proves realism.

## Retrieval questions and explained answers

1. **Question:** What makes a basis of estimate reproducible?
   **Explanation:** Explicit quantities, rates, scope boundaries, assumptions, sources and calculation rules.
2. **Question:** Can management reserve be used to report earned value?
   **Explanation:** Not until authorized through the relevant baseline-change process; it is not automatic earned progress.
3. **Question:** What is the first response to two conflicting estimates?
   **Explanation:** Reconcile scope, maturity, assumptions and method before combining results.

## Put this into practice

Work through [Lab 4: The Estimate Challenge](../labs/lab-04-estimating-and-reserves.md), then write a short paragraph on how the laboratory simplifies the real-world management problem. Use the [existing short Week 4 primer](../../P0-text/lessons/645-667-w04.md) for a second explanation. The assessed deliverable is defined in the original course guide, not by the hypothetical lab.
