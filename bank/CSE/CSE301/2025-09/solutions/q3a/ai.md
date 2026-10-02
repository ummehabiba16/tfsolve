---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'For $X\sim\text{Bin}(n,p)$: $E[X]=np$ (using $k\binom nk=n\binom{n-1}{k-1}$) and $E[X(X-1)]=n(n-1)p^2$, so $\mathrm{Var}(X)=np(1-p)$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 3-4 (binomial distribution, expectation, variance)', 'Ross, Introduction to Probability Models, Ch. 2 (expectation of a random variable)']
---
Let $X\sim\text{Bin}(n,p)$ be the number of successes in $n$ independent trials, each a success with probability $p$, and let $q=1-p$:

$$P(X=k)=\binom{n}{k}p^kq^{n-k},\qquad k=0,1,\dots,n$$

**Mean.** Using $k\binom{n}{k}=n\binom{n-1}{k-1}$ and the binomial theorem:

$$E[X]=\sum_{k=0}^{n}k\binom{n}{k}p^kq^{n-k}=np\sum_{k=1}^{n}\binom{n-1}{k-1}p^{k-1}q^{n-k}$$

$$=np\,(p+q)^{n-1}=np$$

**Second factorial moment.** Using $k(k-1)\binom{n}{k}=n(n-1)\binom{n-2}{k-2}$:

$$E[X(X-1)]=n(n-1)p^2\sum_{k=2}^{n}\binom{n-2}{k-2}p^{k-2}q^{n-k}$$

$$=n(n-1)p^2(p+q)^{n-2}=n(n-1)p^2$$

**Variance.**

$$E[X^2]=E[X(X-1)]+E[X]=n(n-1)p^2+np$$

$$\mathrm{Var}(X)=E[X^2]-(E[X])^2=n(n-1)p^2+np-n^2p^2$$

$$=np-np^2=np(1-p)$$

**Check with indicators.** $X=I_1+\cdots+I_n$, where $I_j$ indicates a success on trial $j$, with $E[I_j]=p$ and $\mathrm{Var}(I_j)=p-p^2=pq$. Linearity gives $E[X]=np$, and since the trials are independent the variances add: $\mathrm{Var}(X)=npq$.

**Answer:** $E[X]=np$ and $\mathrm{Var}(X)=np(1-p)$.
