---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Available (1 printer, 1 scanner): C can finish, then A (needs 3,3) and B (needs 2,3) cannot: the state is unsafe, so deadlock is possible."
sources: ["Tanenbaum MOS 4e, sec. 6.5.3 (Banker's algorithm for multiple resources)"]
---
Resources: 5 printers, 6 scanners. Current holdings and remaining needs (printers, scanners):

| Process | Holds | Needs more | Max |
|:-:|:-:|:-:|:-:|
| A | (0, 2) | (3, 3) | (3, 5) |
| B | (3, 3) | (2, 3) | (5, 6) |
| C | (1, 0) | (1, 1) | (2, 1) |

Available $=(5-4,\ 6-5)=(1,1)$.

**Safety check.** Work $=(1,1)$.

- C needs $(1,1)\le(1,1)$: it can finish and release $(1,0)$, so Work $=(2,1)$.
- A needs $(3,3)\not\le(2,1)$ and B needs $(2,3)\not\le(2,1)$: **neither can finish.**

No safe sequence exists, so the state is **unsafe**, and the processes **can end up in deadlock** (though they do not have to).

**A deadlock path.** Grant the free printer to A and the free scanner to B: Available $=(0,0)$. C needs $(1,1)$, A needs 2 printers and 3 scanners, B needs 2 printers and 2 scanners: nobody can proceed, and no process will release anything: **deadlock**.
