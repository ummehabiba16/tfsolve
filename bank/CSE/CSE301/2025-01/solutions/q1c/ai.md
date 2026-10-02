---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'States $(g,0),(g,1),(b,0),(b,1)$ (economy good/bad, server idle/busy) with four balance equations and normalisation. Empty fraction $=P_{g0}+P_{b0}$; entering rate $=\lambda_1P_{g0}+\lambda_2P_{b0}$ (closed forms in the solution).'
sources: ['CSE301 Queueing_Theory slides 26-31 (choosing a state space, balance equations)', 'Ross, Introduction to Probability Models, Ch. 6 (limiting probabilities of continuous-time Markov chains)']
---
**(i) States.** The number in the system (0 or 1, since arrivals finding the server busy are lost) is not enough on its own, because the arrival rate depends on the state of the economy. Use

| State | Economy | Server |
|:-:|:-:|:-:|
| $(g,0)$ | good | idle |
| $(g,1)$ | good | busy |
| $(b,0)$ | bad | idle |
| $(b,1)$ | bad | busy |

All holding times are exponential, so this is a continuous-time Markov chain with transition rates

| From | To | Rate | Reason |
|:-:|:-:|:-:|:--|
| $(g,0)$ | $(g,1)$ | $\lambda_1$ | arrival enters |
| $(g,0)$ | $(b,0)$ | $\alpha_1$ | good period ends |
| $(g,1)$ | $(g,0)$ | $\mu$ | service completes |
| $(g,1)$ | $(b,1)$ | $\alpha_1$ | good period ends |
| $(b,0)$ | $(b,1)$ | $\lambda_2$ | arrival enters |
| $(b,0)$ | $(g,0)$ | $\alpha_2$ | bad period ends |
| $(b,1)$ | $(b,0)$ | $\mu$ | service completes |
| $(b,1)$ | $(g,1)$ | $\alpha_2$ | bad period ends |

(Arrivals in states $(g,1)$ and $(b,1)$ leave, so they cause no transition.)

**(ii) Balance equations** (rate out of a state = rate into it):

$$(g,0):\quad(\lambda_1+\alpha_1)P_{g0}=\mu P_{g1}+\alpha_2P_{b0}$$

$$(g,1):\quad(\mu+\alpha_1)P_{g1}=\lambda_1P_{g0}+\alpha_2P_{b1}$$

$$(b,0):\quad(\lambda_2+\alpha_2)P_{b0}=\mu P_{b1}+\alpha_1P_{g0}$$

$$(b,1):\quad(\mu+\alpha_2)P_{b1}=\lambda_2P_{b0}+\alpha_1P_{g1}$$

$$P_{g0}+P_{g1}+P_{b0}+P_{b1}=1$$

(One of the four balance equations is redundant.)

**(iii) Proportion of time the system is empty.**

$$P(\text{empty})=P_{g0}+P_{b0}$$

To get it explicitly: the economy alone alternates with rates $\alpha_1,\alpha_2$, so it is good a fraction $g=\frac{\alpha_2}{\alpha_1+\alpha_2}$ of the time and bad a fraction $b=\frac{\alpha_1}{\alpha_1+\alpha_2}$. Substituting $P_{g1}=g-P_{g0}$ and $P_{b1}=b-P_{b0}$ into the $(g,0)$ and $(b,0)$ equations:

$$(\lambda_1+\alpha_1+\mu)P_{g0}-\alpha_2P_{b0}=\mu g$$

$$-\alpha_1P_{g0}+(\lambda_2+\alpha_2+\mu)P_{b0}=\mu b$$

With $D=(\lambda_1+\mu+\alpha_1)(\lambda_2+\mu+\alpha_2)-\alpha_1\alpha_2$, Cramer's rule gives

$$P_{g0}=\frac{\mu\,\alpha_2\,(\alpha_1+\alpha_2+\lambda_2+\mu)}{(\alpha_1+\alpha_2)\,D}$$

$$P_{b0}=\frac{\mu\,\alpha_1\,(\alpha_1+\alpha_2+\lambda_1+\mu)}{(\alpha_1+\alpha_2)\,D}$$

and $P(\text{empty})=P_{g0}+P_{b0}$, $P_{g1}=g-P_{g0}$, $P_{b1}=b-P_{b0}$.

*Check:* if $\lambda_1=\lambda_2=\lambda$, then $D=(\lambda+\mu)(\lambda+\mu+\alpha_1+\alpha_2)$ and $P(\text{empty})=\frac{\mu}{\lambda+\mu}$, the M/M/1/1 (loss) answer, as it should be.

**(iv) Average rate at which customers enter.** Customers enter only when the server is idle, at rate $\lambda_1$ in a good period and $\lambda_2$ in a bad one:

$$\lambda_{\text{enter}}=\lambda_1P_{g0}+\lambda_2P_{b0}$$

(Equivalently, by rate in = rate out, $\lambda_{\text{enter}}=\mu(P_{g1}+P_{b1})=\mu\,(1-P_{g0}-P_{b0})$.)
