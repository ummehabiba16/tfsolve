---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Root value 18. Pruned: the leaf 80 (the MAX node above it is already 40 >= beta = 13), and the leaves -3 and 14 of the middle MIN node (12 <= alpha = 13). Values: left MIN = 13, middle MIN = 12 (cut), right MIN = min(MAX(4, 18) = 18, 28) = 18."
sources: ["AIMA 3e sec. 5.3 (alpha-beta pruning)"]
---
**Tree** (from Figure 5b; triangles pointing up are MAX, down are MIN). Root MAX has three MIN children:

- $m_1$: leaf 13 and a MAX node $M_1$ with MIN leaves 40 and 80;
- $m_2$: leaves 12, $-3$, 14;
- $m_3$: a MAX node $M_2$ (children: MIN node $n_1$ with leaves 20 and 4; MIN node $n_2$ with leaf 18) and leaf 28.

**Trace** ($[\alpha,\beta]$ passed down, children left to right):

1. Root $[-\infty,\infty]$, then $m_1$: leaf 13 gives $v=13$, $\beta=13$.
2. $M_1$ $[-\infty,13]$: leaf 40 gives $v=40\ge\beta=13$. **Prune 80.** $M_1=40$.
3. $m_1=\min(13,40)=13$. Root $\alpha=13$.
4. $m_2$ $[13,\infty]$: leaf 12 gives $v=12\le\alpha=13$. **Prune $-3$ and 14.** $m_2=12$.
5. $m_3$ $[13,\infty]$, then $M_2$ $[13,\infty]$, then $n_1$: leaf 20 ($\beta=20$), leaf 4 gives $v=4\le\alpha=13$, so $n_1=4$ (no children left to prune).
6. $n_2$ $[13,\infty]$: leaf 18, so $n_2=18$. $M_2=\max(4,18)=18$. $m_3$ has $\beta=18$.
7. Leaf 28: $m_3=\min(18,28)=18$.
8. Root $=\max(13,12,18)=$ **18**.

**Root value = 18.** MAX should choose the third (right) branch.

**Pruned branches:** the leaf **80** (under $M_1$), and the leaves **$-3$ and 14** (under $m_2$). (Checked with an alpha-beta script.)
