---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) State: a permutation (a1, a2, a3, a4); initial: the given order; goal: sorted ascending; operators: Swap(i), exchanging positions i and i+1, i = 1..3; path cost: 1 per swap. (ii) 4! = 24 states. (iii) From 4,1,3,2 (h = 6): A* expands 4132 (f 6), 1432 (f 5), 1342 (f 6), 1324 (f 5), then 1234 (f 4): 4 swaps. (iv) Not admissible: one swap changes h by up to 2 (e.g. 2,1,3,4 has h = 2 but cost 1); h/2, or the number of inversions (the exact cost), is admissible."
sources: ["AIMA 3e sec. 3.1 (problem formulation), 3.5.2 (A*), 3.6 (admissible heuristics)"]
---
**(i) Formulation.**

- *State representation:* an ordered list (permutation) $(a_1,a_2,a_3,a_4)$ of the four numbers.
- *Initial state:* the given order, here $(4,1,3,2)$.
- *Goal state:* $(1,2,3,4)$, sorted ascending: $a_1<a_2<a_3<a_4$.
- *Operations:* $Swap(i)$ for $i=1,2,3$: exchange the adjacent elements at positions $i$ and $i+1$.
- *Path cost:* 1 per swap. Minimizing the cost gives the minimum number of swaps.

**(ii) Number of states.** Every permutation is reachable, so there are $4!=$ **24** states.

**(iii) A\* search tree** with $h(s)=\sum_v|\text{pos}_s(v)-\text{pos}_{goal}(v)|$. For $(4,1,3,2)$: $h=|1-4|+|2-1|+|3-3|+|4-2|=3+1+0+2=6$.

```text
4132 (g=0,h=6,f=6)                                  [expanded 1]
 |- 1432 (g=1,h=4,f=5)                              [expanded 2]
 |    |- 1342 (g=2,h=4,f=6)                         [expanded 3]
 |    |    |- 1324 (g=3,h=2,f=5)                    [expanded 4]
 |    |    |    |- 1234 (g=4,h=0,f=4)  GOAL         [selected 5]
 |    |    |    `- 3124 (g=4,h=4,f=8)
 |    |    `- 3142 (g=3,h=6,f=9)
 |    `- 1423 (g=2,h=4,f=6)
 |- 4312 (g=1,h=8,f=9)
 `- 4123 (g=1,h=6,f=7)
```

(Ties at $f=6$ are broken in order of generation; parents are not regenerated.) **Solution:** 4132, 1432, 1342, 1324, 1234: **4 swaps**, which is optimal (there are 4 inversions).

**(iv) Is $h$ admissible? No.** One adjacent swap moves **two** numbers by one position each, so it can reduce $h$ by 2. $h$ can therefore overestimate. *Counter-example:* $(2,1,3,4)$ has $h=1+1=2$, but needs only **1** swap.

**Admissible alternatives:**

- $h'(s)=h(s)/2$: each swap reduces $h$ by at most 2, so $h/2\le$ the true cost;
- even better, $h''(s)$ = the **number of inversions** (pairs out of order). Each adjacent swap fixes exactly one inversion, so $h''$ equals the true cost. It is admissible and perfect: for $(4,1,3,2)$, $h''=4$.
