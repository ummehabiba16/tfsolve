---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Incremental formulation, any square: 64 x 63 x ... x 57 = 1.8 x 10^14 sequences (C(64,8) = 4.4 x 10^9 distinct boards). One queen per column, leftmost first and never attacked: 2,057 states for n = 8. Complete-state, one queen per column: n^n = 8^8 = 16,777,216. In general: n^2!/(n^2 - n)!, sum_k (number of safe k-queen placements), and n^n."
sources: ["AIMA 3e sec. 3.2.1 (8-queens problem), sec. 4.1"]
---
The size of the state space depends on the formulation.

**1. Naive incremental formulation.** States: any arrangement of $0..n$ queens on the board. Action: add a queen to any empty square. The number of action sequences (paths) of length $n$ is

$$n^2\,(n^2-1)\cdots(n^2-n+1)=\frac{(n^2)!}{(n^2-n)!}.$$

For $n=8$: $64\times63\times\dots\times57\approx1.8\times10^{14}$ sequences to explore. (The number of distinct boards with 8 queens is $\binom{64}{8}\approx4.4\times10^9$.)

**2. Improved incremental formulation.** States: $k$ queens ($0\le k\le n$), one per column in the leftmost $k$ columns, with no two attacking. Action: add a queen to the leftmost empty column, on a square not attacked. The state space is the number of partial safe placements:

$$|S|=\sum_{k=0}^{n}\#\{\text{non-attacking placements in the first }k\text{ columns}\}.$$

For $n=8$: $1+8+42+140+344+568+550+312+92=\mathbf{2{,}057}$ states (computed by enumeration). It has 92 goal states.

**3. Complete-state formulation** (for local search). Every state has $n$ queens, one per column, in any rows:

$$|S|=n^n,$$

so $8^8=16{,}777{,}216$ states for $n=8$. (Each state has $n(n-1)=56$ successors, moving one queen within its column.)
