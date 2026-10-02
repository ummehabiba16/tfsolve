---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '(i) Move pairs as units: $A_n=2A_{n-1}+2$, $A_1=2$, so $A_n=2^{n+1}-2$. (ii) Moving a pair as a unit reverses it; using two unit-moves of the top $n-1$ pairs and of the largest pair, then an order-preserving move: $B_n=2A_{n-1}+4+B_{n-1}=2^{n+1}+B_{n-1}$, $B_1=3$, so $B_n=2^{n+2}-5$.'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1 (Tower of Hanoi; exercise on the double tower)']
---
Number the pairs $1,\dots,n$ from the smallest (top) to the largest (bottom).

**(i) Equal disks indistinguishable.** Treat each pair as a unit that needs 2 moves to transfer (one disk at a time, the two disks of a pair may be stacked either way). The usual argument applies: before the two largest disks can leave the source, all smaller pairs must be on the third peg, and afterwards they must be moved on top of the largest pair. So

$$A_1=2,\qquad A_n=2A_{n-1}+2\quad(n\ge2)$$

Adding 2: $A_n+2=2(A_{n-1}+2)$, so

$$A_n=2^{n+1}-2=2T_n$$

i.e. twice the moves of the ordinary tower ($A_1=2$, $A_2=6$, $A_3=14$).

**(ii) Original order must be reproduced.** When a pair is moved as a unit (top disk first, then the other), the two disks end up in the opposite order. In the $A_n$ solution, pair $k$ is moved $2^{n-k}$ times: an even number for $k<n$ (order restored) but only once for the largest pair (reversed). So the $A_n$ method fixes everything except the bottom pair. To fix it:

1. move the top $n-1$ pairs from A to C: $A_{n-1}$ moves;
2. move the two largest disks from A to B: 2 moves (they are now reversed);
3. move the $n-1$ pairs from C back to A: $A_{n-1}$ moves (each of these pairs has now been moved twice in total, so all are in their original order);
4. move the two largest disks from B to C: 2 moves (reversed again, i.e. original order);
5. move the $n-1$ pairs from A to C keeping their order: $B_{n-1}$ moves.

For one pair, $B_1=3$: top disk to B, bottom disk to C, top disk to C. Hence

$$B_1=3,\qquad B_n=2A_{n-1}+4+B_{n-1}=2^{n+1}+B_{n-1}\quad(n\ge2)$$

$$B_n=2^{n+1}+2^n+\cdots+2^3+3=\left(2^{n+2}-8\right)+3=2^{n+2}-5$$

So $B_1=3$, $B_2=11$, $B_3=27$, $B_4=59$. (A breadth-first search over all arrangements of the $2n$ distinguishable disks confirms that $A_n$ and $B_n$ are the minimum numbers of moves for $n\le4$.)
