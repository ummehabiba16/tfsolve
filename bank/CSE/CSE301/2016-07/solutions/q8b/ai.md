---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'State $(n,m)$ = numbers at servers 1 and 2; the product form $P_{n,m}=\left(\frac{\lambda}{\mu_1}\right)^n\left(1-\frac{\lambda}{\mu_1}\right)\left(\frac{\lambda}{\mu_2}\right)^m\left(1-\frac{\lambda}{\mu_2}\right)$ satisfies the balance equations. (i) $L=\frac{\lambda}{\mu_1-\lambda}+\frac{\lambda}{\mu_2-\lambda}$; (ii) $W=\frac{L}{\lambda}=\frac{1}{\mu_1-\lambda}+\frac{1}{\mu_2-\lambda}$ (for $\lambda<\mu_1,\mu_2$).'
sources: ['CSE301 Queueing_Theory slides 32-36 (tandem queues)', 'Ross, Introduction to Probability Models, Ch. 8 (a tandem or sequential system)']
---
Assume $\lambda<\mu_1$ and $\lambda<\mu_2$, so both queues are stable.

**States and balance equations.** Let $(n,m)$ be the numbers of customers at server 1 and at server 2. Transitions: an arrival $(n,m)\to(n+1,m)$ at rate $\lambda$; a server-1 completion $(n,m)\to(n-1,m+1)$ at rate $\mu_1$ ($n\ge1$); a server-2 completion $(n,m)\to(n,m-1)$ at rate $\mu_2$ ($m\ge1$). For $n,m\ge1$ the balance equation is

$$(\lambda+\mu_1+\mu_2)P_{n,m}=\lambda P_{n-1,m}+\mu_1P_{n+1,m-1}+\mu_2P_{n,m+1}$$

with the obvious changes on the boundary, e.g. $\lambda P_{0,0}=\mu_2P_{0,1}$.

**Product-form solution.** Server 1 alone is an M/M/1 queue, and (by reversibility of the M/M/1 queue) its departures form a Poisson process of rate $\lambda$, so server 2 sees Poisson arrivals at rate $\lambda$. Guess

$$P_{n,m}=\left(\frac{\lambda}{\mu_1}\right)^n\left(1-\frac{\lambda}{\mu_1}\right)\left(\frac{\lambda}{\mu_2}\right)^m\left(1-\frac{\lambda}{\mu_2}\right)$$

Substituting into the general balance equation and dividing by $P_{n,m}$ (using $\frac{P_{n-1,m}}{P_{n,m}}=\frac{\mu_1}{\lambda}$, $\frac{P_{n+1,m-1}}{P_{n,m}}=\frac{\lambda}{\mu_1}\cdot\frac{\mu_2}{\lambda}$, $\frac{P_{n,m+1}}{P_{n,m}}=\frac{\lambda}{\mu_2}$), the right-hand side becomes

$$\lambda\cdot\frac{\mu_1}{\lambda}+\mu_1\cdot\frac{\lambda}{\mu_1}\cdot\frac{\mu_2}{\lambda}+\mu_2\cdot\frac{\lambda}{\mu_2}=\mu_1+\mu_2+\lambda$$

which equals the left-hand side, and the boundary equations check in the same way. So the numbers at the two servers are independent, each distributed as in an M/M/1 queue with arrival rate $\lambda$.

**(i) Average number of customers in the system.**

$$L=\sum_{n,m}(n+m)P_{n,m}=\frac{\lambda}{\mu_1-\lambda}+\frac{\lambda}{\mu_2-\lambda}$$

**(ii) Average time a customer spends in the system** (Little's law, $L=\lambda W$):

$$W=\frac{L}{\lambda}=\frac{1}{\mu_1-\lambda}+\frac{1}{\mu_2-\lambda}$$

(the sum of the M/M/1 times at the two servers).
