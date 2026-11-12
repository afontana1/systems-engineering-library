### D02 extension · Feasible-first preference and a reversal equation

Given qualities $q_A,q_B$ and normalized costs $c_A,c_B$, consider $V=wq-(1-w)c$, $0\le w\le1$. The two designs tie when $w(q_A-q_B)=(1-w)(c_A-c_B)$ and, if the denominator is nonzero, $w^*=(c_A-c_B)/[(q_A-q_B)+(c_A-c_B)]$. A reversal weight is meaningful only when the *hard constraints are already satisfied*. NS-U4.1's integrated candidate passes normal service (99.35% total and 100% accessible) but only 45% of scenario weight. With a 95% robustness screen there are no candidates in the feasible set. Preference weights cannot restore feasibility.

**Exercise and solution.** If A has $q=.8,c=.2$ and B has $q=.9,c=.5$, then $V_A-V_B=-.1w+.3(1-w)=.3-.4w$; A and B tie at $w=.75$. This is a stylized preference comparison, not a safety release decision. [Policy outputs](../flagship-integration/outputs/ns-u4.1-results.json).
