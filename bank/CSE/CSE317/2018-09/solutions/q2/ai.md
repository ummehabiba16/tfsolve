---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "States 00, 01, 10, 11; T has 00: (3/4, 1/4, 0, 0), 01: (1/4, 1/2, 1/4, 0), 10: (0, 1/4, 1/2, 1/4), 11: (0, 0, 1/4, 3/4); the left bit is observed exactly. Filtering for 0, 0, 1: t=1 (1/2, 1/2, 0, 0), t=2 (4/7, 3/7, 0, 0), t=3 (0, 0, 1, 0). Smoothing: X0 (5/12, 5/12, 1/6, 0), X1 (1/3, 2/3, 0, 0), X2 = 01, X3 = 10. Viterbi: 01, 01, 01, 10."
sources: ["MNM slides Lecture 6 - Hidden Markov Model (filtering, forward-backward, Viterbi)", "AIMA 4e sec. 14.2 (Fig. 14.4 forward-backward, Viterbi)"]
---
**(a) HMM formulation.** Hidden state $X_t\in\{00,01,10,11\}$ (left bit first), with $P(X_0)$ uniform at $\frac14$. Each step: unchanged with probability $\frac12$, bits swapped with $\frac14$, right bit flipped with $\frac14$. (Swapping 00 or 11 leaves them unchanged.)

Transition model $P(X_t\mid X_{t-1})$:

| from \ to | 00 | 01 | 10 | 11 |
|:-:|:-:|:-:|:-:|:-:|
| 00 | $\frac12+\frac14=\frac34$ | $\frac14$ (flip) | 0 | 0 |
| 01 | $\frac14$ (flip) | $\frac12$ | $\frac14$ (swap) | 0 |
| 10 | 0 | $\frac14$ (swap) | $\frac12$ | $\frac14$ (flip) |
| 11 | 0 | 0 | $\frac14$ (flip) | $\frac12+\frac14=\frac34$ |

Observation model: the **left bit** is observed exactly, so $P(E_t=0\mid X_t)=1$ for 00 and 01, and 0 for 10 and 11. $P(E_t=1\mid X_t)$ is the reverse.

**(b) Filtering** for $e_1=0$, $e_2=0$, $e_3=1$. Each step predicts with $\mathbf{T}$, then zeroes out the states inconsistent with the observed bit and renormalizes.

| $t$ | Prediction $P(X_t\mid e_{1:t-1})$ | Filtered $P(X_t\mid e_{1:t})$ (00, 01, 10, 11) |
|:-:|:--|:--|
| 1 | $(\frac14,\frac14,\frac14,\frac14)$ | $(\frac12,\ \frac12,\ 0,\ 0)$ |
| 2 | $(\frac12,\ \frac38,\ \frac18,\ 0)$ | $(\frac47,\ \frac37,\ 0,\ 0)$ |
| 3 | $(\frac{15}{28},\ \frac{5}{14},\ \frac{3}{28},\ 0)$ | $(0,\ 0,\ 1,\ 0)$ |

For example, at $t=2$: $P(00)=\frac12\cdot\frac34+\frac12\cdot\frac14=\frac12$, $P(01)=\frac12\cdot\frac14+\frac12\cdot\frac12=\frac38$, and $P(10)=\frac12\cdot\frac14=\frac18$. At $t=3$ the left bit is 1, and only 10 can be reached from $\{00,01\}$ (by swapping 01). So $X_3=10$ for certain.

**(c) Forward-backward smoothing.** $b_k(x)=P(e_{k+1:3}\mid X_k=x)$, with $b_3=(1,1,1,1)$ and $b_k(i)=\sum_jT_{ij}\,P(e_{k+1}\mid j)\,b_{k+1}(j)$:

| $k$ | $b_k$ (00, 01, 10, 11) | $P(X_k\mid e_{1:3})\propto f_k\times b_k$ |
|:-:|:--|:--|
| 0 | $(\frac{5}{64},\ \frac{5}{64},\ \frac{1}{32},\ 0)$ | $(\frac{5}{12},\ \frac{5}{12},\ \frac16,\ 0)$ |
| 1 | $(\frac1{16},\ \frac18,\ \frac1{16},\ 0)$ | $(\frac13,\ \frac23,\ 0,\ 0)$ |
| 2 | $(0,\ \frac14,\ \frac34,\ 1)$ | $(0,\ 1,\ 0,\ 0)$ |
| 3 | $(1,1,1,1)$ | $(0,\ 0,\ 1,\ 0)$ |

($f_0$ is the uniform prior.) Seeing a 1 at $t=3$ after a 0 at $t=2$ means a swap from 01 happened, so $X_2=01$ for certain.

**(d) Most likely sequence (Viterbi, including $X_0$).** The path probabilities $P(x_{0:3},e_{1:3})$ of the best candidates are:

| $X_0, X_1, X_2, X_3$ | Probability |
|:--|:-:|
| **01, 01, 01, 10** | $\frac14\cdot\frac12\cdot\frac12\cdot\frac14=\frac1{64}$ |
| 00, 00, 01, 10 | $\frac14\cdot\frac34\cdot\frac14\cdot\frac14=\frac{3}{256}$ |
| 10, 01, 01, 10 | $\frac1{128}$ |
| 00, 01, 01, 10 | $\frac1{128}$ |

**Most likely sequence: $X_0=01$, $X_1=01$, $X_2=01$, $X_3=10$** (the register stays at 01 twice, then its bits are swapped). This was checked by enumerating all $4^4$ paths. Note that it is consistent with the smoothed marginals but not equal to their individual maxima (at $k=0$, 00 and 01 tie).
