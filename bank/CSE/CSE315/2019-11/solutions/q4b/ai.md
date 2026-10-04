---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Code segment 00240H-1023FH, data segment 00400H-103FFH; overlap 00400H-1023FH = FE40H = 65088 bytes."
sources: ["MHE 8086-Memory_Organization slides 8-13 (64 KB segments, overlap)"]
---
Each segment is 64 KB (offsets 0000H-FFFFH):

| Segment | Start | End (start + FFFFH) |
|:--|:-:|:-:|
| Code (CS = 0024H) | 00240H | 1023FH |
| Data (DS = 0040H) | 00400H | 103FFH |

The data segment starts inside the code segment, so the common region is **00400H to 1023FH**:

$$\text{Overlap} = 1023FH - 00400H + 1 = \mathbf{FE40H} = 65088\ \text{bytes}$$

Check: the bases differ by $00400H - 00240H = 1C0H = 448$ bytes, and $65536 - 448 = 65088$.
