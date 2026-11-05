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
