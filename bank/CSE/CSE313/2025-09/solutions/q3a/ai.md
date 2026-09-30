---
author: ai
via: chat
status: unverified
summary: A safe state has an ordering letting every process reach its maximum and finish; an unsafe state has none (but is not yet a deadlock). Banker's grants a request only if the resulting state is still safe.
sources: [Deadlocks slides 25-31, 'Tanenbaum, MOS 4e, sec. 6.5']
imported_from: tfsolve-questions/data/solutions/2023-24.json
---
- Safe state: there is an ordering $P_{i_1},\dots,P_{i_n}$ such that each $P_{i_k}$'s remaining need can be met by the currently available resources plus those held by $P_{i_1},\dots,P_{i_{k-1}}$.
- Unsafe state: no such ordering exists. Unsafe $\ne$ deadlock, the processes might still finish if they do not all claim their maxima, but the system can no longer guarantee it.

Banker's algorithm (multiple resources): keep Allocation, Max and Available. On a request, tentatively grant it, compute Need = Max $-$ Allocation, then run the safety check, repeatedly find a process with Need $\le$ Available, add its Allocation back to Available, and mark it done. If all finish, the state is safe and the grant is kept; otherwise the request is denied and the process waits.
