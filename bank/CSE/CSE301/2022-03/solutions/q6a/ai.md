---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'In second $k$ the ant crawls 1 cm on a $100k$ cm string, so after $n$ s it has covered $\frac{H_n}{100}$; the worm crawls 1 cm per half second on a $100k$ cm string, covering $\frac{H_{2n}}{100}$. The difference $\frac{H_{2n}-H_n}{100}=\frac{1}{100}\sum_{j=1}^{n}\frac{1}{n+j}<\frac{1}{100}=1\%<2\%$, so the statement is true (the difference tends to $\frac{\ln2}{100}\approx0.69\%$).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 6 (harmonic numbers: the worm on the rubber band)']
---
**Model.** Each creature crawls along its string and, at the end of each time step, the string is stretched uniformly, keeping the creature at the same **fraction** of the string. So we track the fraction of the string covered.

**The ant.** During second $k$ ($k=1,2,\dots$) the ant's string has length $100k$ cm (it was stretched by 100 cm at the end of each earlier second), and the ant crawls 1 cm, i.e. a fraction $\frac{1}{100k}$ of the string. Stretching does not change fractions, so after $n$ seconds the ant has covered

$$\frac{1}{100}\left(1+\frac12+\cdots+\frac1n\right)=\frac{H_n}{100}$$

**The worm.** The worm crawls $2$ cm/s, i.e. 1 cm per half second, and its string is stretched by 100 cm every half second. During half-second $k$ ($k=1,2,\dots,2n$) the string has length $100k$ cm, so the worm covers $\frac{1}{100k}$ of it. After $n$ seconds ($2n$ half-seconds):

$$\frac{1}{100}\left(1+\frac12+\cdots+\frac{1}{2n}\right)=\frac{H_{2n}}{100}$$

**The difference.**

$$\frac{H_{2n}}{100}-\frac{H_n}{100}=\frac{1}{100}\left(\frac{1}{n+1}+\frac{1}{n+2}+\cdots+\frac{1}{2n}\right)$$

Each of the $n$ terms in the bracket is less than $\frac1n$, so the bracket is less than $n\cdot\frac1n=1$:

$$\frac{H_{2n}-H_n}{100}<\frac{1}{100}=1\%<2\%$$

So the statement is **true** for every $n\ge1$. (More precisely the difference increases with $n$ and tends to $\frac{\ln2}{100}\approx0.69\%$; for $n=1$ it is $\frac{1}{200}=0.5\%$. Even after either creature reaches the end of its string, its fraction stays at 1, which only makes the difference smaller.)
