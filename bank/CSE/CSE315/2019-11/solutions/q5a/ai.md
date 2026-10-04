---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "CS = 0028H: index 5, TI = 0 (GDT), RPL 0. GDT entry 5 = 0000 9A 01 3B2A 2B1A: access 9AH (present code segment), base 013B2AH, limit 2B1AH. Code segment runs from 013B2AH to 013B2AH + 2B1AH = 016644H."
sources: ["MHE 80286 slides (selector, GDT/LDT, descriptor format, access right byte)", "Brey, The Intel Microprocessors, Sec. 2-3 (protected-mode memory addressing, 80286 descriptor)"]
---
**Step 1: decode the selector**

CS = 0028H = 0000 0000 0010 1**0**00:

| Field | Bits | Value |
|:--|:--|:--|
| Selector (index) | 15-3 | 0000 0000 0010 1 = **5** |
| TI | 2 | **0**: Global Descriptor Table |
| RPL | 1-0 | 00 (privilege level 0) |

So CS selects **descriptor 5 of the GDT** (located at GDT base + $5 \times 8$).

**Step 2: read the descriptor**

GDT entry 5 = 0000 9A 01 3B2A 2B1A. Splitting by bytes (byte 7 on the left, byte 0 on the right):

| Bytes | Field | Value |
|:--|:--|:--|
| 7-6 | Reserved | 0000H |
| 5 | Access rights | **9AH** |
| 4 | Base address (bits 23-16) | **01H** |
| 3-2 | Base address (bits 15-0) | **3B2AH** |
| 1-0 | Limit | **2B1AH** |

Access rights 9AH = 1 00 1 1 0 1 0: P = 1 (present), DPL = 00, S = 1 (code/data descriptor), E = 1 (**code segment**), C = 0, R = 1 (readable), A = 0. So it is a valid code segment.

**Step 3: start and end addresses**

$$\text{Start (base)} = \mathbf{013B2AH}$$

$$\text{End} = \text{base} + \text{limit} = 013B2AH + 2B1AH = \mathbf{016644H}$$

The code segment is $2B1AH + 1 = 2B1BH$ (11035) bytes long, offsets 0000H-2B1AH.
