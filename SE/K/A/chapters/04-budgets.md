# 4. Interfaces and engineering budgets under uncertainty

*Graduate-depth architecture sequence · Part IV · Timing, capacity, energy and reliability*

**Prerequisites.** Previous chapters, queueing fundamentals, basic probability and dimensional analysis. **Use with:** System Conceptual Design, System Design and Integration, Software Systems Engineering, Metrics and Simulation.

## 4.1 Architecture is a set of interdependent constraints

A system is not feasible merely because each component meets its own specifications. A dispatcher may respond in under two seconds on a test machine while the whole dispatch-to-pickup process misses its service requirement. A vehicle may have enough average battery capacity while failing a storm-route energy requirement. Two individually reliable communications links may depend on one fiber connection. An engineering **budget** converts an emergent system obligation into coordinated allocations and reserves across interfaces.

Budgets are useful when effects can be composed, but the mathematical composition must match the physical mechanism. Sequential processing delays often add; independent parallel failures combine differently; serial reliability multiplies only under appropriate conditions; energy obeys conservation and sign conventions. Treating all of these as weighted scores creates plausible-looking but physically meaningless architecture studies.

## 4.2 Sequential timing and resource allocation

For a sequence of operations with durations $T_i$, the end-to-end time is

\[
T_{\mathrm{end}}=\sum_{i=1}^nT_i+T_{\mathrm{queue}}+T_{\mathrm{propagation}},
\]

where overlapping tasks need a different network/scheduling model. Suppose message receipt takes 0.8 s, validation 0.5 s, route calculation 2.0 s, approval 1.2 s, and vehicle dispatch acknowledgement 1.0 s. The serial component budget is 5.5 s before additional queueing. Under a 7 s system limit, the nominal unallocated margin is 1.5 s. The margin is **not free capacity** if queueing can exceed it during bursts.

For independent random delays, the mean of a sum equals the sum of means regardless of independence, while variance is

\[
\operatorname{Var}\left(\sum_iT_i\right)=\sum_i\operatorname{Var}(T_i)+2\sum_{i\lt j}\operatorname{Cov}(T_i,T_j).
\]

The covariance terms matter when network congestion simultaneously delays multiple steps. A design that uses root-sum-square standard deviations without discussing shared causes can understate tail latency. Additionally, a 95th-percentile component budget generally does not sum into a 95th-percentile system budget. Percentiles are nonlinear; either derive conservative bounds or estimate end-to-end tails from an explicit joint distribution.

## 4.3 Queueing can destroy an otherwise correct budget

For a stable M/M/1 queue with Poisson arrivals of rate $\lambda$ and exponential service rate $\mu$, the expected total time in the system is $W=1/(\mu-\lambda)$ and utilization is $\rho=\lambda/\mu$. With $\lambda=8$ requests/hour and $\mu=10$/hour, utilization is 0.8 and $W=0.5$ hour. If demand rises to 9/hour with the same service rate, the expected time doubles to one hour. That nonlinear response can dominate millisecond improvements in local software processing.

These results assume a single server, stable flow, steady state, independent arrivals and exponential service. A multi-vehicle dispatch process is usually not an M/M/1 system, and its service-time distribution depends on geography and routing. Use the analytic model to understand load sensitivity and to check simulation plausibility, not to certify a fleet. A simulation should record all arrivals, cancellations, rejects and completions, use multiple replications, and distinguish queue waiting from travel waiting.

## 4.4 Energy feasibility and reserve policies

Let $d$ be route distance (km), $e$ energy per kilometer (kWh/km), $h$ fixed overhead (kWh), $r$ required reserve (kWh), and $B$ usable battery energy (kWh). Feasibility requires $B-ed-h-r\ge0$. With $B=24$, $d=24$, $e=0.62$, $h=1.8$, and $r=4.0$, the margin is $24-20.68=3.32$ kWh. Under adverse energy intensity $e=0.75$, the margin falls to $24-(18+1.8+4)=0.2$ kWh. An even higher route demand or degraded battery capacity makes the design infeasible.

For uncertain $d$ and $e$, $E[de]=E[d]E[e]+\operatorname{Cov}(d,e)$. If longer routes tend to occur under energy-intensive weather, replacing $E[de]$ by $E[d]E[e]$ is optimistic. For a robust guarantee, define a credible operating envelope $\mathcal U$ and require

\[
\min_{(d,e)\in\mathcal U}\bigl(B-de-h-r\bigr)\ge0.
\]

A worst-case rule over a physically impossible uncertainty set can be excessively conservative; a chance constraint $P(B-de-h-r\ge0)\ge1-\alpha$ is less conservative but demands a defensible joint probability model. Hard safety reserve may still need worst-case or prescribed regulatory treatment.

## 4.5 Reliability allocations and common cause

For $n$ independent series components with reliability $R_i(t)$ over a specified mission interval, total series reliability is $\prod_iR_i(t)$. Two parallel independent channels each with reliability 0.95 yield $1-(0.05)^2=0.9975$. But if there is a shared-cause failure that disables both with probability $q=0.03$ and the remaining independent channel failure probability is 0.05 conditional on no shared cause, then success is

\[
R=(1-q)(1-0.05^2)=0.97(0.9975)=0.967575.
\]

The 0.03 shared-cause event dominates the nominal benefit of redundancy. This formula is a **particular conditional model**: it assumes the shared event and independent residual channel failures have the stated conditional structure. Other mechanisms need different fault trees, event trees or probabilistic graphical models. Reliability over a mission interval is not the same quantity as long-run availability; repair-time and maintenance assumptions matter for availability.

## 4.6 Trade spaces: hard constraints before preferences

Suppose Architecture A costs 80 budget units, has route coverage 0.95, and fails the adverse energy reserve by 1 kWh. Architecture B costs 90, coverage 0.93, and has 2 kWh adverse energy margin. Under a **hard** reserve constraint, A is infeasible even if a weighted utility function ranks it higher. The correct decision sequence is: establish non-compensable constraints, identify feasible options, compare feasible options against stakeholder preferences, test sensitivity, and document residual risks. A lower numerical cost does not compensate for violating a mandatory safety or operational constraint.

A useful decision visualization is a Pareto frontier: an architecture is dominated if another option is at least as good on every compared objective and strictly better on one. Pareto analysis does not select a preferred point by itself. Stakeholder value, risk acceptance and organizational constraints determine the final selection. If probabilities are used, report which assumptions are tested and which are only elicited judgments.

## 4.7 Interface contracts and failure containment

A complete interface agreement states semantic content, units, reference frames, allowed values, timing, freshness, failure signaling, version compatibility, security trust boundaries and responsibility for degraded behavior. For road status, `OPEN` without timestamp or authority identity is an unsafe ambiguity; for vehicle location, coordinates without map datum can be useless; for assignment, an acknowledgement without an idempotency token can produce duplicate actions.

A useful architecture review deliberately breaks one contract at a time. Delay telemetry, corrupt a unit, change schema version, lose an acknowledgement, and inject a shared infrastructure outage. Observe whether the design fails closed, retries safely, degrades predictably, or silently corrupts a decision. This converts architecture diagrams into falsifiable engineering hypotheses.

## Problems — attempt before opening solutions

1. Five sequential activities take 0.8, 0.5, 2.0, 1.2, and 1.0 seconds. Compute total and margin against 7 seconds. Explain why this is not a tail-latency guarantee.
2. With $B=22$ kWh, $d=25$ km, $e=0.7$ kWh/km, $h=1.8$ and $r=4$, compute margin. Identify whether the design is feasible.
3. Two independent parallel channels each have success 0.95, but both are disabled by a shared event of probability 0.03. Compute system reliability under the conditional model above.
4. Explain why $Q_{0.95}(T_1)+Q_{0.95}(T_2)$ is generally not the 95th percentile of $T_1+T_2$.

<details><summary>Worked solutions</summary>

1. Total 5.5 s, margin 1.5 s. Queueing and covariance across operations may cause end-to-end tail delays greater than nominal margin.
2. Required energy $=25(0.7)+1.8+4=23.3$ kWh, so margin is $-1.3$ kWh and the specified route is infeasible.
3. $(1-0.03)[1-(1-0.95)^2]=0.967575$. The independence-only answer 0.9975 is inappropriate when common cause exists.
4. Percentiles are not additive. The distribution of a sum depends on the joint distribution, including dependence; compute or bound the appropriate quantile directly.
</details>

## Applied laboratory

[Interface and budget challenge](../labs/04-budgets.html) · [Python budget tools](../code/model_checks.py) · [Sequence index](../INDEX.html).

**References:** NASA Systems Engineering Handbook for technical budgets and interfaces; NIST SP 800-160 Volume 1 Rev. 1 for security within systems engineering. All performance numbers here are synthetic.

<!-- STEP04-ARCHITECTURE-START -->
---

## Step 04 advanced integration — composing margins without hiding dependencies (NS-AA4.1)

### A1. Derive the end-to-end timing margin

For a sequential decision path of \(k\) stages, let \(d_j\) be nominal duration and \(u_j\ge0\) a deterministic upper deviation for stage \(j\). Under the assumption that the listed stages cover the entire serial critical path, an upper bound is

\[
T_{max}=\sum_{j=1}^{k}(d_j+u_j)+d_{common},\qquad M=T_{limit}-T_{max}.
\]

The [controlled budget](../data/advanced-case.json) uses nominal times \(0.8,0.5,2.0,1.2,1.0\) seconds and respective upper deviations \(0.2,0.2,0.5,0.2,0.1\) seconds. Nominal total \(=5.5\) seconds; summed deviations \(=1.2\) seconds; with no omitted common delay, \(T_{max}=6.7\) seconds. Against a 7-second limit, margin is only **0.3 seconds**. An unmodeled shared communication pause of one second would increase the bound to 7.7 seconds and violate the timing requirement by 0.7 seconds.

Adding every deviation is conservative but valid if each upper bound is genuinely guaranteed and the full critical path is captured. It is **not** a percentile calculation. Replacing worst-case sums with a root-sum-of-squares formula requires a probabilistic error model; correlated stalls invalidate a naive independence assumption. In particular, nominal latency passing says nothing about the delay tail unless the proposed tail bound has evidence.

### A2. Derive two-channel reliability with common cause

Let each redundant channel succeed with conditional probability \(r\), independently *given the absence of* a common-cause shutdown. Let a shared shutdown occur with probability \(q\) and disable both channels. Then

\[
P(\mathrm{success})=P(\neg C)P(\mathrm{channel1}\lor\mathrm{channel2}\mid\neg C)
=(1-q)[1-(1-r)^2].
\]

For the invented inputs \(r=0.95\) and \(q=0.03\), this is \(0.97\times0.9975=0.967575\), **below the 0.97 screening requirement**, despite each independent channel being reasonably reliable. The largest allowable common-cause probability under the same conditional model is

\[
q_{max}=1-\frac{0.97}{1-(1-0.95)^2}\approx0.0275689.
\]

Reducing the hypothetical shared-cause probability from 0.03 to 0.02 yields \(0.98\times0.9975=0.97755\). Neither number is a measured hazard frequency; real causes may violate conditional independence or have severity dependent on context. Do **not** add reliability margins to energy margins as though they were commensurate quantities.

### A3. Energy and multi-constraint design

For a vehicle energy screen, let \(B\) be available battery energy, \(d\) route distance, \(e\) specific energy, \(h\) overhead, and \(r_E\) reserve, all with consistent units:

\[M_E=B-de-h-r_E.\]

Using the original architecture teaching baseline \(B=24\) kWh, \(d=24\) km, \(e=0.62\) kWh/km, \(h=1.8\) kWh and \(r_E=4\) kWh, margin is \(24-14.88-1.8-4=3.32\) kWh. The break-even intensity is \((24-1.8-4)/24=0.758333\) kWh/km. At \(e=0.77\), margin becomes \(-0.28\) kWh. Even if the energy requirement passes, the dispatch design still fails the independent shared-cause reliability screen.

**Exercise.** Recalculate timing with \(d_{common}=0.5\) seconds and reliability with \(q=0.025\). **Worked solution:** total upper timing \(=7.2\) seconds, so \(M=-0.2\) seconds (fail). Reliability \(=0.975(0.9975)=0.9725625\) (nominally pass). A favorable reliability result cannot compensate for the timing failure unless requirements have been explicitly renegotiated—and no safety constraint should be converted into a discretionary weighted benefit.

**Reproduce:** [Python margin functions](../code/advanced_case.py). Continue to [configured evidence and defeaters](05-assurance.html).
<!-- STEP04-ARCHITECTURE-END -->
