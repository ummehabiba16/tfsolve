---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Data journaling writes TxB, bitmap, inode, 3 data blocks, then TxE, then checkpoints; metadata journaling writes data first and journals only bitmap+inode; the checksum version drops the wait before commit."
sources: ["OSTEP ch. 42 (crash consistency: journaling)"]
---
Blocks to be updated: data blocks **8, 11, 12**; inode in block **3**; bitmap in block **2**. The journal occupies blocks **24-31**.

**i. Data journaling.** All the blocks are first written to the journal:

| Journal block | 24 | 25 | 26 | 27 | 28 | 29 | 30 | 31 |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Contents | TxB | bitmap (2) | inode (3) | D8 | D11 | D12 | TxE | free |

Timeline:

1. **Journal write:** write TxB, bitmap, inode, D8, D11, D12 (24-29) and wait for them to complete.
2. **Journal commit:** write TxE (30) and wait: the transaction is committed.
3. **Checkpoint:** write bitmap (2), inode (3), D8, D11, D12 to their home locations.
4. **Free:** mark the transaction free in the journal superblock.

**ii. Metadata journaling.** Only the metadata (bitmap and inode) goes to the journal: TxB (24), bitmap (25), inode (26), TxE (27).

1. **Data write:** write D8, D11, D12 to their final locations.
2. **Journal write:** TxB, bitmap, inode (24-26). (Steps 1 and 2 may be issued together.)
3. Wait for *both* to complete, then **journal commit:** write TxE (27) and wait.
4. **Checkpoint:** write bitmap (2) and inode (3) to their final locations.
5. **Free** the transaction.

The data is written first so that the inode never points to garbage after a crash.

**iii. Metadata journaling with checksum optimisation.** TxB holds a checksum of the whole transaction, and there is no separate wait before TxE:

1. **Journal write and commit in one go:** write TxB (with checksum), bitmap, inode and the final data blocks D8, D11, D12 at the same time; wait for all.
2. **Checkpoint:** write bitmap (2) and inode (3).
3. **Free.**

On recovery the checksum of the journalled blocks is recomputed; if it does not match, the transaction is discarded. This removes one rotation/wait of the protocol.
