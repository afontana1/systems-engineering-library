## Step 04 integrated case — NS-QSE4.1: verify a finite-horizon dispatch queue

The integrated queue is not an M/M/1 model. It represents a **finite one-hour intake window** in which request arrival times are sampled uniformly over the hour; each request is assigned to the first available of \(c\) parallel servers, which takes a constant \(s\) minutes per request. The simulation intentionally removes route geometry, passenger grouping, labor breaks, priority discipline, failed vehicles, and time-varying dispatch rules. It is useful for queue-mechanics education and for identifying assumptions to test next, not for credible regional fleet sizing.

### Event-calendar recurrence and conservation

Let the ordered arrivals be \(a_1\le\dots\le a_n\). Maintain each server's next available time \(f_j\), initialized to zero. For request \(i\), choose \(j^*=\arg\min_j(f_j,j)\) with a deterministic tie break; service begins at \(b_i=\max(a_i,f_{j^*})\), waiting is \(w_i=b_i-a_i\ge0\), and finish is \(f_{j^*}\gets b_i+s\). This yields two mandatory invariants: \(0\le a_i\le b_i\le f_i\) for every request, and

\[
N_{\mathrm{arrived}}=N_{\mathrm{finished\ by\ 60}}+N_{\mathrm{finished\ after\ 60}}.
\]

Every request in this simplified model finishes eventually; overtime is counted, not treated as disappearance or abandonment. The code rejects unsorted arrivals, invalid server counts, negative demand and nonfinite numbers. `ns-qse4-policy-days.csv` contains all daily results for four policies and three conditions.

### Controlled outcomes and comparison with queueing benchmarks

For the twelve storm windows, request-weighted average waiting time is approximately **17.98 minutes** for two servers at 10 minutes each, and **2.52 minutes** for three servers at 8 minutes each. The timely fraction, defined as the fraction whose wait is at most 12 minutes, increases from approximately **42.59%** to **98.15%**. But in compound demand plus slower travel, even the combined policy reaches only **82.95%** timely service, below the illustrative 90% minimum. It also finishes approximately **26.89%** of requests after the intake hour. Thus its nominal benefit does not pass the combined stress screen.

An M/M/1 stationarity result is an independent **analytic benchmark**: \(W=1/(\mu-\lambda)\), where arrivals and service are exponential, one server operates steadily, and \(\lambda<\mu\). You must not insert the multi-server deterministic 60-minute simulation parameters into that formula and present the result as validation. What can be checked are basic limits: no arrivals implies zero wait; adding a truly idle server cannot worsen any FCFS job's wait under the identical arrival stream and common deterministic service duration; reducing service time should not increase waits under the stated assignment rule.

### Replication, warm-up, and uncertainty

The finite intake-hour experiment is a **transient study**; clearing the queue between days is part of its model definition. A real dispatcher operating through multiple shifts may inherit backlog and nonempty server states. Clearing it at each hour could be dangerously optimistic. For a steady-state queue, warm-up handling and long-run batch means are appropriate, but merely deleting warm-up observations without checking stationarity creates another bias. Replicate *entire coherent shifts or days*, not correlated requests, when constructing confidence intervals for policy differences.

<details><summary>Worked exercises and interpretation</summary>

1. **Tiny event trace.** Two servers, three arrivals at [0, 1, 2] minutes and fixed five-minute service. Service starts at [0, 1, 5]; waits are [0, 0, 3]; finishes are [5, 6, 10]. All three requests complete, so conservation holds.
2. **Deadline.** If only completions by minute 60 count, is the combined policy's compound timely fraction a measure of completed-by-deadline success? No. `timely_fraction` refers to *wait before pickup*; overtime completions are counted separately. Conflating the metrics could approve an unsuitable design.
3. **Invalid model.** Supply decreasing arrival times. The checker must reject them; sorting silently would conceal a bad upstream event log and weaken traceability.

</details>

**Transfer:** Book 11's broader mobility simulator and Book 18's interdependent constituents need additional mechanisms before any quantitative prediction is considered operationally credible.
