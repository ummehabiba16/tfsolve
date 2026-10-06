---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The code violates mutual exclusion: P0 passes while turn != 0 check with blocked[1] false, P1 does the same and enters, then P0 sets turn = 0 and also enters (Hyman's incorrect algorithm)."
sources: ["Tanenbaum MOS 4e, sec. 2.3.3 (mutual exclusion: Dekker, Peterson); Hyman 1966"]
---
(The code uses `id` inside the procedures where the parameter is called `process_id`; they are taken to be the same, and `blocked[]` is initially false, `turn` initially 0 or 1.)

```c
enter_critical_section(process_id) {
    blocked[process_id] = true;
    while (turn != process_id) {
        while (blocked[1 - process_id]) ;     /* wait while the other is blocked */
        turn = process_id;
    }
}
leave_critical_section(process_id) { blocked[process_id] = false; }
```

**The code does NOT solve the problem: it violates mutual exclusion.** Counter-example (initially `turn = 1`, i.e. it is not Process 0's turn):

| Step | Process 0 (id 0) | Process 1 (id 1) |
|:-:|:--|:--|
| 1 | `blocked[0] = true` | |
| 2 | tests `turn != 0`: true, enters the loop; tests `blocked[1]`: **false**, leaves the inner loop; **(preempted before `turn = 0`)** | |
| 3 | | `blocked[1] = true` |
| 4 | | tests `turn != 1`: **false** (turn is 1), so it **enters the critical section** |
| 5 | resumes: `turn = 0`; the loop test `turn != 0` is now false, so it **also enters the critical section** | still in the critical section |

Both processes are in the critical region at the same time, so **mutual exclusion is violated**. (This is a known incorrect solution published in 1966; Dekker's and Peterson's algorithms fix it by testing/setting the turn variable in a safe order.)
