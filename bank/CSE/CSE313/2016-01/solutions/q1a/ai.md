---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Optimal 6 faults (6 hits), FIFO 9 faults (3 hits), LRU 7 faults (5 hits)."
sources: ["Tanenbaum MOS 4e, sec. 3.4 (optimal, FIFO, LRU page replacement)"]
---
Reference string (12 references): $2,3,2,1,5,2,4,5,3,2,5,2$; 3 frames, initially empty. Each cell shows the frames after the reference (F = page fault, H = hit). All three simulations were checked with a short script.

**(i) Optimal** (evict the page whose next use is farthest in the future)

| Ref | 2 | 3 | 2 | 1 | 5 | 2 | 4 | 5 | 3 | 2 | 5 | 2 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Frames | 2 | 2 3 | 2 3 | 2 3 1 | 2 3 5 | 2 3 5 | 4 3 5 | 4 3 5 | 4 3 5 | 2 3 5 | 2 3 5 | 2 3 5 |
| Result | F | F | H | F | F | H | F | H | H | F | H | H |

Faults $=6$, **hits $=6$**.

**(ii) FIFO** (evict the oldest page)

| Ref | 2 | 3 | 2 | 1 | 5 | 2 | 4 | 5 | 3 | 2 | 5 | 2 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Frames (oldest first) | 2 | 2 3 | 2 3 | 2 3 1 | 3 1 5 | 1 5 2 | 5 2 4 | 5 2 4 | 2 4 3 | 2 4 3 | 4 3 5 | 3 5 2 |
| Result | F | F | H | F | F | F | F | H | F | H | F | F |

Faults $=9$, **hits $=3$**.

**(iii) LRU** (evict the least recently used page)

| Ref | 2 | 3 | 2 | 1 | 5 | 2 | 4 | 5 | 3 | 2 | 5 | 2 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Frames | 2 | 2 3 | 2 3 | 2 3 1 | 2 5 1 | 2 5 1 | 2 5 4 | 2 5 4 | 3 5 4 | 3 5 2 | 3 5 2 | 3 5 2 |
| Result | F | F | H | F | F | H | F | H | F | F | H | H |

Faults $=7$, **hits $=5$**.

**Summary:** Optimal 6 hits $>$ LRU 5 hits $>$ FIFO 3 hits.
