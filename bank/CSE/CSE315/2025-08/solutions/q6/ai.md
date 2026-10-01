---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Linear = 0140F4A2H, split 5 / 15 / 4A2H. PDE at 114H = 00200001H; PTE at 23CH = 00600001H; physical address = 006004A2H."
sources: ["MHE 80386-updated slides 21-26 (paging; physical memory access example)"]
---
**Linear address** (protected mode: the CS cache gives the base directly)

$$\text{Linear} = \text{CS base} + EIP = 01400000H + 0000F4A2H = 0140F4A2H$$

**Split into 10 + 10 + 12 bits**

$$0140F4A2H = 0000\,0001\,01\ |\ 00\,0000\,1111\ |\ 0100\,1010\,0010$$

- Directory = $(0000000101)_2 = 5$
- Page table = $(0000001111)_2 = 15$
- Offset = 4A2H

**(i) Page directory entry's physical address**

$$= CR3 + 5\times4 = 100H + 14H = \mathbf{114H}$$

Bytes at 114H to 117H are 01 00 20 00 (little-endian), so the PDE is **00200001H**. Only its upper 20 bits, 00200H, are used for addressing; the low bits are status bits (P = 1).

**(ii) Page table entry's physical address**

Using the PDE's upper 20 bits, 00200H, as the page table address and adding $15\times4 = 3CH$ (as in the slide example "20000H + 101 x 4"):

$$= 200H + 3CH = \mathbf{23CH}$$

Bytes at 23CH to 23FH are 01 00 60 00, so the PTE is **00600001H**, and the page frame (upper 20 bits) is 00600H.

*Note: by the strict rule, the page table starts at 00200000H, which would give the PTE at 0020003CH. That address is not in the snapshot. The given snapshot (234H to 243H) clearly intends 23CH.*

**(iii) Physical address of the instruction**

Page frame 00600H followed by the 12-bit offset 4A2H:

$$PA = 00600000H + 4A2H = \mathbf{006004A2H}$$
