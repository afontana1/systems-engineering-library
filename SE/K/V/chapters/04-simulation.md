# 4 · Stochastic simulation as an instrument of inference

*Graduate methods companion · Foundations of Modeling and Simulation (Book XI)*

A computer program that produces plausible numbers is not yet an engineering simulation. The model must have a stated **intended use**, a defensible conceptual abstraction, verified implementation, calibrated inputs, designed experiments, and a disciplined account of uncertainty. This chapter treats simulation as a scientific instrument for comparing operational policies—not as a machine for generating precise-looking predictions.

## 4.1 Begin with a model contract

For the Northstar dispatch case, the intended use is to compare capacity and scheduling policies during an evening peak. Inputs include arrivals, trip durations, geography, vehicle availability, and communication faults. Outputs include served fraction, p90 waiting time *for all requests with a clearly stated censoring policy*, missed service, and resource utilization. The model does not claim to predict passenger behavior under a real emergency. Those omissions define the validity envelope.

A discrete-event simulation (DES) advances from one event to the next rather than stepping uniformly in clock time. State might comprise a priority queue of pending requests, vehicle release times, and the current authorization revision. An event calendar should have explicit tie-breaking rules: simultaneous completion, cancellation, and route-change events can produce different behavior depending on how they are ordered. Deterministic replay with a fixed seed is necessary for debugging but does not make stochastic outcomes scientifically repeatable on its own.

## 4.2 The simplest queue model is a warning label

For an M/M/1 queue with Poisson arrivals rate $\lambda$ and exponential service rate $\mu>\lambda$, utilization is $\rho=\lambda/\mu$. The mean *total* time in the system is

$$W=\frac{1}{\mu-\lambda},$$

and mean time *waiting in queue* is

$$W_q=\frac{\lambda}{\mu(\mu-\lambda)}.$$

With $\lambda=8$ per hour and $\mu=10$ per hour, $W=0.5$ hours (30 minutes), $W_q=0.4$ hours (24 minutes), and mean service time is 6 minutes. As arrival rate approaches service rate, delays increase nonlinearly. Real dispatch services often violate memoryless interarrival and service assumptions, have multiple resource classes, geography, priority queues, rejection, and temporary capacity losses. The formula teaches the mechanism; the simulation must test what happens when those assumptions fail.

## 4.3 Random streams and paired comparisons

If architectures A and B are run on independently generated demand, variance in the comparison includes demand differences. Common random numbers deliberately pair them on the same demand streams. The paired difference $D_i=Y_{Ai}-Y_{Bi}$ can have much lower variance than the difference of two independent averages, especially if demand affects the two outputs in similar ways.

However, pairing can be invalid when a policy changes the meaning of the observation or uses a different number of random draws in a way that destroys intended alignment. Prefer independently specified input streams (demand, weather, travel times, failures) and document the stream mapping. Use one or more held-out seeds for confirmatory results after model tuning.

## 4.4 Initial transients and run length

A simulated queue starting empty is not necessarily representative of stationary operation. For transient questions (such as the first hour after a storm) the initial state is part of the estimand. For long-run steady-state metrics, warm-up deletion may reduce bias, but deleting too much data increases variance and cannot cure structural nonstationarity. Pick run length and replications using convergence evidence, not a round number of simulated days.

Suppose four paired differences in average wait are 5, 9, 7, and 11 minutes. The estimated advantage is 8 minutes with a wide 95% interval $[3.89,12.11]$. A large number of individual requests in each run does not automatically create a large independent sample size: shared congestion and policy effects create within-run dependence. The four independent replications, not the thousands of customer rows, may be the relevant units for output analysis.

## 4.5 Separate verification from validation

**Verification** asks whether the implementation correctly executes the conceptual model: conservation of vehicle capacity, no negative waits, no double allocation, deterministic behavior under a fixed seed, and correct event ordering. **Validation** asks whether the abstraction is fit for its intended comparison: are arrivals representative, route times credible, outage modes complete enough, and sensitivity rankings consistent with operational knowledge?

A verification test can intentionally force arrivals to zero and confirm zero completed trips, or force one vehicle to remain unavailable and confirm that it never serves a trip. A validation exercise may compare aggregate baseline waiting-time distributions with separately gathered pilot observations. Good agreement on a single mean is weak validation; compare distributions, subgroup behavior, transient periods, extreme conditions, and mechanisms.

Calibration must not be confused with validation. If the same dataset is used to tune service rates and demonstrate accuracy, the apparent agreement is partly engineered. Hold out data or use independent tests. Report which parameters are identifiable: different combinations of demand and service heterogeneity may reproduce the same average wait.

## 4.6 Credibility under changes of configuration

Simulation evidence is configuration-dependent. When the fleet, routing policy, or geographic service envelope changes, the claim supported by a prior simulation may no longer hold. Record source hashes, inputs, seed sets, code version, scenario envelope, and analysis notebook. A result file without a provenance chain can be correct numerically yet unusable for a formal design decision.

Use sensitivity and uncertainty analysis differently. **Parameter uncertainty** describes imperfect knowledge within the model; **model-form uncertainty** concerns missing or incorrect mechanisms. Running more Monte Carlo replications reduces statistical error, but it cannot fix a biased arrival process or missing outage mechanism. The credibility argument must include both.

## Worked problems with explained solutions

**A.** Compute $\rho$, $W$, and $W_q$ for $\lambda=8$, $\mu=10$ per hour. **Solution:** $\rho=0.8$, $W=30$ minutes, $W_q=24$ minutes.

**B.** Why does 100,000 customer observations across four simulation runs not necessarily justify treating $n=100,000$ as an independent sample? **Solution:** Customers share stochastic system states and common run-level disturbances. Use independent replications or model within-run dependence.

**C.** Can a 10,000-replication Monte Carlo experiment prove the model's geographic travel times are accurate? **Solution:** No. It reduces numerical sampling uncertainty for the specified model; external validation of travel-time mechanisms is a separate task.

**D.** The new controller rejects some requests; should the reported wait exclude them? **Solution:** Only if the estimand is explicitly conditional on completed requests, and the decision report also provides rejection and service-coverage outcomes.

## Independent research question

Construct a conceptual model review checklist covering entities, events, resources, random variables, correlation, warm-up, verification oracles, validation data, and configuration provenance. Explain which omissions could reverse a policy comparison.

**Practice:** [Simulation credibility laboratory](../labs/04-simulation.html) · [Notebook](../notebooks/04-simulation.ipynb).

## 4.7 Model-form uncertainty and structural alternatives

There may be no single correct modeling abstraction. A queue model with exponential service times, a geographic agent-based model, and an empirical event-replay model may all reproduce a baseline mean while predicting different failure behavior during a storm. Comparing multiple plausible model forms is useful precisely because it exposes assumptions that cannot be resolved by increasing random replications.

When alternative models disagree, do not average them without considering why. Ask which mechanisms matter for the intended decision, whether any model has external validation data in the stressed regime, and whether the disagreement can be reduced by targeted observations. A decision that is stable across plausible model forms is more defensible than one requiring a single conveniently favorable abstraction.

## 4.8 Output analysis beyond a single mean

Means can hide operationally important tails. Report percentiles, missed requests, peak queues, subgroup outcomes, and conditional results for failure states. Estimated percentiles themselves have uncertainty; bootstrap methods can help under suitable resampling assumptions, while a small number of independent simulation runs may require run-level rather than transaction-level resampling. Common random numbers should be preserved when bootstrapping paired differences.

Rare-event simulation may require importance sampling or splitting to obtain enough adverse cases efficiently. But any biased sampling scheme must carry an explicit reweighting or estimation method; otherwise its observed event fraction is not an estimate of the original event probability. Students should be able to explain not only how many runs they completed but why those runs give credible information about the intended decision.

<!-- STEP04-CONNECTED-EVIDENCE-START -->
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
<!-- STEP04-CONNECTED-EVIDENCE-END -->
