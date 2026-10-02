---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Balance: $\lambda P_0=\mu P_1$, $(\lambda+\mu)P_n=\lambda P_{n-1}+\mu P_{n+1}$, $\mu P_N=\lambda P_{N-1}$; so $P_n=\frac{\rho^n(1-\rho)}{1-\rho^{N+1}}$ ($\rho=\lambda/\mu\ne1$) and $L=\frac{\rho[1-(N+1)\rho^N+N\rho^{N+1}]}{(1-\rho)(1-\rho^{N+1})}$ (for $\rho=1$: $P_n=\frac{1}{N+1}$, $L=N/2$).'
sources: ['CSE301 Queueing_Theory slides 22-25 (M/M/1 with finite capacity N)', 'Ross, Introduction to Probability Models, Ch. 8 (a single-server exponential system having finite capacity)']
---
Customers arrive as a Poisson process with rate $\lambda$, service is exponential with rate $\mu$, and at most $N$ customers can be in the system (an arrival finding $N$ present is lost). Let $P_n$, $n=0,\dots,N$, be the long-run proportion of time with $n$ customers, and $\rho=\lambda/\mu$.

**Balance equations** (rate out = rate in):

$$\text{state }0:\quad\lambda P_0=\mu P_1$$

$$\text{state }n,\ 1\le n\le N-1:\quad(\lambda+\mu)P_n=\lambda P_{n-1}+\mu P_{n+1}$$

$$\text{state }N:\quad\mu P_N=\lambda P_{N-1}$$

(In state $N$ arrivals are lost, so the only way out is a service completion.)

**Solution.** Adding the equations for states $0,\dots,n$ gives $\lambda P_n=\mu P_{n+1}$ for $n=0,\dots,N-1$, so

$$P_n=\rho^nP_0,\qquad n=0,1,\dots,N$$

Normalising with a finite geometric sum, $P_0\sum_{n=0}^{N}\rho^n=P_0\frac{1-\rho^{N+1}}{1-\rho}=1$:

$$P_n=\frac{\rho^n(1-\rho)}{1-\rho^{N+1}},\qquad n=0,\dots,N\quad(\rho\ne1)$$

(No condition $\lambda<\mu$ is needed, because the state space is finite. If $\rho=1$, $P_n=\frac{1}{N+1}$.)

**Average number in the system.** Using $\sum_{n=0}^{N}n\rho^n=\rho\frac{d}{d\rho}\frac{1-\rho^{N+1}}{1-\rho}=\frac{\rho\,[1-(N+1)\rho^N+N\rho^{N+1}]}{(1-\rho)^2}$:

$$L=\sum_{n=0}^{N}nP_n=\frac{\rho\,\big[1-(N+1)\rho^N+N\rho^{N+1}\big]}{(1-\rho)(1-\rho^{N+1})}$$

or, in terms of $\lambda$ and $\mu$,

$$L=\frac{\lambda\,\big[1+N(\lambda/\mu)^{N+1}-(N+1)(\lambda/\mu)^N\big]}{(\mu-\lambda)\big(1-(\lambda/\mu)^{N+1}\big)}$$

For $\rho=1$, $L=\frac{0+1+\cdots+N}{N+1}=\frac N2$. (Customers actually enter at rate $\lambda_a=\lambda(1-P_N)$, so by Little's law $W=L/\lambda_a$.)
