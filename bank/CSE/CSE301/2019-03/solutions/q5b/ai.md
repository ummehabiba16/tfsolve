---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$\mathrm{Spec}(\alpha)=\{\lfloor\alpha\rfloor,\lfloor2\alpha\rfloor,\lfloor3\alpha\rfloor,\dots\}$. The number of its elements $\le n$ is $N(\alpha,n)=\lceil\frac{n+1}{\alpha}\rceil-1$. With $x=\frac{n+1}{\sqrt2}$ (irrational) and $\frac{n+1}{2+\sqrt2}=n+1-x$: $p+q=\lceil x\rceil+\lceil n+1-x\rceil-2=\lceil x\rceil-\lfloor x\rfloor+n-1=n$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 3 (spectra, equations (3.12)-(3.13))']
---
**Spectrum.** For a real $\alpha>0$, the spectrum of $\alpha$ is the multiset

$$\mathrm{Spec}(\alpha)=\{\lfloor\alpha\rfloor,\ \lfloor2\alpha\rfloor,\ \lfloor3\alpha\rfloor,\ \dots\}$$

For example $\mathrm{Spec}(\sqrt2)=\{1,2,4,5,7,8,9,11,\dots\}$ and $\mathrm{Spec}(2+\sqrt2)=\{3,6,10,13,17,\dots\}$.

**Counting the elements up to $n$.** For a positive integer $m$,

$$\lfloor m\alpha\rfloor\le n\iff\lfloor m\alpha\rfloor<n+1\iff m\alpha<n+1\iff m<\frac{n+1}{\alpha}$$

(the middle step because $n+1$ is an integer). The number of positive integers $m<\frac{n+1}{\alpha}$ is $\left\lceil\frac{n+1}{\alpha}\right\rceil-1$. So

$$N(\alpha,n)=\left\lceil\frac{n+1}{\alpha}\right\rceil-1$$

**Apply to $\sqrt2$ and $2+\sqrt2$.** Note

$$\frac{1}{2+\sqrt2}=\frac{2-\sqrt2}{2}=1-\frac{1}{\sqrt2}$$

so with $x=\frac{n+1}{\sqrt2}$ we have $\frac{n+1}{2+\sqrt2}=(n+1)-x$. Therefore

$$p+q=\big(\lceil x\rceil-1\big)+\big(\lceil n+1-x\rceil-1\big)=\lceil x\rceil+(n+1)+\lceil-x\rceil-2=n-1+\lceil x\rceil-\lfloor x\rfloor$$

using $\lceil k+y\rceil=k+\lceil y\rceil$ for integer $k$ and $\lceil-x\rceil=-\lfloor x\rfloor$. Since $\sqrt2$ is irrational, $x=\frac{n+1}{\sqrt2}$ is not an integer, so $\lceil x\rceil-\lfloor x\rfloor=1$ and

$$p+q=n\qquad\blacksquare$$

So every positive integer lies in exactly one of the two spectra (they partition the positive integers). Check $n=10$: $\mathrm{Spec}(\sqrt2)$ has $1,2,4,5,7,8,9$ ($p=7$) and $\mathrm{Spec}(2+\sqrt2)$ has $3,6,10$ ($q=3$); $p+q=10$.
