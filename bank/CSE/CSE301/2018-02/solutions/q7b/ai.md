---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$P_i$ (reach $N$ first) satisfies $P_i=pP_{i+1}+qP_{i-1}$, $P_0=0$, $P_N=1$, so $P_i=\frac{1-(q/p)^i}{1-(q/p)^N}$ ($p\ne\frac12$). Probability of reaching 0 first: $1-P_i=\frac{(q/p)^i-(q/p)^N}{1-(q/p)^N}$, or $\frac{N-i}{N}$ when $p=\frac12$.'
sources: ['CSE301 Markov_Chain slides 30-36 (gambler''s ruin)', 'Ross, Introduction to Probability Models, Ch. 4 (the gambler''s ruin problem)']
---
Let $P_i$ be the probability that, starting with $i$ units, the gambler's fortune reaches $N$ before 0. Write $q=1-p$.

**First-step analysis.** Conditioning on the outcome of the first play,

$$P_i=p\,P_{i+1}+q\,P_{i-1}\qquad(1\le i\le N-1),\qquad P_0=0,\quad P_N=1$$

Since $p+q=1$, this can be written $p\,(P_{i+1}-P_i)=q\,(P_i-P_{i-1})$, i.e.

$$P_{i+1}-P_i=\frac qp\,(P_i-P_{i-1})$$

so the differences form a geometric sequence: $P_{i+1}-P_i=\left(\frac qp\right)^iP_1$ (using $P_0=0$).

**Summing the differences.**

$$P_i=P_1\left[1+\frac qp+\left(\frac qp\right)^2+\cdots+\left(\frac qp\right)^{i-1}\right]=\begin{cases}P_1\,\dfrac{1-(q/p)^i}{1-q/p},&p\ne\frac12\\[2mm]i\,P_1,&p=\frac12\end{cases}$$

**Using $P_N=1$** to find $P_1$ gives

$$P_i=\begin{cases}\dfrac{1-(q/p)^i}{1-(q/p)^N},&p\ne\frac12\\[2mm]\dfrac iN,&p=\frac12\end{cases}$$

**Probability of reaching 0 first.** The game ends with probability 1 (with probability 1 the fortune eventually leaves the interval), so the probability that the fortune reaches 0 before $N$ is $1-P_i$:

$$1-P_i=\begin{cases}\dfrac{(q/p)^i-(q/p)^N}{1-(q/p)^N},&p\ne\frac12\\[2mm]\dfrac{N-i}{N},&p=\frac12\end{cases}$$

(By symmetry this is also the formula for reaching $N$ first with $p$ and $q$ exchanged and $i$ replaced by $N-i$.)

**Example.** $p=0.4$, $i=5$, $N=10$: $q/p=1.5$, so the probability of ruin is $\frac{1.5^5-1.5^{10}}{1-1.5^{10}}=\frac{7.59-57.67}{-56.67}\approx0.884$.
