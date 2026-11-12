### D08 extension · Discrete stability and the nonnegative-state warning

For $\dot B=u-kB$ with $u=4$ requests/min and $k=.4$ per minute, equilibrium is $B^*=10$ requests. Explicit Euler at step $h$ gives $B_{n+1}=B_n+h(u-kB_n)$, so error $e_{n+1}=(1-hk)e_n$. Numerical stability requires $|1-hk|<1$, hence $0<h<5$ min. Starting at $B_0=20$, $h=2$ gives $B_1=12$, $B_2=10.4$; $h=6$ gives $B_1=-4$, an impossible backlog due solely to poor numerical discretization.

**Exercise and solution.** At $h=2.5$ minutes, the multiplier is zero and this linear model lands at equilibrium in one step. That numerical property does not imply a physical queue can instantaneously eliminate its backlog. [Model](../flagship-integration/code/ns_u_case.py).
