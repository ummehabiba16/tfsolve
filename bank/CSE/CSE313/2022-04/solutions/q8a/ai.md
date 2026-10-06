---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Evict table index 1 at t=430 (oldest R=0 page, all inside the working set); evict index 7 at t=440 (R=0, age 53 > 50)."
sources: ["Tanenbaum MOS 4e, sec. 3.4.8 (working-set page replacement)"]
---
**Algorithm** (working set with execution-time approximation). For every page, scan the table:

- if $R=1$: write the current virtual time into its "time of last use" (and it is in the working set);
- if $R=0$: $\text{age} = \text{current time}-\text{time of last use}$; if $\text{age}>\tau$ the page is **not in the working set**, so evict it (the first such page found);
- otherwise remember the page with the **smallest** time of last use;
- if no page with $\text{age}>\tau$ exists, evict the remembered (oldest) page.

Here $\tau = 50$; the last clock interrupt that cleared the $R$ bits was at $t=425$ and the next is at $t=445$, so the $R$ bits are unchanged at $t=430$ and $t=440$.

**Fault at $t=430$.**

| Index | Time | R | Age = 430 - time | Note |
|:-:|:-:|:-:|:-:|:--|
| 0 | 214 | 1 | | $R=1$: time becomes 430 |
| 1 | 381 | 0 | 49 | $\le 50$ |
| 2 | 402 | 1 | | time becomes 430 |
| 3 | 289 | 1 | | time becomes 430 |
| 4 | 409 | 0 | 21 | $\le 50$ |
| 5 | 160 | 1 | | time becomes 430 |
| 6 | 315 | 1 | | time becomes 430 |
| 7 | 387 | 0 | 43 | $\le 50$ |

No page has age $>50$, so every page is in the working set; evict the page with the **smallest time of last use** among the $R=0$ pages: index 1 (381). **Evicted: page frame 1.**

**Fault at $t=440$.** The new page loaded into frame 1 has time $430$ (and $R=1$). The $R=1$ pages get time 440. The $R=0$ pages: index 4: age $440-409 = 31\le50$; index 7: age $440-387 = 53 > 50$, so it is outside the working set and is evicted at once. **Evicted: page frame 7.**

**Answer:** frame **1** at $t=430$ and frame **7** at $t=440$.
