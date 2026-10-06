---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "2^36 entries x 4 B = 256 GB per process: infeasible; use multi-level or inverted page tables."
sources: ["Tanenbaum MOS 4e, sec. 3.3.2-3.3.4 (multilevel and inverted page tables)", "OSTEP ch. 20"]
---
**Calculation.** 48-bit virtual addresses, 4 KB $=2^{12}$ pages:

$$\text{VPN bits} = 48-12 = 36\ \Rightarrow\ \text{entries} = 2^{36}$$

$$\text{size} = 2^{36}\times 4\text{ B} = 2^{38}\text{ B} = \mathbf{256\ GB}\ \text{per process}$$

**Feasibility.** Not feasible: the table would have to be kept (contiguously) in memory for every running process and is far larger than the physical memory of a typical machine. Moreover, most of it is wasted, since a typical process uses only a tiny part of its 256 TB address space.

**Better alternatives** (only the parts of the table that are actually used are stored):

1. **Multilevel (hierarchical) page tables**: the VPN is split into several fields (e.g. four levels of 9 bits in x86-64); lower-level tables are allocated only for regions in use.
2. **Inverted page table** (one entry per *physical frame*, searched with a hash on (PID, VPN)): its size depends on the physical memory size, not on the virtual address space. (A hashed page table is a variant.)
