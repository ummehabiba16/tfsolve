---
author: ai
via: chat
status: unverified
imported_from: cse313_mem_fs_solved.tex
changes:
  - "2026-09-30 (import review): explained the * notation for the clock hand."
---
Reference string: $1,2,3,4,1,2,5,1,2,3,4,5$ (12 references), 3 frames, all initially empty. Using the Clock (second-chance) algorithm (use bit $R$ set on load/access, cleared as the hand sweeps past). Notation as in the hint of 2021-22 Q5(a): `*` marks the frame the hand stopped at (the one just filled); the next search starts at the frame after it, and a hit does not move the hand.

| Ref \# | Page | Frames after (page(R), \* = hand) | Fault? |
|:--:|:--:|:---|:--:|
| 1 | 1 | 1(1)\*, --, -- | Fault (cold) |
| 2 | 2 | 1(1), 2(1)\*, -- | Fault (cold) |
| 3 | 3 | 1(1), 2(1), 3(1)\* | Fault (cold, now full) |
| 4 | 4 | sweep clears 1,2,3 $\to$ evict 1: 4(1)\*,2(0),3(0) | Fault |
| 5 | 1 | evict 2 (R=0): 4(1),1(1)\*,3(0) | Fault |
| 6 | 2 | evict 3 (R=0): 4(1),1(1),2(1)\* | Fault |
| 7 | 5 | sweep clears 4,1,2 $\to$ evict 4: 5(1)\*,1(0),2(0) | Fault |
| 8 | 1 | hit, set R=1: 5(1),1(1),2(0) | Hit |
| 9 | 2 | hit, set R=1: 5(1),1(1),2(1) | Hit |
| 10 | 3 | sweep clears 1,2,5 $\to$ evict 1: 5(0),3(1)\*,2(0) | Fault |
| 11 | 4 | evict 2 (R=0): 5(0),3(1),4(1)\* | Fault |
| 12 | 5 | hit, set R=1: 5(1),3(1),4(1) | Hit |

**Total page faults $=9$** (refs 1,2,3,4,5,6,7,10,11); **hits $=3$** (refs 8,9,12).
