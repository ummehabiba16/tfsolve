---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Starvation: a process waits indefinitely although the resource is repeatedly granted to others; the solution can starve deleters, because a steady stream of searchers or inserters keeps the lightswitch locked."
sources: ["Tanenbaum MOS 4e, sec. 6.7.3 (starvation); Downey, Little Book of Semaphores"]
---
**Starvation.** A process is **perpetually denied** a resource it needs (it waits indefinitely, although it is not deadlocked) because other processes keep getting it (e.g. a policy that always serves the shortest job lets a long job wait forever). Unlike a deadlock, the system as a whole makes progress.

**Does the solution starve?** **Yes, deleters can starve.** A deleter must acquire `noSearcher` and `noInserter`. `noSearcher` is held as long as **at least one searcher is active** (the lightswitch only releases it when the *last* searcher leaves). If new searchers keep arriving before the previous ones finish, the counter never reaches 0, so the semaphore stays locked and **the deleter waits forever**; the same holds for a steady stream of inserters and `noInserter`.

(The searchers and inserters themselves do not starve in this solution, except that, once a deleter holds `noSearcher`, they wait for it; as soon as the deleter finishes, they continue.)

**A remedy:** make arriving searchers/inserters wait while a deleter is waiting (a turnstile semaphore that the deleter takes first: `down(&turnstile); ... up(&turnstile)` and each searcher/inserter passes through it), or use a queue that serves requests in arrival order.
