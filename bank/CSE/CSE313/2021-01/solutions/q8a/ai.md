---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A journaling file system writes a log of intended changes before applying them, so after a crash the log is replayed instead of running a full fsck; example ext3/ext4."
sources: ["Tanenbaum MOS 4e, sec. 4.4.3 (journaling file systems)", "OSTEP ch. 42"]
---
A **journaling file system** first writes a **log (journal)** of the changes it is about to make to the file system (a transaction: begin, the blocks/operations, commit) and only then performs the changes on the real structures (the *checkpoint*). After a crash the system reads the journal and **replays** the committed transactions (and ignores incomplete ones) instead of scanning the whole disk with `fsck`, so recovery takes seconds and the file system structure stays consistent. The logged operations must be **idempotent** so that replaying them again is harmless.

**Examples:** Linux **ext3/ext4**, **XFS**, **JFS**, Windows **NTFS** (log file), Apple APFS/HFS+.
