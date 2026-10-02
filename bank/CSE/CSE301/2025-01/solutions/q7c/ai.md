---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'The index $k$ runs over all integers with $k^2\le30$, i.e. $k=-5,\dots,5$; $a_{k^2}=\log k^2=2\log|k|$ for $k\ne0$ and $a_0=0$. Sum $=2\cdot2(\log1+\cdots+\log5)=4\log120$ ($\approx19.15$ for natural logs, $8.32$ for base 10).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 2 (sums and the meaning of the index condition)']
---
**Which $k$?** In $\sum_{0\le k^2\le30}$ the index $k$ runs over **all integers** satisfying the condition (the convention of Concrete Mathematics), including negative ones. $k^2\le30$ means $|k|\le5$, so

$$k\in\{-5,-4,-3,-2,-1,0,1,2,3,4,5\}$$

**The terms.** For $k=0$: $a_{k^2}=a_0=0$. For $k\ne0$: $k^2\ne0$, so $a_{k^2}=\log|k^2|=\log k^2=2\log|k|$. Each value $k^2\in\{1,4,9,16,25\}$ occurs twice ($\pm k$):

$$\sum_{0\le k^2\le30}a_{k^2}=a_0+2\left(a_1+a_4+a_9+a_{16}+a_{25}\right)$$

$$=0+2\left(\log1+\log4+\log9+\log16+\log25\right)=2\log(1\cdot4\cdot9\cdot16\cdot25)=2\log14400$$

Since $14400=120^2=(5!)^2$,

$$\sum_{0\le k^2\le30}a_{k^2}=4\log120=4\log5!$$

Numerically: $4\ln120\approx19.15$ (natural log) or $4\log_{10}120\approx8.32$ (base 10).

(If only $k\ge0$ were meant, each value would be counted once and the sum would be $2\log120$.)
