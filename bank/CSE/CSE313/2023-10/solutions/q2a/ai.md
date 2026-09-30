---
author: ai
via: chat
status: unverified
summary: '(i) Under priority scheduling a high-priority H busy-waits forever on a low-priority L that is inside the region but never scheduled (priority inversion). (ii) Under round-robin the inversion is temporary: L eventually gets a slice, leaves the region, and H proceeds.'
sources: [IPC slides 19-23, 'Tanenbaum, MOS 4e, sec. 2.3.3']
imported_from: tfsolve-questions/data/solutions/2021-22.json
---
(i) Priority inversion. A low-priority process $L$ is inside its critical region ($interested[L]=TRUE$). A high-priority $H$ becomes ready; the scheduler always prefers $H$, so $H$ spins in $enter\_region$ waiting for $L$. But $L$, being lower priority, is never chosen to run and so never leaves the region. $H$ busy-waits forever and $L$ never progresses, the high-priority process is blocked by the low-priority one.

(ii) With round-robin instead of priority scheduling the deadlock does not persist: RR eventually gives $L$ a time slice, $L$ finishes its critical region and clears $interested[L]$, then $H$'s spin condition becomes false and $H$ enters. Some busy-wait cycles are wasted, but there is no permanent inversion or starvation.
