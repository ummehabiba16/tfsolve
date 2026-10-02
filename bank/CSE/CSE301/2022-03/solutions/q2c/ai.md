---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$P(Y=k)=\sum_{n\ge k}e^{-\lambda}\frac{\lambda^n}{n!}\binom nk(1-p)^kp^{n-k}=e^{-\lambda}\frac{(\lambda(1-p))^k}{k!}\sum_{m\ge0}\frac{(\lambda p)^m}{m!}=e^{-\lambda(1-p)}\frac{(\lambda(1-p))^k}{k!}$.'
sources: ['Ross, Introduction to Probability Models, Ch. 3 (computing probabilities by conditioning)', 'Blitzstein & Hwang, Introduction to Probability, Ch. 7 (chicken-egg story)']
---
Given $N=n$, $X\sim\text{Bin}(n,p)$ counts "successes" and $Y=N-X$ counts "failures", so

$$P(Y=k\mid N=n)=P(X=n-k\mid N=n)=\binom{n}{n-k}p^{n-k}(1-p)^k=\binom nk(1-p)^kp^{n-k},\quad0\le k\le n$$

**Condition on $N$.** For $k=0,1,2,\dots$ (only $n\ge k$ contributes):

$$P(Y=k)=\sum_{n=k}^{\infty}P(N=n)\,P(Y=k\mid N=n)=\sum_{n=k}^{\infty}e^{-\lambda}\frac{\lambda^n}{n!}\cdot\frac{n!}{k!\,(n-k)!}(1-p)^kp^{n-k}$$

Write $\lambda^n=\lambda^k\lambda^{n-k}$ and put $m=n-k$:

$$P(Y=k)=e^{-\lambda}\frac{\big(\lambda(1-p)\big)^k}{k!}\sum_{m=0}^{\infty}\frac{(\lambda p)^m}{m!}=e^{-\lambda}\frac{\big(\lambda(1-p)\big)^k}{k!}\,e^{\lambda p}$$

$$P(Y=k)=e^{-\lambda(1-p)}\frac{\big(\lambda(1-p)\big)^k}{k!},\qquad k=0,1,2,\dots$$

So $Y\sim\text{Pois}\big(\lambda(1-p)\big)$, with mean $\lambda(1-p)$. (By the same calculation $X\sim\text{Pois}(\lambda p)$, and in fact $X$ and $Y$ are independent: $P(X=j,Y=k)=P(X=j)P(Y=k)$. This is the "thinning" of a Poisson count.)
