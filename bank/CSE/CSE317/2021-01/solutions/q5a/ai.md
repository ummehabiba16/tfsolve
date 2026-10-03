---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "P(+x|-y) = 0.3/0.4 = 0.75; P(-y|+x) = 0.3/0.5 = 0.6; P(+x|+y) = 0.2/0.6 = 0.333; P(-x|+y) = 0.4/0.6 = 0.667."
sources: ["MNM slides Uncertainty-1-(quantifying) (conditional probability, marginalization)", "AIMA 4e sec. 12.2-12.3"]
---
Use $P(a\mid b)=\dfrac{P(a,b)}{P(b)}$, with the marginals obtained by summing the joint table.

**Marginals.**

$$P(+x)=0.2+0.3=0.5,\qquad P(-x)=0.4+0.1=0.5$$

$$P(+y)=0.2+0.4=0.6,\qquad P(-y)=0.3+0.1=0.4$$

**i)** $P(+x\mid -y)=\dfrac{P(+x,-y)}{P(-y)}=\dfrac{0.3}{0.4}=\mathbf{0.75}$

**ii)** $P(-y\mid +x)=\dfrac{P(+x,-y)}{P(+x)}=\dfrac{0.3}{0.5}=\mathbf{0.6}$

**iii)** $P(+x\mid +y)=\dfrac{P(+x,+y)}{P(+y)}=\dfrac{0.2}{0.6}=\mathbf{0.333}$

**iv)** $P(-x\mid +y)=\dfrac{P(-x,+y)}{P(+y)}=\dfrac{0.4}{0.6}=\mathbf{0.667}$

*Check:* (iii) + (iv) $=1$, as conditional probabilities given $+y$ must sum to 1.
