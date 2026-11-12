### D03 extension · Evidence update with an explicitly conditional independence assumption

Using $P(B)=.15$, sensitivity $P(+|B)=.80$ and false-positive probability $P(+|\neg B)=.10$, compute $P(+)=.80(.15)+.10(.85)=.205$. Therefore $P(B|+)=.12/.205\approx.58537$. Under an **additional**, unverified conditional-independence assumption a second positive produces $[.80(.58537)]/[.80(.58537)+.10(.41463)]\approx.91866$. If the alarms share one camera or weather sensor, using the update twice would double-count information. Posterior probability describes belief under the stated likelihood model; it does not authorize an unsafe route.

**Exercise and solution.** With false positive .20 instead, $P(B|+)=.12/(.12+.17)=.41379$. A lower-specificity alarm is weaker evidence. [Run](../flagship-integration/code/ns_u_case.py).
