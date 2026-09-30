---
author: ai
via: chat
status: unverified
summary: Safe. Sequence P2 $\to$ P1 $\to$ P3 $\to$ P4 (the worked example in the course notes).
sources: [Deadlocks slides 28-31, 'Tanenbaum, MOS 4e, sec. 6.5.3', Notes on algorithm simulation]
imported_from: tfsolve-questions/data/solutions/2021-22.json
---
Available = $(9,3,6) - (9,2,5) = (0,1,1)$. Need = Max $-$ Allocation:

|  | A | B | C |
|:--|:-:|:-:|:-:|
| P1 | 2 | 2 | 2 |
| P2 | 0 | 0 | 1 |
| P3 | 1 | 0 | 3 |
| P4 | 4 | 2 | 0 |

*Need matrix*

1. P2 need $(0,0,1) \le (0,1,1)$ $\Rightarrow$ run; Avail $\gets (0,1,1)+(6,1,2)=(6,2,3)$.
2. P1 need $(2,2,2) \le (6,2,3)$ $\Rightarrow$ run; Avail $\gets +(1,0,0)=(7,2,3)$.
3. P3 need $(1,0,3) \le (7,2,3)$ $\Rightarrow$ run; Avail $\gets +(2,1,1)=(9,3,4)$.
4. P4 need $(4,2,0) \le (9,3,4)$ $\Rightarrow$ run; Avail $\gets +(0,0,2)=(9,3,6)$.

All finish $\Rightarrow$ safe.
