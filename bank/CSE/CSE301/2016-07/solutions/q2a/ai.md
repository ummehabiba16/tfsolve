---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Disks moved $2^t$ times: $\binom{t+5}{5}$ for $t<K_{max}$; $\binom{10}{6}=210\le378<462$ gives $K_{max}=5$, $N_a(K_{max})=168$; total $M(378,8)=7937$ moves; root split (378,8) $\to$ 2 x (126,8) + (252,7) (any $k\in[126,210]$ is optimal).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1 (Tower of Hanoi)', 'Frame-Stewart algorithm for the multi-peg Tower of Hanoi (presumed optimal solution)']
---
**Properties of the presumed optimal solution** (used below):

- it is recursive: the top $k$ disks are moved twice with all $p$ pegs, the bottom $n-k$ once with $p-1$ pegs;
- a disk is moved $2^t$ times, where $t$ is the number of left edges above it in the binary tree;
- with $p$ pegs at most $\binom{t+p-3}{p-3}$ disks are moved $2^t$ times, and the optimum uses these cheap "slots" first, so the number of moves is $\sum_t2^t\times(\text{disks at level }t)$;
- the optimal split $k$ is not unique in general; it lies in an interval determined by the capacities below.

**Presumed optimal (Frame-Stewart) solution.** To move $n$ disks with $p$ pegs:

1. move the top $k$ disks to an intermediate peg, using all $p$ pegs;
2. move the remaining $n-k$ disks to the destination, using only $p-1$ pegs (the peg holding the $k$ disks cannot be used);
3. move the $k$ disks onto the destination, using all $p$ pegs again.

$$M(n,p)=\min_{1\le k<n}\big[2M(k,p)+M(n-k,p-1)\big],\qquad M(n,3)=2^n-1,\quad M(1,p)=1$$

**Binary tree.** Each node $(m,q)$ ($m$ disks, $q$ pegs) has a left child $(k,q)$, which is executed twice, and a right child $(m-k,q-1)$. Following a disk from the root to its leaf, every left edge doubles the number of times it is moved, so a disk at "left-depth" $t$ is moved $2^t$ times. With $p$ pegs at most $\binom{t+p-3}{p-3}$ disks can be moved only $2^t$ times, and the presumed optimal solution fills these levels from $t=0$ upwards. Hence:

- $K_{max}$ is the largest number of doublings, defined by

$$\binom{K_{max}+p-3}{p-2}\le n<\binom{K_{max}+p-2}{p-2}$$

- exactly $\binom{t+p-3}{p-3}$ disks are moved $2^t$ times for $t=0,1,\dots,K_{max}-1$;
- the remaining $N_a(K_{max})=n-\binom{K_{max}+p-3}{p-2}$ disks, with $0\le N_a(K_{max})<\binom{K_{max}+p-3}{p-3}$, are moved $2^{K_{max}}$ times;

$$M(n,p)=\sum_{t=0}^{K_{max}-1}2^t\binom{t+p-3}{p-3}+2^{K_{max}}N_a(K_{max})$$

**Here $n=378$, $p=8$.** Since $\binom{10}{6}=210\le378<\binom{11}{6}=462$:

$$K_{max}=5,\qquad N_a(K_{max})=378-210=168$$

and $0\le168<\binom{10}{5}=252$ as required.

| $t$ (doublings) | disks moved $2^t$ times | $2^t$ | moves |
|:-:|:-:|:-:|:-:|
| 0 | $\binom{5}{5}=1$ | 1 | 1 |
| 1 | $\binom{6}{5}=6$ | 2 | 12 |
| 2 | $\binom{7}{5}=21$ | 4 | 84 |
| 3 | $\binom{8}{5}=56$ | 8 | 448 |
| 4 | $\binom{9}{5}=126$ | 16 | 2016 |
| 5 ($=K_{max}$) | $N_a(K_{max})=168$ | 32 | 5376 |
| total | 378 | | **7937** |

**Splitting the root.** Of the $N_a(K_{max})$ disks at the top level, let $x$ go to the right subtree ($p-1$ pegs) and $N_a(K_{max})-x$ to the left subtree. The capacities give the inequalities

$$0\le x\le\binom{K_{max}+p-4}{p-4}=126,\qquad0\le N_a(K_{max})-x\le\binom{K_{max}+p-4}{p-3}=126$$

and then $k=\binom{K_{max}+p-4}{p-2}+N_a(K_{max})-x=84+168-x$. So every $k$ with $126\le k\le210$ is optimal (a full search of $\min_k[2M(k,8)+M(378-k,7)]$ confirms exactly this range). Taking $k=126$:

```text
Level 0:  (378, 8)   [7937 moves]
Level 1:  left  2 x (126, 8)   [2 x 1217 moves]
          right (252, 7)   [5503 moves]
Level 2:  under (126, 8):  left 2 x (28, 8) [2 x 97],  right (98, 7) [1023]
          under (252, 7):  left 2 x (126, 7) [2 x 1471],  right (126, 6) [2561]
```

The same rule is applied inside every node until the leaves are 3-peg towers ($2^m-1$ moves) or single disks. Check at the root: $2\times1217+5503=7937$.

**Answer.** $K_{max}=5$, $N_a(K_{max})=168$, and the presumed optimal solution uses $\mathbf{7937}$ moves.

(The tree above is the requested binary tree of level 2. The class notation may differ; the quantities are defined explicitly so that they can be matched.)
