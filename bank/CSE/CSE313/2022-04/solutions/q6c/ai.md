---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Stable storage = a pair of disks forming an error-free block via stable write, stable read and crash recovery."
sources: ["Tanenbaum MOS 4e, sec. 5.4.4 (stable storage)"]
---
**Stable storage** is storage that survives disk and CPU failures (a write is either completely done or not done at all, and a stored block is never lost). It is built from **two identical disks** whose corresponding blocks together act as one error-free block. When there are no errors, corresponding blocks are identical and either can be read.

**Assumptions.**

1. A block is either written correctly or not at all, and a bad block can be **detected** by its ECC (a read returns an ECC error).
2. A good block can **spontaneously go bad** at any time.
3. The CPU can crash (e.g. power failure) in the middle of a write, leaving a half-written (detectably bad) or an old block.
4. The probability that the *same* block goes bad on *both* disks within a short time is negligible.

**The three operations.**

1. **Stable write.** Write the block on drive 1 and read it back to verify; if there is an error, repeat up to $n$ times (the block may be remapped to a spare). Only after drive 1 is good, do the same on drive 2.
2. **Stable read.** Read the block from drive 1; on an ECC error, retry; if all retries fail, read the same block from drive 2 (which, by assumption 4, is good).
3. **Crash recovery.** After a crash, scan both disks comparing corresponding blocks. If both are good and equal, do nothing; if one has an ECC error, overwrite it with the good copy; if both are good but different, the crash happened during the write of drive 1 or between the writes, so copy drive 1's (new) block over drive 2's.

These steps ensure that after any single failure, one copy of every block is intact.
