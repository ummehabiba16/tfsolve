---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$X_0=0$; to move $n$ disks from A to C without A$\leftrightarrow$C moves: $n-1$ disks A$\to$C, disk $n$ A$\to$B, $n-1$ disks C$\to$A, disk $n$ B$\to$C, $n-1$ disks A$\to$C, so $X_n=3X_{n-1}+2$ ($n\ge1$), giving $X_n=3^n-1$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1 (Tower of Hanoi; exercise on the restricted Tower of Hanoi)']
---
Call the pegs A (leftmost, source), B (middle) and C (rightmost, destination). Every move must be to or from B. Let $X_n$ be the minimum number of moves needed to transfer a tower of $n$ disks from A to C (by symmetry, also from C to A).

**Forming the recursion.** Consider the largest disk $n$. It cannot jump from A to C, so it must go A $\to$ B and later B $\to$ C.

- When disk $n$ moves A $\to$ B, every smaller disk must be on C (they cannot be on A, above disk $n$, or on B, where disk $n$ is going). Getting the $n-1$ smaller disks from A to C takes $X_{n-1}$ moves.
- When disk $n$ moves B $\to$ C, all smaller disks must be on A. Getting them from C to A takes $X_{n-1}$ moves.
- Finally the $n-1$ smaller disks must go from A to C on top of disk $n$: $X_{n-1}$ moves.

So the moves are: $X_{n-1}$ (A$\to$C), 1 (disk $n$ A$\to$B), $X_{n-1}$ (C$\to$A), 1 (disk $n$ B$\to$C), $X_{n-1}$ (A$\to$C).

**Recurrence with base case.**

$$X_0=0,\qquad X_n=3X_{n-1}+2\quad(n\ge1)$$

(equivalently $X_1=2$: one disk goes A$\to$B$\to$C.)

**Closed form** (not required): adding 1, $X_n+1=3(X_{n-1}+1)$, so $X_n=3^n-1$; e.g. $X_1=2$, $X_2=8$, $X_3=26$. (A breadth-first search over all states for $n\le5$ confirms these minimum values.) In fact this solution passes through all $3^n$ arrangements of the disks.
