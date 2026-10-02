---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'States $(0,0),(1,0),(0,1),(1,1),(b,1)$ (contents of chairs 1 and 2; $b$ = finished but blocked in chair 1). Transitions: $(0,0)\xrightarrow{\lambda}(1,0)\xrightarrow{\mu_1}(0,1)\xrightarrow{\mu_2}(0,0)$, $(0,1)\xrightarrow{\lambda}(1,1)$, $(1,1)\xrightarrow{\mu_2}(1,0)$, $(1,1)\xrightarrow{\mu_1}(b,1)\xrightarrow{\mu_2}(0,1)$.'
sources: ['CSE301 Queueing_Theory slides 26-31 (shoe shine shop)', 'Ross, Introduction to Probability Models, Ch. 6 (limiting probabilities: the shoeshine shop)']
---
**(i) State space.** Counting customers is not enough: we must know which chair each customer occupies and whether a customer who has finished at chair 1 is stuck there. Use five states:

| State | Meaning |
|:-:|:--|
| $(0,0)$ | system empty |
| $(1,0)$ | one customer, in chair 1 |
| $(0,1)$ | one customer, in chair 2 |
| $(1,1)$ | two customers, both being served |
| $(b,1)$ | two customers; the one in chair 1 is finished but blocked, waiting for chair 2 |

A potential customer enters only when chair 1 is empty, i.e. in states $(0,0)$ and $(0,1)$.

**(ii) State transition diagram.**

| From | To | Rate | Event |
|:-:|:-:|:-:|:--|
| $(0,0)$ | $(1,0)$ | $\lambda$ | arrival enters chair 1 |
| $(1,0)$ | $(0,1)$ | $\mu_1$ | chair 1 done, moves to the free chair 2 |
| $(0,1)$ | $(1,1)$ | $\lambda$ | arrival enters chair 1 |
| $(0,1)$ | $(0,0)$ | $\mu_2$ | chair 2 done, leaves |
| $(1,1)$ | $(b,1)$ | $\mu_1$ | chair 1 done, chair 2 still busy: blocked |
| $(1,1)$ | $(1,0)$ | $\mu_2$ | chair 2 done, leaves |
| $(b,1)$ | $(0,1)$ | $\mu_2$ | chair 2 done; the blocked customer moves to chair 2 |


```text
           lam             mu1
   (0,0) --------> (1,0) --------> (0,1)
     ^               ^             | ^ |
     |               | mu2     lam | | |
     |               |             | | |
     |             (1,1) <---------+ | |
     |               |               | |
     |               | mu1           | |
     |               v          mu2  | |
     |             (b,1) ------------+ |
     |                                 |
     +-------------- mu2 --------------+
```

(`lam` $=\lambda$, `mu1` $=\mu_1$, `mu2` $=\mu_2$.) Arrivals in states $(1,0)$, $(1,1)$ and $(b,1)$ are blocked, so they cause no transition, and the only way out of $(b,1)$ is a chair-2 completion.

For later use, the diagram gives the balance equations (rate out = rate in): $\lambda P_{00}=\mu_2P_{01}$, $\mu_1P_{10}=\lambda P_{00}+\mu_2P_{11}$, $(\lambda+\mu_2)P_{01}=\mu_1P_{10}+\mu_2P_{b1}$, $(\mu_1+\mu_2)P_{11}=\lambda P_{01}$, $\mu_2P_{b1}=\mu_1P_{11}$, with the probabilities summing to 1.
