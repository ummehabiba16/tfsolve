---
author: ai
via: chat
status: unverified
summary: As transcribed the state is unsafe for every x, because A's maximum claim for R5 (3) exceeds the total R5 in the system (2), so A can never finish. If A's R5 maximum is 1 (consistent with the totals), the smallest safe value is x = 1, with sequence D $\to$ A $\to$ C $\to$ B.
sources: [Deadlocks slides 28-31, 'Tanenbaum, MOS 4e, sec. 6.5.3 (variant of the four-process / five-resource problem)']
imported_from: tfsolve-questions/data/solutions/2019-20.json
---
Need = Max $-$ Allocation:

|  | R1 | R2 | R3 | R4 | R5 |
|:--|:-:|:-:|:-:|:-:|:-:|
| A | 0 | 1 | 0 | 0 | 2 |
| B | 0 | 2 | 1 | 0 | 0 |
| C | 1 | 0 | 3 | 0 | 0 |
| D | 0 | 0 | 1 | 1 | 1 |

*Need matrix*

Resource totals (allocated + available) = $(5,2,4{+}x,5,2)$. Process A needs 3 units of R5, but only 2 units of R5 exist in the whole system, so A can never acquire its maximum and can never complete. Therefore no value of $x$ makes the state safe.

Taking A's R5 maximum as 1 (Need for R5 = 0, the value consistent with the totals, and the likely intended figure): the smallest working value is $x=1$, giving the safe sequence D $\to$ A $\to$ C $\to$ B.

**Explanation.**

Corrected case $x=1$, Available $=(0,0,1,1,1)$:

1. D need $(0,0,1,1,1) \le$ Avail $\Rightarrow$ run D; Avail $\gets (1,1,2,2,1)$.
2. A need $(0,1,0,0,0) \le$ Avail $\Rightarrow$ run A; Avail $\gets (2,1,4,3,2)$.
3. C need $(1,0,3,0,0) \le$ Avail $\Rightarrow$ run C; Avail $\gets (3,2,4,4,2)$.
4. B need $(0,2,1,0,0) \le$ Avail $\Rightarrow$ run B. All finish $\Rightarrow$ safe.

With $x=0$ nothing can start (D needs one R3), so $x=1$ is the minimum.
