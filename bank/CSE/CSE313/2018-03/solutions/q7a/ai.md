---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Two-phase locking: a growing phase in which all locks are acquired and a shrinking phase in which they are released; no lock is acquired after the first release."
sources: ["Tanenbaum MOS 4e, sec. 6.8.2 (two-phase locking)"]
---
**Two-phase locking (2PL)** is a locking protocol used for transactions (e.g. in databases):

- **Phase 1 (growing):** the process tries to **lock all the records it needs, one at a time**. If a needed record is already locked, it **releases all locks it holds and starts over** (so that deadlock cannot occur).
- **Phase 2 (shrinking):** once all locks have been acquired, the process performs its updates and then **releases the locks**; it never acquires a new lock after it has released one.

The two phases guarantee that concurrent transactions are **serialisable** (the result equals some serial order).
