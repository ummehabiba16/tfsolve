---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Linked-list allocation stores the next-block pointer in each data block (no external fragmentation, but slow random access and less data per block); with a FAT in memory the pointers are kept in a table, giving fast random access at the cost of memory."
sources: ["Tanenbaum MOS 4e, sec. 4.3.2 (linked-list allocation; linked list using a table in memory)"]
---
| | **Linked-list allocation** | **Linked list using a table in memory (FAT)** |
|:--|:--|:--|
| Where the pointers are | in the **first bytes of each data block** (each block points to the next) | in a **table (FAT) with one entry per disk block**, kept in memory; the directory entry gives the first block |
| Data per block | less than a full block (the pointer takes a few bytes: the block size is no longer a power of 2) | a **full block** of data per block |
| Sequential access | good | good |
| **Random access** | very **slow**: to reach block $n$ the system must read the $n$ preceding blocks from the disk | **fast**: follow the chain in the table **in memory** (no disk access), though still $O(n)$ memory steps |
| Memory needed | none | the **whole table** in memory (one entry per block): for a 1 TB disk with 4 KB blocks, $2^{28}$ entries $\times4$ B $=1$ GB: a problem for big disks |
| Fragmentation | no external fragmentation; any free block can be used | same |
| Reliability | one damaged pointer loses the rest of the file | table can be duplicated on disk |

Used by: the first (linked list) is rarely used; the second is the **MS-DOS/Windows FAT file system**.
