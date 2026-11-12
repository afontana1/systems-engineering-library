
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
