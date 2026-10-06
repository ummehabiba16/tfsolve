---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "FAT random access follows a linked list of blocks (O(position) steps, even if the FAT is cached); FFS finds any block in at most four index lookups: FFS is far more efficient."
sources: ["Anderson and Dahlin, OSPP, ch. 13 (FAT vs FFS)"]
---
- **FAT:** a file is a **linked list of blocks** whose "next" pointers are in the FAT. To read block $i$ the system must start at the file's first block and **follow $i$ links** in the FAT: the cost is **proportional to the position $i$** ($O(i)$). If the whole FAT is cached in memory each step is a memory reference, but for a large disk the FAT is big (it must all be in memory), and if it is not cached each step costs a disk access. Random access to the end of a large file is therefore slow.
- **FFS:** the **inode's multi-level index** gives the address of block $i$ in **at most four steps** (inode, up to three indirect blocks), independent of $i$ and of the file size: **$O(1)$** constant time, and frequently used indirect blocks stay in the cache.

So **FFS random access is much more efficient** than FAT's; FAT is acceptable for sequential access or small devices.
