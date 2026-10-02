---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'State $(n,s)$: $n$ in orbit ($0..N$), server idle/busy; $2(N+1)$ balance equations. Served fraction $=1-P_{N,1}$; average orbit time per served customer $=\sum_n n(P_{n,0}+P_{n,1})\big/\big(\lambda(1-P_{N,1})\big)$ (Little''s law).'
sources: ['CSE301 Queueing_Theory slides 3-11 (Little''s law, balance equations, PASTA) and 26-31 (choosing the state space)', 'Ross, Introduction to Probability Models, Ch. 6 and Ch. 8 (exercises on retrial (orbit) queues)']
---
**(i) States.** Let the state be $(n,s)$, where $n\in\{0,1,\dots,N\}$ is the number of customers in orbit and $s=0$ (server idle) or $s=1$ (server busy). This gives $2(N+1)$ states. All times are exponential, so this is a continuous-time Markov chain with transitions:

| From | To | Rate | Event |
|:-:|:-:|:-:|:--|
| $(n,0)$ | $(n,1)$ | $\lambda$ | new arrival finds the server free |
| $(n,0)$, $n\ge1$ | $(n-1,1)$ | $n\theta$ | one of the $n$ orbiting customers returns to a free server |
| $(n,1)$ | $(n,0)$ | $\mu$ | service completion |
| $(n,1)$, $n<N$ | $(n+1,1)$ | $\lambda$ | arrival finds the server busy and joins the orbit |

An arrival in state $(N,1)$ is lost, and an orbiting customer who returns to a busy server goes back into orbit; neither changes the state.

**(ii) Balance equations** (rate out = rate in):

$$(0,0):\quad\lambda P_{0,0}=\mu P_{0,1}$$

$$(n,0),\ 1\le n\le N:\quad(\lambda+n\theta)P_{n,0}=\mu P_{n,1}$$

$$(0,1):\quad(\lambda+\mu)P_{0,1}=\lambda P_{0,0}+\theta P_{1,0}$$

$$(n,1),\ 1\le n\le N-1:\quad(\lambda+\mu)P_{n,1}=\lambda P_{n,0}+(n+1)\theta P_{n+1,0}+\lambda P_{n-1,1}$$

$$(N,1):\quad\mu P_{N,1}=\lambda P_{N,0}+\lambda P_{N-1,1}$$

together with $\sum_{n=0}^{N}(P_{n,0}+P_{n,1})=1$.

**(iii) Proportion of customers eventually served.** A customer is lost only if, on arrival, the server is busy and there are already $N$ customers in orbit. Everyone else is eventually served (customers in orbit keep returning until they find the server free). Poisson arrivals see time averages (PASTA), so

$$P(\text{served})=1-P_{N,1}$$

(Check: the service completion rate $\mu\sum_nP_{n,1}$ must equal the rate $\lambda(1-P_{N,1})$ of customers who are served.)

**(iv) Average time a served customer spends in orbit.** The average number of customers in orbit is

$$L_{\text{orbit}}=\sum_{n=0}^{N}n\,(P_{n,0}+P_{n,1})$$

Customers who are served enter the system at rate $\lambda(1-P_{N,1})$, and lost customers never enter the orbit. By Little's law applied to the orbit,

$$W_{\text{orbit}}=\frac{L_{\text{orbit}}}{\lambda\,(1-P_{N,1})}=\frac{\sum_{n=0}^{N}n\,(P_{n,0}+P_{n,1})}{\lambda\,(1-P_{N,1})}$$

This is the average over all served customers (those served at once count as 0). The average over only the customers who do go into orbit is $L_{\text{orbit}}\big/\big(\lambda\sum_{n=0}^{N-1}P_{n,1}\big)$.
