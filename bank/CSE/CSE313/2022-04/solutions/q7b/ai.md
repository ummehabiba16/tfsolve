---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Three essential file properties: large storage, persistence beyond the process, shared concurrent access; contiguous allocation causes internal fragmentation (partly filled last block) and external fragmentation (holes between files)."
sources: ["Tanenbaum MOS 4e, ch. 4 intro and sec. 4.3.2 (file implementation: contiguous allocation)"]
---
**Three essential properties** (Tanenbaum, ch. 4): a file system must give

1. **Large storage:** the ability to store a very large amount of information (more than fits in a process's address space/RAM).
2. **Persistence:** information must **survive** the termination of the process that created it (and power-off); it is stored on disk, not in memory.
3. **Concurrent, shared access:** multiple processes must be able to access the information at the same time, which is why files are named and independent of any process.

**Fragmentation in contiguous allocation.** Each file occupies a run of consecutive disk blocks.

- **Internal fragmentation.** Space is allocated in whole blocks, so the last block of every file is only partly used. On average about half a block per file is wasted.
- **External fragmentation.** When files are deleted they leave **holes** of different sizes between the remaining files. After many creations and deletions the free space is broken into many small pieces: the total free space may be large, but no single hole is big enough for a new file that needs a contiguous run, so the allocation fails. (Compaction fixes it but is very expensive.) The final size of the file must also be known when it is created.
