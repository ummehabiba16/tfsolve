---
author: ai
via: chat
status: unverified
summary: Yes. Making even philosophers take the left fork first and odd philosophers the right fork first prevents deadlock by breaking the circular-wait condition.
sources: [IPC slides 51-54, 'Tanenbaum, MOS 4e, sec. 2.5.1 and 6.6.4']
imported_from: tfsolve-questions/data/solutions/2021-22.json
---
With everyone grabbing left-then-right, all can hold their left fork and wait on the right, circular wait, deadlock. The even/odd rule changes the acquisition order so two neighbours contend for the SAME fork first: e.g. philosopher 0 (even, left first) and philosopher 1 (odd, right first) both reach for the fork between them. One gets it; the loser is not yet holding any other fork, so no 'hold one and wait for the next' cycle can close.

Hence the circular-wait condition cannot arise and the protocol is deadlock-free (it may still be unfair, but never deadlocked).
