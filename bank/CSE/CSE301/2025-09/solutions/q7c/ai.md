---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'State $n$ = number of machines down ($0..M$), a birth-death process with $\lambda_n=(M-n)\lambda$, $\mu_n=\mu$: $P_n=\frac{M!}{(M-n)!}(\frac\lambda\mu)^nP_0$, $P_0=\big[\sum_{n=0}^{M}\frac{M!}{(M-n)!}(\frac\lambda\mu)^n\big]^{-1}$; $L=\sum_nnP_n=M-\frac{\mu(1-P_0)}{\lambda}$; a given machine works a fraction $\frac{M-L}{M}=\frac{\mu(1-P_0)}{M\lambda}$ of the time.'
sources: ['Ross, Introduction to Probability Models, Ch. 6 (birth and death processes: a machine repair model)', 'CSE301 Queueing_Theory slides 6-11 (balance equations)']
---
**(i) State space.** Let $X(t)$ be the number of machines out of service (broken, waiting or being repaired), with states $\{0,1,\dots,M\}$. When $n$ machines are down, $M-n$ are working, each failing at rate $\lambda$, so the next failure comes at rate $(M-n)\lambda$; if $n\ge1$ the technician is repairing one machine, which finishes at rate $\mu$. So $X(t)$ is a birth-death process with

$$\lambda_n=(M-n)\lambda\quad(0\le n<M),\qquad\mu_n=\mu\quad(1\le n\le M)$$

**(ii) Steady-state probabilities.** Balancing the flow between $n$ and $n+1$ (rate up = rate down):

$$(M-n)\lambda\,P_n=\mu\,P_{n+1},\qquad n=0,1,\dots,M-1$$

so

$$P_n=\frac{M(M-1)\cdots(M-n+1)\lambda^n}{\mu^n}P_0=\frac{M!}{(M-n)!}\left(\frac{\lambda}{\mu}\right)^nP_0,\qquad n=0,\dots,M$$

and, since the probabilities sum to 1,

$$P_0=\left[\sum_{n=0}^{M}\frac{M!}{(M-n)!}\left(\frac{\lambda}{\mu}\right)^n\right]^{-1}$$

(The state space is finite, so these exist for all $\lambda,\mu>0$.)

**(iii) Long-run expected number of machines out of service.**

$$L=\sum_{n=0}^{M}nP_n=\frac{\sum_{n=0}^{M}n\frac{M!}{(M-n)!}(\lambda/\mu)^n}{\sum_{n=0}^{M}\frac{M!}{(M-n)!}(\lambda/\mu)^n}$$

A simpler form follows from rate in = rate out: machines are repaired at rate $\mu(1-P_0)$ (the technician is busy whenever $n\ge1$) and break down at rate $\lambda\,E[M-X]=\lambda(M-L)$. Equating,

$$L=M-\frac{\mu\,(1-P_0)}{\lambda}$$

**(iv) Fraction of time a particular machine is working.** By symmetry each machine is working a fraction $E[M-X]/M$ of the time:

$$P(\text{a given machine works})=\sum_{n=0}^{M}\frac{M-n}{M}P_n=\frac{M-L}{M}=\frac{\mu\,(1-P_0)}{M\lambda}$$

*Example:* $M=2$, $\lambda=1$, $\mu=2$: $P_0:P_1:P_2=1:1:\frac12$, so $P_0=0.4$, $L=1(0.4)+2(0.2)=0.8$ and each machine works $\frac{2-0.8}{2}=60\%$ of the time (check: $\frac{2(1-0.4)}{2\cdot1}=0.6$).
