---
author: ai
via: chat
status: unverified
summary: 'State diagram: New$\to$Ready$\to$Running with Running$\to$Ready (preempt), Running$\to$Blocked$\to$Ready, Running$\to$Terminated. Starvation = stuck in Ready; livelock = actively Running but making no progress.'
sources: [Process/Thread slides 11-14, 'Tanenbaum, MOS 4e, sec. 2.1.5 and 6.7']
imported_from: tfsolve-questions/data/solutions/2022-23.json
---
States and transitions: New $\to$ Ready (admitted); Ready $\to$ Running (dispatch); Running $\to$ Ready (time-out / preempt); Running $\to$ Blocked (wait for I/O or event); Blocked $\to$ Ready (event done); Running $\to$ Terminated (exit).

- (i) Starvation: the process sits in the Ready state and is repeatedly passed over by the scheduler, runnable but never dispatched.
- (ii) Livelock: the process is actively Running (not blocked) but keeps executing without making progress, e.g. two processes repeatedly backing off and retrying so neither proceeds.
