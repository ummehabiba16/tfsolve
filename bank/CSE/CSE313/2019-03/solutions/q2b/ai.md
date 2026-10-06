---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "NRU replaces page 1; FIFO replaces page 2; LRU replaces page 0; second chance replaces page 1."
sources: ["Tanenbaum MOS 4e, sec. 3.4.3-3.4.6 (NRU, FIFO, second chance, LRU)"]
---
| Page | Loaded | Last ref. | R | M | NRU class |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | 230 | 265 | 0 | 1 | 1 |
| 1 | 140 | 270 | 0 | 0 | 0 |
| 2 | 110 | 285 | 1 | 1 | 3 |
| 3 | 126 | 280 | 1 | 0 | 2 |

(NRU classes: $0$ = not referenced, not modified; $1$ = not referenced, modified; $2$ = referenced, not modified; $3$ = referenced, modified.)

**i. NRU:** remove a page from the lowest non-empty class: class 0 contains only page 1, so **page 1** is replaced.

**ii. FIFO:** replace the page that has been in memory longest, i.e. the smallest load time (110): **page 2**.

**iii. LRU:** replace the page unused for the longest time, i.e. the smallest last-reference time (265): **page 0**.

**iv. Second chance:** examine the pages in FIFO order (oldest first): page 2 (loaded 110) has $R=1$, so it gets a second chance (R cleared, treated as newly loaded, moved to the back); page 3 (126) has $R=1$, same treatment; page 1 (140) has $R=0$: **page 1** is replaced.
