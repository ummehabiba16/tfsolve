---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Disks moved $2^t$ times: $\binom{t+4}{4}$ for $t<K_{max}$; $\binom{10}{5}=252\le347<462$ gives $K_{max}=6$, $N_a(K_{max})=95$; total $M(347,7)=11583$ moves; root split (347,7) $\to$ 2 x (137,7) + (210,6) (any $k\in[137,221]$ is optimal).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 1 (Tower of Hanoi)', 'Frame-Stewart algorithm for the multi-peg Tower of Hanoi (presumed optimal solution)']
---
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

**Here $n=347$, $p=7$.** Since $\binom{10}{5}=252\le347<\binom{11}{5}=462$:

$$K_{max}=6,\qquad N_a(K_{max})=347-252=95$$

and $0\le95<\binom{10}{4}=210$ as required.

| $t$ (doublings) | disks moved $2^t$ times | $2^t$ | moves |
|:-:|:-:|:-:|:-:|
| 0 | $\binom{4}{4}=1$ | 1 | 1 |
| 1 | $\binom{5}{4}=5$ | 2 | 10 |
| 2 | $\binom{6}{4}=15$ | 4 | 60 |
| 3 | $\binom{7}{4}=35$ | 8 | 280 |
| 4 | $\binom{8}{4}=70$ | 16 | 1120 |
| 5 | $\binom{9}{4}=126$ | 32 | 4032 |
| 6 ($=K_{max}$) | $N_a(K_{max})=95$ | 64 | 6080 |
| total | 347 | | **11583** |

**Splitting the root.** Of the $N_a(K_{max})$ disks at the top level, let $x$ go to the right subtree ($p-1$ pegs) and $N_a(K_{max})-x$ to the left subtree. The capacities give the inequalities

$$0\le x\le\binom{K_{max}+p-4}{p-4}=84,\qquad0\le N_a(K_{max})-x\le\binom{K_{max}+p-4}{p-3}=126$$

and then $k=\binom{K_{max}+p-4}{p-2}+N_a(K_{max})-x=126+95-x$. So every $k$ with $137\le k\le221$ is optimal (a full search of $\min_k[2M(k,7)+M(347-k,6)]$ confirms exactly this range). Taking $k=137$:

```text
Level 0:  (347, 7)   [11583 moves]
Level 1:  left  2 x (137, 7)   [2 x 1823 moves]
          right (210, 6)   [7937 moves]
Level 2:  under (137, 7):  left 2 x (56, 7) [2 x 351],  right (81, 6) [1121]
          under (210, 6):  left 2 x (126, 6) [2 x 2561],  right (84, 5) [2815]
```

The same rule is applied inside every node until the leaves are 3-peg towers ($2^m-1$ moves) or single disks. Check at the root: $2\times1823+7937=11583$.

**Answer.** $K_{max}=6$, $N_a(K_{max})=95$, and the presumed optimal solution uses $\mathbf{11583}$ moves.

(The class notation for the tree may differ; the quantities above are defined explicitly so that they can be matched.)
