---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '(i) The special customer alternates between Expo($\theta$) absences and Expo($\mu_1$) services, so she arrives at rate $\frac{1}{1/\theta+1/\mu_1}=\frac{\theta\mu_1}{\theta+\mu_1}$. (ii) States $(n,s)$: $n$ ordinary customers, $s=0$ special away, $s=1$ special in service. (iii) Each time an ordinary customer is in service, the special one returns before he finishes with probability $\frac{\theta}{\theta+\mu}$: $P(\text{bumped }n\text{ times})=\left(\frac{\theta}{\theta+\mu}\right)^n\frac{\mu}{\theta+\mu}$.'
sources: ['Ross, Introduction to Probability Models, Ch. 6 (limiting probabilities; exercise on a preemptive special customer)', 'CSE301 Queueing_Theory slides 26-31 (choosing a state space)']
---
**(i) Average arrival rate of the special customer.** She alternates between being out of the system (exponential, mean $\frac1\theta$) and being served (exponential with rate $\mu_1$, mean $\frac{1}{\mu_1}$; she always goes straight into service). One cycle lasts on average $\frac1\theta+\frac{1}{\mu_1}$, and she arrives once per cycle, so by renewal reasoning her long-run arrival rate is

$$\lambda_s=\frac{1}{\frac1\theta+\frac1{\mu_1}}=\frac{\theta\,\mu_1}{\theta+\mu_1}$$

(Equivalently: she is away a fraction $\frac{\mu_1}{\theta+\mu_1}$ of the time and arrives at rate $\theta$ while away.)

**(ii) State space and balance equations.** Let the state be $(n,s)$, where $n\ge0$ is the number of ordinary customers in the system and $s=1$ if the special customer is in service, $s=0$ if she is away. When $s=1$ no ordinary customer is served (they all wait); when $s=0$ and $n\ge1$ one ordinary customer is in service.

Transitions: $(n,0)\to(n+1,0)$ at rate $\lambda$; $(n,0)\to(n-1,0)$ at rate $\mu$ ($n\ge1$); $(n,0)\to(n,1)$ at rate $\theta$ (special arrives, bumping anyone in service back into the queue); $(n,1)\to(n+1,1)$ at rate $\lambda$; $(n,1)\to(n,0)$ at rate $\mu_1$.

Balance equations (rate out = rate in):

$$(0,0):\quad(\lambda+\theta)P_{0,0}=\mu P_{1,0}+\mu_1P_{0,1}$$

$$(n,0),\ n\ge1:\quad(\lambda+\mu+\theta)P_{n,0}=\lambda P_{n-1,0}+\mu P_{n+1,0}+\mu_1P_{n,1}$$

$$(0,1):\quad(\lambda+\mu_1)P_{0,1}=\theta P_{0,0}$$

$$(n,1),\ n\ge1:\quad(\lambda+\mu_1)P_{n,1}=\lambda P_{n-1,1}+\theta P_{n,0}$$

with $\sum_n(P_{n,0}+P_{n,1})=1$. (Summing over $n$: $\theta\sum_nP_{n,0}=\mu_1\sum_nP_{n,1}$, so the special customer is in service a fraction $\frac{\theta}{\theta+\mu_1}$ of the time, consistent with (i).)

**(iii) Probability that an ordinary customer is bumped $n$ times.** While an ordinary customer is in service the special customer is away, so two exponential clocks compete: his service (rate $\mu$) and her return (rate $\theta$). He is bumped if her return comes first:

$$P(\text{bumped during one service attempt})=\frac{\theta}{\theta+\mu}$$

After a bump he eventually re-enters service, and by the memoryless property each new attempt is independent of the past with the same probabilities. So the number of bumps is geometric:

$$P(\text{bumped exactly }n\text{ times})=\left(\frac{\theta}{\theta+\mu}\right)^n\frac{\mu}{\theta+\mu},\qquad n=0,1,2,\dots$$

(with mean $\frac\theta\mu$ bumps).
