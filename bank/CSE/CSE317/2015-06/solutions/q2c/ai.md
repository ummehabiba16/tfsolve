---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "State (a, b, c) = gallons in the 12-, 8- and 3-gallon jugs, 0 <= a <= 12, 0 <= b <= 8, 0 <= c <= 3; initial (0, 0, 0); goal test: some jug holds exactly 1 gallon; successors: Fill(jug) from the faucet, Empty(jug) onto the ground, Pour(x, y) until x is empty or y is full; cost 1 per action."
sources: ["AIMA 3e sec. 3.1.1 (problem formulation), Exercise 3.9 (water jugs)"]
---
**State representation.** $(a,b,c)$ = the number of gallons in the 12-, 8- and 3-gallon jugs, with $0\le a\le12$, $0\le b\le8$, $0\le c\le3$ (integers). There are at most $13\times9\times4=468$ states.

**Initial state.** $(0,0,0)$: all jugs empty.

**Goal test.** Some jug contains exactly one gallon: $a=1\lor b=1\lor c=1$.

**Successor function (actions).** For jugs $x$ and $y$ with capacities $C_x$ and $C_y$:

| Action | Precondition | Result |
|:--|:--|:--|
| $Fill(x)$ | $x<C_x$ | $x\leftarrow C_x$ (from the faucet) |
| $Empty(x)$ | $x>0$ | $x\leftarrow0$ (onto the ground) |
| $Pour(x,y)$ | $x>0$, $y<C_y$ | $t=\min(x,\ C_y-y)$; $x\leftarrow x-t$, $y\leftarrow y+t$ |

For example, $Pour(12\to8)$ from $(12,0,0)$ gives $(4,8,0)$. There are 3 fill, 3 empty and 6 pour actions.

**Cost function.** 1 per action, so the path cost is the number of operations. (Alternatively, count the gallons of water used.)
