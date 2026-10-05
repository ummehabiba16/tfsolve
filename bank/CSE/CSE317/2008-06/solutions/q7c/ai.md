---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "(i) P(not A, W, H) = P(W) P(not A | W) P(H | W) = 0.2 x 0.2 x 0.3 = 0.012. (ii) P(not A, H) = 0.012 + 0.8 x 0.6 x 0.1 = 0.060; P(H) = 0.2 x 0.3 + 0.8 x 0.1 = 0.14; P(not A | H) = 0.06/0.14 = 0.429."
sources: ["MNM slides Uncertainty-2-BN", "AIMA 3e sec. 14.2"]
---
**Network** (figure 7(c)): $W\to A$, $W\to H$, so $P(W,A,H)=P(W)\,P(A\mid W)\,P(H\mid W)$, with $P(W)=0.2$; $P(A\mid W)=0.8$, $P(A\mid\neg W)=0.4$; $P(H\mid W)=0.3$, $P(H\mid\neg W)=0.1$.

**(i)** (4)

$$P(\neg A,W,H)=P(W)\,P(\neg A\mid W)\,P(H\mid W)=0.2\times0.2\times0.3=\mathbf{0.012}$$

**(ii)** (8) Sum out $W$:

$$P(\neg A,H)=\sum_wP(w)P(\neg A\mid w)P(H\mid w)=0.2(0.2)(0.3)+0.8(0.6)(0.1)=0.012+0.048=0.060$$

$$P(H)=\sum_wP(w)P(H\mid w)=0.2(0.3)+0.8(0.1)=0.14$$

$$P(\neg A\mid H)=\frac{0.060}{0.14}=\mathbf{0.429}$$
