---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Take reciprocals: $b_n=1/a_n$ satisfies $b_n=\frac{2a_{n-2}-a_{n-1}}{a_{n-1}a_{n-2}}=2b_{n-1}-b_{n-2}$, an arithmetic progression with $b_0=1$, $b_1=\frac{11}{4}$, so $b_n=1+\frac{7n}{4}$ and $a_n=\frac{4}{7n+4}$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1-2 (transforming a recurrence)']
---
**Take reciprocals.** Let $b_n=\frac{1}{a_n}$ (all $a_n$ turn out to be non-zero). For $n\ge2$,

$$b_n=\frac{1}{a_n}=\frac{2a_{n-2}-a_{n-1}}{a_{n-1}a_{n-2}}=\frac{2}{a_{n-1}}-\frac{1}{a_{n-2}}=2b_{n-1}-b_{n-2}$$

So $b_n-b_{n-1}=b_{n-1}-b_{n-2}$: the differences are constant and $(b_n)$ is an **arithmetic progression**.

**Initial values.** $b_0=\frac{1}{a_0}=1$ and $b_1=\frac{1}{a_1}=\frac{11}{4}$, so the common difference is $\frac{11}{4}-1=\frac74$ and

$$b_n=1+\frac{7n}{4}=\frac{7n+4}{4}$$

**Solution.**

$$a_n=\frac{4}{7n+4},\qquad n\ge0$$

(The denominators $2a_{n-2}-a_{n-1}=\frac{8}{7n-10}-\frac{4}{7n-3}\ne0$, so the recurrence is always defined.)

**Check.** $a_2=\frac{a_1a_0}{2a_0-a_1}=\frac{4/11}{2-4/11}=\frac{4/11}{18/11}=\frac29=\frac{4}{18}$ and $a_3=\frac{4}{25}$, both matching the formula.

*[Supplementary materials, page 1](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-1.png), [page 2](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-2.png), [page 3](https://github.com/ummehabiba16/tfsolve/blob/main/CSE301/tables/supplementary-materials-3.png) (open in a new tab).*
