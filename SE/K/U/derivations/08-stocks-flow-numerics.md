# D08 · Stock-flow models and numerical integration error

**Skill:** Move from a causal diagram to an equation, then distinguish a numerical approximation from the modeled dynamics.

## Stock conservation

Let `B(t)` be unfinished work orders. Its continuous model is `dB/dt = arrivals(t)−closures(t)` with units of jobs/day. If arrivals are 18/day and closures 15/day, then `dB/dt=3/day`. Starting with 100 jobs, constant rates give `B(5)=100+3×5=115` jobs.

For a feedback closure rate, consider `dB/dt = −k B` with `k=0.4/day` (a simplified depletion model and no arrivals). Separation yields `dB/B = −k dt`. Integrating gives `ln B = −kt + constant`, hence `B(t)=B0 exp(−kt)`. Starting at 100, the exact value after one day is `100e^(−0.4)≈67.032`.

## Forward Euler and convergence

The explicit Euler approximation is `B_(n+1)=B_n + h f(B_n)`, here `B_(n+1)=B_n(1−0.4h)`. With one step of size 1 day, Euler returns 60. With two steps of 0.5 day it returns `100×0.8²=64`. With four steps of 0.25 day it returns `100×0.9⁴=65.61`. The approximations approach the exact 67.032 as step size shrinks.

For this simple decay model, an explicit Euler step becomes negative if `h>1/k=2.5 days`, which is physically nonsensical for a nonnegative backlog. This is a numerical artifact, not a prediction that backlog becomes negative. Use step-size sensitivity, positivity constraints or a better solver.

## Feedback and time delays

In a real process, staffing responds to measured backlog after a delay. A strong delayed response can create oscillation even when the undelayed control is balancing. Specify what is delayed: observation, staffing approval or actual throughput; those mechanisms produce different dynamics.

Parameter uncertainty is different from discretization error. Running smaller steps cannot fix an incorrect closure-rate function or an omitted backlog-generation mechanism.

## Practice

**Question:** If Euler at 1-day steps gives 60 and at 0.25-day steps gives 65.61, can we claim the real backlog will be 67.032?

<details><summary>Solution</summary>

No. The convergence comparison addresses a numerical approximation to the chosen differential equation. Whether the equation captures actual arrivals, closures and feedback must be established separately through data and model validation.

</details>

**Transfer artifact:** Stock units, flow equations, source of each rate, conservation checks, step-size study and comparison to held-out time series. See [stocks, flows and feedback](../../encyclopedia/stocks-flows-feedback.md).
