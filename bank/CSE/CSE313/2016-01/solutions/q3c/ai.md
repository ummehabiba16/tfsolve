---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "On each clock interrupt: FIFO nothing; second chance clears R bits; NFU adds R to the counter; aging shifts the counter right and puts R in the leftmost bit; WSClock updates the virtual time/time stamps and clears R."
sources: ["Tanenbaum MOS 4e, sec. 3.4 (page replacement algorithms)"]
---
| Algorithm | Tasks on each clock interrupt |
|:--|:--|
| **(i) FIFO** (replaces the oldest page) | **nothing**: it only depends on the load order (a queue of pages by arrival); no reference information is used |
| **(ii) Second chance** (FIFO with the R bit) | the **R bits are cleared periodically** (every tick or every few ticks) so that R means "referenced recently"; at a page fault the oldest page is given a second chance if its R bit is 1 |
| **(iii) NFU** (not frequently used, a crude LRU) | for **every page add its R bit to its software counter** ($\text{counter}\mathrel{+}=R$), then **clear R** |
| **(iv) Aging** (a much better LRU approximation) | for every page **shift the counter right by one bit**, **insert the R bit at the leftmost position** ($\text{counter}=(\text{counter}\gg1)\,|\,(R\ll k-1)$), then **clear R** |
| **(v) WSClock** (working-set information) | **advance the virtual time** and, for each page, if $R=1$ **record the current virtual time as the page's time of last use** and **clear R** (the age $=$ current time $-$ time of last use is used at a page fault) |
