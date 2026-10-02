---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$P(e_j\text{ ahead of }e_i)=\frac{P_j}{P_i+P_j}$ in the long run, so $E[\text{position of the requested element}]=\sum_iP_i\big(1+\sum_{j\ne i}\frac{P_j}{P_i+P_j}\big)=1+2\sum_{i<j}\frac{P_iP_j}{P_i+P_j}$.'
sources: ['Ross, Introduction to Probability Models, Ch. 3 (computing expectations by conditioning: list ordering)']
---
Let $P_i$ be the probability that a request is for $e_i$ ($\sum_iP_i=1$).

**Key observation.** After the process has run a long time, $e_j$ is ahead of $e_i$ in the list if and only if, among all past requests for $e_i$ or $e_j$, the most recent one was for $e_j$ (every requested element jumps to the front, so the more recently requested of the two is in front). Each request that is for $e_i$ or $e_j$ is for $e_j$ with probability $\frac{P_j}{P_i+P_j}$, so in the long run

$$P(e_j\text{ precedes }e_i)=\frac{P_j}{P_i+P_j}$$

**Position of $e_i$.** The position of $e_i$ is 1 plus the number of elements ahead of it:

$$\text{Pos}(e_i)=1+\sum_{j\ne i}I\{e_j\text{ precedes }e_i\}$$

$$E[\text{Pos}(e_i)]=1+\sum_{j\ne i}\frac{P_j}{P_i+P_j}$$

**Position of the requested element.** The next request is independent of the current ordering (which depends only on past requests). Conditioning on which element is requested:

$$E[\text{position of the requested element}]=\sum_{i=1}^{n}P_i\,E[\text{Pos}(e_i)]$$

$$=\sum_{i=1}^{n}P_i\left(1+\sum_{j\ne i}\frac{P_j}{P_i+P_j}\right)=1+\sum_{i=1}^{n}\sum_{j\ne i}\frac{P_iP_j}{P_i+P_j}$$

$$=1+2\sum_{i<j}\frac{P_iP_j}{P_i+P_j}$$

**Check.** If all $P_i=\frac1n$, each term is $\frac{1}{2n}$ and there are $\binom n2$ pairs, giving $1+\frac{n-1}{2}=\frac{n+1}{2}$, the average position in a random order, as expected.
