### F04 extension · Backlog conservation and numerical stability

**A dynamic mechanism.** NS-U4.1's six service windows model separate standard and accessible queues. For group $g$ and window $t$, let $B_{g,t}$ be unfinished requests, $A_{g,t}$ be new arrivals, and $S_{g,t}=\min(B_{g,t}+A_{g,t},C_{g,t})$ be dispatched requests. Conservation requires

$$B_{g,t+1}=B_{g,t}+A_{g,t}-S_{g,t}\ge0.$$

Timely service in this deliberately simplified FIFO model means served *in the arrival window*, not road pickup time. Old backlog is served first, so $T_{g,t}=\min(A_{g,t},\max(0,S_{g,t}-B_{g,t}))$. The runner checks $\sum A=\sum S+B_{final}$ for every scenario and class. Failing to count the final backlog would improve an apparently favorable rate by deleting unmet requests.

**The nonlinear bottleneck.** Arrivals can remain stable while the queue explodes when service capacity drops below demand. Normal baseline accessible capacity is 4 per window, but arrivals peak at 7. The run ends with 8 unfinished accessible requests. Integrated capacity of 7 removes the normal accessible backlog, yet the grid case reduces effective capacity and leaves 3 unfinished. Raising only standard fleet capacity cannot repair that accessibility bottleneck.

**Numerical counterexample.** A separate continuous approximation is $\dot B=u-kB$ with $u=4$ requests/min, $k=0.4/\text{min}$, and equilibrium $B^*=u/k=10$. Explicit Euler yields $B_{n+1}=B_n+h(u-kB_n)$; error multiplies by $1-hk$. Stability requires $|1-hk|<1$, or $0<h<2/k=5$ minutes. At $h=2$ the error multiplier is $0.2$; at $h=6$ it is $-1.4$, causing numerical oscillation to grow even though the underlying continuous dynamics are stable. Numerical convergence is not physical validation.

**Worked exercise and solution.** Start $B_0=20$ and use $h=2$: $B_1=20+2(4-0.4\times20)=12$, then $B_2=12+2(4-4.8)=10.4$. Repeat with $h=6$: $B_1=20+6(-4)=-4$, an impossible negative physical backlog that exposes the need for a bounded numerical method or smaller step. Do not silently clip it and call the original scheme validated.

**Reproduce:** [D06 queue derivation](../derivations/06-queue-utilization.md), [D08 numerical derivation](../derivations/08-stocks-flow-numerics.md), [controlled results](../flagship-integration/outputs/ns-u4.1-results.json).
