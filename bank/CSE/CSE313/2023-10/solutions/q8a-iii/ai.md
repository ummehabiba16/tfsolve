---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
changes:
  - "2026-09-30 (import): split from the combined (i)-(iii) solution."
---
Because lfs only ever *appends* new log entries (it never overwrites live data in place), a crash mid-`rm` simply leaves the update incomplete in the log:

- If the segment containing the new (updated) directory data was never fully written (the checksum in its segment summary fails to validate), recovery discards that partial segment entirely, and the file system reverts to its state *before* the `rm` began -- `lfsfile.txt` is still present, exactly as if the delete had never been attempted.
- If the segment *was* fully written and validated before the crash (the crash happened only before the next checkpoint), **roll-forward** recovery (replaying validated post-checkpoint segments) ensures the delete is still correctly reflected.

Either way, the file system ends up in a consistent state -- either fully deleted or not deleted at all, never half-deleted -- because of the atomic, append-only, checksum-validated nature of lfs's log.
