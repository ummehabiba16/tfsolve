---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'First-step analysis: $E_1=\frac13(4)+\frac13(2+E_1)+\frac13(3+E_2)$ and $E_2=\frac13(3+E_1)+\frac13(1)+\frac13(2+E_2)$ give $E_1=8$ hours (and $E_2=7$).'
sources: ['Ross, Introduction to Probability Models, Ch. 3 (computing expectations by conditioning: the trapped miner)']
---
Let $E_1$ and $E_2$ be the expected time to safety starting from mine M1 and mine M2. Door D3 joins M1 and M2 (3 hours either way). Condition on the door chosen first (each door equally likely):

**From M1** (doors D1, D2, D3):

$$E_1=\frac13(4)+\frac13(2+E_1)+\frac13(3+E_2)$$

**From M2** (doors D3, D4, D5):

$$E_2=\frac13(3+E_1)+\frac13(1)+\frac13(2+E_2)$$

Multiplying by 3 and collecting terms:

$$3E_1=9+E_1+E_2\ \Rightarrow\ 2E_1-E_2=9$$

$$3E_2=6+E_1+E_2\ \Rightarrow\ -E_1+2E_2=6$$

From the second equation $E_1=2E_2-6$; substituting into the first, $4E_2-12-E_2=9$, so $E_2=7$ and $E_1=8$.

**Answer:** starting in M1, the miner needs on average $\mathbf{8}$ **hours** to reach safety (7 hours from M2).
