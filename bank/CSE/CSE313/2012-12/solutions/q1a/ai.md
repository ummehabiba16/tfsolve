---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A pure triple-indirect scheme would make every access, even to small files, cost three extra block reads and waste index blocks; the hierarchy keeps small files fast."
sources: ["Bach, ch. 4 (inode structure); Tanenbaum MOS 4e, sec. 4.3.2"]
---
Using **only triple indirection** would give almost the same maximum file size, but it would be **very inefficient for the typical (small) file**:

- **Access time:** to reach *any* data block the kernel would have to read the triple-indirect block, then a double-indirect block, then a single-indirect block before the data block: **3 extra disk accesses for every block** (even for a 1-block file). With direct pointers the first 10-16 blocks, which cover most files, are found in the inode that is already in memory with **no extra access**; single indirection costs 1 extra access, double 2, triple 3, so the cost grows only with the file size.
- **Space:** a small file would need **three pointer blocks** (one per level) just to address its few data blocks; with direct pointers it needs none. Most files are small, so the waste would be large.
- **Caching:** the index blocks would have to be cached for every file.

The mixed design is a **tree with unbalanced depth**: small files are cheap, large files can still be handled, and the maximum size is determined by the deepest level.
