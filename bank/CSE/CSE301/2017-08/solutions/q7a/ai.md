---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Markov chain on $\{S,C,R\}$ (from $S$: $C$ or $R$ w.p. $\frac12$; from $C$ or $R$: same again w.p. $\frac12$, each other state w.p. $\frac14$). Balance equations: $\pi_S=1/5$, $\pi_C=\pi_R=2/5$. Sunny $1/5$ of days, cloudy $2/5$.'
sources: ['CSE301 Markov_Chain slides 19-22 (limiting probabilities, long-run weather proportions)', 'Ross, Introduction to Probability Models, Ch. 4 (limiting probabilities)']
---
**Model.** Let $X_n$ be the weather on day $n$, with states $S$ (sunny), $C$ (cloudy) and $R$ (rainy). Tomorrow's weather depends only on today's, so $\{X_n\}$ is a Markov chain:

- From $S$: never sunny again, cloudy or rainy with probability $\frac12$ each.
- From $C$: cloudy again with probability $\frac12$; otherwise it changes, to $S$ or $R$ with probability $\frac14$ each.
- From $R$: rainy again with probability $\frac12$; otherwise $S$ or $C$ with probability $\frac14$ each.

| From \ To | $S$ | $C$ | $R$ |
|:-:|:-:|:-:|:-:|
| $S$ | 0 | 1/2 | 1/2 |
| $C$ | 1/4 | 1/2 | 1/4 |
| $R$ | 1/4 | 1/4 | 1/2 |

The chain is irreducible (every state can reach every other) and aperiodic ($P_{CC}>0$), so limiting probabilities exist and are the unique solution of $\pi_j=\sum_i\pi_iP_{ij}$, $\sum_j\pi_j=1$.

**Balance equations.**

$$\pi_S=\tfrac14\pi_C+\tfrac14\pi_R$$

$$\pi_C=\tfrac12\pi_S+\tfrac12\pi_C+\tfrac14\pi_R$$

$$\pi_R=\tfrac12\pi_S+\tfrac14\pi_C+\tfrac12\pi_R$$

$$\pi_S+\pi_C+\pi_R=1$$

Subtracting the third equation from the second gives $\pi_C-\pi_R=\frac12\pi_C-\frac12\pi_R$, so $\pi_C=\pi_R$ (the chain treats cloudy and rainy symmetrically). The first equation then gives $\pi_S=\frac12\pi_C$. Normalising:

$$\tfrac12\pi_C+\pi_C+\pi_C=1\ \Rightarrow\ \pi_C=\tfrac25,\quad \pi_R=\tfrac25,\quad \pi_S=\tfrac15$$

**Answer.** In the long run, $\mathbf{1/5}$ (20%) of the days are sunny and $\mathbf{2/5}$ (40%) are cloudy (and 40% are rainy).
