---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "P(B | j, m) = alpha P(B) sum_e P(e) sum_a P(a|B,e) P(j|a) P(m|a). VE: f_A(B,E) = sum_a ..., which is 0.5985 (b,e), 0.5922 (b, not e), 0.1831 (not b, e), 0.00113 (not b, not e); f_E(B) = sum_e P(e) f_A(B,e) = 0.59224 for b and 0.001493 for not b; times P(B): 5.922e-4 and 1.4919e-3, so P(B | j, m) = (0.284, 0.716)."
sources: ["MNM slides Uncertainty-4-BN-INF (variable elimination)", "AIMA 3e sec. 14.4.2 (burglary example, P(B | j, m) = 0.284)"]
---
**Network** (from the figure): $P(B)=0.001$, $P(E)=0.002$; $P(A\mid B,E)$: $tt$ 0.95, $tf$ 0.94, $ft$ 0.29, $ff$ 0.001; $P(J\mid A)$: 0.9 / 0.05; $P(M\mid A)$: 0.7 / 0.01.

$$P(B\mid j,m)=\alpha\,P(B)\sum_eP(e)\sum_aP(a\mid B,e)\,P(j\mid a)\,P(m\mid a)$$

**Factors.** $f_1(B)=P(B)$, $f_2(E)=P(E)$, $f_3(A,B,E)=P(A\mid B,E)$; the evidence-restricted $f_4(A)=P(j\mid A)=(0.9,0.05)$ and $f_5(A)=P(m\mid A)=(0.7,0.01)$.

**Eliminate $A$:** $f_6(B,E)=\sum_af_3(a,B,E)f_4(a)f_5(a)=0.63\,P(a\mid B,E)+0.0005\,P(\neg a\mid B,E)$.

| $B$ | $E$ | $f_6(B,E)$ |
|:-:|:-:|:-:|
| t | t | 0.598525 |
| t | f | 0.592230 |
| f | t | 0.183055 |
| f | f | 0.001130 |

**Eliminate $E$:** $f_7(B)=\sum_ef_2(e)f_6(B,e)$.

$$f_7(b)=0.002(0.598525)+0.998(0.592230)=0.592243$$

$$f_7(\neg b)=0.002(0.183055)+0.998(0.001130)=0.001494$$

**Multiply by $P(B)$ and normalize.**

$$P(b)f_7(b)=0.001\times0.592243=5.922\times10^{-4}$$

$$P(\neg b)f_7(\neg b)=0.999\times0.001494=1.492\times10^{-3}$$

$$P(B\mid J=\text{true},M=\text{true})=\alpha\langle0.000592,\ 0.001492\rangle=\mathbf{\langle0.284,\ 0.716\rangle}.$$

(The same as AIMA's result.) Even with both John and Mary calling, a burglary has only about a 28% chance, because the alarm is also set off by earthquakes and false alarms.
