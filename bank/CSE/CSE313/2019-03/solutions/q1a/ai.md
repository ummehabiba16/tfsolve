---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "First fit takes the first hole that fits, next fit resumes from the last allocation (slightly worse in practice). Best fit: 12, 10, 9 MB holes; worst fit: 20, 18, 15 MB holes."
sources: ["Tanenbaum MOS 4e, sec. 3.2.3 (first fit, next fit, best fit, worst fit)"]
---
**First fit:** scan the list of holes from the beginning and take the *first* hole that is large enough; the hole is split into the allocated part and a smaller hole. It is fast because it searches as little as possible.

**Next fit:** like first fit, but the search **starts from the place where it stopped the last time** (not from the beginning). Simulations (Bays) show that next fit gives **slightly worse performance** than first fit, so **first fit performs better in practice** (and is simpler).

**Holes** (in memory order): 10, 4, 20, 18, 7, 9, 12, 15 MB. Requests: 12 MB, then 10 MB, then 9 MB.

**Best fit** (smallest hole that fits):

| Request | Candidates ($\ge$ request) | Hole taken | Left over |
|:-:|:--|:-:|:-:|
| 12 MB | 20, 18, 12, 15 | **12 MB** | 0 |
| 10 MB | 10, 20, 18, 15 | **10 MB** | 0 |
| 9 MB | 20, 18, 9, 15 | **9 MB** | 0 |

**Worst fit** (largest hole):

| Request | Largest hole | Hole taken | Left over |
|:-:|:-:|:-:|:-:|
| 12 MB | 20 | **20 MB** | 8 |
| 10 MB | 18 | **18 MB** | 8 |
| 9 MB | 15 | **15 MB** | 6 |

(Each request is placed in the holes that remain after the earlier ones.)
