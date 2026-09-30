---
author: ai
via: chat
status: unverified
summary: 'The lost-wakeup race: count is tested and updated without mutual exclusion, so a wakeup sent to a not-yet-sleeping process is lost and both can sleep forever.'
sources: [IPC slides 24-28, 'Tanenbaum, MOS 4e, sec. 2.3.4']
imported_from: tfsolve-questions/data/solutions/2019-20.json
---
$count$ is shared and accessed without a lock. Race: the buffer is empty ($count=0$). The consumer tests $count==0$ and decides to sleep, but before it actually calls $sleep()$ the scheduler switches to the producer. The producer inserts an item, sets $count=1$, and calls $wakeup(consumer)$, but the consumer is not sleeping yet, so the wakeup is lost. The consumer resumes and sleeps. The producer keeps filling until $count==N$ and then also sleeps. Both sleep forever.

Root cause: the test of $count$ and the decision to sleep are not atomic (no mutual exclusion around the shared counter). Semaphores fix this by making test-and-block atomic.
