## Integrated case NS-G4.1 — Human workload and alarm interpretation

> **NS-G4.1 case convention.** Every number in this extension comes from a controlled, fictional emergency-dispatch dataset, unless explicitly identified as an illustrative assumption. A Python screening result is not an operational safety finding, a validated queue model, or an authorization from independently managed agencies. The case is shared with the other five advanced-studies chapters; use the same `revision: 1.0` throughout.

**Reproduce:** [controlled JSON](../data/ns-g4.1-case.json) · [Python model](../code/ns_advanced_case.py) · [computed results](../outputs/ns-g4.1-results.json) · [integrated laboratory](../labs/INTEGRATED-CASE.html).

### G1. Derive operator delay from a stated queue model

A dispatcher must triage alarms before a mobility action is committed. For the *illustrative stationary M/M/1* model, arrivals are Poisson at rate \(\lambda\) alarms/hour, service times are independent exponential at rate \(\mu\) alarms/hour, FIFO service is assumed, and \(\rho=\lambda/\mu<1\). Under those assumptions, the mean number awaiting service is \(L_q=\rho^2/(1-\rho)\). Little's law, \(L_q=\lambda W_q\), gives

\[
W_q=\frac{\lambda}{\mu(\mu-\lambda)}\quad\mathrm{hours};
\qquad W_q(\mathrm{min})=60\frac{\lambda}{\mu(\mu-\lambda)}.
\]

**Worked example.** With \(\lambda=8.4\) and baseline \(\mu=9.6\) per hour, utilization is \(0.875\) and \(W_q=43.75\) minutes. A process change raising \(\mu\) to 12.2 gives \(\rho\approx0.6885\), \(W_q=10.87\) minutes. The ratio is dramatic because waiting time diverges as \(\lambda\to\mu^-\); it is not evidence that actual dispatchers behave exponentially. Under a 17% demand surge, arrival rises to \(9.828\)/hour and the *improved* model predicts \(20.38\) minutes, failing the 15-minute illustrative screen. At \(\lambda\ge\mu\), the stationary mean is undefined; the simulator returns `null`, not a fabricated zero.

### G2. Alarm positive predictive value is not the detection rate

False alarms can increase attentional load and erode trust. Let \(P(H)=0.03\) denote the assumed fraction of true hazards, sensitivity \(P(+\mid H)=0.90\), and false-alarm probability \(P(+\mid\neg H)=f\). Bayes' rule gives

\[
P(H\mid +)=\frac{0.90(0.03)}{0.90(0.03)+f(0.97)}.
\]

At \(f=0.10\), the positive predictive value is **21.77%** despite 90% sensitivity. Reducing \(f\) to 0.04 yields **41.03%**, above the exercise's 35% screen. The computation assumes stable prevalence and conditional detection rates across the operating environment; correlated alarms, shifting weather, and operator responses can change all three inputs. Improving the displayed PPV is not, by itself, proof of safe attention allocation.

### G3. Mixed-initiative work is a control problem

Assign each action to an actor: route authority may close a corridor; automation can recommend a route; a trained operator can request a bounded override; only an authorized body may permit degraded operations. A good interface displays evidence time, revision, destination, expiry, and what an override actually changes. Test adversarial sequences: contradictory visual and audible alerts; ACK without displayed consequence; a transition from automated to manual mode with stale routes; and alarms occurring while a dispatcher is already occupied.

A system optimized solely for average handling time may penalize operators who pause for accessible service checks. Track abandoned and unacknowledged cases, response-time distribution (not just mean), operator workload, accessibility-specific outcomes, and retrospective incident analysis. For human-participant experiments, specify consent, training effects, counterbalancing, and a valid way to capture task errors without exposing sensitive information. The simple queue has no fatigue, task-switching, or team-coordination mechanism.

### Worked exercise with explained solution

**Problem.** Suppose \(\lambda=10.0\)/hour while \(\mu=12.2\)/hour. Compute \(W_q\), and decide whether reducing the false-positive alarm rate changes this queue result *within the current model*.

**Solution.** \(W_q=60(10)/(12.2\cdot2.2)\approx22.35\) min, exceeding the 15-minute screen. PPV may improve if false-alarm rate falls, but this simplified model holds the arrival rate fixed. To claim false-alarm filtering reduces \(\lambda\), first specify the mixture of true and false alarm arrivals, recalculate demand, and account for missed hazards. Do not double-count the benefit by changing both \(\lambda\) and PPV without a justified causal mechanism.
