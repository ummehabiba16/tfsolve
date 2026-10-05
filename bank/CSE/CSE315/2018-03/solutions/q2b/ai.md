---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "01405000h: directory index 5, table index 5, offset 000. PDE at 10000000h + 5 x 4 = 10000014h = 20000XXX: page table at 20000000h. PTE at 20000000h + 5 x 4 = 20000014h = 10000XXX: frame 10000000h. Physical address = 10000000h, which is the page directory itself, so this page contains the page directory entries."
sources: ["MHE 80386-updated slides 21-26 (10 + 10 + 12 split, CR3, physical memory access example)"]
---
**Split the linear address**

$$01405000h = 0000\ 0001\ 01\ |\ 00\ 0000\ 0101\ |\ 0000\ 0000\ 0000$$

| Field | Bits | Value |
|:--|:--|:--|
| Directory index | 31-22 | 0000000101 = **5** |
| Table index | 21-12 | 0000000101 = **5** |
| Offset | 11-0 | **000h** |

**Step 1: page directory entry** (PDBR = CR3 = 10000000h, 4 bytes per entry)

$$\text{PDE address} = 10000000h + 5 \times 4 = 10000014h$$

Content = 2000 0XXX: the upper 20 bits give the **page table base = 20000000h** (low 12 bits are attributes; assumed present).

**Step 2: page table entry**

$$\text{PTE address} = 20000000h + 5 \times 4 = 20000014h$$

Content = 1000 0XXX: **page frame base = 10000000h**.

**Step 3: physical address**

$$PA = 10000000h + 000h = \mathbf{10000000h}$$

**Comment on the page.** The page frame 10000000h is the **same address as the PDBR**: this linear address maps onto the **page directory itself**. The page therefore contains the page directory entries (0100AXXX, 001A0XXX, 102A0XXX, ...). Mapping the directory into the linear address space like this lets the operating system read and change its own page directory and tables through ordinary linear addresses (a self-mapping/recursive mapping trick), but a program writing here would corrupt the paging structures, so the page should be accessible only at supervisor level.
