---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Paging divides linear and physical memory into fixed-size pages (4 KB) and maps each linear page to any physical frame through page tables, invisible to programs. Segmentation divides a program into variable-size logical segments (code, data, stack) with base, limit and rights. Differences: fixed vs variable size; physical/OS view vs logical/program view; no external fragmentation vs external fragmentation; page tables vs descriptor tables; per-page vs per-segment protection; paging maps linear to physical, segmentation logical to linear."
sources: ["MHE 80386-updated slides 16-24 (segmentation, paging)", "Brey, The Intel Microprocessors, Sec. 2-4"]
---
**Paging.** A memory-management scheme in which the **linear address space and physical memory are divided into equal fixed-size blocks** (pages and page frames, 4 KB on the 80386). Page tables map each linear page to any physical frame. Pages can be moved to disk and brought back when needed (virtual memory). It is invisible to application programs.

**Paging vs segmentation**

| | Segmentation | Paging |
|:--|:--|:--|
| Unit | **segments of variable size** (1 byte to 64 KB / 4 GB) | **pages of fixed size** (4 KB) |
| View | logical: follows the program's structure (code, data, stack) | physical: chosen by the OS, not visible to the program |
| Address translation | logical (selector:offset) $\to$ linear: base + offset | linear $\to$ physical: directory, table, frame + offset |
| Tables | descriptor tables (GDT, LDT) | page directory and page tables (CR3) |
| Protection | per segment: limit, type, privilege levels 0-3 | per page: present, read/write, user/supervisor |
| Fragmentation | **external** fragmentation (holes between segments), whole segments swapped | no external fragmentation (any free frame fits); small internal fragmentation in the last page |
| Swapping | large, variable units: slow | small, equal units: efficient |

On the 80386/Pentium both are used together: segmentation first gives a linear address, then paging maps it to a physical address.
