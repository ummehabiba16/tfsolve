---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '(i) States 0 (free), $w_1$ (washing a type-1), $w_3$ (washing a type-3), $c$ (cutting a type-2 or type-3; identical from then on). (ii) $\lambda P_0=\mu_1P_{w_1}+\mu_2P_c$, $\mu_1P_{w_1}=\lambda p_1P_0$, $\mu_1P_{w_3}=\lambda p_3P_0$, $\mu_2P_c=\lambda p_2P_0+\mu_1P_{w_3}$. With $D=1+\frac{\lambda(p_1+p_3)}{\mu_1}+\frac{\lambda(p_2+p_3)}{\mu_2}$: (iii) $P_c=\frac{\lambda(p_2+p_3)/\mu_2}{D}$; (iv) entering rate $\lambda P_0=\frac{\lambda}{D}$.'
sources: ['Ross, Introduction to Probability Models, Ch. 6 (limiting probabilities)', 'CSE301 Queueing_Theory slides 26-31 (choosing a state space)']
---
**(i) Four states.** The server holds at most one customer (a potential customer who finds the server busy leaves). What matters for the future is what the server is doing:

| State | Meaning |
|:-:|:--|
| $0$ | server free |
| $w_1$ | washing a type-1 customer (who leaves after the wash) |
| $w_3$ | washing a type-3 customer (who will then be cut) |
| $c$ | cutting hair (a type-2 customer, or a type-3 customer after the wash) |

A type-2 customer being cut and a type-3 customer being cut behave identically (cut at rate $\mu_2$, then leave), so they can share the state $c$. All times are exponential, so this is a continuous-time Markov chain with transitions

$$0\xrightarrow{\lambda p_1}w_1,\qquad0\xrightarrow{\lambda p_2}c,\qquad0\xrightarrow{\lambda p_3}w_3,\qquad w_1\xrightarrow{\mu_1}0,\qquad w_3\xrightarrow{\mu_1}c,\qquad c\xrightarrow{\mu_2}0$$

**(ii) Balance equations** (rate out = rate in):

$$0:\quad\lambda P_0=\mu_1P_{w_1}+\mu_2P_c$$

$$w_1:\quad\mu_1P_{w_1}=\lambda p_1P_0$$

$$w_3:\quad\mu_1P_{w_3}=\lambda p_3P_0$$

$$c:\quad\mu_2P_c=\lambda p_2P_0+\mu_1P_{w_3}$$

$$P_0+P_{w_1}+P_{w_3}+P_c=1$$

**Solution.** $P_{w_1}=\frac{\lambda p_1}{\mu_1}P_0$, $P_{w_3}=\frac{\lambda p_3}{\mu_1}P_0$ and $P_c=\frac{\lambda(p_2+p_3)}{\mu_2}P_0$. With

$$D=1+\frac{\lambda(p_1+p_3)}{\mu_1}+\frac{\lambda(p_2+p_3)}{\mu_2}$$

normalisation gives $P_0=\frac1D$.

**(iii) Proportion of time the server is cutting hair.**

$$P_c=\frac{\lambda(p_2+p_3)/\mu_2}{1+\frac{\lambda(p_1+p_3)}{\mu_1}+\frac{\lambda(p_2+p_3)}{\mu_2}}$$

**(iv) Average arrival rate of entering customers.** Potential customers enter only when the server is free (PASTA):

$$\lambda_{\text{enter}}=\lambda P_0=\frac{\lambda}{1+\frac{\lambda(p_1+p_3)}{\mu_1}+\frac{\lambda(p_2+p_3)}{\mu_2}}$$

(Check: each entering customer needs on average $\frac{p_1+p_3}{\mu_1}+\frac{p_2+p_3}{\mu_2}$ of server time, and $\lambda_{\text{enter}}$ times this equals the busy fraction $1-P_0$.)
