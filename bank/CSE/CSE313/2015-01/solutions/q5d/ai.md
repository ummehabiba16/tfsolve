---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Use a two-level page table: only the second-level tables for used 4 MB regions are allocated, so a 12 MB process needs 16 KB instead of 4 MB."
sources: ["Tanenbaum MOS 4e, sec. 3.3.2 (multilevel page tables)"]
---
**Problem.** 32-bit address space, 4 KB pages $\Rightarrow$ $2^{20}$ pages. With 4-byte entries a single-level table is $2^{20}\times4=4$ MB **per process**, permanently in memory, although a process uses only a small part of its address space.

**Solution: a two-level (multilevel) page table.** Split the 20-bit page number into two 10-bit fields PT1 and PT2 (assumption: 4-byte entries, each table is one 4 KB page).

![Two-level page table](figures/twolevel.png)

- The **top-level table** has $2^{10}=1024$ entries (4 KB); entry PT1 points to a **second-level table** of 1024 PTEs (4 KB), which maps a $1024\times4\text{ KB}=4$ MB region.
- A second-level table is **allocated only when its 4 MB region is used**; unused entries of the top-level table are marked invalid.

**Proof of space efficiency.** Let a process touch $k$ distinct 4 MB regions. Then

$$\text{size}=\underbrace{4\text{ KB}}_{\text{top level}}+k\times4\text{ KB}\;\le\;4\text{ KB}+1024\times4\text{ KB}=4\text{ MB}+4\text{ KB}$$

- **Typical process** (code, data/heap and stack in 3 regions, 12 MB in use): $4+3\times4=16$ KB, i.e. $256$ times smaller than the 4 MB of the single-level table.
- **Worst case** (all 1024 regions used): only 4 KB more than the single-level table, which happens only for processes that use the whole 4 GB.

So the memory spent on page tables is proportional to the memory actually used, not to the size of the address space. (The price is one extra memory access per level on a TLB miss.)
