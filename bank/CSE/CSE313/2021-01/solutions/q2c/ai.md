---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A sorted delta list of pending timers with one hardware clock: the head counter is decremented every tick; when it reaches 0 the first timer fires and the next delta is loaded."
sources: ["Tanenbaum MOS 4e, sec. 5.5.3 (soft timers; simulating multiple timers with a single clock)"]
---
**Idea.** The hardware has one clock. The OS keeps a **linked list of pending timer requests sorted by time**, in which each entry stores only the **difference (delta, in ticks) to the previous entry**, plus a variable holding the current time and a counter *next signal* for the first entry.

Current time $=3000$; pending requests at $3006,\ 5014,\ 5019,\ 5025,\ 5039$:

| Entry | 1 | 2 | 3 | 4 | 5 |
|:--|:-:|:-:|:-:|:-:|:-:|
| Absolute time | 3006 | 5014 | 5019 | 5025 | 5039 |
| Delta stored | **6** | **2008** | **5** | **6** | **14** |

(Check: $3000+6=3006$, $+2008=5014$, $+5=5019$, $+6=5025$, $+14=5039$.)

**Operation.** On every clock tick the interrupt handler increments the current time and decrements the counter of the first entry.

- After 6 ticks (time 3006) the counter reaches 0: the first request is signalled (its process is woken or its handler run), the entry is removed, and the counter is loaded with the next delta, 2008.
- After another 2008 ticks (time 5014) the second request fires, then 5 ticks later (5019) the third, 6 ticks later (5025) the fourth, 14 ticks later (5039) the last.

A **new request**, e.g. at 5022, is inserted in sorted position (between 5019 and 5025) and the deltas around it are adjusted (the 6 of the 4th entry becomes 3, the new entry gets 3). Only one hardware timer is needed, and each tick costs $O(1)$.
