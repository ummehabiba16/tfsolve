---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'If $x=\lceil x\rceil$ there is nothing to prove. Otherwise $x<\lceil x\rceil$, so $\lceil f(x)\rceil\le\lceil f(\lceil x\rceil)\rceil$. If the inequality were strict, then $f(x)\le\lceil f(x)\rceil<f(\lceil x\rceil)$ and by continuity some $y\in[x,\lceil x\rceil)$ has $f(y)=\lceil f(x)\rceil$, an integer; then $y$ is an integer strictly between $x$ and $\lceil x\rceil$, impossible.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 3 (floors and ceilings, equation (3.10))']
---
**Claim.** If $f$ is continuous and strictly increasing, and $f(y)\in\mathbb Z\Rightarrow y\in\mathbb Z$, then $\lceil f(\lceil x\rceil)\rceil=\lceil f(x)\rceil$ for all real $x$ (in the domain).

**Proof.** If $x$ is an integer, then $\lceil x\rceil=x$ and both sides are equal.

Otherwise $x<\lceil x\rceil$. Since $f$ is increasing, $f(x)<f(\lceil x\rceil)$, and since the ceiling function is non-decreasing,

$$\lceil f(x)\rceil\le\lceil f(\lceil x\rceil)\rceil$$

Suppose the inequality were strict: $\lceil f(x)\rceil<\lceil f(\lceil x\rceil)\rceil$. The integer $N=\lceil f(x)\rceil$ is then less than $\lceil f(\lceil x\rceil)\rceil$, which forces $N<f(\lceil x\rceil)$ (if $N\ge f(\lceil x\rceil)$, then $N\ge\lceil f(\lceil x\rceil)\rceil$). So

$$f(x)\le N<f(\lceil x\rceil)$$

By the intermediate value theorem ($f$ is continuous) there is a $y$ with $x\le y<\lceil x\rceil$ and $f(y)=N$. Since $N$ is an integer, the special property of $f$ says $y$ is an integer. But there is no integer $y$ with $x\le y<\lceil x\rceil$, because $\lceil x\rceil$ is the **smallest** integer $\ge x$. This contradiction shows the inequality cannot be strict, so

$$\lceil f(\lceil x\rceil)\rceil=\lceil f(x)\rceil\qquad\blacksquare$$

**Example.** $f(x)=\sqrt x$ has the property ($\sqrt y=m\Rightarrow y=m^2$), so $\lceil\sqrt{\lceil x\rceil}\rceil=\lceil\sqrt x\rceil$.
