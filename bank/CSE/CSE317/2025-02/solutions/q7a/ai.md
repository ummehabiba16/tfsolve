---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) P(p1, not p3, p4) = sum over p2 = 0.1792 + 0.0336 = 0.2128. (ii) f1(P2) = (0.62, 0.38), times P(not p3 | P2) = (0.496, 0.266), P4 sums to 1, so P(p2 | not p3) = 0.496/0.762 = 0.651."
sources: ["MNM slides Uncertainty-4-BN-INF (enumeration, variable elimination: restrict, multiply, sum out, normalize)", "AIMA 4e sec. 13.3"]
---
**Network.** $P_1\to P_2$, $P_2\to P_3$, $P_2\to P_4$, so

$$P(P_1,P_2,P_3,P_4)=P(P_1)\,P(P_2\mid P_1)\,P(P_3\mid P_2)\,P(P_4\mid P_2).$$

CPTs: $P(p_1)=0.4$; $P(p_2\mid p_1)=0.8$, $P(p_2\mid\neg p_1)=0.5$; $P(p_3\mid p_2)=0.2$, $P(p_3\mid\neg p_2)=0.3$; $P(p_4\mid p_2)=0.7$, $P(p_4\mid\neg p_2)=0.6$.

**(i) Inference by enumeration.** The only hidden variable is $P_2$:

$$P(p_1,\neg p_3,p_4)=\sum_{x\in\{p_2,\neg p_2\}}P(p_1)\,P(x\mid p_1)\,P(\neg p_3\mid x)\,P(p_4\mid x)$$

$$=P(p_1,p_2,\neg p_3,p_4)+P(p_1,\neg p_2,\neg p_3,p_4)$$

$$P(p_1,p_2,\neg p_3,p_4)=0.4\times0.8\times(1-0.2)\times0.7=0.4\times0.8\times0.8\times0.7=0.1792$$

$$P(p_1,\neg p_2,\neg p_3,p_4)=0.4\times(1-0.8)\times(1-0.3)\times0.6=0.4\times0.2\times0.7\times0.6=0.0336$$

$$P(p_1,\neg p_3,p_4)=0.1792+0.0336=\mathbf{0.2128}$$

**(ii) $P(P_2\mid\neg p_3)$ by variable elimination.**

$$P(P_2\mid\neg p_3)=\alpha\sum_{p_1}P(p_1)P(P_2\mid p_1)\;\cdot\;P(\neg p_3\mid P_2)\;\cdot\;\sum_{p_4}P(p_4\mid P_2)$$

*Factors* (with the evidence $P_3=\neg p_3$ restricted):

- $f_1(P_1)=P(P_1)=(0.4,\ 0.6)$
- $f_2(P_1,P_2)=P(P_2\mid P_1)$
- $f_3(P_2)=P(\neg p_3\mid P_2)=(0.8,\ 0.7)$
- $f_4(P_2,P_4)=P(P_4\mid P_2)$

*Eliminate $P_4$:* $\sum_{p_4}P(p_4\mid P_2)=1$ for each value of $P_2$. $P_4$ is irrelevant (a leaf that is not query or evidence), so drop $f_4$.

*Eliminate $P_1$:* multiply $f_1\times f_2$ and sum out $P_1$, giving $f_5(P_2)$:

$$f_5(p_2)=0.4(0.8)+0.6(0.5)=0.32+0.30=0.62$$

$$f_5(\neg p_2)=0.4(0.2)+0.6(0.5)=0.08+0.30=0.38$$

*Multiply the remaining factors* $f_5\times f_3$:

$$p_2:\ 0.62\times0.8=0.496,\qquad \neg p_2:\ 0.38\times0.7=0.266$$

*Normalize:* $P(\neg p_3)=0.496+0.266=0.762$.

$$P(p_2\mid\neg p_3)=\frac{0.496}{0.762}=\mathbf{0.651},\qquad P(\neg p_2\mid\neg p_3)=\frac{0.266}{0.762}=0.349.$$
