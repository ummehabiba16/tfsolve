---
marks: 12
topics: [peterson-priority-inversion]
kind: analysis
source: {page: 2}
---
Peterson's solution for achieving mutual exclusion for using critical regions is presented in Figure for Question 4(a).

(i) Discuss priority inversion problem with a high-priority process, H, and a low-priority process, L.

(ii) Does the same problem occur if round-robin scheduling is used instead of priority scheduling? Justify.

*Figure for Question 4(a): Peterson's solution for 2 processes*

```c
#define FALSE 0
#define TRUE  1
#define N     2                       /* number of processes */

int turn;                             /* whose turn is it? */
int interested[N];                    /* all values initially 0 (FALSE) */

void enter_region(int process)        /* process is 0 or 1 */
{
    int other;                        /* number of the other process */

    other = 1 - process;              /* the opposite of process */
    interested[process] = TRUE;       /* show that you are interested */
    turn = process;                   /* set flag */
    while (turn == process && interested[other] == TRUE) /* null statement */;
}

void leave_region(int process)        /* process: who is leaving */
{
    interested[process] = FALSE;      /* indicate departure from critical region */
}
```
