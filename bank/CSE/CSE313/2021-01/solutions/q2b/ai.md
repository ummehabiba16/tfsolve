---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Elevator order 20, 30, 40, 50, 19, 16, 8: 72 cylinders x 6 ms = 432 ms."
sources: ["Tanenbaum MOS 4e, sec. 5.4.3 (disk arm scheduling: elevator algorithm)"]
---
The arm starts at cylinder 20 moving **upward**; it serves all requests in the direction of motion, then reverses at the last request in that direction.

Requests: 8, 30, 20, 19, 40, 16, 50.

Service order: $20\to30\to40\to50$ (up), then $19\to16\to8$ (down).

| Move | Cylinders |
|:--|:-:|
| $20\to20$ (request at 20, served immediately) | 0 |
| $20\to30$ | 10 |
| $30\to40$ | 10 |
| $40\to50$ | 10 |
| $50\to19$ (reverse) | 31 |
| $19\to16$ | 3 |
| $16\to8$ | 8 |
| **Total** | **72** |

$$\text{seek time} = 72\times 6\text{ ms} = \mathbf{432\ ms}$$
