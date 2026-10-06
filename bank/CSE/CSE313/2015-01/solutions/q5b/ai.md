---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "After the four ticks the counters are 11110000, 01100000, 00010000, 01000000, 10110000, 01010000; page 2 (00010000) is replaced."
sources: ["Tanenbaum MOS 4e, sec. 3.4.7 (aging)"]
---
At each tick: shift every counter right by one bit and insert the page's R bit as the leftmost bit. R bits (page 0 ... page 5): 101011, 110010, 110101, 100010; counters start at 00000000.

| After tick | R bits | Page 0 | Page 1 | Page 2 | Page 3 | Page 4 | Page 5 |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 101011 | 10000000 | 00000000 | 10000000 | 00000000 | 10000000 | 10000000 |
| 2 | 110010 | 11000000 | 10000000 | 01000000 | 00000000 | 11000000 | 01000000 |
| 3 | 110101 | 11100000 | 11000000 | 00100000 | 10000000 | 01100000 | 10100000 |
| 4 | 100010 | 11110000 | 01100000 | 00010000 | 01000000 | 10110000 | 01010000 |

Final values: 240, 96, **16**, 64, 176, 80. The **smallest counter is page 2** ($00010000$), so **page 2 is replaced** if a replacement is needed after the last tick (it was referenced only in tick 1 and not in the three later ticks). The values were computed with a short script.
