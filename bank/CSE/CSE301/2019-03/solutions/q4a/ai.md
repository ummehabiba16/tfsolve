---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'States $(0,0),(1,0),(0,1),(1,1),(b,1)$ with 5 balance equations. Enter: $P_{00}+P_{01}$; $L=P_{10}+P_{01}+2(P_{11}+P_{b1})$; $W=L/(\lambda(P_{00}+P_{01}))$.'
sources: ['CSE301 Queueing_Theory slides 26-31 (shoe shine shop)', 'Ross, Introduction to Probability Models, Ch. 6 (limiting probabilities: the shoeshine shop)']
---
**(i) States.** Counting customers is not enough: we must know which chair each customer occupies and whether a customer who has finished at chair 1 is stuck there. Use five states:

| State | Meaning |
|:-:|:--|
| $(0,0)$ | system empty |
| $(1,0)$ | one customer, in chair 1 |
| $(0,1)$ | one customer, in chair 2 |
| $(1,1)$ | two customers, both being served |
| $(b,1)$ | two customers; the one in chair 1 is finished but blocked, waiting for chair 2 |

A potential customer enters only when chair 1 is empty, i.e. in states $(0,0)$ and $(0,1)$.

**(i) State diagram (transition rates).**

| From | To | Rate | Event |
|:-:|:-:|:-:|:--|
| $(0,0)$ | $(1,0)$ | $\lambda$ | arrival enters chair 1 |
| $(1,0)$ | $(0,1)$ | $\mu_1$ | chair 1 done, moves to the free chair 2 |
| $(0,1)$ | $(1,1)$ | $\lambda$ | arrival enters chair 1 |
| $(0,1)$ | $(0,0)$ | $\mu_2$ | chair 2 done, leaves |
| $(1,1)$ | $(b,1)$ | $\mu_1$ | chair 1 done, chair 2 still busy: blocked |
| $(1,1)$ | $(1,0)$ | $\mu_2$ | chair 2 done, leaves |
| $(b,1)$ | $(0,1)$ | $\mu_2$ | chair 2 done; the blocked customer moves to chair 2 |

**(i) Balance equations** (rate out = rate in):

$$(0,0):\quad\lambda P_{00}=\mu_2P_{01}$$

$$(1,0):\quad\mu_1P_{10}=\lambda P_{00}+\mu_2P_{11}$$

$$(0,1):\quad(\lambda+\mu_2)P_{01}=\mu_1P_{10}+\mu_2P_{b1}$$

$$(1,1):\quad(\mu_1+\mu_2)P_{11}=\lambda P_{01}$$

$$(b,1):\quad\mu_2P_{b1}=\mu_1P_{11}$$

with $P_{00}+P_{10}+P_{01}+P_{11}+P_{b1}=1$.

**Solving.** Express everything through $P_{00}$: $P_{01}=\frac{\lambda}{\mu_2}P_{00}$, $P_{11}=\frac{\lambda P_{01}}{\mu_1+\mu_2}$, $P_{b1}=\frac{\mu_1}{\mu_2}P_{11}$, $P_{10}=\frac{\lambda P_{00}+\mu_2P_{11}}{\mu_1}$. Normalising gives, with $D$ the sum of the five numerators,

$$P_{00}=\frac{\mu_1\mu_2^2(\mu_1+\mu_2)}{D},\qquad P_{10}=\frac{\lambda\mu_2^2(\lambda+\mu_1+\mu_2)}{D},\qquad P_{01}=\frac{\lambda\mu_1\mu_2(\mu_1+\mu_2)}{D}$$

$$P_{11}=\frac{\lambda^2\mu_1\mu_2}{D},\qquad P_{b1}=\frac{\lambda^2\mu_1^2}{D}$$

For example, with $\lambda=1$, $\mu_1=1$, $\mu_2=2$: $(P_{00},P_{10},P_{01},P_{11},P_{b1})=\left(\frac{12}{37},\frac{16}{37},\frac{6}{37},\frac{2}{37},\frac{1}{37}\right)$.

**(ii) Proportion of potential customers who enter.** By PASTA, arrivals see the time-average state, and they enter only if chair 1 is empty:

$$P(\text{enter})=P_{00}+P_{01}=\frac{\mu_1\mu_2(\mu_1+\mu_2)(\lambda+\mu_2)}{D}$$

(In the example, $\frac{18}{37}$.)

**(iii) Mean number in the system.** One customer in states $(1,0),(0,1)$ and two in $(1,1),(b,1)$:

$$L=P_{10}+P_{01}+2\,(P_{11}+P_{b1})$$

(In the example, $L=\frac{16+6+2\cdot3}{37}=\frac{28}{37}$.)

**(iv) Average time an entering customer spends in the system.** Customers enter at rate $\lambda_a=\lambda(P_{00}+P_{01})$, so by Little's law

$$W=\frac{L}{\lambda_a}=\frac{P_{10}+P_{01}+2(P_{11}+P_{b1})}{\lambda\,(P_{00}+P_{01})}$$

(In the example, $W=\frac{28/37}{18/37}=\frac{14}{9}$.)
