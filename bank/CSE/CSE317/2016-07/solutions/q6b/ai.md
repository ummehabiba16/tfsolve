---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Forward checking: after assigning X, delete from each unassigned neighbour's domain the values inconsistent with X; backtrack as soon as some domain becomes empty. Example: Australia map colouring, WA = red, Q = green, V = blue empties SA's domain immediately. It helps backtracking by detecting failures earlier, pruning the tree, and supplying up-to-date domain sizes for MRV."
sources: ["AIMA 3e sec. 6.3.2 (Interleaving search and inference)"]
---
**Forward checking (FC).** During backtracking search, whenever a variable $X$ is assigned, for every unassigned variable $Y$ connected to $X$ by a constraint, remove from $D_Y$ every value that is inconsistent with the value chosen for $X$. If any domain becomes empty, the current assignment cannot be extended: backtrack immediately and restore the removed values.

```text
function FC-BACKTRACK(assignment, csp):
    if assignment complete: return assignment
    X <- SELECT-UNASSIGNED-VARIABLE(csp)            // e.g. MRV
    for each value v in DOMAIN(X):
        assign X = v;  removed <- {}
        for each unassigned neighbour Y of X:
            remove from D(Y) all values inconsistent with X = v  (record in removed)
        if no domain became empty:
            result <- FC-BACKTRACK(assignment, csp)
            if result != failure: return result
        restore removed values;  unassign X
    return failure
```

**Example: map colouring of Australia** (R, G, B).

| | WA | NT | Q | NSW | V | SA | T |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| initial domains | RGB | RGB | RGB | RGB | RGB | RGB | RGB |
| after WA = R | R | GB | RGB | RGB | RGB | GB | RGB |
| after Q = G | R | B | G | RB | RGB | B | RGB |
| after V = B | R | B | G | R | B | (empty) | RGB |

After V = B the domain of SA is empty, so FC backtracks immediately without assigning NT, NSW or SA.

**How it helps backtracking search.**

- **Early failure detection**: plain backtracking would only discover the problem when it tries to assign SA, possibly after assigning other variables, wasting a whole subtree.

- **Smaller domains**: the values tried later are already consistent with the past assignment, so fewer consistency checks fail.

- **Works with MRV**: FC keeps the remaining-values counts up to date, which is exactly what MRV needs.

Limitation: FC checks only arcs from the newly assigned variable to its neighbours; it does not notice that NT and SA (both {B}) conflict with each other. Maintaining arc consistency (MAC) propagates further.
