### D09 extension · Schedule-path calculation and earned-value independence

Suppose work can flow through either A–B–C with durations 3+4+2=9 days or A–D–C with durations 3+5+2=10 days. In this fixed deterministic network, the second path is critical at 10 days; a one-day delay in D increases finish time unless schedule logic or concurrency changes. Separately, earned value $EV=100$, actual cost $AC=130$, and planned value $PV=120$ (same monetary units), giving $CPI=EV/AC=.76923$, $CV=-30$ and $SV=EV-PV=-20$. Neither CPI nor SV gives an exact forecast of critical-path completion.

**Exercise and solution.** Shortening D by two days yields A–D–C=8 while A–B–C stays 9; the critical path switches. CPI remains .76923 if no cost/evidence records change. [Input model](../flagship-integration/data/ns-u4.1-case.json).
