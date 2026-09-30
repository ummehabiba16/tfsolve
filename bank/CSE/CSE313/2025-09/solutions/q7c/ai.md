---
author: ai
via: chat
status: unverified
summary: "(i) Correct for data journaling. For metadata journaling it is unsafe unless data is still written before the transaction: the checksum does not cover data blocks, so TxE could reach disk first and replay would point at garbage. (ii) Yes, one wait per transaction disappears; drawbacks are the checksum cost, extra recovery work and the ordering still needed for metadata journaling."
imported_from: cse313_mem_fs_solved.tex
changes:
  - "2026-09-30 (import review): part (i) corrected. The earlier answer called the scheme sound for metadata journaling. There, data blocks go to their home locations outside the journal, so the checksum cannot enforce 'data before commit'."
---
This is the "transactional checksum" idea used by Linux ext4 (and described in OSTEP's journaling chapter): write the whole transaction at once and let the checksum reveal, at recovery time, whether it all made it to disk.

**(i) Correctness.**

- **Data journaling: correct.** Everything that must be atomic (the new data *and* the metadata) is inside the transaction, so the checksum covers it all. If a crash leaves any journal block missing or torn, the recomputed checksum does not match the value in TxB/TxE and recovery discards the transaction; if it matches, replay is safe. This needs a checksum strong enough to catch torn writes (ext4 uses CRC32C; a plain 32-bit sum is weaker).
- **Metadata (ordered) journaling: there is a problem.** User data is written straight to its home location and is **not** in the journal, so the checksum does not cover it. Ordered journaling is safe only because the data write *finishes before* the commit is written. If Bob issues every write at once, TxE can reach the disk before the data block. After a crash, the transaction's checksum still matches, recovery replays the metadata, and the file now points to a block that never received its new data: garbage, or another file's old contents.
  - Fix: keep waiting for the data writes before writing the transaction. Only the wait *inside* the journal (between the body and TxE) goes away.
  - Alternatively, put checksums of the data blocks into the transaction, so recovery can detect that they were never written.

**(ii) Performance.** Yes, commits get faster. The classic protocol writes TxB and the body, *waits* for them to reach the disk, then writes TxE. With checksums, TxB, the body and TxE go in one batch, which saves at least one full disk round-trip (and a cache flush) per transaction. Hidden drawbacks:

- CPU time to compute the checksum on every commit, and to recompute it for every transaction during recovery.
- The number of bytes written is the same, so the benefit is only the removed wait; it is small where flushes are already cheap.
- For metadata journaling the data-before-commit ordering still has to be enforced (or covered by extra checksums), so the gain there is smaller.
- A weak checksum can miss some torn writes, turning a rare crash into silent corruption.
