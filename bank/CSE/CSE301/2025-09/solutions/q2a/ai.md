---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Faulty bolts per packet $\approx$ Poisson($\lambda=np=0.2$). Packets with at least one faulty bolt $\approx2000(1-e^{-0.2})=362.5\approx363$ (about 1637 packets have none, 327 one, 33 two, 2 three).'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 4 (Poisson distribution and the Poisson approximation to the binomial)']
---
Let $X$ be the number of faulty bolts in a packet. Each of the $n=100$ bolts is faulty with probability $p=0.2\%=0.002$, independently, so $X\sim\text{Bin}(100,\ 0.002)$.

Here $n$ is large and $p$ is small, so $X$ is approximately Poisson with

$$\lambda=np=100\times0.002=0.2$$

$$P(X=k)\approx\frac{e^{-0.2}(0.2)^k}{k!},\qquad e^{-0.2}=0.81873$$

**Packets with no faulty bolt.**

$$2000\times P(X=0)\approx2000\times0.81873=1637.5$$

**Packets with at least one faulty bolt.**

$$P(X\ge1)=1-e^{-0.2}=0.18127$$

$$2000\times0.18127=362.5\approx\mathbf{363}$$

**Breakdown** (expected number of packets $=2000\,P(X=k)$):

| Faulty bolts $k$ | $P(X=k)$ | Expected packets |
|:-:|:-:|:-:|
| 0 | 0.81873 | 1637.5 |
| 1 | 0.16375 | 327.5 |
| 2 | 0.01637 | 32.7 |
| 3 | 0.00109 | 2.2 |
| 4 or more | 0.00006 | 0.1 |

So about **363 of the 2000 packets** contain at least one faulty bolt: about 327 with one, 33 with two and 2 with three. The exact binomial value, $2000(1-0.998^{100})=362.9$, agrees.
