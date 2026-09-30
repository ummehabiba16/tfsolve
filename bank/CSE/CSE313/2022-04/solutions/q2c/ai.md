---
author: ai
via: chat
status: unverified
summary: (i) Marking THINKING after the two test() calls tests while still EATING, so hungry neighbours are never woken (lost wakeup / starvation). (ii) Moving up(&s[i]) outside the if signals s[i] on every call, breaking fork mutual exclusion so two neighbours can eat at once.
sources: [IPC slides 51-56, 'Tanenbaum, MOS 4e, sec. 2.5.1']
imported_from: tfsolve-questions/data/solutions/2019-20.json
---
(i) Setting $state[i]=THINKING$ after the two $test()$ calls (instead of before): $test(LEFT)$ and $test(RIGHT)$ run while philosopher $i$ is still marked $EATING$. A hungry neighbour fails its check (the condition $state[i]\ne EATING$ is false), so it is not woken even though $i$ is about to stop eating. Neighbours can be left blocked forever, a lost wakeup and possible starvation.

(ii) Putting $up(\&s[i])$ outside the $if$ in $test()$: $s[i]$ is signalled on every call, even when the philosopher did not move HUNGRY$\to$EATING. The extra signals push $s[i]$ above 1, so a later $down(\&s[i])$ that should block does not, letting two neighbours hold the shared fork and eat simultaneously, mutual exclusion on the forks is broken.
