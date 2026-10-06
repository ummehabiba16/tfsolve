---
marks: 10
topics: [mutex-requirements]
kind: analysis
source: {page: 55}
note: "The text names the shared variable 'truth' (initially 0), but the figure code uses 'turn'. Printed as is."
---
Any facility or capability that is to provide support for mutual exclusion should meet the following requirements:

(i) No two processes simultaneously in critical region

(ii) No assumptions made about speeds or numbers of CPUs

(iii) No process running outside its critical region may block another process

(iv) No process must wait forever to enter its critical region

A software solution to the mutual exclusion problem for two processes (Process 0 and Process 1) is proposed in Figure for Q. No. 4(c). Here the program fragments are written in C. The integer variable **truth**, initially 0, is shared by Process 0 and Process 1.

**Process 0**

```c
while (TRUE) {
    while (turn != 0);
    critical_region( );
    turn = 0;
    noncritical_region( );
}
```

**Process 1**

```c
while (TRUE) {
    while (turn != 1);
    critical_region( );
    turn = 1;
    noncritical_region( );
}
```

*Figure for Q. No. 4(c)*

Mention the conditions violated by this solution with proper explanation.
