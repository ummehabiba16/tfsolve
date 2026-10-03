---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "P(B | -e, +j) = alpha P(B) P(-e) sum_a P(a | B, -e) P(+j | a) (M sums out): +b: 0.001(0.998)(0.849) = 8.47e-4; -b: 0.999(0.998)(0.05085) = 0.0507; P(+b | -e, +j) = 0.0164."
sources: ["MNM slides Uncertainty-4-BN-INF (exact inference)", "AIMA 4e sec. 13.3.1 (burglary network)"]
---
**Enumeration.** The query is $B$, the evidence is $E=-e$ and $J=+j$, and the hidden variables are $A$ and $M$:

$$P(B\mid -e,+j)=\alpha\,P(B)\,P(-e)\sum_{a}P(a\mid B,-e)\,P(+j\mid a)\sum_{m}P(m\mid a).$$

$\sum_mP(m\mid a)=1$: $M$ is a leaf that is neither query nor evidence, so it drops out.

**$B=+b$.**

$$\sum_aP(a\mid +b,-e)P(+j\mid a)=0.94(0.9)+0.06(0.05)=0.846+0.003=0.849$$

$$0.001\times0.998\times0.849=8.473\times10^{-4}$$

**$B=-b$.**

$$\sum_aP(a\mid -b,-e)P(+j\mid a)=0.001(0.9)+0.999(0.05)=0.0009+0.04995=0.05085$$

$$0.999\times0.998\times0.05085=0.05070$$

**Normalize.** $P(-e,+j)=0.000847+0.05070=0.05154$.

$$P(+b\mid -e,+j)=\frac{0.000847}{0.05154}=\mathbf{0.0164},\qquad P(-b\mid -e,+j)=\mathbf{0.9836}$$

A call from John raises the probability of a burglary from 0.001 to about **1.6%**. ($P(-e)=0.998$ cancels in the normalization.)
