---
author: ai
via: chat
status: unverified
summary: "An inode map (imap) gives each inode number its current log address; the checkpoint region says where the imap pieces are."
imported_from: cse313_mem_fs_solved.tex
changes:
  - "2026-09-30 (import): split from the combined (i)-(iii) solution."
---
Because lfs writes inodes to new locations on every update (never in place), a fixed, statically-computable inode table (as in vsfs/ffs) cannot be used -- there is no fixed slot to always find inode $i$ at. lfs solves this with the **inode map (imap)**: a level of indirection that maps each inode number to its *current* on-disk location. The imap itself is small enough to be mostly kept in memory (and is itself periodically written to the log), with the **checkpoint region** providing a fixed, well-known place to bootstrap finding the current imap pieces after a reboot.
