---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Traffic equations: $\lambda_1=5$, $\lambda_2=40$, $\lambda_3=170/3$; $L=\frac{5}{5}+\frac{40}{10}+\frac{170/3}{130/3}=1+4+\frac{17}{13}=\frac{82}{13}\approx6.31$; $W=L/30=\frac{41}{195}\approx0.210$ hour (about 12.6 minutes).'
sources: ['CSE301 Queueing_Theory slides 37-39 (open Jackson networks)', 'Ross, Introduction to Probability Models, Ch. 8 (open network of queues)']
---
This is an open (Jackson) network: Poisson external arrivals, exponential single servers, probabilistic routing.

**Traffic equations.** Let $\lambda_j$ be the total arrival rate to station $j$ (external plus internal):

$$\lambda_1=5$$

$$\lambda_2=10+\tfrac13\lambda_1+\tfrac12\lambda_3$$

$$\lambda_3=15+\tfrac13\lambda_1+\lambda_2$$

So $\lambda_1=5$, $\lambda_2=\frac{35}{3}+\frac12\lambda_3$ and $\lambda_3=\frac{50}{3}+\lambda_2$. Hence $\lambda_2=\frac{35}{3}+\frac{25}{3}+\frac12\lambda_2=20+\frac12\lambda_2$:

$$\lambda_1=5,\qquad\lambda_2=40,\qquad\lambda_3=\frac{170}{3}\approx56.67$$

Utilisations: $\rho_1=\frac{5}{10}=0.5$, $\rho_2=\frac{40}{50}=0.8$, $\rho_3=\frac{170/3}{100}=\frac{17}{30}$, all below 1, so a steady state exists. By Jackson's theorem the stations behave like independent M/M/1 queues with these arrival rates, and the long-run probability of having $n$ customers at station $j$ is $(1-\rho_j)\rho_j^n$.

**Average number of customers in the system.**

$$L=\sum_{j=1}^{3}\frac{\lambda_j}{\mu_j-\lambda_j}=\frac{5}{10-5}+\frac{40}{50-40}+\frac{170/3}{100-170/3}=1+4+\frac{17}{13}=\frac{82}{13}\approx\mathbf{6.31}$$

**Average time a customer spends in the system.** Customers enter from outside at total rate $5+10+15=30$, so by Little's law

$$W=\frac{L}{30}=\frac{82/13}{30}=\frac{41}{195}\approx\mathbf{0.210}$$

hours, i.e. about 12.6 minutes.

(This uses exactly the given M/M/1 results: station $j$ behaves like an M/M/1 queue with arrival rate $\lambda_j$, so its mean number is $\frac{\rho_j}{1-\rho_j}=\frac{\lambda_j}{\mu_j-\lambda_j}$, and the stations' numbers add.)
