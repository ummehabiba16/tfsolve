---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "With T = d, A sums out. P(R, M, d): (l,y) 0.192, (l,n) 0.096, (h,y) 0.012, (h,n) 0.090; P(d) = 0.39. P(R | d) = (l: 0.738, h: 0.262); P(M | d) = (y: 0.523, n: 0.477)."
sources: ["MNM slides Uncertainty-4-BN-INF (inference by enumeration)", "AIMA 4e sec. 13.3.1"]
---
**Network and CPTs.** $R\to M$, $R\to T$, $M\to T$, $T\to A$:

$$P(R,M,T,A)=P(R)\,P(M\mid R)\,P(T\mid R,M)\,P(A\mid T).$$

The missing entries are complements:

- $P(R=h)=0.2$
- $P(M=n\mid l)=0.4$, $P(M=n\mid h)=0.9$
- $P(T=d\mid R,M)=1-P(T=t\mid R,M)$: $(l,y)\ 0.4$, $(l,n)\ 0.3$, $(h,y)\ 0.6$, $(h,n)\ 0.5$

**Enumeration with evidence $T=d$.** $A$ is below the evidence and is neither query nor evidence, so $\sum_aP(a\mid d)=1$ and it drops out:

$$P(R,M\mid d)=\alpha\,P(R)\,P(M\mid R)\,P(d\mid R,M).$$

| $R$ | $M$ | $P(R)\,P(M\mid R)\,P(d\mid R,M)$ |
|:-:|:-:|:--|
| l | y | $0.8\times0.6\times0.4=0.192$ |
| l | n | $0.8\times0.4\times0.3=0.096$ |
| h | y | $0.2\times0.1\times0.6=0.012$ |
| h | n | $0.2\times0.9\times0.5=0.090$ |

$P(T=d)=0.192+0.096+0.012+0.090=0.390$.

**Updated distribution of $R$.**

$$P(R=l\mid d)=\frac{0.192+0.096}{0.39}=\frac{0.288}{0.39}=\mathbf{0.738},\qquad P(R=h\mid d)=\frac{0.102}{0.39}=\mathbf{0.262}$$

(The prior was $0.8/0.2$.)

**Updated distribution of $M$.**

$$P(M=y\mid d)=\frac{0.192+0.012}{0.39}=\frac{0.204}{0.39}=\mathbf{0.523},\qquad P(M=n\mid d)=\frac{0.186}{0.39}=\mathbf{0.477}$$

(The prior was $P(M=y)=0.8(0.6)+0.2(0.1)=0.50$.)

Observing $T=d$ makes $R=h$ more likely (0.2 to 0.26) and $M=y$ slightly more likely (0.50 to 0.52).
