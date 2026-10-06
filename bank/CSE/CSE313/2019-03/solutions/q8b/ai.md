---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Fragmentation: unusable pieces of space; contiguous allocation causes external fragmentation (holes after deletions) and internal fragmentation (last block)."
sources: ["Tanenbaum MOS 4e, sec. 4.3.2 (contiguous allocation)"]
---
**Disk fragmentation.** The free disk space becomes broken into **many small pieces that are not contiguous**, or space inside allocated blocks is wasted, so that although the total free space is large, it cannot be used for a request. There are two kinds: **internal** (unused space *inside* an allocated block) and **external** (unusable free holes *between* allocated areas).

**Contiguous allocation.** Each file occupies a **run of consecutive blocks**. Initially the files are packed one after the other, but

- when a file is **deleted**, it leaves a **hole**; files are of different sizes, so after many creations and deletions the disk looks like a checkerboard of files and holes of various sizes. A new file of $n$ blocks needs a hole of $n$ consecutive blocks; if every hole is smaller, the allocation fails although the total free space is more than $n$: **external fragmentation**. Compaction would fix it, but moving the whole disk is too expensive.
- the **last block** of every file is on average half empty: **internal fragmentation**.
- A file cannot grow if the following blocks are used; its maximum size must be known at creation.

(Contiguous allocation works well only for write-once media like CD-ROMs, where the sizes are known in advance.)
