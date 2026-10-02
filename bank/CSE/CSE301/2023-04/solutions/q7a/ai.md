---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Linear growth with immigration: $\lambda_n=n\lambda+\theta$, $\mu_n=n\mu$; rates $q_{n,n+1}=n\lambda+\theta$, $q_{n,n-1}=n\mu$, total rate out $\nu_n=n(\lambda+\mu)+\theta$.'
sources: ['Ross, Introduction to Probability Models, Ch. 6 (birth and death processes: linear growth model with immigration)']
---
In a linear growth process with immigration, the state $n$ is the population size. Each individual independently gives birth at exponential rate $\lambda$ and dies at exponential rate $\mu$, and in addition new individuals immigrate at rate $\theta$ (a Poisson stream, independent of the population).

It is a birth-death process with

$$\lambda_n=n\lambda+\theta\quad(n\ge0),\qquad\mu_n=n\mu\quad(n\ge1),\quad\mu_0=0$$

**Instantaneous transition rates.**

$$q_{n,n+1}=n\lambda+\theta,\qquad q_{n,n-1}=n\mu,\qquad q_{n,j}=0\ \text{ for }|j-n|>1$$

so the time spent in state $n$ is exponential with rate

$$\nu_n=q_{n,n+1}+q_{n,n-1}=n(\lambda+\mu)+\theta$$

and on leaving $n$ the process jumps to $n+1$ with probability $\frac{n\lambda+\theta}{n(\lambda+\mu)+\theta}$ and to $n-1$ with probability $\frac{n\mu}{n(\lambda+\mu)+\theta}$. (Without immigration, $\theta=0$, state 0 would be absorbing.)
