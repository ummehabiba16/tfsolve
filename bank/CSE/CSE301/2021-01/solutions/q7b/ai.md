---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'The list ordering is a Markov chain on the $n!$ permutations; it is time reversible with stationary probabilities $\pi(i_1,\dots,i_n)=C\,P_{i_1}^{n-1}P_{i_2}^{n-2}\cdots P_{i_{n-1}}$ (check: $\pi(\dots i\,j\dots)P_j=\pi(\dots j\,i\dots)P_i$). The long-run average position of the requested element is $\sum_\sigma\pi(\sigma)\sum_{m=1}^{n}m\,P_{\sigma_m}$ (for $n=2$: $1+2P_1P_2$).'
sources: ['Ross, Introduction to Probability Models, Ch. 4 (time reversible Markov chains: the transposition rule)']
---
**Markov chain.** The state is the current ordering $\sigma=(i_1,i_2,\dots,i_n)$ of the list ($i_m$ is the element in position $m$). If the element in position $m\ge2$ is requested (probability $P_{i_m}$), it swaps places with the element in position $m-1$; if the front element is requested, nothing changes. Requests are independent, so the orderings form an irreducible, aperiodic Markov chain on the $n!$ permutations.

**Stationary distribution (time reversibility).** Guess

$$\pi(i_1,i_2,\dots,i_n)=C\,P_{i_1}^{n-1}P_{i_2}^{n-2}\cdots P_{i_{n-1}}^{1}P_{i_n}^{0}$$

(elements nearer the front carry higher powers of their request probabilities), with $C$ chosen so that the probabilities sum to 1.

Check the detailed balance equations. Let $\sigma$ have $i$ in position $k$ and $j$ in position $k+1$, and let $\sigma'$ be $\sigma$ with $i$ and $j$ swapped. The chain goes $\sigma\to\sigma'$ when $j$ is requested and $\sigma'\to\sigma$ when $i$ is requested. In $\pi(\sigma)$ the factors for $i$ and $j$ are $P_i^{n-k}P_j^{n-k-1}$, and in $\pi(\sigma')$ they are $P_j^{n-k}P_i^{n-k-1}$; all other factors agree. So

$$\frac{\pi(\sigma)}{\pi(\sigma')}=\frac{P_i}{P_j}\qquad\Longrightarrow\qquad\pi(\sigma)\,P_j=\pi(\sigma')\,P_i$$

which is exactly detailed balance (rate $\sigma\to\sigma'$ equals rate $\sigma'\to\sigma$). Every transition between different states is of this form, so the guessed $\pi$ satisfies $\pi_j=\sum_i\pi_iP_{ij}$ and is the stationary distribution; the chain is time reversible. (A numerical solution of the chain for $n=3$ confirms it.)

**Long-run average position of the requested element.** In the long run the ordering is $\sigma$ with probability $\pi(\sigma)$, and the next request is independent of the current ordering, so

$$E[\text{position}]=\sum_{\sigma}\pi(\sigma)\sum_{m=1}^{n}m\,P_{\sigma_m}=C\sum_{(i_1,\dots,i_n)}\left(\prod_{m=1}^{n}P_{i_m}^{n-m}\right)\left(\sum_{m=1}^{n}m\,P_{i_m}\right)$$

**Example $n=2$.** $\pi(1,2)=\frac{P_1}{P_1+P_2}=P_1$ and $\pi(2,1)=P_2$. Then

$$E[\text{position}]=P_1\big(1\cdot P_1+2P_2\big)+P_2\big(1\cdot P_2+2P_1\big)=(P_1+P_2)^2+2P_1P_2=1+2P_1P_2$$

(For $n=2$ the transposition rule coincides with move-to-front. For $n=3$ with $P=(0.5,0.3,0.2)$ the formula gives $1.874$, slightly better than move-to-front's $1.901$; the transposition rule never does worse in the long run.)
