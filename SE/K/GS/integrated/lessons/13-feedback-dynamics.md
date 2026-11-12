## NS-GS4.1 extension — delay changes the feedback stability boundary

Policies that allocate more dispatch and evidence-review capacity in response to a growing backlog are feedback controllers, even if the enterprise calls them governance interventions. Consider a local deviation \(x_t\) from a desired backlog, measured once per review interval. The model isolates delay effects so that stability can be derived rather than assumed.

### Two characteristic equations

With an instantaneous response \(x_{t+1}=(1-g)x_t\), convergence requires \(|1-g|<1\), i.e. \(0<g<2\). But when the action is based on the **previous** review's backlog, \(x_{t+1}=x_t-gx_{t-1}\). Seeking solutions \(x_t=r^t\) yields \(r^2-r+g=0\). The discrete second-order stability test gives \(0<g<1\). A gain of 1.2, which would be valid in the no-delay simplification, is **unstable** under this one-period delay.

### Reproducible Northstar example

Start with \(x_{-1}=10\), \(x_0=10\). With \(g=0.7\), the next three deviations are 3, −4, and −6.1; the oscillations subsequently decay, ending at approximately 0.542 by the twelfth modeled update. With \(g=1.2\), the trajectory begins −2, −14, −11.6, and 5.2, reaches a magnitude above 33 over the same horizon and does not settle. These are signed **deviations**, not negative counts of passengers. Production backlog and staff capacity would require nonnegative saturation, fatigue, integer resources and nonstationary demand.

### Limits and policy interpretation

The linearized model explains local behavior around a steady operating point; it does not justify indefinitely extending signed quantities into a physical queue. A review board should identify latency, controller saturation and rework before prescribing “stronger escalation.” A good empirical test compares the arrival process and evidence-backed completions under the same units and time window. Do not claim a controller is stable from a short favorable trajectory alone.

### Worked exercise and explained solution

**Problem.** Assess delayed gains 0.9 and 1.05 without simulation.

**Solution.** For the characteristic \(r^2-r+g\), \(0<g<1\) is required, so 0.9 satisfies the local stability criterion while 1.05 does not. At gain 0.9 the complex-root modulus is \(\sqrt{0.9}\approx0.949\), which implies slow oscillatory decay. With 1.05 its modulus is \(\sqrt{1.05}\approx1.025\), indicating amplification. This is a **local** prediction only. Repeat the exercise in the [integrated lab](../integrated/labs/INTEGRATED-CASE.html) with a realistic capacity cap.

**Canonical overlap.** This chapter complements [dynamics-and-resilience](../../U/flagships/F04-dynamics-and-resilience.html) by testing one-period organizational delay explicitly.

**Reproducibility record.** Re-run the [controlled executable model](../integrated/code/ns_gs_case.py) using the [shared case data](../integrated/data/ns-gs4.1-case.json), then compare with the [computed evidence record](../integrated/outputs/ns-gs4.1-results.json). The numerical outputs do not establish field validation or an authorized operating decision.
