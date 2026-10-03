---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Each CPT has at most n^k rows of n entries: at most N n^{k+1} numbers (N (n-1) n^k independent), i.e. O(N n^k), versus n^N for the full joint. With n = (last digit + 1) mod 3: digits 1, 4, 7 give n = 2 (N 2^{k+1} numbers); digits 0, 3, 6, 9 give n = 1; digits 2, 5, 8 give n = 0 (degenerate)."
sources: ["MNM slides Uncertainty-2-BN (size of CPTs)", "AIMA 4e sec. 13.2.2 (compactness)", "Berkeley CS188 Bayes nets lecture ('How big is an N-node net?')"]
---
**Size of one node's CPT.** A node $X_i$ with domain size $n$ and at most $k$ parents (each of domain size $n$) has

$$n^k\ \text{parent configurations (rows)}\times n\ \text{values} = n^{k+1}\ \text{entries}.$$

Each row sums to 1, so it has $n-1$ free parameters: $(n-1)\,n^k$ independent numbers.

**Whole network of $N$ nodes.**

$$\text{size}\ \le\ N\cdot n^{k+1}\ \text{entries}\quad\big(N\,(n-1)\,n^k\ \text{independent parameters}\big)=O(N\,n^k),$$

linear in $N$. The full joint distribution needs $n^N$ entries ($n^N-1$ independent), exponential in $N$. For example, with $n=2$, $N=30$ and $k=5$: the BN has at most $30\times2^6=1920$ numbers, while the joint has $2^{30}\approx10^9$.

**With $n=(\text{last digit of roll number}+1)\bmod 3$.**

| Last digit | $n$ | Network size |
|:--|:-:|:--|
| 1, 4, 7 | 2 | at most $N\cdot2^{k+1}$ entries ($N\cdot2^k$ independent), vs $2^N$ for the joint |
| 0, 3, 6, 9 | 1 | each variable has a single value: one entry (=1) per node, 0 free parameters |
| 2, 5, 8 | 0 | an empty domain: no valid variable. Use the general formula $O(N n^k)$ |

*Note:* the answer depends on the student's roll number. Only $n=2$ gives a meaningful network, so take the general formula $N\,n^{k+1}$ with the student's own $n$. "mode 3" on the paper means $\bmod 3$.
