---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Restrict to b, i, m; the constant factors P(b), P(m), P(i|b,m) cancel. Sum out G: P(j | b, i, m) = 0.9 x 0.9 + 0.1 x 0 = 0.81."
sources: ["MNM slides Uncertainty-4-BN-INF (variable elimination)", "AIMA 4e Fig. 13.24 and Exercise 13.POLI (politically motivated prosecutor)"]
---
**Query.** $P(J\mid b,i,m)$, with evidence $B=t$, $I=t$, $M=t$ and hidden variable $G$:

$$P(J\mid b,i,m)=\alpha\,P(b)\,P(m)\,P(i\mid b,m)\sum_{g}P(g\mid b,i,m)\,P(J\mid g).$$

**Factors after restricting to the evidence.**

- $f_1=P(b)=0.9$, $f_2=P(m)=0.1$, $f_3=P(i\mid b,m)=0.9$: constants (no free variables).
- $f_4(G)=P(G\mid b,i,m)$: $f_4(g)=0.9$, $f_4(\neg g)=0.1$.
- $f_5(J,G)=P(J\mid G)$:

| $G$ | $J$ | $f_5$ |
|:-:|:-:|:-:|
| t | t | 0.9 |
| t | f | 0.1 |
| f | t | 0.0 |
| f | f | 1.0 |

**Eliminate $G$.** Multiply $f_4\times f_5$ and sum out $G$:

$$f_6(j)=f_4(g)f_5(j,g)+f_4(\neg g)f_5(j,\neg g)=0.9(0.9)+0.1(0.0)=0.81$$

$$f_6(\neg j)=0.9(0.1)+0.1(1.0)=0.19$$

**Multiply in the constants and normalize.** $\alpha\,f_1f_2f_3\,f_6(J)$; the constants $0.9\times0.1\times0.9=0.081$ cancel when normalizing:

$$P(J\mid b,i,m)=\frac{(0.081\times0.81,\ 0.081\times0.19)}{0.081\times(0.81+0.19)}=(0.81,\ 0.19).$$

$$\mathbf{P(j\mid b,i,m)=0.81}$$

Someone who broke the law, was indicted and faces a politically motivated prosecutor goes to jail with probability **0.81**.
