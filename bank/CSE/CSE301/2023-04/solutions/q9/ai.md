---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Traffic equations $\lambda_1=4+\frac14\lambda_2$, $\lambda_2=5+\frac12\lambda_1$ give $\lambda_1=6$, $\lambda_2=8$; $P(n,m)=(\frac34)^n\frac14(\frac45)^m\frac15$; $L=\frac{6}{8-6}+\frac{8}{10-8}=7$; $W=L/(4+5)=7/9$.'
sources: ['CSE301 Queueing_Theory slides 37-39 (open Jackson networks)', 'Ross, Introduction to Probability Models, Ch. 8 (network of queues: open systems)']
---
This is an open (Jackson) network: Poisson external arrivals, exponential service, probabilistic routing.

**Traffic equations.** Let $\lambda_j$ be the total arrival rate to server $j$ (external plus internal):

$$\lambda_1=4+\tfrac14\lambda_2,\qquad\lambda_2=5+\tfrac12\lambda_1$$

Substituting the second into the first: $\lambda_1=4+\frac14\left(5+\frac12\lambda_1\right)=5.25+\frac18\lambda_1$, so

$$\lambda_1=6,\qquad\lambda_2=5+3=8$$

Both servers are stable: $\lambda_1/\mu_1=6/8=\frac34<1$ and $\lambda_2/\mu_2=8/10=\frac45<1$.

**Limiting probabilities.** By Jackson's theorem the two servers behave like independent M/M/1 queues with arrival rates $\lambda_j$ (product form):

$$P(n\text{ at server 1},\ m\text{ at server 2})=\left(\frac{\lambda_1}{\mu_1}\right)^n\left(1-\frac{\lambda_1}{\mu_1}\right)\left(\frac{\lambda_2}{\mu_2}\right)^m\left(1-\frac{\lambda_2}{\mu_2}\right)$$

$$=\left(\frac34\right)^n\frac14\left(\frac45\right)^m\frac15,\qquad n,m\ge0$$

**Average number in the system.**

$$L=\frac{\lambda_1}{\mu_1-\lambda_1}+\frac{\lambda_2}{\mu_2-\lambda_2}=\frac{6}{2}+\frac{8}{2}=3+4=\mathbf{7}$$

**Average time in the system.** Customers enter from outside at total rate $4+5=9$, so by Little's law

$$W=\frac{L}{4+5}=\frac79\approx\mathbf{0.778}\text{ time units}$$
