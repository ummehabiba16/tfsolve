---
author: ai
via: chat
status: unverified
summary: Deadlock. The graph contains the cycle C$\to$5$\to$D$\to$6$\to$A$\to$1$\to$B$\to$4$\to$C, so A, B, C, D are deadlocked.
sources: [Deadlocks slides 16-19, 'Tanenbaum, MOS 4e, sec. 6.4.1', Notes on algorithm simulation]
imported_from: tfsolve-questions/data/solutions/2022-23.json
---
Edges, assignment (resource$\to$holder): $6\to A,\ 1\to B,\ 4\to C,\ 5\to D$. Request (process$\to$resource): $A\to 1,\ A\to 3,\ B\to 4,\ C\to 3,\ C\to 5,\ D\to 6$. (Resources 2 and 3 are held by no one.)

Detection from C (depth-first, tracking the visited list $L$):

1. $L=\{C\}$. C requests 5, held by D $\Rightarrow$ visit D. $L=\{C,D\}$.
2. D requests 6, held by A $\Rightarrow$ visit A. $L=\{C,D,A\}$.
3. A requests 1, held by B $\Rightarrow$ visit B. $L=\{C,D,A,B\}$.
4. B requests 4, held by C, which is already in $L$ $\Rightarrow$ cycle found.

Cycle C$\to$D$\to$A$\to$B$\to$C $\Rightarrow$ deadlock; the deadlocked set is $\{A,B,C,D\}$. (The branch C$\to$3 is a dead end, since 3 is free.)
