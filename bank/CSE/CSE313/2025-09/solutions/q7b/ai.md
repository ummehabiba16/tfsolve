---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
---
**(i) Scenario A -- metadata journaling, crash after data $D$ written but before the metadata commit record.** In the standard ("ordered mode") protocol, the file's actual data is written to its *home* location *before* the corresponding metadata transaction is even committed to the journal -- precisely to avoid inconsistency. Since the crash happens before the commit record for the metadata is written, recovery finds an **incomplete** journal transaction (no valid commit block) and simply **discards** it, exactly as if the operation never started. The on-disk metadata is therefore left in its old, unmodified, fully **consistent** state (no pointer refers to $D$ yet). Data block $D$ physically exists on disk but is simply an orphaned, unreferenced block -- wasted space, but harmless: no metadata is stale or points at invalid data, because the metadata was never touched.

**(ii) Scenario B -- metadata journaling, crash after the metadata commit but before $D$ is flushed to its home location.** This describes what happens if the "data-before-commit" ordering rule is *not* enforced (akin to ext3's weaker "writeback" mode). On reboot, the journal replay sees a fully committed metadata transaction and **replays it**, updating the inode/pointers to reference block $D$ -- but $D$'s actual on-disk *content* was never flushed with the new data, so it may still contain **stale leftover content** from whatever previously occupied that block (potentially another, unrelated file). The result is an inconsistency where valid-looking metadata now points at garbage/stale data -- a well-known security/correctness hazard, which is exactly why "ordered" journaling (write data before committing metadata) is the safer default.

**(iii) Scenario C -- data journaling, crash after the data is journaled (committed) but before it is checkpointed to its home location.** Because *both* the data and the metadata were fully written and committed together inside the journal before the crash, the durable log already contains a complete, valid, "redo"-able copy of everything needed. **Yes**, recovery results in a fully consistent state: the recovery procedure scans the journal, finds the completed (TxB\...TxE) transaction, and simply **replays / re-copies** its contents from the journal to their home locations, finishing the interrupted checkpoint. Nothing is lost -- this is exactly the guarantee write-ahead (journal-then-checkpoint) logging is designed to provide.

**(iv) Metadata vs. data journaling.**

- *Speed*: metadata journaling is **faster**, because only the (usually much smaller) metadata blocks are written into the journal -- actual file data is written to its home location just once. Data journaling writes every data byte *twice* (once to the journal, once at checkpoint), roughly doubling write I/O.

- *Never-see-garbage guarantee*: **data journaling** gives the stronger guarantee -- because data and metadata are logged and committed together atomically, recovery can always restore a fully consistent *combination* of both, so users can never observe stale/garbage data after a crash (as can happen in Scenario B under weaker metadata-only journaling).
