---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "LDTR = 001CH: GDT entry 3 at 100018H gives LDT base 300000H. CS = 0014H: LDT entry 2 at 300010H gives base 700000H (AR FF: present code). Physical = 700000H + 0020H = 700020H."
sources: ["MHE 80286 slides 43-52 (selector, GDT/LDT, LDTR, descriptor format)", "MHE 80286 slides 56-63 (access right byte)"]
---
Descriptor layout in memory (8 bytes, lowest address first): limit (2 B), base B0-B15 (2 B), base B16-B23 (1 B), access rights (1 B), 0000 (2 B).

**Step 1: LDTR selector (it selects a GDT descriptor that defines the LDT)**

LDTR = 001CH = 0000 0000 0001 1 | 1 | 00: index 3, RPL = 00. The LDTR selector always refers to the GDT, so the TI bit is ignored here.

$$\text{GDT descriptor address} = GDTR + 3\times8 = 100000H + 18H = 100018H$$

Bytes at 100018H: FF FF 00 00 30 FF 00 00, giving limit FFFFH and **LDT base = 300000H**.

**Step 2: CS selector**

CS = 0014H = 0000 0000 0001 0 | 1 | 00: **index 2, TI = 1 (LDT)**, RPL = 00.

$$\text{LDT descriptor address} = 300000H + 2\times8 = 300010H$$

Bytes at 300010H: FF FF 00 00 70 FF 00 00:

- Limit = FFFFH
- Base = **700000H**
- Access rights = FFH = 1 11 1 1 1 1 1: P = 1 (present), DPL = 11, S = 1, E = 1 (**code**), C = 1, R = 1 (readable), A = 1

**Step 3: physical address of the instruction**

Offset IP = 0020H $\le$ limit FFFFH, so the access is valid.

$$PA = \text{base} + IP = 700000H + 0020H = \mathbf{700020H}$$
