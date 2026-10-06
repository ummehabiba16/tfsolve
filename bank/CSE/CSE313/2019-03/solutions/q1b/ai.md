---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "i. a multilevel table needs memory only for the used parts of the address space; ii. 16 KB pages give a 14-bit offset, 4096 entries per table: 12 bits top level + 12 bits second level."
sources: ["Tanenbaum MOS 4e, sec. 3.3.2 (multilevel page tables)"]
---
**i. Advantage of a multilevel page table.** A single-level table needs an entry for *every* virtual page (here $2^{38-14}=2^{24}$ entries per process) and the whole table must be in memory. A multilevel table is a tree: second-level tables are created **only for the parts of the address space that are in use**, and unused parts need no memory; the tables can also be paged out. Memory for page tables is therefore proportional to the memory actually used, not to the size of the address space.

**ii. Splitting the 38-bit address** (16 KB pages, 4-byte entries):

- Page offset: $16\text{ KB}=2^{14}\Rightarrow$ **14 bits**.
- A page-table page holds $16\text{ KB}/4\text{ B}=2^{12}=4096$ entries $\Rightarrow$ each table is indexed with **12 bits** if every table is to fit exactly in one page.
- Remaining bits: $38-14=24=12+12$.

$$\boxed{\text{top-level field}=12\text{ bits},\quad\text{second-level field}=12\text{ bits},\quad\text{offset}=14\text{ bits}}$$

(Total $12+12+14=38$.)
