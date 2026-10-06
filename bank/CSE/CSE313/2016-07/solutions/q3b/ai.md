---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Three copies of x: parent 20, first child 20, grandchild 30."
sources: ["OSTEP ch. 5 (fork); Tanenbaum MOS 4e, sec. 2.1.2"]
---
Trace of the program (`x` is initialised **after** the first `fork()`, so each process has its own `x`):

```c
int child = fork();      // creates process C; in P: child = pid of C (non-zero), in C: child = 0
int x = 10;
if (child) {             // P (parent)
    x += 10;             //   x = 20
} else {                 // C
    child = fork();      //   creates process G; in C child != 0, in G child == 0
    x += 10;             //   x = 20 in C, and in G (copied x = 10, +10 = 20)
    if (child == 0) {    //   only in G
        x += 10;         //   x = 30
    }
}
return 0;
```

| Process | Created by | `child` after forks | Final `x` |
|:-:|:-:|:-:|:-:|
| P (original) | | pid of C | $10+10=\mathbf{20}$ |
| C | first `fork` | pid of G | $10+10=\mathbf{20}$ |
| G | second `fork` (in C) | 0 | $10+10+10=\mathbf{30}$ |

**There are 3 different copies of `x`** (one in each of the 3 processes), with the final values **20, 20 and 30**.
