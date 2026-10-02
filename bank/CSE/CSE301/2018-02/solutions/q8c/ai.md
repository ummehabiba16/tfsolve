---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'States $(s_1,s_2)$ (servers busy/idle): balance equations give $P_{00}=\frac12$, $P_{10}=\frac14$, $P_{01}=\frac16$, $P_{11}=\frac1{12}$. (i) $\frac1{12}$ of customers are lost. (ii) $L=\frac7{12}$, $\lambda_a=2\cdot\frac{11}{12}=\frac{11}{6}$, $W=\frac{L}{\lambda_a}=\frac{7}{22}$ h ($\approx19.1$ min). (iii) $\frac{P_{00}+P_{01}}{1-P_{11}}=\frac{8}{11}$ of entering customers are served by server 1.'
sources: ['CSE301 Queueing_Theory slides 26-31 (choosing a state space, balance equations) and 3-11 (Little''s law, PASTA)', 'Ross, Introduction to Probability Models, Ch. 6 (limiting probabilities)']
---
Rates per hour: arrivals $\lambda=2$, server 1 $\mu_1=4$, server 2 $\mu_2=6$.

**States.** Each server holds at most one customer. Let $(s_1,s_2)$ record whether server 1 and server 2 are busy (1) or idle (0).

| From | To | Rate | Event |
|:-:|:-:|:-:|:--|
| $(0,0)$ | $(1,0)$ | 2 | arrival starts with server 1 |
| $(0,1)$ | $(1,1)$ | 2 | arrival starts with server 1 |
| $(1,0)$ | $(1,1)$ | 2 | arrival finds 1 busy, 2 free: starts with server 2 |
| $(1,0)$ | $(0,1)$ | 4 | server 1 done, 2 free: customer moves to server 2 |
| $(1,1)$ | $(0,1)$ | 4 | server 1 done, 2 busy: customer departs |
| $(0,1)$ | $(0,0)$ | 6 | server 2 done |
| $(1,1)$ | $(1,0)$ | 6 | server 2 done |

**Balance equations.**

$$(0,0):\quad2P_{00}=6P_{01}$$

$$(1,0):\quad(2+4)P_{10}=2P_{00}+6P_{11}$$

$$(0,1):\quad(2+6)P_{01}=4P_{10}+4P_{11}$$

$$(1,1):\quad(4+6)P_{11}=2P_{10}+2P_{01}$$

Solving with $P_{00}+P_{10}+P_{01}+P_{11}=1$:

$$P_{00}=\frac12,\qquad P_{10}=\frac14,\qquad P_{01}=\frac16,\qquad P_{11}=\frac{1}{12}$$

(check $(1,1)$: $10\cdot\frac1{12}=\frac56=2\cdot\frac14+2\cdot\frac16$).

**(i) Fraction of customers who do not enter.** Arrivals are lost when both servers are busy; by PASTA this fraction is

$$P_{11}=\frac{1}{12}\approx0.083$$

**(ii) Average time an entering customer spends in the system.** Customers enter at rate $\lambda_a=2(1-P_{11})=\frac{11}{6}$ per hour, and the average number in the system is

$$L=P_{10}+P_{01}+2P_{11}=\frac14+\frac16+\frac16=\frac{7}{12}$$

By Little's law,

$$W=\frac{L}{\lambda_a}=\frac{7/12}{11/6}=\frac{7}{22}\text{ hour}\approx19.1\text{ minutes}$$

**(iii) Fraction of entering customers served by server 1.** A customer is served by server 1 exactly when server 1 is free on arrival (states $(0,0)$ and $(0,1)$):

$$\frac{\lambda(P_{00}+P_{01})}{\lambda_a}=\frac{\frac12+\frac16}{\frac{11}{12}}=\frac{8}{11}\approx0.727$$
