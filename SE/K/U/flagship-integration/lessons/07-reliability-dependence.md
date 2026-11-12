### D07 extension · The common-cause gate changes the conclusion

For two independent components with availability $a$, parallel availability is $A_{ind}=1-(1-a)^2$. With $a=.985$, $A_{ind}=.999775$, above a 99% threshold. Let a separate common-cause event with probability $q=.03$ disable both; assuming that event is independent of the residual component-failure process, $A=(1-q)A_{ind}=.97(.999775)=.96978175$. Independence is a *model choice*, not a property conveyed by a block diagram. A shared power supply, supplier firmware or dispatch authority can invalidate redundancy claims.

**Exercise and solution.** At $q=.005$, $A=.995(.999775)=.994776125> .99$; this sensitivity does not establish that $q=.005$ is true. The availability gate still needs field evidence and configuration-specific scope. [Parameters](../flagship-integration/data/ns-u4.1-case.json).
