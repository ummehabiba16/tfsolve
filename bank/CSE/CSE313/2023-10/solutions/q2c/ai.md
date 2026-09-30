---
author: ai
via: chat
status: unverified
summary: 'The four requirements: mutual exclusion; no assumptions about CPU speed/number; a process outside its critical region must not block others; no process waits forever to enter.'
sources: [IPC slides 11-18, 'Tanenbaum, MOS 4e, sec. 2.3.2']
imported_from: tfsolve-questions/data/solutions/2021-22.json
---
1. No two processes may be inside their critical regions at the same time (mutual exclusion).
2. No assumptions may be made about speeds or the number of CPUs.
3. No process running outside its critical region may block another process.
4. No process should have to wait forever to enter its critical region (bounded waiting).
