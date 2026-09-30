---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
Both `ffs` and `lfs` are reactions to the limitations of the simple vsfs design, but they optimize for *opposite* ends of the I/O path:

**ffs (Fast File System)** optimizes primarily for **read performance / on-disk locality**. It divides the disk into block groups (cylinder groups) and uses *placement heuristics at allocation time*: keep a file's data in the same group as its (parent) directory's inode, keep files within the same directory close together, and spread only very large files across multiple groups (via a chunk-size threshold) so they don't monopolize one group's free space. The goal is to minimize **seek time for typical access patterns** (directory traversal, reading many small related files) by physically clustering related data.

**lfs (Log-structured File System)** optimizes primarily for **write performance**. It buffers updates (both data and metadata) in memory and writes them all out together as one large, purely **sequential append** to a fresh segment at the end of the log, converting many small, scattered random writes into one big sequential write that exploits the disk's much higher sequential bandwidth. This targets the small-random-write bottleneck that plagues in-place-update file systems, but at the cost of extra machinery: inodes move on every update (needing an inode map / imap to find them), and old, superseded data must eventually be reclaimed via **segment cleaning** (garbage collection).

In short: ffs optimizes *placement* (mostly to help future *reads*); lfs optimizes the *write path itself* (batching and sequentializing writes), accepting extra cleaning overhead and a level of indirection (the imap) on reads in exchange.
