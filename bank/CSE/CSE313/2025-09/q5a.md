---
marks: 18
topics: [multilevel-page-table]
---
Consider a 32-bit virtual address space with 4KB pages. Each page table entry (PTE) or page directory entry (PDE) is 4-byte. A 3-level paging scheme is used where the virtual address is divided into 8 bits for level-1, 6 bits for level-2, 6 bits for level-3, and 12 bits for the page offset.

A process uses virtual pages 0--3 for code, 1024--2047 for heap, and $2^{20}-4$ to $2^{20}-1$ for stack. The rest of the pages are unused. (3+9+6=18)

i.  If a single-level page table is used, **determine** the total amount of memory required to store only the page table.

ii. If a 3-level page table is used, **compare** the total amount of memory used by the page table structures for this process.

iii. For the 3-level page table, identify and explain any memory wastage due to internal or external fragmentation in our current setting. Determine the reason and **propose** a possible solution to mitigate such wastage.
