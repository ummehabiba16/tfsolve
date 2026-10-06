---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Counters after the last tick: p0=01111100, p1=01001001, p2=00110111, p3=11010001; page 2 (lowest counter) is replaced."
sources: ["Tanenbaum MOS 4e, sec. 3.4.7 (aging algorithm)"]
---
**Aging:** at every tick, shift every counter right by one bit and put the page's $R$ bit in the leftmost bit; $R$ is then cleared. The page with the lowest counter is replaced.

R bits at the ticks (page 0, 1, 2, 3): 0111, 0010, 1010, 1100, 1011, 1010, 1101, 0001. Counters (8 bits), starting at all zeros:

| Tick | R bits | Page 0 | Page 1 | Page 2 | Page 3 |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 0111 | 00000000 | 10000000 | 10000000 | 10000000 |
| 2 | 0010 | 00000000 | 01000000 | 11000000 | 01000000 |
| 3 | 1010 | 10000000 | 00100000 | 11100000 | 00100000 |
| 4 | 1100 | 11000000 | 10010000 | 01110000 | 00010000 |
| 5 | 1011 | 11100000 | 01001000 | 10111000 | 10001000 |
| 6 | 1010 | 11110000 | 00100100 | 11011100 | 01000100 |
| 7 | 1101 | 11111000 | 10010010 | 01101110 | 10100010 |
| 8 | 0001 | 01111100 | 01001001 | 00110111 | 11010001 |

**Final counters:** page 0 $=01111100$ (124), page 1 $=01001001$ (73), page 2 $=00110111$ (55), page 3 $=11010001$ (209).

The lowest counter belongs to **page 2** (55), so page 2 is replaced. (Values computed with a short script.)
