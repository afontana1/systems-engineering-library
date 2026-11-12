### D05 extension · Two-factor contrast as an interaction, not a causal proof

Consider a balanced synthetic $2\times2$ table of mean waits (minutes): base $y_{00}=18$, capacity-only $y_{10}=15$, process-only $y_{01}=14$, both $y_{11}=8$. The interaction on the raw response scale is $I=y_{11}-y_{10}-y_{01}+y_{00}=8-15-14+18=-3$ minutes. The joint intervention saves 3 more minutes than the sum of separately estimated reductions predicts. An interaction depends on the response scale and design; repeated randomization, controlled scenario blocks and a standard error are required before inferring a population effect.

**Exercise and solution.** If $y_{11}$ were 11 instead of 8, $I=0$ and the table would be additive on this scale. A single noiseless synthetic table cannot certify additivity outside its assumed domain. [Case data](../flagship-integration/data/ns-u4.1-case.json).
