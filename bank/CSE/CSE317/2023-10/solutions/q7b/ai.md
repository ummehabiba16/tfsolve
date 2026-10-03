---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Value iteration with V_{k+1}(s) = max(exit reward, gamma max over moves V_k(s')) converges after 6 iterations: U(A) = 25, U(B) = 3.125. The policy heads for the +100 exit, even from the +1 exit cell (moving Down gives 25 > 1)."
sources: ["MNM slides MDP-1-SB (value iteration)", "AIMA 4e sec. 17.2.1", "UC Berkeley CS188 grid-world exit convention"]
---
**Set-up.** Label cells (row, column), with row 1 at the top. $B=(1,1)$; the wall is $(2,2)$; $A=(3,2)$. EXIT is available at $(1,4)$ with $r=+1$ and at $(3,4)$ with $r=+100$, and leads to the terminal state $T$ with $U(T)=0$. Moves are deterministic, give reward 0, and a move into the wall or off the grid leaves the agent in place. $\gamma=\frac12$.

**Value-iteration update** (rewards on actions, $R(s,a,s')$ form):

$$V_{k+1}(s)=\max\Big\{\ r_{\text{exit}}(s)\ \text{(if EXIT is available)},\ \ \max_{\text{move}}\ \gamma\,V_k(s')\ \Big\}.$$

**Utilities after each iteration** (## = wall):

| $k$ | Row 1 | Row 2 | Row 3 |
|:-:|:--|:--|:--|
| 0 | 0, 0, 0, 0 | 0, ##, 0, 0 | 0, 0, 0, 0 |
| 1 | 0, 0, 0, **1** | 0, ##, 0, 0 | 0, 0, 0, **100** |
| 2 | 0, 0, 0.5, 1 | 0, ##, 0, 50 | 0, 0, 50, 100 |
| 3 | 0, 0.25, 0.5, 25 | 0, ##, 25, 50 | 0, 25, 50, 100 |
| 4 | 0.125, 0.25, 12.5, 25 | 0, ##, 25, 50 | 12.5, 25, 50, 100 |
| 5 | 0.125, 6.25, 12.5, 25 | 6.25, ##, 25, 50 | 12.5, 25, 50, 100 |
| 6 | **3.125**, 6.25, 12.5, 25 | 6.25, ##, 25, 50 | 12.5, **25**, 50, 100 |
| 7 | (no change) | | |

Some of the steps:

- Iteration 1: only the EXIT actions give non-zero values, $V_1(1,4)=1$ and $V_1(3,4)=100$.
- Iteration 3: at the $+1$ cell, moving Down gives $\frac12V_2(2,4)=\frac12(50)=25>1$, so $V_3(1,4)=25$. Exiting is no longer best there.
- $A=(3,2)$: its best neighbour is $(3,3)$, so $V(A)=\frac12\times50=25$, reached at iteration 3.
- $B=(1,1)$: its neighbours $(1,2)$ and $(2,1)$ both reach 6.25, so $V(B)=\frac12\times6.25=3.125$, reached at iteration 6.

**Optimal utilities:** $\mathbf{U(A)=25}$, $\mathbf{U(B)=3.125}$.

**Optimal policy** (every state heads for the $+100$ exit):

| Row | Col 1 | Col 2 | Col 3 | Col 4 |
|:-:|:-:|:-:|:-:|:-:|
| 1 | $\rightarrow$ or $\downarrow$ | $\rightarrow$ | $\rightarrow$ or $\downarrow$ | $\downarrow$ (not EXIT) |
| 2 | $\downarrow$ | wall | $\rightarrow$ or $\downarrow$ | $\downarrow$ |
| 3 | $\rightarrow$ | $\rightarrow$ (A) | $\rightarrow$ | EXIT (+100) |

("or" marks ties.)

*Note:* this assumes, as stated, that the exit reward is received when the EXIT action is taken, and that all other moves earn 0.
