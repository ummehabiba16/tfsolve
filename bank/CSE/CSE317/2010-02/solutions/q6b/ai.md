---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Chain A -> B -> C. P(not c | a) = 0.8(0.3) + 0.2(0.8) = 0.40; P(not c | not a) = 0.1(0.3) + 0.9(0.8) = 0.75. P(a, not c) = 0.2 x 0.40 = 0.08; P(not a, not c) = 0.8 x 0.75 = 0.60; P(A = t | C = f) = 0.08/0.68 = 0.118."
sources: ["MNM slides Uncertainty-4-BN-INF (exact inference)", "AIMA 3e sec. 14.4.1"]
---
**Network:** $A\to B\to C$, with $P(a)=0.2$; $P(b\mid a)=0.8$, $P(b\mid\neg a)=0.1$; $P(c\mid b)=0.7$, $P(c\mid\neg b)=0.2$.

$$P(A\mid\neg c)=\alpha\,P(A)\sum_bP(b\mid A)\,P(\neg c\mid b)$$

**Sum out $B$.** $P(\neg c\mid b)=0.3$ and $P(\neg c\mid\neg b)=0.8$:

$$A=t:\ \sum_bP(b\mid a)P(\neg c\mid b)=0.8(0.3)+0.2(0.8)=0.24+0.16=0.40$$

$$A=f:\ \sum_bP(b\mid\neg a)P(\neg c\mid b)=0.1(0.3)+0.9(0.8)=0.03+0.72=0.75$$

**Multiply by $P(A)$.**

$$P(a,\neg c)=0.2\times0.40=0.08,\qquad P(\neg a,\neg c)=0.8\times0.75=0.60$$

**Normalize.** $P(\neg c)=0.68$.

$$P(A=t\mid C=f)=\frac{0.08}{0.68}=\mathbf{0.118}$$

(The prior was 0.2. Observing $C$ false makes $A$ less likely.)

*Note:* $P(A)=0.2$ is read from the partly blacked-out figure.
