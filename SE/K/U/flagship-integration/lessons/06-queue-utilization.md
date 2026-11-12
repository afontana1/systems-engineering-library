### D06 extension · A discrete conservation check and queue boundary

A single-class FIFO queue obeys $B_{t+1}=B_t+A_t-S_t$, with $S_t=\min(B_t+A_t,C_t)$ and all variables in requests per *one service window*. Over $N$ windows, telescoping yields $B_N=B_0+\sum_t A_t-\sum_t S_t$. NS-U4.1 computes this separately for standard and accessible service. In the baseline normal scenario, accessible capacity 4 per window cannot clear arrivals $[4,5,6,7,6,4]$, leaving 8 accessible requests unfinished after the observation horizon. The unfinished cases remain in the denominator for timely-service analysis. Little's law $L=\lambda W$ applies to properly defined, stable long-run systems, not automatically to this finite transient with remaining backlog.

**Exercise and solution.** If arrivals total 32, served total 24 and the system starts empty, $B_N=8$ by conservation. Deleting those eight would be an accounting error. [Capacity trace](../flagship-integration/outputs/ns-u4.1-results.json).
