---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Variables s_0..s_{n-1}; domains {0, ..., n-1}; constraints, for each i: s_i = sum_{j=0}^{n-1} [s_j = i] (s_i counts the occurrences of i in S). Redundant constraints that prune well: sum_i s_i = n and sum_i i s_i = n. For n = 4, the solutions are (1, 2, 1, 0) and (2, 0, 2, 0)."
sources: ["AIMA 3e sec. 6.1 (defining CSPs: global and higher-order constraints)", "CSPLib prob019 (magic sequence)"]
---
**CSP formulation** for a magic sequence of length $n$ (the example with $n=4$ has $S=(s_0,s_1,s_2,s_3)$):

- **Variables:** $X=\{s_0,s_1,\dots,s_{n-1}\}$.
- **Domains:** $D_i=\{0,1,\dots,n-1\}$ for every $s_i$. A value cannot exceed $n-1$, because then the sequence would need too many elements.
- **Constraints:** for every $i\in\{0,\dots,n-1\}$,

$$s_i=\sum_{j=0}^{n-1}[\,s_j=i\,],$$

where $[\cdot]$ is 1 if the condition holds and 0 otherwise. That is, $s_i$ equals the number of occurrences of $i$ in $S$. Each is a global ("count", or `among`) constraint over all $n$ variables.
- **Redundant constraints** (implied, but they help propagation): $\sum_{i=0}^{n-1}s_i=n$ (the counts of all values add up to the length of the sequence) and $\sum_{i=0}^{n-1}i\cdot s_i=n$ (summing the elements in two ways).

**Check** with $n=4$, $S=(2,0,2,0)$: there are two 0's, so $s_0=2$; no 1's, so $s_1=0$; two 2's, so $s_2=2$; no 3's, so $s_3=0$. The sums are $\sum s_i=4$ and $\sum i\,s_i=0+0+4+0=4$. $\checkmark$. $(1,2,1,0)$ is the other solution for $n=4$.
