---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Traffic: $\lambda_1=6$, $\lambda_2=30$, $\lambda_3=40$ ($\rho=\frac12,\frac12,\frac13$). (i) $P=(1-\frac12)\cdot(\frac12)^2(\frac12)\cdot\frac13\cdot\frac23=\frac1{72}\approx0.0139$. (ii) $L=1+1+\frac12=2.5$. (iii) $W=2.5/22=5/44\approx0.114$.'
sources: ['CSE301 Queueing_Theory slides 37-39 (open Jackson networks)', 'Ross, Introduction to Probability Models, Ch. 8 (open network of queues)']
---
This is an open (Jackson) network: Poisson external arrivals, exponential single servers, probabilistic routing.

**Traffic equations.** Let $\lambda_j$ be the total arrival rate to station $j$ (external plus internal):

$$\lambda_1=6$$

$$\lambda_2=8+\tfrac13\lambda_1+\tfrac12\lambda_3$$

$$\lambda_3=8+\tfrac13\lambda_1+\lambda_2$$

So $\lambda_1=6$, $\lambda_2=10+\frac12\lambda_3$ and $\lambda_3=10+\lambda_2$. Hence $\lambda_2=10+\frac12(10+\lambda_2)=15+\frac12\lambda_2$:

$$\lambda_1=6,\qquad\lambda_2=30,\qquad\lambda_3=40$$

Utilisations: $\rho_1=\frac{6}{12}=\frac12$, $\rho_2=\frac{30}{60}=\frac12$, $\rho_3=\frac{40}{120}=\frac13$, all below 1.

By Jackson's theorem, in the long run the stations behave like independent M/M/1 queues:

$$P(n_1,n_2,n_3)=\prod_{j=1}^{3}\rho_j^{n_j}(1-\rho_j)$$

**(i) Station 1 empty, 2 at station 2, 1 at station 3.**

$$P(0,2,1)=\left(1-\tfrac12\right)\cdot\left(\tfrac12\right)^2\left(1-\tfrac12\right)\cdot\tfrac13\left(1-\tfrac13\right)=\frac12\cdot\frac18\cdot\frac29=\frac{1}{72}\approx\mathbf{0.0139}$$

**(ii) Average number in the system.**

$$L=\sum_j\frac{\lambda_j}{\mu_j-\lambda_j}=\frac{6}{6}+\frac{30}{30}+\frac{40}{80}=1+1+0.5=\mathbf{2.5}$$

**(iii) Average time in the system.** External arrivals enter at total rate $6+8+8=22$, so by Little's law

$$W=\frac{L}{22}=\frac{2.5}{22}=\frac{5}{44}\approx\mathbf{0.114}\text{ time units}$$
