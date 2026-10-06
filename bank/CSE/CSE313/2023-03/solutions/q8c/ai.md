---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Raw swap partition avoids file-system overhead and allows large contiguous I/O and fast direct page-to-block mapping; paging must also work when the file system needs memory."
sources: ["OSTEP ch. 21-22 (swapping)", "Tanenbaum MOS 4e, sec. 3.6 (backing store)"]
---
The swap area is a **raw partition** (or a pre-allocated contiguous file) that the VM system manages itself instead of going through the file API, because:

- **Speed.** Reading or writing a file needs path lookup, inode and indirect-block traversal, permission checks, and goes through the buffer cache and (often) a journal. Page-fault handling is on the critical path and must be fast. In a swap partition the disk address of a page is computed directly (partition start $+$ slot number $\times$ page size), with no metadata.
- **Contiguity and large I/O.** The swap area is allocated in contiguous disk regions, so pages can be written out in big sequential chunks, avoiding fragmentation and seeks.
- **No circular dependency.** The file system itself needs memory (buffers, cache, structures). Under memory pressure the OS must be able to write pages out *without* allocating memory through the file system, which could trigger even more paging.
- **Semantics.** Swap contents are only meaningful while the system runs: no need for names, permissions, durability or crash consistency, so the file abstraction would be pure overhead.
