---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Log records are replayed after a crash, possibly more than once (even during recovery); an idempotent operation gives the same result however many times it is applied."
sources: ["OSTEP ch. 42 (crash consistency: journaling; recovery); Tanenbaum MOS 4e, sec. 4.4.3"]
---
**Idempotent** means that applying an operation **several times has the same effect as applying it once**.

**Why the logged operations must be idempotent.** After a crash the file system recovery **replays (redoes) the committed log records**. The system may crash **again during recovery**, or it cannot know whether a logged operation had already been applied to the file system before the crash (the log is only truncated after the changes are checkpointed). So some records will be replayed **more than once**. If an operation were not idempotent, the second replay would corrupt the file system.

**Example.**

- *Idempotent:* "mark block 17 as allocated in the bitmap" (set bit 17 to 1) or "write the contents $X$ into block 42": repeating it leaves the same state.
- *Not idempotent:* "toggle bit 17", "add 1 to the free-block count" or "append this entry to the directory": replaying twice would flip the bit back, miscount, or add the entry twice.

Journaling file systems therefore log the *new values* of the blocks (physical/redo records: block 17's new contents), not the *actions* that produced them.
