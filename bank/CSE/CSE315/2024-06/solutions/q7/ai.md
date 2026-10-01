---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "CS = 0020H: GDT descriptor 4 (38D4 9A23 A216 320B), base 3823A216H, G = 1. Linear = 58CEB2E3H = dir 355 / table 235 / offset 2E3H. PDE at CR3 + 58CH, PTE at 000503ACH, physical = 000802E3H."
sources: ["MHE 80386-updated slides 17-26 (80386 descriptor; physical memory access example)"]
---
**Selector.** CS = 0020H = 0000 0000 0010 0 | 0 | 00: **index 4**, TI = 0 (GDT), RPL = 00, so descriptor 4 at $GDTR + 4\times8$ = GDTR + 20H.

**Descriptor 4 = 38D4 9A23 A216 320B** (written MSB first, as in the slide example):

| Field | Value |
|:--|:--|
| Base B31-B24 | 38 |
| G D 0 AV / Limit L19-L16 | D4 = 1101 0100: G = 1, D = 1, AV = 1, L19-L16 = 4 |
| Access rights | 9A = 1 00 1 1 0 1 0: present, DPL 00, code, readable |
| Base B23-B16 | 23 |
| Base B15-B0 | A216 |
| Limit L15-L0 | 320B |

- Base = **3823A216H**
- Limit = 4320BH $\times$ 4K = 4320B000H (G = 1)
- Offset 20AB10CDH $\le$ limit, so the access is OK

**Linear address**

$$3823A216H + 20AB10CDH = 58CEB2E3H$$

**Split 10 + 10 + 12**

$$58CEB2E3H = 0101\,1000\,11\ |\ 00\,1110\,1011\ |\ 0010\,1110\,0011$$

- Directory = $(0101100011)_2 = 355$
- Page table = $(0011101011)_2 = 235$
- Offset = 2E3H

**(ii) Page directory entry physical address**

$$= CR3 + 355\times4 = CR3 + 58CH$$

CR3 is not given; with CR3 = 00000000H this is **0000058CH**. Page directory entry 355 = 00050000H, so the page table starts at **00050000H** (upper 20 bits 00050H).

**(iii) Page table entry physical address**

$$= 00050000H + 235\times4 = 00050000H + 3ACH = \mathbf{000503ACH}$$

Page table entry 235 = 00080000H, so the page frame starts at 00080000H.

**(i) Physical address of the instruction**

$$= 00080000H + 2E3H = \mathbf{000802E3H}$$
