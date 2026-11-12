## Step 04 integrated case — NS-CE4.1: queuing assumptions and paired comparison

The linked case uses two deliberately different forms of evidence: an analytic stationary queue formula for a **single nominal operating regime**, and a six-scenario paired comparison. Their numerical conclusions cannot be substituted for one another. Stationary queue models are useful precisely because they reveal when a proposed inference is invalid.

### Begin with stability, not a predicted mean

Assume a single-server M/M/1 approximation with Poisson request arrivals at $\lambda=8$ requests/hour and exponential service at $\mu=10$ requests/hour. Stationarity requires $0\le\lambda<\mu$. Utilization is $\rho=\lambda/\mu=0.8$. The mean *total time in the system* is

$$E[T]=\frac{1}{\mu-\lambda}=\frac{1}{2}\ \text{hour}=30\ \text{min},$$

and the mean *waiting time before service* is $E[W_q]=\lambda/[\mu(\mu-\lambda)]=0.4$ hour = 24 minutes. That distinction matters: a 30-minute total does not mean a 30-minute dispatch wait. Under a storm demand assumption $\lambda_s=11$ requests/hour while service remains 10/hour, $\rho_s=1.1$ and no finite stationary M/M/1 mean exists. It is wrong to extrapolate $1/(10-11)$ to obtain 'negative 60 minutes.' A finite-horizon simulation can still report transient queues, but it must state its horizon, initial conditions, unserved backlog, and ending-state rules.

### Paired scenario comparisons and uncertainty

The illustrative six-scenario baseline waits are $[19,21,16,23,25,18]$ minutes, and treatment waits are $[16,17,15,21,18,18]$ minutes. Pair by the **same scenario**, not by two independently reshuffled lists. The baseline-minus-treatment differences are $d=[3,4,1,2,7,0]$ minutes, giving

$$\overline d=\frac{17}{6}=2.8333\ \text{min},\quad s_d=\sqrt{\frac{\sum(d_i-\overline d)^2}{5}}=2.4833\ \text{min}.$$

Using the stated two-sided Student $t$ critical value 2.571 with five degrees of freedom, the *illustrative* 95% interval is

$$\overline d\pm 2.571\frac{s_d}{\sqrt 6}\approx[0.227,5.440]\ \text{min}.$$

This interval formula requires independent, approximately normal paired differences across the sampled scenario-generating process. The six numbers here were invented for teaching, so **the nominal 95% coverage property is not a real-world empirical confidence claim**. The positive sample mean is a model comparison conditional on the generated scenarios. It does not show that storms have been sampled representatively, nor that safety and equity obligations are met.

### Verification, validation, and credibility cannot be collapsed

**Numerical verification:** evaluate the queue formula at the stable nominal parameters, confirm conserved request counts, and reject unstable stationary inputs. **Conceptual validation:** establish that a single server approximates the real dispatch process. **Operational validation:** compare calibrated demand and observed service distributions with independent data in the intended deployment envelope. **Credibility decision:** independently judge whether the evidence is sufficient for the decision at hand. These are four separate activities.

Common random numbers can reduce the variance of paired differences when comparing policies, but an over-correlated or nonrepresentative scenario set can produce a narrow interval around the wrong estimand. The sample unit is the independently generated scenario replication, not each event within the same shared random seed. Near saturation, queue output is nonlinear in capacity: $dE[T]/d\lambda=(\mu-\lambda)^{-2}$ hours squared per request, so small rate errors may create large time errors.

### Reproduction and worked exercises

The case checker outputs both queue quantities and the paired interval. Test at least three regimes: stable nominal ($8<10$), near saturation (e.g., $9.9<10$), and unstable storm ($11>10$). Define the simulation termination and backlog handling before comparing policy means.

**Worked exercise 1 — near saturation.** Evaluate mean total time for $\lambda=9.5,\mu=10$ per hour. **Solution:** $1/(10-9.5)=2$ hours = 120 minutes. This is four times the 30-minute nominal mean for a 19% higher arrival rate.

**Worked exercise 2 — paired data.** Replace a treatment wait of 18 with 16 in the sixth scenario. What happens to the paired mean reduction? **Solution:** The sixth difference changes from 0 to 2; the sum increases from 17 to 19, so the mean becomes $19/6\approx3.167$ minutes. Recalculate the standard deviation and interval; do not copy the original interval.

**Adverse case.** Deliberately set nominal arrivals equal to nominal service rate. The analytic checker must reject that assumption rather than divide by zero. A full discrete-event model requires event-queue validation, independent seed handling, warm-up diagnostics, and independent physical-system evidence before it informs a procurement decision.
