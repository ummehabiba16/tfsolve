---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '(i) The walk is symmetric, so the stationary distribution is uniform, $\pi_i=\frac1N$, and the expected return time is $\frac{1}{\pi_i}=N$. (ii) After the first step (to a neighbour), all other states are visited before returning iff the walk reaches the other neighbour of the start before the start itself: gambler''s ruin with $p=\frac12$ from 1 to $N-1$, probability $\frac{1}{N-1}$.'
sources: ['CSE301 Markov_Chain slides 19-22 (limiting probabilities) and 30-36 (gambler''s ruin)', 'Ross, Introduction to Probability Models, Ch. 4 (mean return times, gambler''s ruin)']
---
Label the states $0,1,\dots,N-1$ around the ring (so $1,\dots,N$ relabelled), start at 0, and let the walk move to each neighbour with probability $\frac12$.

**(i) Expected return time.** Every column of the transition matrix also sums to 1 (each state is entered from its two neighbours with probability $\frac12$ each), so the matrix is doubly stochastic and the uniform distribution $\pi_i=\frac1N$ satisfies $\pi_j=\sum_i\pi_iP_{ij}$. The chain is irreducible (and positive recurrent, being finite), so the mean time to return to a state is the reciprocal of its stationary probability:

$$E[\text{return time to the start}]=\frac{1}{\pi_0}=N$$

(Check, $N=3$: the walk is back after 2 steps with probability $\frac12$ and otherwise moves round; solving the first-step equations gives 3.)

**(ii) Visiting all other states before returning.** The first step goes to a neighbour, say state 1 (the case of state $N-1$ is symmetric). Cut the ring at 0 and unroll it into the path $0,1,2,\dots,N-1,0$. Starting from 1, the walk visits every state before returning to 0 exactly when it reaches state $N-1$ (the other neighbour of 0) before it reaches 0. This is the gambler's ruin problem with fair steps ($p=\frac12$), initial fortune 1 and target $N-1$:

$$P(\text{reach }N-1\text{ before }0\mid\text{start at }1)=\frac{1}{N-1}$$

So the probability that $X_n$ visits all the other states before returning to its starting position is

$$\frac{1}{N-1}\qquad(N\ge2)$$
