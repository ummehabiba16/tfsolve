---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Eliminate A: f1(B,E) = sum_a P(a|B,E) P(j|a) P(m|a); eliminate B: f2(E) = sum_b P(b) f1(b,E); then P(E | j, m) = alpha P(E) f2(E). With AIMA's CPTs: f2 = (0.18347, 0.001721), so P(e | j, m) = 0.176 (not e: 0.824)."
sources: ["MNM slides Uncertainty-4-BN-INF (variable elimination)", "AIMA 4e sec. 13.3.2 (variable elimination, burglary network)"]
---
**Expression** (hidden variables $B$ and $A$):

$$P(E\mid j,m)=\alpha\,P(E)\sum_bP(b)\sum_aP(a\mid b,E)\,P(j\mid a)\,P(m\mid a).$$

**Variable elimination steps** (10 marks).

1. *Factors:* $f_E(E)=P(E)$, $f_B(B)=P(B)$, $f_A(A,B,E)=P(A\mid B,E)$, and, restricted to the evidence, $f_J(A)=P(j\mid A)$ and $f_M(A)=P(m\mid A)$.
2. *Eliminate $A$* (innermost): multiply the factors that mention $A$ and sum it out:

$$f_1(B,E)=\sum_af_A(a,B,E)\,f_J(a)\,f_M(a).$$

3. *Eliminate $B$:*

$$f_2(E)=\sum_bf_B(b)\,f_1(b,E).$$

4. *Multiply the remaining factors* and **normalize**: $P(E\mid j,m)=\alpha\,f_E(E)\,f_2(E)$.

**Numbers (5 marks)**, using AIMA's burglary CPTs ($P(b)=0.001$, $P(e)=0.002$; $P(a\mid B,E)=0.95,0.94,0.29,0.001$; $P(j\mid a)=0.9$, $P(j\mid\neg a)=0.05$; $P(m\mid a)=0.7$, $P(m\mid\neg a)=0.01$):

| $B$ | $E$ | $f_1(B,E)=0.63\,P(a\mid B,E)+0.0005\,P(\neg a\mid B,E)$ |
|:-:|:-:|:-:|
| b | e | 0.598525 |
| b | $\neg$e | 0.592230 |
| $\neg$b | e | 0.183055 |
| $\neg$b | $\neg$e | 0.001130 |

$$f_2(e)=0.001(0.598525)+0.999(0.183055)=0.183470$$

$$f_2(\neg e)=0.001(0.592230)+0.999(0.001130)=0.001721$$

$$P(E\mid j,m)=\alpha\,\langle0.002\times0.183470,\ 0.998\times0.001721\rangle=\alpha\langle0.000367,\ 0.001717\rangle=\mathbf{\langle0.176,\ 0.824\rangle}.$$

*Note:* the paper shows only the structure. The standard AIMA CPTs for this network are assumed.
