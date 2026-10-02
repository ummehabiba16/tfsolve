---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Failed machines form an M/M/1 queue with $\lambda=6$, $\mu=8$: $L=\lambda/(\mu-\lambda)=3$ machines down on average, so the cost rate is $10\times3=$ Tk. 30 per hour.'
sources: ['CSE301 Queueing_Theory slides 12-21 (M/M/1)', 'Ross, Introduction to Probability Models, Ch. 8 (the M/M/1 queue)']
---
**Model.** Machines fail according to a Poisson process with rate $\lambda=6$ per hour (exponential times between breakdowns), and the single repairman repairs them one at a time with exponential repair times of rate $\mu=8$ per hour. Failed machines are the "customers" and the repairman is the "server", so the number of machines out of service is an **M/M/1** queue with

$$\lambda=6,\qquad\mu=8,\qquad\rho=\frac{\lambda}{\mu}=\frac34<1$$

**Average number of machines out of service** (waiting or being repaired):

$$L=\frac{\lambda}{\mu-\lambda}=\frac{6}{8-6}=3$$

**Average cost rate.** Each machine out of service costs Tk. 10 per hour, so

$$\text{cost rate}=10\times L=10\times3=\textbf{Tk. 30 per hour}$$

(Equivalently: each failed machine is down for $W=\frac{1}{\mu-\lambda}=\frac12$ hour on average, costing Tk. 5, and 6 machines fail per hour: $6\times5=30$.)
