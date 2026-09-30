---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
**VSFS** places its metadata (inodes, bitmaps) at **fixed, statically-known** disk locations -- e.g. inode number $i$ always lives at a location computable directly as (fixed inode-table start) $+\, i\times(\text{inode size})$. Nothing ever moves, so any inode can always be found again with a simple calculation; no separate "pointer" structure is needed to remember where things currently are.

**LFS** writes *everything* -- including inodes -- to new locations at the tail of the append-only log on every update, so an inode's physical location changes every single time it (or its data) is modified. This requires an **inode map (imap)** to track each inode's current location, but the imap itself also moves as it gets updated. A **checkpoint region** is therefore needed as a small, fixed, well-known location on disk that periodically records where the current, up-to-date pieces of the imap (and hence the entire file system) can be found -- giving the system a reliable starting point to bootstrap lookups/recovery from after a reboot or crash. VSFS has no analogous "moving target" problem, so it needs no such bootstrap-pointer structure.
