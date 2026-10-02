---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'The $k$-th moment is $E[X^k]$; $M(t)=E[e^{tX}]$ gives $E[X^k]=M^{(k)}(0)$. For $\text{Bin}(n,p)$: $M(t)=\sum_k\binom nk(pe^t)^k(1-p)^{n-k}=(pe^t+1-p)^n$. For independent $X\sim\text{Bin}(n,p)$, $Y\sim\text{Bin}(m,p)$: $M_{X+Y}=(pe^t+1-p)^{n+m}$, so $X+Y\sim\text{Bin}(n+m,p)$.'
sources: ['Ross, Introduction to Probability Models, Ch. 2 (moment generating functions)', 'Blitzstein & Hwang, Introduction to Probability, Ch. 6']
---
**Moments.** The $k$-th moment of a random variable $X$ is $E[X^k]$ ($k=1,2,\dots$): $E[X]$ is the mean, and $\mathrm{Var}(X)=E[X^2]-(E[X])^2$.

**From the moment generating function.** $M(t)=E[e^{tX}]$. Expanding $e^{tX}=\sum_k\frac{t^kX^k}{k!}$ and taking expectations, $M(t)=\sum_k\frac{E[X^k]}{k!}t^k$, so

$$E[X^k]=M^{(k)}(0)=\frac{d^k}{dt^k}M(t)\Big|_{t=0}$$

(equivalently, differentiating under the expectation, $M^{(k)}(t)=E[X^ke^{tX}]$, then put $t=0$).

**MGF of the binomial.** For $X\sim\text{Bin}(n,p)$,

$$M(t)=\sum_{k=0}^{n}e^{tk}\binom nkp^k(1-p)^{n-k}=\sum_{k=0}^{n}\binom nk\left(pe^t\right)^k(1-p)^{n-k}=\left(pe^t+1-p\right)^n$$

by the binomial theorem. (Check: $M'(t)=n(pe^t+1-p)^{n-1}pe^t$, so $E[X]=M'(0)=np$; differentiating again gives $E[X^2]=n(n-1)p^2+np$ and $\mathrm{Var}(X)=np(1-p)$.)

**Distribution of $X+Y$.** If $X\sim\text{Bin}(n,p)$ and $Y\sim\text{Bin}(m,p)$ are independent,

$$M_{X+Y}(t)=M_X(t)\,M_Y(t)=\left(pe^t+1-p\right)^n\left(pe^t+1-p\right)^m=\left(pe^t+1-p\right)^{n+m}$$

which is the MGF of $\text{Bin}(n+m,\ p)$. Since the MGF determines the distribution,

$$X+Y\sim\text{Bin}(n+m,\ p)$$

(Intuitively: $n+m$ independent trials with the same success probability $p$.)
