---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'The forbidden cells are three disjoint $2\times2$ blocks, so $R(x)=(1+4x+2x^2)^3=1+12x+54x^2+112x^3+108x^4+48x^5+8x^6$, and the count is $\sum_k(-1)^kr_k(6-k)!=720-1440+1296-672+216-48+8=80$.'
sources: ['Brualdi, Introductory Combinatorics, Ch. 6 (permutations with forbidden positions, rook polynomials)']
---
Rows are positions and columns are values: a placement of six non-attacking rooks is a permutation of $\{1,\dots,6\}$, and we must avoid the marked cells. The forbidden cells form three $2\times2$ blocks, $\{1,2\}\times\{1,2\}$, $\{3,4\}\times\{3,4\}$ and $\{5,6\}\times\{5,6\}$, which share no row or column.

**Rook polynomial of the forbidden board.** For one $2\times2$ block there is 1 way to place no rook, 4 ways to place one rook and 2 ways to place two non-attacking rooks, so its rook polynomial is $1+4x+2x^2$. For disjoint boards (no common rows or columns) rook polynomials multiply:

$$R(x)=(1+4x+2x^2)^3=1+12x+54x^2+112x^3+108x^4+48x^5+8x^6$$

so $r_0,\dots,r_6=1,12,54,112,108,48,8$ (check: $R(1)=7^3=343$).

**Inclusion-exclusion.** The number of permutations avoiding all forbidden cells is

$$\sum_{k=0}^{6}(-1)^kr_k(6-k)!=6!-12\cdot5!+54\cdot4!-112\cdot3!+108\cdot2!-48\cdot1!+8\cdot0!$$

$$=720-1440+1296-672+216-48+8=\mathbf{80}$$

(A computer enumeration of all $720$ permutations confirms 80.)
