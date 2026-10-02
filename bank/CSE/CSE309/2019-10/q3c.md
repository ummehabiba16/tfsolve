---
marks: 15
topics: [ll1]
kind: conceptual
source: {page: 32}
note: "Marks printed as (7+8). Printed as 'does not derive ay string'."
---
(i) To find out whether a grammar $G$ is LL(1) or not, we test this condition among other conditions, "If whenever $A \to \alpha \mid \beta$ are two distinct productions of $G$, for no terminal $a$ do both $\alpha$ and $\beta$ derive strings beginning with $a$". State with necessary explanations, how this condition will be changed for an LL(3) grammar.

(ii) To find out whether a grammar $G$ is LL(1) or not, we test this condition as well among other conditions, "If whenever $A \to \alpha \mid \beta$ are two distinct productions of $G$, if $\beta \overset{*}{\Rightarrow} \epsilon$, then $\alpha$ does not derive ay string beginning with a terminal in FOLLOW(A). Likewise, if $\alpha \overset{*}{\Rightarrow} \epsilon$, then $\beta$ does not derive any string beginning with a terminal in FOLLOW(A)". Explain and justify this condition.
