---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Both pairs give the same physical address 018F0h (CS:IP = 01540h + 03B0h, DS:SI = 01710h + 01E0h). Code segment 01540h-1153Fh and data segment 01710h-1170Fh overlap from 01710h to 1153Fh = FE30h = 65072 bytes."
sources: ["MHE 8086-Memory_Organization slides 8-13, 18 (physical address = segment x 10H + offset, overlap, redundancy of segment:offset pairs)"]
---
**i. Physical addresses**

Physical address = segment $\times$ 10H + offset (append a 0 to the segment and add the offset).

$$CS:IP = 0154h:03B0h \ \Rightarrow\ 01540h + 03B0h = \mathbf{018F0h}$$

$$DS:SI = 0171h:01E0h \ \Rightarrow\ 01710h + 01E0h = \mathbf{018F0h}$$

**Comment:** two different segment:offset pairs give the **same** physical address. This is possible because segments can start at any 16-byte paragraph and **overlap**, so one physical byte has many logical names (up to 4096). Here the next instruction to be fetched (CS:IP) and the data byte pointed to by DS:SI are the **same memory location**. A write through DS:SI would change the code about to be executed (self-modifying code), so the code and data segments must be placed carefully.

**ii. Overlap between the code and data segments**

Each segment is 64 KB (offset 0000h-FFFFh):

| Segment | Start (base) | End (base + FFFFh) |
|:--|:-:|:-:|
| Code (CS = 0154h) | 01540h | 1153Fh |
| Data (DS = 0171h) | 01710h | 1170Fh |

The data segment starts inside the code segment, so the common part runs from **01710h to 1153Fh**:

$$\text{Overlap} = 1153Fh - 01710h + 1 = \mathbf{FE30h} = 65072 \text{ bytes}$$

Check: the two bases differ by $01710h - 01540h = 1D0h = 464$ bytes, and $65536 - 464 = 65072$ bytes ($\approx 63.5$ KB).
