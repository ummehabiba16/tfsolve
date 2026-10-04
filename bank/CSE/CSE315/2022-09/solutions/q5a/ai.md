---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Segment must satisfy 0 <= 2A3B4h - 10h x seg <= FFFFh, so seg = 1A3Ch ... 2A3Bh (4096 pairs). First five: 1A3Ch:FFF4h, 1A3Dh:FFE4h, 1A3Eh:FFD4h, 1A3Fh:FFC4h, 1A40h:FFB4h. Last five: 2A37h:0044h, 2A38h:0034h, 2A39h:0024h, 2A3Ah:0014h, 2A3Bh:0004h."
sources: ["MHE 8086-Memory_Organization slides 11-13, 18 (physical address = segment x 10H + offset; 4096 segment:offset pairs per address)"]
---
**Condition.** Physical address $= \text{segment} \times 10h + \text{offset}$ with $0000h \le \text{offset} \le FFFFh$. For $PA = 2A3B4h$:

- **Largest segment** (smallest offset): $\lfloor 2A3B4h / 10h \rfloor = 2A3Bh$, offset $= 2A3B4h - 2A3B0h = 0004h$.
- **Smallest segment** (largest offset $\le FFFFh$): $2A3B4h - FFFFh = 1A3B5h$, so the segment must be at least $1A3B5h / 10h = 1A3B.5h$, i.e. $1A3Ch$. Offset $= 2A3B4h - 1A3C0h = FFF4h$.

Each step of 1 in the segment lowers the offset by 10h. There are $2A3Bh - 1A3Ch + 1 = 1000h = 4096$ valid pairs.

**First five** (lowest segments)

| # | Segment:Offset | Check |
|:-:|:-:|:--|
| 1 | **1A3Ch:FFF4h** | 1A3C0h + FFF4h = 2A3B4h |
| 2 | **1A3Dh:FFE4h** | 1A3D0h + FFE4h = 2A3B4h |
| 3 | **1A3Eh:FFD4h** | 1A3E0h + FFD4h = 2A3B4h |
| 4 | **1A3Fh:FFC4h** | 1A3F0h + FFC4h = 2A3B4h |
| 5 | **1A40h:FFB4h** | 1A400h + FFB4h = 2A3B4h |

**Last five** (highest segments)

| # | Segment:Offset | Check |
|:-:|:-:|:--|
| 4092 | **2A37h:0044h** | 2A370h + 0044h = 2A3B4h |
| 4093 | **2A38h:0034h** | 2A380h + 0034h = 2A3B4h |
| 4094 | **2A39h:0024h** | 2A390h + 0024h = 2A3B4h |
| 4095 | **2A3Ah:0014h** | 2A3A0h + 0014h = 2A3B4h |
| 4096 | **2A3Bh:0004h** | 2A3B0h + 0004h = 2A3B4h |

*Note:* "first" is taken as the smallest segment value. The list was checked by a script that enumerates all segments with a valid offset.
