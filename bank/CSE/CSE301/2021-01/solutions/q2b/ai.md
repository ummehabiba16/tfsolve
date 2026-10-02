---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Inclusion-exclusion over the $n-1$ forbidden "successions" $(i,i+1)$: $Q_n=\sum_{k=0}^{n-1}(-1)^k\binom{n-1}{k}(n-k)!$. Writing $\binom{n-1}{k}=\binom nk-\binom{n-1}{k-1}$ splits this into $\big(D_n-(-1)^n\big)+\big(D_{n-1}+(-1)^n\big)=D_n+D_{n-1}$.'
sources: ['Brualdi, Introductory Combinatorics, Ch. 6 (another forbidden position problem: $Q_n$)']
---
Number the boys $1,2,\dots,n$ in their order on the first day, so boy $i+1$ was preceded by boy $i$. A new order is a permutation of $\{1,\dots,n\}$, and it is allowed when none of the $n-1$ "successions" $12,\ 23,\ \dots,\ (n-1)n$ appears in it (boy $i$ immediately followed by boy $i+1$).

**Expression for $Q_n$.** Let $A_i$ ($1\le i\le n-1$) be the set of permutations in which $i$ is immediately followed by $i+1$. If we require $k$ given successions, glue each such pair into a block: the $n$ boys form $n-k$ blocks, which can be ordered in $(n-k)!$ ways (the pairs may chain, e.g. $123$, which is still fine). So

$$|A_{i_1}\cap\cdots\cap A_{i_k}|=(n-k)!$$

and by inclusion-exclusion

$$Q_n=\sum_{k=0}^{n-1}(-1)^k\binom{n-1}{k}(n-k)!=n!-\binom{n-1}{1}(n-1)!+\binom{n-1}{2}(n-2)!-\cdots+(-1)^{n-1}\binom{n-1}{n-1}1!$$

**Proof that $Q_n=D_n+D_{n-1}$ ($n\ge2$).** Recall $D_m=\sum_{j=0}^{m}(-1)^j\binom mj(m-j)!$. By Pascal's rule, $\binom{n-1}{k}=\binom nk-\binom{n-1}{k-1}$, so

$$Q_n=\sum_{k=0}^{n-1}(-1)^k\binom nk(n-k)!-\sum_{k=1}^{n-1}(-1)^k\binom{n-1}{k-1}(n-k)!$$

The first sum is $D_n$ without its $k=n$ term, which is $(-1)^n\binom nn0!=(-1)^n$:

$$\sum_{k=0}^{n-1}(-1)^k\binom nk(n-k)!=D_n-(-1)^n$$

In the second sum put $j=k-1$ (so $n-k=(n-1)-j$); it is $-D_{n-1}$ without its $j=n-1$ term, which is $(-1)^{n-1}$:

$$\sum_{k=1}^{n-1}(-1)^k\binom{n-1}{k-1}(n-k)!=-\sum_{j=0}^{n-2}(-1)^j\binom{n-1}{j}(n-1-j)!=-\big(D_{n-1}-(-1)^{n-1}\big)$$

Therefore

$$Q_n=D_n-(-1)^n+D_{n-1}-(-1)^{n-1}=D_n+D_{n-1}$$

since $(-1)^n+(-1)^{n-1}=0$. **Check:** $Q_2=1=D_2+D_1$, $Q_3=6-4+1=3=D_3+D_2$, $Q_4=24-18+6-1=11=D_4+D_3$.
