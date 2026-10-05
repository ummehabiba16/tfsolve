---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "00200000H = 0000000000 | 1000000000 | 000000000000: directory index 0, table index 200H (512), offset 000H. PDE at CR3 + 0 gives the page table base; PTE at table base + 512 x 4 = base + 800H gives the page frame; physical = frame + 000H."
sources: ["MHE 80386-updated slides 21-26 (paging: 10 + 10 + 12 split, CR3, PDE and PTE addresses, example)"]
---
**Split the linear address** (10 + 10 + 12 bits):

$$00200000H = 0000\ 0000\ 00\ |\ 10\ 0000\ 0000\ |\ 0000\ 0000\ 0000$$

| Field | Bits | Value |
|:--|:--|:--|
| Page directory index | 31-22 | 0000000000 = **0** |
| Page table index | 21-12 | 1000000000 = **200H = 512** |
| Offset | 11-0 | **000H** |

**Translation**

1. **CR3** holds the physical address of the page directory. The PDE is at
   $$\text{CR3} + 0 \times 4 = \text{CR3}$$
   Its upper 20 bits give the **base of the page table** (if P = 1).
2. The PTE is at
   $$\text{page table base} + 512 \times 4 = \text{page table base} + 800H$$
   Its upper 20 bits give the **page frame** address (if P = 1).
3. **Physical address = page frame + 000H**, i.e. the first byte of that 4 KB frame.

*Example:* if CR3 = 00010000H, the PDE at 00010000H = 00020001H (table at 00020000H) and the PTE at 00020800H = 00500001H, then the physical address is **00500000H**. (If either entry has P = 0, a page fault occurs and CR2 = 00200000H.) The TLB is checked first; on a hit no table is read.
