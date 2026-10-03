---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Elapse: B'(R1) = (0.54, 0.46); observe +u: B(R1) = (0.841, 0.159); elapse: B'(R2) = (0.636, 0.364); observe -u: B(R2) = (+r 0.179, -r 0.821). Each elapse step pulls the belief towards (0.5, 0.5), and each observation sharpens it."
sources: ["MNM slides Lecture 6 - Hidden Markov Model (forward algorithm: passage of time, observation)", "Berkeley CS188 HMM lecture (umbrella example)"]
---
**Forward algorithm.** Two steps are repeated at each time step:

- *Elapse time:* $B'(R_{t+1})=\sum_{r_t}P(R_{t+1}\mid r_t)\,B(r_t)$
- *Observe:* $B(R_{t+1})=\alpha\,P(u_{t+1}\mid R_{t+1})\,B'(R_{t+1})$

Vectors are $(+r,-r)$, and $B(R_0)=(0.6,\ 0.4)$.

**$t=1$.**

*Elapse:*

$$B'(+r)=0.7(0.6)+0.3(0.4)=0.54,\qquad B'(-r)=0.3(0.6)+0.7(0.4)=0.46$$

*Observe $U_1=+u$:*

$$(0.9\times0.54,\ 0.2\times0.46)=(0.486,\ 0.092)\ \xrightarrow{\ \div0.578\ }\ B(R_1)=(0.841,\ 0.159)$$

**$t=2$.**

*Elapse:*

$$B'(+r)=0.7(0.841)+0.3(0.159)=0.636,\qquad B'(-r)=0.3(0.841)+0.7(0.159)=0.364$$

*Observe $U_2=-u$:*

$$(0.1\times0.636,\ 0.8\times0.364)=(0.0636,\ 0.2910)\ \xrightarrow{\ \div0.3546\ }\ B(R_2)=(0.179,\ 0.821)$$

**Belief at $t=2$:** $\mathbf{P(+r\mid +u_1,-u_2)=0.179}$ and $\mathbf{P(-r\mid +u_1,-u_2)=0.821}$.

| Step | $B(+r)$ | $B(-r)$ | Effect |
|:--|:-:|:-:|:--|
| $R_0$ | 0.600 | 0.400 | |
| elapse to $R_1$ | 0.540 | 0.460 | moves towards 0.5: less certain |
| observe $+u$ | 0.841 | 0.159 | sharper: more certain |
| elapse to $R_2$ | 0.636 | 0.364 | moves towards 0.5 again: less certain |
| observe $-u$ | 0.179 | 0.821 | sharper again |

**Justification of the statement.** The transition model is symmetric, with stationary distribution $(0.5,0.5)$. Each passage of time mixes the belief towards this uniform distribution: $0.6\to0.54$ and $0.841\to0.636$, so the belief becomes flatter and **uncertainty accumulates**. Each observation multiplies by a likelihood that strongly favors one state ($0.9$ vs $0.2$, or $0.1$ vs $0.8$) and renormalizes, so the belief becomes peaked and **uncertainty decreases**. Measured by entropy: $H(0.54)=0.995$ bits drops to $H(0.841)=0.632$ after the observation; it rises to $0.946$ at the next elapse, then falls to $0.678$.
