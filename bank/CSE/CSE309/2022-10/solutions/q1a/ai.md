---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "S-attributed SDD with synthesized attributes cnt (numbers so far = next index), max, maxi (index of the maximum) and gt (count with value > index): N -> num { N.cnt = 1; N.max = num.val; N.maxi = 0; N.gt = (num.val > 0 ? 1 : 0) }; N -> N1 , num { i = N1.cnt; N.cnt = i + 1; if num.val > N1.max then (N.max = num.val; N.maxi = i) else (N.max = N1.max; N.maxi = N1.maxi); N.gt = N1.gt + (num.val > i ? 1 : 0) }; L -> { N } { print(N.maxi); print(N.gt) }."
sources: ["KMS Chapter 5 slides 9-17, 31 (SDD, Synthesized Attributes, S-attributed SDD)", "Dragon book 2e sec. 5.1"]
---
**Assumptions.** If the maximum occurs more than once, the index of its **first** occurrence is printed (strict `>` comparison). `num.val` is the integer value supplied by the lexer.

**Attributes** (all synthesized, so the SDD is S-attributed). For the list derived from $N$:

- `N.cnt`: number of elements so far. This is also the index the next element will get.
- `N.max`: the maximum value so far.
- `N.maxi`: the index of that maximum.
- `N.gt`: how many elements so far have value greater than their index.

**SDD:**

| Production | Semantic rules |
|:--|:--|
| $N \to \textbf{num}$ | $N.cnt = 1$ |
| | $N.max = \textbf{num}.val$ |
| | $N.maxi = 0$ |
| | $N.gt =$ **if** $\textbf{num}.val > 0$ **then** 1 **else** 0 |
| $N \to N_1\ ','\ \textbf{num}$ | $N.cnt = N_1.cnt + 1$ |
| | $N.max =$ **if** $\textbf{num}.val > N_1.max$ **then** $\textbf{num}.val$ **else** $N_1.max$ |
| | $N.maxi =$ **if** $\textbf{num}.val > N_1.max$ **then** $N_1.cnt$ **else** $N_1.maxi$ |
| | $N.gt = N_1.gt +$ (**if** $\textbf{num}.val > N_1.cnt$ **then** 1 **else** 0) |
| $L \to\ '\{'\ N\ '\}'$ | $print(N.maxi)$ |
| | $print(N.gt)$ |

In $N \to N_1 , \textbf{num}$, the new number has index $N_1.cnt$ (indices start at 0), so it is compared with that index and, if it is a new maximum, that index is recorded.

**Check with {3, 6, 1, 2, 5}:**

| Element | Index | max | maxi | value > index? | gt |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 3 | 0 | 3 | 0 | yes | 1 |
| 6 | 1 | 6 | 1 | yes | 2 |
| 1 | 2 | 6 | 1 | no | 2 |
| 2 | 3 | 6 | 1 | no | 2 |
| 5 | 4 | 6 | 1 | yes | 3 |

The SDD prints **1** and **3**, as required.
