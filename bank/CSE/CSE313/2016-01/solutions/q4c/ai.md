---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The solution violates condition (iii) (a process outside its critical region blocks the other) and (iv) (the other process can wait forever): turn never changes in favour of the other process."
sources: ["Tanenbaum MOS 4e, sec. 2.3.3 (mutual exclusion with busy waiting)"]
---
(The question calls the shared variable `truth` but the code uses `turn`; they are taken to be the same, initially 0.)

```c
/* Process 0 */                       /* Process 1 */
while (TRUE) {                        while (TRUE) {
    while (turn != 0);                    while (turn != 1);
    critical_region();                    critical_region();
    turn = 0;                             turn = 1;
    noncritical_region();                 noncritical_region();
}                                     }
```

**Behaviour.** Process 0 enters when `turn == 0` and afterwards sets `turn = 0` again (it should have given the turn to the other process, `turn = 1`); Process 1 enters only when `turn == 1`, a value that **only Process 1 itself ever writes**, and it can never get there because it cannot leave its busy-wait loop. Starting with `turn = 0`, Process 0 may enter its critical region **again and again**, while Process 1 **loops forever** in `while (turn != 1);`.

**Requirements checked**

| Requirement | Satisfied? | Explanation |
|:--|:-:|:--|
| (i) no two processes simultaneously in the critical region | yes | only one process ever gets in |
| (ii) no assumptions about speeds or number of CPUs | yes | the code makes none |
| (iii) **no process running outside its critical region may block another process** | **no, violated** | Process 0, while in its *noncritical* region (or anywhere outside the critical region), keeps `turn = 0`, which blocks Process 1 |
| (iv) **no process must wait forever to enter its critical region** | **no, violated** | Process 1 waits forever (starvation): `turn` is never set to 1 by Process 0 |

(If `turn` were initially 1, the roles would be exchanged.) Even the intended strict alternation (`turn = 1` in Process 0 and `turn = 0` in Process 1) would still violate (iii): a slow process in its noncritical region blocks the other.
