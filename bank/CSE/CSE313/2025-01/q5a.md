---
marks: 13
topics: [multilevel-page-table]
---
Imagine a small address space of size 16KB, with 64-byte pages. Assume each PTE is 4 bytes. A process uses virtual pages 0 and 1 for code segment, virtual pages 4 to 32 for the heap, and virtual pages 254 and 255 for the stack; the rest of the pages of the address space are unused.

i.  If we use single-level page table, determine the total amount of physical memory used by the process?

ii. If we use two-level page table, determine the total amount of physical memory used by the process?
