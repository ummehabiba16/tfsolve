---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'States $(o,0),(o,1),(p,0),(p,1)$ (non-pandemic/pandemic period, server idle/busy) with four balance equations plus normalisation. Empty fraction $=P_{o0}+P_{p0}$; entering rate $=\lambda_1P_{o0}+\lambda_2P_{p0}$ (closed forms in the solution).'
sources: ['CSE301 Queueing_Theory slides 26-31 (choosing a state space, balance equations)', 'Ross, Introduction to Probability Models, Ch. 6 (limiting probabilities of continuous-time Markov chains)']
---
Here period type $o$ is non-pandemic (arrival rate $\lambda_1$, lasts $\text{Expo}(\alpha_1)$) and type $p$ is pandemic (arrival rate $\lambda_2$, lasts $\text{Expo}(\alpha_2)$).

**(i) States.** The number in the system (0 or 1, since arrivals finding the server busy are lost) is not enough on its own, because the arrival rate depends on whether it is a pandemic period. Use

| State | Period | Server |
|:-:|:-:|:-:|
| $(o,0)$ | non-pandemic | idle |
| $(o,1)$ | non-pandemic | busy |
| $(p,0)$ | pandemic | idle |
| $(p,1)$ | pandemic | busy |

All holding times are exponential, so this is a continuous-time Markov chain with transition rates

| From | To | Rate | Reason |
|:-:|:-:|:-:|:--|
| $(o,0)$ | $(o,1)$ | $\lambda_1$ | arrival enters |
| $(o,0)$ | $(p,0)$ | $\alpha_1$ | non-pandemic period ends |
| $(o,1)$ | $(o,0)$ | $\mu$ | service completes |
| $(o,1)$ | $(p,1)$ | $\alpha_1$ | non-pandemic period ends |
| $(p,0)$ | $(p,1)$ | $\lambda_2$ | arrival enters |
| $(p,0)$ | $(o,0)$ | $\alpha_2$ | pandemic period ends |
| $(p,1)$ | $(p,0)$ | $\mu$ | service completes |
| $(p,1)$ | $(o,1)$ | $\alpha_2$ | pandemic period ends |

(Arrivals in states $(o,1)$ and $(p,1)$ leave, so they cause no transition.)

**(ii) Balance equations** (rate out of a state = rate into it):

$$(o,0):\quad(\lambda_1+\alpha_1)P_{o0}=\mu P_{o1}+\alpha_2P_{p0}$$

$$(o,1):\quad(\mu+\alpha_1)P_{o1}=\lambda_1P_{o0}+\alpha_2P_{p1}$$

$$(p,0):\quad(\lambda_2+\alpha_2)P_{p0}=\mu P_{p1}+\alpha_1P_{o0}$$

$$(p,1):\quad(\mu+\alpha_2)P_{p1}=\lambda_2P_{p0}+\alpha_1P_{o1}$$

$$P_{o0}+P_{o1}+P_{p0}+P_{p1}=1$$

(One of the four balance equations is redundant.)

**(iii) Proportion of time the system is empty.**

$$P(\text{empty})=P_{o0}+P_{p0}$$

To get it explicitly: the periods alone alternate with rates $\alpha_1,\alpha_2$, so a fraction $u=\frac{\alpha_2}{\alpha_1+\alpha_2}$ of the time is non-pandemic and a fraction $v=\frac{\alpha_1}{\alpha_1+\alpha_2}$ is pandemic. Substituting $P_{o1}=u-P_{o0}$ and $P_{p1}=v-P_{p0}$ into the $(o,0)$ and $(p,0)$ equations:

$$(\lambda_1+\alpha_1+\mu)P_{o0}-\alpha_2P_{p0}=\mu u$$

$$-\alpha_1P_{o0}+(\lambda_2+\alpha_2+\mu)P_{p0}=\mu v$$

With $D=(\lambda_1+\mu+\alpha_1)(\lambda_2+\mu+\alpha_2)-\alpha_1\alpha_2$, Cramer's rule gives

$$P_{o0}=\frac{\mu\,\alpha_2\,(\alpha_1+\alpha_2+\lambda_2+\mu)}{(\alpha_1+\alpha_2)\,D}$$

$$P_{p0}=\frac{\mu\,\alpha_1\,(\alpha_1+\alpha_2+\lambda_1+\mu)}{(\alpha_1+\alpha_2)\,D}$$

and $P(\text{empty})=P_{o0}+P_{p0}$, $P_{o1}=u-P_{o0}$, $P_{p1}=v-P_{p0}$.

*Check:* if $\lambda_1=\lambda_2=\lambda$, then $D=(\lambda+\mu)(\lambda+\mu+\alpha_1+\alpha_2)$ and $P(\text{empty})=\frac{\mu}{\lambda+\mu}$, the M/M/1/1 (loss) answer, as it should be.

**(iv) Average rate at which customers enter.** Customers enter only when the server is idle, at rate $\lambda_1$ in a non-pandemic period and $\lambda_2$ in a pandemic one:

$$\lambda_{\text{enter}}=\lambda_1P_{o0}+\lambda_2P_{p0}$$

(Equivalently, by rate in = rate out, $\lambda_{\text{enter}}=\mu(P_{o1}+P_{p1})=\mu\,(1-P_{o0}-P_{p0})$.)
