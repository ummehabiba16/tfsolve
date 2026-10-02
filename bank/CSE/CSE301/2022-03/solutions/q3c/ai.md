---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'A counting process $N(t)$ counts events in $[0,t]$: $N(t)\ge0$, integer-valued, non-decreasing, $N(t)-N(s)$ = events in $(s,t]$. It is a Poisson process with rate $\lambda$ if $N(0)=0$, it has independent increments, and $N(s+t)-N(s)\sim\text{Pois}(\lambda t)$ (equivalently: stationary increments, $P\{N(h)=1\}=\lambda h+o(h)$, $P\{N(h)\ge2\}=o(h)$).'
sources: ['Ross, Introduction to Probability Models, Ch. 5 (counting processes, definition of the Poisson process)']
---
**Counting process.** A stochastic process $\{N(t),t\ge0\}$ is a counting process if $N(t)$ is the total number of events that have occurred up to time $t$ (customers arriving, calls, failures, ...). It must satisfy:

- $N(t)\ge0$;
- $N(t)$ is integer-valued;
- if $s<t$ then $N(s)\le N(t)$;
- for $s<t$, $N(t)-N(s)$ is the number of events in the interval $(s,t]$.

Two further properties a counting process may have:

- **Independent increments:** the numbers of events in disjoint time intervals are independent (e.g. $N(10)$ is independent of $N(15)-N(10)$).
- **Stationary increments:** the distribution of the number of events in an interval depends only on its length, i.e. $N(t+s)-N(s)$ has the same distribution for all $s$.

**When is it a Poisson process?** A counting process is a Poisson process with rate $\lambda>0$ if

- $N(0)=0$;
- it has independent increments;
- the number of events in any interval of length $t$ is Poisson with mean $\lambda t$: for all $s,t\ge0$,

$$P\{N(t+s)-N(s)=n\}=e^{-\lambda t}\frac{(\lambda t)^n}{n!},\qquad n=0,1,2,\dots$$

Equivalently: $N(0)=0$, independent and stationary increments, $P\{N(h)=1\}=\lambda h+o(h)$ and $P\{N(h)\ge2\}=o(h)$ (events occur one at a time, at rate $\lambda$). Then the inter-arrival times are i.i.d. $\text{Expo}(\lambda)$.
