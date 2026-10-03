---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Root value 10. Pruned: the leaves 12 and 3 under the second MIN node (cutoff once 5 <= alpha = 8); the whole MIN subtree (20, 3, 15) after its MAX parent reaches 11 >= beta = 8; the leaf 2 under (3, 2) after 3 <= alpha = 10; and the MIN subtree (9, 5) after its MAX parent reaches 14 >= beta = 10."
sources: ["AIMA 3e sec. 5.3 (alpha-beta pruning)"]
---
**Tree labels.** MAX root $R$; MIN nodes $m_1$ (left) and $m_2$ (right); MAX nodes $M_1$, $M_2$ under $m_1$ and $M_3$, $M_4$ under $m_2$; bottom MIN nodes $n_1..n_8$ with leaves (8), (10, 5, 12, 3), (11, 15), (20, 3, 15), (12, 10), (3, 2), (14), (9, 5).

**Trace** (children left to right; $[\alpha,\beta]$ passed down):

1. $R$ $[-\infty,+\infty]$, then $m_1$, then $M_1$, then $n_1$: leaf 8, so $n_1=8$. $M_1$ has $\alpha=8$.
2. $n_2$ $[8,+\infty]$: leaf 10 gives $v=10$, $\beta=10$; leaf 5 gives $v=5\le\alpha=8$. **Prune leaves 12 and 3.** $n_2=5$, $M_1=\max(8,5)=8$. $m_1$ has $\beta=8$.
3. $M_2$ $[-\infty,8]$, then $n_3$: leaves 11 and 15 give $n_3=11$. $M_2$ has $v=11\ge\beta=8$, so **prune $n_4$ = (20, 3, 15)**. $M_2=11$. $m_1=\min(8,11)=8$. $R$ has $\alpha=8$.
4. $m_2$ $[8,+\infty]$, then $M_3$, then $n_5$: leaves 12 and 10 give $n_5=10$. $M_3$ has $\alpha=10$.
5. $n_6$ $[10,+\infty]$: leaf 3 gives $v=3\le\alpha=10$. **Prune leaf 2.** $n_6=3$, $M_3=\max(10,3)=10$. $m_2$ has $\beta=10$.
6. $M_4$ $[8,10]$, then $n_7$: leaf 14 gives $n_7=14$. $M_4$ has $v=14\ge\beta=10$, so **prune $n_8$ = (9, 5)**. $M_4=14$. $m_2=\min(10,14)=10$.
7. $R=\max(8,10)=$ **10**.

**Result.** **Root value = 10.** MAX moves to the right MIN node, then to $M_3$.

**Pruned branches:**

- leaves **12, 3** of $n_2$;
- the whole subtree **$n_4$ (20, 3, 15)**;
- leaf **2** of $n_6$;
- the whole subtree **$n_8$ (9, 5)**.

(Checked with an alpha-beta script: value 10, with the same four cutoffs.)
