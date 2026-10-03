---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Eliminate A: f1(B,E) = sum_a P(a|B,E) P(j|a) P(m|a) = (0.5985, 0.5922, 0.1831, 0.00113). Eliminate B: f2(E) = sum_b P(b) f1(b,E) = (0.18347, 0.001721). Then P(E)f2(E) = (3.669e-4, 1.717e-3), so P(+e | +j, +m) = 0.176."
sources: ["MNM slides Uncertainty-4-BN-INF (variable elimination)", "AIMA 4e sec. 13.3.2"]
---
**Query.** $P(E\mid +j,+m)=\alpha\,P(E)\sum_bP(b)\sum_aP(a\mid b,E)\,P(+j\mid a)\,P(+m\mid a)$.

**Factors after restricting to the evidence.**

- $f_B(B)=P(B)$, $f_E(E)=P(E)$, $f_A(A,B,E)=P(A\mid B,E)$
- $f_J(A)=P(+j\mid A)=(0.9,\ 0.05)$
- $f_M(A)=P(+m\mid A)=(0.7,\ 0.01)$

**Eliminate $A$.** Multiply $f_A\,f_J\,f_M$ and sum out $A$:

$$f_1(B,E)=\sum_aP(a\mid B,E)\,(0.9\cdot0.7\text{ if }a\text{, else }0.05\cdot0.01)=0.63\,P(+a\mid B,E)+0.0005\,P(-a\mid B,E)$$

| $B$ | $E$ | $f_1(B,E)$ |
|:-:|:-:|:--|
| +b | +e | $0.95(0.63)+0.05(0.0005)=0.598525$ |
| +b | $-$e | $0.94(0.63)+0.06(0.0005)=0.592230$ |
| $-$b | +e | $0.29(0.63)+0.71(0.0005)=0.183055$ |
| $-$b | $-$e | $0.001(0.63)+0.999(0.0005)=0.001130$ |

**Eliminate $B$.** Multiply by $f_B$ and sum out $B$:

$$f_2(E)=\sum_bP(b)\,f_1(b,E)$$

$$f_2(+e)=0.001(0.598525)+0.999(0.183055)=0.183470$$

$$f_2(-e)=0.001(0.592230)+0.999(0.001130)=0.001721$$

**Multiply by $P(E)$ and normalize.**

$$P(+e)\,f_2(+e)=0.002\times0.183470=3.669\times10^{-4}$$

$$P(-e)\,f_2(-e)=0.998\times0.001721=1.717\times10^{-3}$$

$$P(+e\mid +j,+m)=\frac{3.669\times10^{-4}}{3.669\times10^{-4}+1.717\times10^{-3}}=\mathbf{0.176}$$

(and $P(-e\mid +j,+m)=0.824$). This matches the textbook value $P(E\mid j,m)\approx\langle0.176,\ 0.824\rangle$.
