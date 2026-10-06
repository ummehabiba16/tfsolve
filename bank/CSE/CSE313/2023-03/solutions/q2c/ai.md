---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "3 processes in total (2 new); outputs: 3 2 2 4, 2 3 2 4, 2 2 3 4, 2 2 4 3."
sources: ["OSTEP ch. 5 (fork/wait)", "Tanenbaum MOS 4e, sec. 2.1"]
---
Name the processes: $P$ (original), $C$ (child of the first `fork`) and $G$ (child of the second `fork`, made by $C$).

**Trace.**

- $P$: the first `fork` returns a non-zero value, so $P$ does `count = 1+2 = 3` and prints **3**. Then `count != 1` (skip), `pid2 == 0` (skip), and it ends.
- $C$: the first `fork` returned $0$, so the first `if` is skipped; `count == 1`, so `count = 2`, `pid2 = fork()` (this creates $G$); $C$ prints **2**. Since `pid2` is non-zero, $C$ waits for $G$, then `count = 2 * 2 = 4` and prints **4**.
- $G$: `pid2 == 0`, `count == 2`; it prints **2**, skips the last `if`, and ends.

**i. Processes created.** $C$ and $G$: **2 new processes** (3 processes including the original $P$).

**ii. Possible outputs.** $P$'s "3" can come at any time relative to the rest. $C$'s and $G$'s "2" print before $C$'s "4", because $C$ waits for $G$ to terminate and only then prints. So "4" is after both "2"s and "3" can be in any of four positions:

| Output |
|:--|
| `3 2 2 4` |
| `2 3 2 4` |
| `2 2 3 4` |
| `2 2 4 3` |

(The two 2s are indistinguishable in the output.)
