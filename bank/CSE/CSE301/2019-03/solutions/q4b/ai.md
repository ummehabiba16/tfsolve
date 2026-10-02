---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Balance equations give $P_n=(\lambda/\mu)^n(1-\lambda/\mu)$; then $L=\frac{\lambda}{\mu-\lambda}$, $W=\frac{1}{\mu-\lambda}$, $L_Q=\frac{\lambda^2}{\mu(\mu-\lambda)}$, $W_Q=\frac{\lambda}{\mu(\mu-\lambda)}$ (for $\lambda<\mu$).'
sources: ['CSE301 Queueing_Theory slides 12-21 (M/M/1: balance equations, L, W, L_Q, W_Q)', 'Ross, Introduction to Probability Models, Ch. 8 (the M/M/1 queue)']
---
Let $P_n$ be the long-run proportion of time with $n$ customers in the system. The number in the system is a birth-death process with birth rate $\lambda$ and death rate $\mu$ (for $n\ge1$); we need $\lambda<\mu$ for a steady state.

**Balance equations** (rate out = rate in):

$$\text{state }0:\quad\lambda P_0=\mu P_1$$

$$\text{state }n\ge1:\quad(\lambda+\mu)P_n=\lambda P_{n-1}+\mu P_{n+1}$$

Adding the equations for states $0,\dots,n$ telescopes to $\lambda P_n=\mu P_{n+1}$, so with $\rho=\lambda/\mu$

$$P_{n}=\rho^nP_0,\qquad\sum_{n\ge0}\rho^nP_0=1\ \Rightarrow\ P_0=1-\rho$$

$$P_n=\left(\frac{\lambda}{\mu}\right)^n\left(1-\frac{\lambda}{\mu}\right),\qquad n\ge0$$

**(i) Average number in the system.**

$$L=\sum_{n\ge0}nP_n=(1-\rho)\sum_{n\ge0}n\rho^n=(1-\rho)\frac{\rho}{(1-\rho)^2}=\frac{\rho}{1-\rho}=\frac{\lambda}{\mu-\lambda}$$

**(ii) Average time in the system** (Little's law, $L=\lambda W$):

$$W=\frac{L}{\lambda}=\frac{1}{\mu-\lambda}$$

**(iv) Average time in the queue.** The time in the system is the waiting time plus one service time of mean $1/\mu$:

$$W_Q=W-\frac1\mu=\frac{1}{\mu-\lambda}-\frac1\mu=\frac{\lambda}{\mu(\mu-\lambda)}$$

**(iii) Average number in the queue** (Little's law for the queue):

$$L_Q=\lambda W_Q=\frac{\lambda^2}{\mu(\mu-\lambda)}$$

(Check: $L-L_Q=\frac{\lambda}{\mu-\lambda}-\frac{\lambda^2}{\mu(\mu-\lambda)}=\frac{\lambda}{\mu}=P(\text{server busy})$, the mean number in service.)
