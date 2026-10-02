---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'A birth-death process is a CTMC on $\{0,1,2,\dots\}$ that moves only $n\to n+1$ (rate $\lambda_n$) or $n\to n-1$ (rate $\mu_n$). Immigration: immigrants arrive as a Poisson stream at rate $\theta$ regardless of $n$, and each individual leaves/dies at rate $\mu$ (and may give birth at rate $\lambda$): $\lambda_n=n\lambda+\theta$, $\mu_n=n\mu$.'
sources: ['Ross, Introduction to Probability Models, Ch. 6 (birth and death processes, linear growth model with immigration)']
---
**Birth-death process.** A continuous-time Markov chain $\{X(t)\}$ on the states $\{0,1,2,\dots\}$ (the population size) in which, from state $n$, the only possible transitions are

- a **birth** $n\to n+1$, at rate $\lambda_n$;
- a **death** $n\to n-1$, at rate $\mu_n$ ($\mu_0=0$).

The time spent in state $n$ is exponential with rate $\lambda_n+\mu_n$, after which the process moves up with probability $\frac{\lambda_n}{\lambda_n+\mu_n}$ and down otherwise. The M/M/1 queue ($\lambda_n=\lambda$, $\mu_n=\mu$) is an example.

**A model with immigration.** Let $X(t)$ be the number of people in a region (or the size of a population):

- **Immigration:** newcomers arrive from outside as a Poisson process with rate $\theta$. Their arrival does not depend on how many people are already there, so it contributes a constant $\theta$ to the up-rate.
- **Births:** each individual independently produces a new one at rate $\lambda$, so $n$ individuals together give rate $n\lambda$.
- **Departures/deaths:** each individual independently leaves (emigrates or dies) after an exponential time with rate $\mu$, so the down-rate is $n\mu$.

$$\lambda_n=n\lambda+\theta,\qquad\mu_n=n\mu$$

**Justification.** Using exponential (memoryless) times makes the future depend only on the current size $n$, so the process is Markov. Independent individuals make the birth and death rates proportional to $n$, while immigration is an external stream and does not grow with $n$. Without immigration ($\theta=0$) state 0 would be absorbing (an extinct population stays extinct); with $\theta>0$ the population can always be restarted, which is the essential feature of immigration.

**Behaviour.** The mean size $M(t)=E[X(t)]$ satisfies $M'(t)=\theta+(\lambda-\mu)M(t)$. The simplest special case, immigration with departures only ($\lambda=0$), is the "immigration-death" process, whose long-run distribution is Poisson with mean $\theta/\mu$.
