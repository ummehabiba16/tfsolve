---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "CS segment 00240H-1023FH, DS segment 00400H-103FFH: overlap 00400H-1023FH = FE40H = 65088 bytes."
sources: ["MHE 8086-Memory_Organization slides 7-12 (64KB segments may overlap)"]
---
Each segment is 64KB = 10000H bytes long.

| Segment | Start = seg $\times$ 10H | End = start + FFFFH |
|:--|:-:|:-:|
| Code (CS = 0024H) | 00240H | 1023FH |
| Data (DS = 0040H) | 00400H | 103FFH |

The overlap runs from the later start to the earlier end: **00400H to 1023FH**.

$$\text{Overlap} = 1023FH - 00400H + 1 = FE40H = \mathbf{65088\text{ bytes}}$$

Equivalently, $10000H - (00400H - 00240H) = 10000H - 1C0H = FE40H$.
