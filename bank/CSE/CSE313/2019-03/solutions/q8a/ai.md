---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A race condition is when the result of shared access depends on the exact order of execution; cooperating processes are needed for information sharing, speed-up, modularity and convenience."
sources: ["Tanenbaum MOS 4e, sec. 2.3.1-2.3.2 (race conditions)", "Silberschatz, OS Concepts, ch. 3"]
---
**Race condition.** A situation in which **two or more processes read or write shared data and the final result depends on who runs precisely when** (the order of the interleaving), so the outcome is not deterministic. *Example:* two processes both do `counter = counter + 1`, each executing `LOAD, ADD, STORE`; if both load the same value before either stores, one increment is lost. (Another: two processes add a file to the print-spooler queue at the same slot of the shared `in` variable.) It is avoided by mutual exclusion.

**Why cooperating processes are necessary.** A cooperating process can affect or be affected by others, and is needed for:

1. **Information sharing:** several users interested in the same information (a shared file, database).
2. **Computation speed-up:** a task is split into subtasks that run in parallel (on a multiprocessor).
3. **Modularity:** a system is built as separate cooperating processes or threads (e.g. a pipeline of commands, client-server).
4. **Convenience:** a user can do several things at once (edit, compile, print).
