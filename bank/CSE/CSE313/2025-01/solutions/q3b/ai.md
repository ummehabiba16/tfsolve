---
author: ai
via: chat
status: unverified
summary: Safe. Sequence P1 $\to$ P2 $\to$ P3 $\to$ P4.
sources: [Deadlocks slides 28-31, 'Tanenbaum, MOS 4e, sec. 6.5.2']
imported_from: tfsolve-questions/data/solutions/2022-23.json
---
Need = Max $-$ Has: P1=4, P2=6, P3=6, P4=15. Available (free) = 7.

1. P1 need $4 \le 7$ $\Rightarrow$ run; free $= 7+5 = 12$.
2. P2 need $6 \le 12$ $\Rightarrow$ run; free $= 12+6 = 18$.
3. P3 need $6 \le 18$ $\Rightarrow$ run; free $= 18+2 = 20$.
4. P4 need $15 \le 20$ $\Rightarrow$ run; free $= 20$.

All processes finish, so the state is safe.
