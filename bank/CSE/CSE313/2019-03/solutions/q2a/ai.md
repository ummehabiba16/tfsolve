---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) tick 10: pages 0 and 1 get R=0 and time stamp 10; (ii) fault on page 3: assuming the hand starts at page 0, pages 0 and 1 get R=0, page 2 (R=0, age 3 > 2, clean) is replaced by page 3 (time stamp 10, V=1, R=1, M=0)."
sources: ["Tanenbaum MOS 4e, sec. 3.4.9 (WSClock)"]
---
**WSClock rules.** $\tau=2$, current virtual time $=10$; age $=10-\text{time stamp}$. Pages are on a circular list. **Assumptions:** (a) a clock interrupt records the use of every page with $R=1$ (time stamp $\leftarrow 10$) and clears $R$; (b) on a page fault the hand starts at page 0; a page with $R=1$ is given a "second chance" ($R\leftarrow0$, hand moves on); a page with $R=0$ and age $>\tau$ is replaced if it is clean (a dirty one would first be scheduled for writing).

Initial table:

| Page | Time stamp | V | R | M |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 9 | 1 | 1 | 0 |
| 1 | 9 | 1 | 1 | 1 |
| 2 | 7 | 1 | 0 | 0 |
| 3 | 4 | 0 | 0 | 0 |
| 4 | 6 | 1 | 0 | 1 |

**(i) Clock interrupt at tick 10.** Pages with $R=1$ (pages 0 and 1) have been used since the last tick: their time stamp becomes 10 and $R$ is cleared. The other entries are unchanged.

| Page | Time stamp | V | R | M |
|:-:|:-:|:-:|:-:|:-:|
| 0 | **10** | 1 | **0** | 0 |
| 1 | **10** | 1 | **0** | 1 |

**(ii) Page fault at tick 10 (read of page 3, which is not valid).**

- Hand at page 0: $R=1$ $\to$ set $R=0$, move on.
- Page 1: $R=1$ $\to$ set $R=0$, move on.
- Page 2: $R=0$, age $=10-7=3>\tau=2$ and the page is **clean** ($M=0$) $\to$ **replace page 2's frame**.

The frame is given to page 3 and page 2 becomes invalid; the new page is read, so $R=1$, $M=0$, time stamp $=10$. New entries:

| Page | Time stamp | V | R | M |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 9 | 1 | **0** | 0 |
| 1 | 9 | 1 | **0** | 1 |
| 2 | 7 | **0** | 0 | 0 |
| 3 | **10** | **1** | **1** | 0 |

Page 4 is unchanged ($6,1,0,1$).
