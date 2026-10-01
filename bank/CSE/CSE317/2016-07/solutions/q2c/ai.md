---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "BFS: complete (finite b), optimal for unit costs, O(b^d) time and space. DFS: incomplete, not optimal, O(b^m) time, O(bm) space. UCS: complete and optimal (cost >= e), O(b^(1+C*/e)) time and space. IDS: complete, optimal for unit costs, O(b^d) time, O(bd) space. For b = 10, d = 5: BFS generates 111,110 nodes, IDS 123,450."
sources: ["AIMA 3e sec. 3.4 (Figure 3.21)"]
---
Let $b$ = branching factor, $d$ = depth of the shallowest goal, $m$ = maximum depth, $C^*$ = optimal cost, $\epsilon$ = minimum step cost.

| | BFS | DFS | UCS | IDS |
|:--|:-:|:-:|:-:|:-:|
| Complete | yes (finite $b$) | no | yes (step cost $\ge\epsilon$) | yes (finite $b$) |
| Time | $O(b^d)$ | $O(b^m)$ | $O(b^{1+\lfloor C^*/\epsilon\rfloor})$ | $O(b^d)$ |
| Space | $O(b^d)$ | $O(bm)$ | $O(b^{1+\lfloor C^*/\epsilon\rfloor})$ | $O(bd)$ |
| Optimal | yes, if step costs equal | no | yes | yes, if step costs equal |

**Calculations.**

*BFS* generates every node down to depth $d$:

$$N_{BFS}=b+b^2+\dots+b^d=O(b^d)$$

and all of them may be in memory (the frontier alone holds $O(b^d)$). With $b=10,d=5$: $10+100+1000+10^4+10^5=111{,}110$ nodes.

*DFS* stores only the current path and the siblings of nodes on it: at most $b$ nodes per level, so $bm$ nodes: $O(bm)$. In the worst case it visits the whole tree to depth $m$: $O(b^m)$, with $m$ possibly much larger than $d$ (or infinite: incomplete).

*UCS* expands nodes in order of path cost. Every node with $g<C^*$ is expanded; each step costs at least $\epsilon$, so such nodes have depth at most $\lfloor C^*/\epsilon\rfloor$, and generating their children gives

$$O(b^{1+\lfloor C^*/\epsilon\rfloor})$$

time and space; with all costs equal this is $O(b^{d+1})$.

*IDS* runs depth-limited search with limits $0..d$. Nodes at depth $i$ are generated $d-i+1$ times:

$$N_{IDS}=d\,b+(d-1)b^2+\dots+1\cdot b^d=O(b^d)$$

With $b=10,d=5$: $50+400+3000+20{,}000+100{,}000=123{,}450$, only about 11% more than BFS, while memory is $O(bd)$ (about 50 nodes) instead of $O(b^d)$.

So IDS combines BFS's completeness and optimality with DFS's linear memory and is the preferred uninformed method for large spaces with unknown solution depth; UCS is the one to use when step costs differ.
