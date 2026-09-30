---
author: ai
via: chat
status: unverified
summary: The four requirements are mutual exclusion, no CPU-speed/number assumptions, no process outside its critical region blocking others, and bounded waiting. Strict alternation violates the third.
sources: [IPC slides 11-18, 'Tanenbaum, MOS 4e, sec. 2.3.2']
imported_from: tfsolve-questions/data/solutions/2023-24.json
---
1. No two processes may be inside their critical regions at the same time (mutual exclusion).
2. No assumptions may be made about speeds or the number of CPUs.
3. No process running outside its critical region may block another process.
4. No process should have to wait forever to enter its critical region (bounded waiting).

Example violating (3): strict alternation with a shared $turn$ variable. If it is process 0's turn but process 0 is busy outside its critical region, process 1, though it wants to enter, is blocked waiting for $turn$ to change, a process outside its critical region prevents another from entering.
