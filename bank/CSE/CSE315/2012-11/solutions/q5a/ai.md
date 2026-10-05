---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "With TI = 0 the selector's 13-bit index picks the descriptor at GDTR.base + 8 x index (checked against GDTR.limit). The descriptor (base, limit, access rights) is checked (present, type, max(CPL, RPL) <= DPL) and loaded into the segment register's hidden cache. For each access the offset is checked against the limit and linear address = base + offset; with paging off this is the physical address, otherwise paging translates it."
sources: ["MHE 80386-updated slides 16-20 (segmentation, descriptors)", "MHE 80286 slides (selector, GDTR, descriptor cache)", "Brey, The Intel Microprocessors, Sec. 2-3"]
---
```text
 segment register (visible)          hidden descriptor cache
 +------------------+--+---+         +-----------+-----------+--------+
 |   index (13)     |TI|RPL|         | base (32) | limit (20)| rights |
 +--------+---------+--+---+         +-----+-----+-----+-----+---+----+
          |        TI = 0                  ^           |         |
          v                                | loaded    |         |
  GDTR: | base | limit |                   | once      |         |
          |                                |           v         v
          +--> GDT base + 8 x index ---> descriptor   offset <= limit?  rights ok?
                                         (8 bytes)        |  no: #GP
  instruction: offset (EA) -----------------------------> (+) <--- base
                                                           |
                                                    LINEAR address --> paging --> physical
```

**Steps**

1. **Selector.** The segment register holds a selector: index (bits 15-3), **TI = 0** (GDT) and RPL (bits 1-0).
2. **Locate the descriptor.** The processor checks that $8 \times index + 7 \le$ **GDTR.limit**, then reads the 8-byte descriptor at **GDTR.base + 8 $\times$ index**. (Index 0 is the null descriptor and may not be used for memory access.)
3. **Check the descriptor** when the selector is loaded: present (P = 1), correct type (a data segment for DS/ES/FS/GS, a writable data segment for SS, a code segment for CS), and privilege: for data $\max(CPL, RPL) \le DPL$. A failure gives an exception (#GP, #NP, #SS).
4. **Cache it.** Base, limit and access rights are copied into the segment register's **hidden descriptor cache**, so later accesses do not read the GDT again.
5. **Each memory access:** the offset (effective address from the instruction) is checked against the **limit** (and the access type against the rights: e.g. no writes to read-only data), and

$$\text{linear address} = \text{base} + \text{offset}$$

6. If paging is disabled, the linear address is the physical address; otherwise the **paging unit** translates it (page directory, page table) to a physical address.

*Example:* DS = 0010H (index 2, GDT, RPL 0), GDTR.base = 00010000H: descriptor at 00010010H with base 00200000H, limit FFFFFH (G = 0): `MOV AL, [1234H]` reads linear address 00201234H.
