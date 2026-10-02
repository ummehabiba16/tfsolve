---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Both sides count the $k$-subsets of $\{1,\dots,n\}$ that contain at least one of $1,2,3$: the left side as all subsets minus those avoiding $\{1,2,3\}$; the right side by the smallest of $1,2,3$ that the subset contains.'
sources: ['Brualdi, Introductory Combinatorics, Ch. 5 (combinatorial identities)']
---
Count the $k$-element subsets of $S=\{1,2,\dots,n\}$ that contain **at least one** of the elements $1,2,3$.

**Left side.** There are $\binom nk$ $k$-subsets in all. Those containing none of $1,2,3$ are $k$-subsets of $\{4,\dots,n\}$, which has $n-3$ elements: $\binom{n-3}{k}$ of them. So the number we want is

$$\binom nk-\binom{n-3}{k}$$

**Right side.** Split the subsets by the **smallest** of the elements $1,2,3$ that they contain:

- they contain 1: the other $k-1$ elements come from $\{2,\dots,n\}$: $\binom{n-1}{k-1}$ subsets;
- they do not contain 1 but contain 2: the other $k-1$ come from $\{3,\dots,n\}$: $\binom{n-2}{k-1}$;
- they contain neither 1 nor 2 but contain 3: the other $k-1$ come from $\{4,\dots,n\}$: $\binom{n-3}{k-1}$.

These cases are disjoint and cover every subset we want, so the number is

$$\binom{n-1}{k-1}+\binom{n-2}{k-1}+\binom{n-3}{k-1}$$

Both expressions count the same set, hence

$$\binom nk-\binom{n-3}{k}=\binom{n-1}{k-1}+\binom{n-2}{k-1}+\binom{n-3}{k-1}$$
