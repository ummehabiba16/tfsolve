---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Perturbation: with $U_n=\sum3^k=\frac{3^{n+1}-1}{2}$ and $V_n=\sum k3^k=\frac{(2n-1)3^{n+1}+3}{4}$, $S_n+(n+1)^23^{n+1}=3S_n+6V_n+3U_n$ gives $\sum_{0\le k\le n}k^23^k=\frac{(n^2-n+1)3^{n+1}-3}{2}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 2 (the perturbation method)', 'Supplementary materials (sums, item 3)']
---
Let $S_n=\sum_{0\le k\le n}k^23^k$, $V_n=\sum_{0\le k\le n}k3^k$ and $U_n=\sum_{0\le k\le n}3^k=\frac{3^{n+1}-1}{2}$.

**Perturbation method** ($S_n+a_{n+1}=a_0+\sum_{0\le k\le n}a_{k+1}$).

*First $V_n$.* With $a_k=k3^k$:

$$V_n+(n+1)3^{n+1}=0+\sum_{0\le k\le n}(k+1)3^{k+1}=3V_n+3U_n$$

$$2V_n=(n+1)3^{n+1}-\frac{3\left(3^{n+1}-1\right)}{2}\ \Rightarrow\ V_n=\frac{(2n-1)3^{n+1}+3}{4}$$

*Now $S_n$.* With $a_k=k^23^k$ and $(k+1)^2=k^2+2k+1$:

$$S_n+(n+1)^23^{n+1}=\sum_{0\le k\le n}(k+1)^23^{k+1}=3S_n+6V_n+3U_n$$

$$2S_n=(n+1)^23^{n+1}-6V_n-3U_n$$

$$=(n+1)^23^{n+1}-\frac{3\big((2n-1)3^{n+1}+3\big)}{2}-\frac{3\left(3^{n+1}-1\right)}{2}$$

$$=3^{n+1}\Big[(n+1)^2-\tfrac32(2n-1)-\tfrac32\Big]-\tfrac92+\tfrac32=3^{n+1}\left(n^2-n+1\right)-3$$

$$\sum_{0\le k\le n}k^23^k=\frac{(n^2-n+1)\,3^{n+1}-3}{2}$$

**Check.** $n=1$: $3=\frac{1\cdot9-3}{2}$. $n=2$: $3+36=39=\frac{3\cdot27-3}{2}$. $n=3$: $39+243=282=\frac{7\cdot81-3}{2}$.
