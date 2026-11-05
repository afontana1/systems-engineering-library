# Workshop 7 · Factorial interactions can reverse engineering conclusions

*Companion to Book X, Chapter 6 · Factorial experiments and confirmation evidence*

## Why one-factor-at-a-time testing misses the point

Northstar evaluates a scheduling algorithm under two temperatures: cold and warm. The response is p90 completed-trip wait, where lower is better. A software optimization may help in both environments, but the **size of its effect** can differ. An experiment that runs only the warm environment cannot support the claim that the improvement transfers unchanged to cold operation.

A balanced \(2\times2\) factorial design compares all combinations of temperature and algorithm. Each combination has three independent synthetic replications. The provided dataset yields mean waits of 24 min (cold/base), 18 (cold/optimized), 16 (warm/base) and 14 (warm/optimized). The optimization effect is \(-6\) min in cold conditions and \(-2\) min in warm conditions. The **difference in differences** is

\[
I=(14-16)-(18-24)=(-2)-(-6)=4\ \text{minutes}.
\]

A nonzero interaction means the effect of one factor depends on the other. The 4-minute interaction here does **not** mean the optimized design is four minutes slower. It means the optimization benefit is four minutes smaller in warm conditions than in cold conditions.

## Estimating noise and uncertainty

The three replications in every cell are centered at the cell mean with residuals \(-1,0,+1\) min. Under an independent homoskedastic normal-error model, each cell's sample variance is 1 min\(^2\), and the pooled within-cell mean square error is \(MSE=1\) with \(4(3-1)=8\) residual degrees of freedom. The standard error of the difference of four cell means is

\[
SE(I)=\sqrt{MSE\left(\frac13+\frac13+\frac13+\frac13\right)}=\sqrt{\frac43}\approx1.155.
\]

With a two-sided 95% Student-\(t\) multiplier \(t_{0.975,8}\approx2.306\), the approximate interval is \(4\pm2.663\), or **[1.34, 6.66] minutes**. These inference assumptions are stronger than simply calculating the four sample means; the experiment needs randomized order, independent replications, stable instrumentation and evidence that the residual model is reasonable. This tiny teaching dataset is deliberately stylized and should not be used for operational decisions.

## The engineering interpretation

The experiment suggests the optimization provides a larger benefit under cold conditions. Does it imply the optimized design is preferable? Not without assessing reliability, dropped requests, resource use, safety and operational demands. And the p90 statistic from only a few runs may be noisy or biased if runs have different demand mixes. Experiment validity requires that the response be defined consistently and that the factor manipulation not change the eligible request population.

## Worked problems

**Problem 1.** Compute the algorithm effect at warm temperature.

<details><summary>Worked solution 1</summary>

Warm optimized mean 14 less warm baseline mean 16 equals \(-2\) min. State that a negative difference is a wait reduction.
</details>

**Problem 2.** Compute the interaction by subtracting cold optimization benefit from warm benefit.

<details><summary>Worked solution 2</summary>

\((-2)-(-6)=4\) min, showing a four-minute *difference in the effects*, not a four-minute response itself.
</details>

**Problem 3.** Why is it invalid to treat the 12 request-level waits inside one simulation run as 12 independent replications?

<details><summary>Worked solution 3</summary>

Requests share the same demand stream, resources and simulated faults. The independently randomized **run** is the experimental unit, not an individual request nested inside it. Treating nested observations as independent inflates precision (pseudoreplication).
</details>

**Problem 4.** What does the confidence interval exclude under the stated model, and what does it not establish?

<details><summary>Worked solution 4</summary>

The interval excludes a zero interaction under the specified independent normal-error model. It does not prove practical acceptability, external validity, robust behavior in other temperatures, or safety.
</details>

## Transfer to engineering work

Load the factorial CSV, verify the four means, fit a four-cell model and report the interaction with its assumptions. Design a new randomized confirmation experiment in which demand scenarios are paired across algorithms. Compare the interaction estimate before and after adding an additional environmental factor; explain how the design would have to change.
