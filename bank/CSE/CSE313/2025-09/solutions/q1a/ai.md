---
author: ai
via: chat
status: unverified
summary: UNSAFE.
sources: [Deadlocks slides 28-31, 'Tanenbaum, MOS 4e, sec. 6.5.3']
imported_from: tfsolve-questions/data/solutions/2023-24.json
---
Available = total $-$ allocated = $(0,0,1)$. Need = Max $-$ Allocation:

|  | A | B | C |
|:--|:-:|:-:|:-:|
| P1 | 2 | 0 | 2 |
| P2 | 0 | 0 | 1 |
| P3 | 5 | 3 | 2 |
| P4 | 5 | 0 | 6 |

*Need matrix*

1. Only P2 has Need $(0,0,1) \le$ Avail $(0,0,1)$. Run P2; Avail $\gets (0,0,1)+(2,0,1)=(2,0,2)$.
2. P1 Need $(2,0,2) \le (2,0,2)$. Run P1; Avail $\gets (2,0,2)+(4,2,3)=(6,2,5)$.
3. Now P3 Need $(5,3,2)$ needs $B=3>2$, and P4 Need $(5,0,6)$ needs $C=6>5$. Neither can proceed.

No safe sequence exists, so the state is unsafe.

**Explanation.**

The binding shortages are B and C: after P1 and P2 finish, the free pool $(6,2,5)$ still cannot satisfy P3 (short one B) or P4 (short one C). Each waits on a unit the other's completion would release, so they can deadlock.
