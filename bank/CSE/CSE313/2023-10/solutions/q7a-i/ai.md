---
author: ai
via: chat
status: unverified
summary: "mkdir p is one transaction TxB, 4, 5, 6, D_p, TxE that fills journal blocks 26-31 exactly; mv is a second one after checkpointing. Both commands only touch metadata, so data and metadata journaling log the same blocks; the checksum version writes each transaction in one batch without waiting before TxE."
imported_from: cse313_mem_fs_solved.tex
changes:
  - "2026-09-30 (import review): added p's new directory-data block (D_p), which mkdir must allocate and journal; the mkdir transaction then fills journal blocks 26-31 exactly. The mv transaction is listed separately."
---
**What the commands change.** All of these are metadata. No regular-file data is written: the 1GB file's blocks are untouched by `mv`.

- `mkdir p`: allocate an inode and a data block for `p` (bitmaps, **block 4**); initialise `p`'s inode and update the root inode's size, link count and time (inodes, **block 5**); write `p`'s new directory data with `.` and `..` (a newly allocated block, call it $D_p$); add the entry `p` to the root directory (**block 6**).
- `mv /q/foo.txt /p/bar.txt`: remove `foo.txt` from `/q`'s directory data ($D_q$), add `bar.txt` (same inode number) to $D_p$, and update the inodes of `q` and `p` (**block 5**).

**(a) Data journaling.** Each operation is one transaction. For `mkdir p`:

| Journal block | 26 | 27 | 28 | 29 | 30 | 31 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| Contents | TxB | block 4 (bitmaps) | block 5 (inodes) | block 6 (root data) | $D_p$ (p's data) | TxE |

Timeline: write 26-30 and wait for them to finish, then write TxE (31) and wait: the transaction is **committed**. Then **checkpoint**: write blocks 4, 5, 6 and $D_p$ to their home locations, and mark the journal space free. The `mv` transaction (TxB, block 5, $D_q$, $D_p$, TxE) then reuses the journal from block 26 (it is circular) and follows the same commit-then-checkpoint steps.

**(b) Metadata journaling.** Directory contents are metadata (ext3/ext4 journal them in ordered mode), and these commands write no regular-file data, so the journal contents and the timeline are the same as in (a). The two modes only differ when a file's own data blocks change: metadata journaling writes that data to its home location *first* and journals only the metadata.

**(c) Metadata journaling with checksum optimization.** Same transactions, but TxB and TxE carry a checksum of the transaction's blocks, so blocks 26-31 are written in **one batch** with no wait before TxE. On recovery the checksum is recomputed; a mismatch means the transaction was torn and it is discarded. The checkpoint step is unchanged.
