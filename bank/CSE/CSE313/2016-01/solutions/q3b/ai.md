---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "t=22: P1,P2,P4 blocked, P3 ready, P5 running; t=37: P1,P2 ready, P3,P4 blocked, P5 running; t=47: P5 exited, P4 blocked, P3 ready, P1/P2 ready or running (one of them runs)."
sources: ["Tanenbaum MOS 4e, sec. 2.1.5; Stallings, five-state model"]
---
Events (from time 5): P1 reads the disk (5); P3's time slice expires (15); P4 writes (18); P2 reads (20); P5 sleeps for 7 units (23); P3 writes (24); P5 wakes (30); disk 2: P2's read done (33); disk 3: P1's read done (36); P5 terminates (38); P3's write done (40); P4's write done (48).

A process that executes an I/O command or sleeps must have been **Running** at that moment and becomes **Blocked**; a time-out moves Running $\to$ Ready; I/O completion or the end of the sleep moves Blocked $\to$ Ready; and the CPU is never idle while a process is Ready (so exactly one process is Running if any is runnable).

**(i) At time 22**

| P1 | P2 | P3 | P4 | P5 |
|:-:|:-:|:-:|:-:|:-:|
| **Blocked** (waiting for its read since 5) | **Blocked** (read since 20) | **Ready** (preempted at 15, not yet dispatched again) | **Blocked** (write since 18) | **Running** (it goes to sleep at 23) |

**(ii) At time 37**

| P1 | P2 | P3 | P4 | P5 |
|:-:|:-:|:-:|:-:|:-:|
| **Ready** (read finished at 36) | **Ready** (read finished at 33) | **Blocked** (write 24-40) | **Blocked** (write until 48) | **Running** (terminates at 38) |

**(iii) At time 47**

| P1 | P2 | P3 | P4 | P5 |
|:-:|:-:|:-:|:-:|:-:|
| Ready or Running | Ready or Running | Ready or Running (write done at 40) | **Blocked** (completes at 48) | **Exit** |

Exactly one of P1, P2, P3 is **Running** and the other two are **Ready**; the information given does not say which one (with round robin and the usual FIFO ready queue, P2 would have been dispatched first at 38, then P1, then P3), so the process that is running at 47 cannot be determined uniquely from the data.

*Assumption:* the time-slice length is not given, so no time-outs other than the listed one are assumed.
