---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Total demand is 260 bytes, below the 300 bytes: load all four contiguously using base and limit registers; relocation adds the base in hardware, with no extra memory access."
sources: ["Tanenbaum MOS 4e, sec. 3.1.3 (base and limit registers; dynamic relocation)"]
---
The four processes need $48+64+120+28=260$ bytes, which is less than the $300$ bytes available, so **all four fit in memory at the same time**. To minimise memory accesses use **contiguous allocation with base and limit registers** (dynamic relocation): each process is placed in one contiguous partition, and the hardware adds the **base register** to every address and compares the offset with the **limit register**. This relocation is done by an adder in the MMU, so it needs **no extra memory reference** per access (in contrast, paging or segmentation need one or more page/segment-table accesses unless the TLB hits).

| Process | Size | Base | Limit | Address range |
|:-:|:-:|:-:|:-:|:--|
| P1 | 48 | 0 | 48 | 0-47 |
| P2 | 64 | 48 | 64 | 48-111 |
| P3 | 120 | 112 | 120 | 112-231 |
| P4 | 28 | 232 | 28 | 232-259 |

The remaining $300-260=40$ bytes are free. At each context switch the OS loads the base and limit registers of the next process.
