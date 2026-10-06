---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "With 3 frames: optimal 9 page faults, FIFO 15 page faults (LRU 12 for reference)."
sources: ["Tanenbaum MOS 4e, sec. 3.4 (optimal, FIFO page replacement); Silberschatz, ch. 9"]
---
Reference string (20 references): $7,0,1,2,0,3,0,4,2,3,0,3,2,1,2,0,1,7,0,1$; 3 frames, initially empty. Simulated with a script (F = page fault, H = hit; frames listed after each reference).

**(i) Optimal** (replace the page used farthest in the future)

| Ref | 7 | 0 | 1 | 2 | 0 | 3 | 0 | 4 | 2 | 3 | 0 | 3 | 2 | 1 | 2 | 0 | 1 | 7 | 0 | 1 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Frames | 7 | 70 | 701 | 201 | 201 | 203 | 203 | 243 | 243 | 243 | 203 | 203 | 203 | 201 | 201 | 201 | 201 | 701 | 701 | 701 |
| | F | F | F | F | H | F | H | F | H | H | F | H | H | F | H | H | H | F | H | H |

**Optimal: 9 page faults.**

**(ii) FIFO** (replace the oldest page; frames listed oldest first)

| Ref | 7 | 0 | 1 | 2 | 0 | 3 | 0 | 4 | 2 | 3 | 0 | 3 | 2 | 1 | 2 | 0 | 1 | 7 | 0 | 1 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Frames | 7 | 70 | 701 | 012 | 012 | 123 | 230 | 304 | 042 | 423 | 230 | 230 | 230 | 301 | 012 | 012 | 012 | 127 | 270 | 701 |
| | F | F | F | F | H | F | F | F | F | F | F | H | H | F | F | H | H | F | F | F |

**FIFO: 15 page faults.**

For comparison, LRU gives 12 page faults; Optimal is the lower bound (9).
