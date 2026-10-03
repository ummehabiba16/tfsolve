---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Evidence C = No. P(D = Yes | C = No) = 0.092 / 0.22 = 0.418 (M and T are irrelevant and sum to 1)."
sources: ["MNM slides Uncertainty-4-BN-INF (exact inference)", "AIMA 4e sec. 13.3.1 (inference by enumeration)"]
---
"Could not communicate reliably" means the evidence is $C=\text{No}$ ($\neg c$). The query is $P(D\mid \neg c)$; the hidden variables are $T$, $P$ and $M$.

**Enumeration.**

$$P(D\mid\neg c)=\alpha\sum_{t}\sum_{p}\sum_{m}P(D)\,P(t)\,P(p\mid D)\,P(m\mid t,p)\,P(\neg c\mid p).$$

$M$ is a leaf that is neither query nor evidence, so $\sum_m P(m\mid t,p)=1$. Then $\sum_t P(t)=1$ as well (an irrelevant variable). This leaves

$$P(D\mid\neg c)=\alpha\,P(D)\sum_{p}P(p\mid D)\,P(\neg c\mid p),$$

with $P(\neg c\mid p)=1-0.9=0.1$ and $P(\neg c\mid\neg p)=1-0.3=0.7$.

$D=\text{Yes}$:

$$0.2\,[\,0.4(0.1)+0.6(0.7)\,]=0.2(0.04+0.42)=0.2(0.46)=0.092$$

$D=\text{No}$:

$$0.8\,[\,0.9(0.1)+0.1(0.7)\,]=0.8(0.09+0.07)=0.8(0.16)=0.128$$

**Normalise.** $P(\neg c)=0.092+0.128=0.22$, so $\alpha=1/0.22$.

$$P(D=\text{Yes}\mid\neg c)=\frac{0.092}{0.22}=\mathbf{0.418},\qquad P(D=\text{No}\mid\neg c)=\frac{0.128}{0.22}=0.582.$$

Losing communication raises the probability of a dust storm from the prior 0.2 to about **0.42**.

*Note:* $P(P\mid D=\text{No})=0.9$ is the handwritten correction on the paper.
