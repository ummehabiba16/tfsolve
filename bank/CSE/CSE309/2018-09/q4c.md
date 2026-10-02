---
marks: 9
topics: [ll1, first-follow]
kind: conceptual
source: {page: 37}
note: "Printed as 'can not' and 'for alpha =>* epsilon, beta does not derive'."
---
Among other reasons, a grammar can not be LL(1), if, whenever $A \to \alpha \mid \beta$ are two distinct productions of G, the following condition does *not* hold:

"If $\beta \overset{*}{\Rightarrow} \epsilon$, then $\alpha$ does not derive any string beginning with a terminal in FOLLOW($A$). Likewise, for $\alpha \overset{*}{\Rightarrow} \epsilon, \beta$ does not derive any string beginning with a terminal in FOLLOW($A$)". Why? Explain with necessary examples.
