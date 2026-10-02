---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Birth-death with $\mu_1=\mu$, $\mu_n=2\mu$ ($n\ge2$): $P_0=\frac{2\mu-\lambda}{2\mu+\lambda}$, $P_n=2(\frac{\lambda}{2\mu})^nP_0$. Rate $0\to1=\lambda P_0$, rate $2\to1=2\mu P_2=\frac{\lambda^2(2\mu-\lambda)}{\mu(2\mu+\lambda)}$. Clerk checking: $P(n\ge2)+P_{1C}=\frac{\lambda^2(\lambda+4\mu)}{2\mu(\lambda+\mu)(\lambda+2\mu)}$.'
sources: ['CSE301 Queueing_Theory slides 6-11 (balance equations) and 26-31 (choosing the state space)', 'Ross, Introduction to Probability Models, Ch. 6 (birth and death processes, limiting probabilities)']
---
Assume $\lambda<2\mu$ so that a steady state exists.

**(i) The proportions $P_n$.** With $n$ customers in the system, the total service rate is $0$ for $n=0$, $\mu$ for $n=1$ (one customer is being served, by one of the two counters) and $2\mu$ for $n\ge2$ (the clerk has joined, so both counters work). Arrivals occur at rate $\lambda$ in every state. So the number in the system is a birth-death process with

$$\lambda_n=\lambda,\qquad\mu_1=\mu,\qquad\mu_n=2\mu\ (n\ge2)$$

Balance across the cut between $n$ and $n+1$ (rate up = rate down):

$$\lambda P_0=\mu P_1,\qquad\lambda P_n=2\mu P_{n+1}\ (n\ge1)$$

$$P_1=\frac{\lambda}{\mu}P_0,\qquad P_n=\frac{\lambda}{\mu}\left(\frac{\lambda}{2\mu}\right)^{n-1}P_0=2\left(\frac{\lambda}{2\mu}\right)^nP_0\quad(n\ge1)$$

Normalising, $1=P_0\Big[1+\frac{\lambda}{\mu}\sum_{n\ge1}\big(\frac{\lambda}{2\mu}\big)^{n-1}\Big]=P_0\Big[1+\frac{2\lambda}{2\mu-\lambda}\Big]$, so

$$P_0=\frac{2\mu-\lambda}{2\mu+\lambda},\qquad P_n=2\left(\frac{\lambda}{2\mu}\right)^n\frac{2\mu-\lambda}{2\mu+\lambda}\quad(n\ge1)$$

**(ii) Transition rates.** The number goes from 0 to 1 at each arrival while the system is empty, and from 2 to 1 at each service completion while there are two customers (total service rate $2\mu$):

$$\text{rate}(0\to1)=\lambda P_0=\frac{\lambda(2\mu-\lambda)}{2\mu+\lambda}$$

$$\text{rate}(2\to1)=2\mu P_2=2\mu\cdot\frac{\lambda^2}{2\mu^2}P_0=\frac{\lambda^2(2\mu-\lambda)}{\mu(2\mu+\lambda)}$$

(As a check, the second equals the rate $\lambda P_1$ from 1 to 2.)

**(iii) Proportion of time the stock clerk is checking.** The clerk checks whenever $n\ge2$. With $n=1$ we must be careful: if the permanent checker finishes first when $n=2$, the clerk keeps serving the remaining customer until he completes his service. So split state 1 into $1_P$ (the permanent checker serves the one customer) and $1_C$ (the clerk serves it). State $1_C$ is entered only from state 2 when the permanent checker completes (rate $\mu$), and is left by an arrival (to state 2, rate $\lambda$) or by the clerk completing (to state 0, rate $\mu$):

$$(\lambda+\mu)P_{1C}=\mu P_2\ \Rightarrow\ P_{1C}=\frac{\mu P_2}{\lambda+\mu}$$

Hence

$$P(\text{clerk checking})=\sum_{n\ge2}P_n+P_{1C}=1-P_0-P_1+\frac{\mu P_2}{\lambda+\mu}$$

Substituting $1-P_0-P_1=\frac{\lambda^2}{\mu(\lambda+2\mu)}$ and $P_{1C}=\frac{\lambda^2(2\mu-\lambda)}{2\mu(\lambda+\mu)(\lambda+2\mu)}$:

$$P(\text{clerk checking})=\frac{\lambda^2(\lambda+4\mu)}{2\mu(\lambda+\mu)(\lambda+2\mu)}$$

(A numerical solution of the full chain with states $0,1_P,1_C,2,3,\dots$ for $\lambda=1.3$, $\mu=1$ gives $0.5901$, matching this formula.)
