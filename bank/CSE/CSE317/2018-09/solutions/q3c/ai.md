---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "D-separation: X and Y are conditionally independent given evidence Z if every undirected path between them is blocked (inactive). A path is active iff every consecutive triple on it is active: a chain or common cause is active iff the middle node is NOT observed; a common effect (v-structure) is active iff the middle node or one of its descendants IS observed."
sources: ["MNM slides Uncertainty-3-BN-IND and BN-independence (d-separation, active triples)", "AIMA 4e sec. 13.2.1", "Berkeley CS188 Bayes nets: independence"]
---
**D-separation rule** (8 marks). In a Bayesian network, for disjoint sets of variables $X$, $Y$ and evidence $Z$:

$$X\perp Y\mid Z\ \text{ is guaranteed if } X \text{ and } Y \text{ are d-separated by } Z,$$

that is, if **every** undirected path between a node of $X$ and a node of $Y$ is **blocked (inactive)** given $Z$. If some path is active, independence is not guaranteed: it can fail for some CPTs.

Algorithm: list all paths between $X$ and $Y$ (ignoring edge directions) and check each path's triples. Independence holds iff no path is active.

**When is a path active?** (7 marks) A path is active iff **every consecutive triple** on it is active. There are three kinds of triple:

| Triple | Shape | Active when |
|:--|:--|:--|
| Causal chain | $A\to B\to C$ (or $A\leftarrow B\leftarrow C$) | $B$ is **not** observed |
| Common cause | $A\leftarrow B\to C$ | $B$ is **not** observed |
| Common effect (v-structure) | $A\to B\leftarrow C$ | $B$ **or one of its descendants** is observed |

- Chain or common cause: observing the middle node blocks the flow of influence. For example, knowing $Alarm$ makes $Burglary$ and $JohnCalls$ independent.
- Common effect: the opposite, *explaining away*. $Burglary$ and $Earthquake$ are independent, but once $Alarm$ (or $JohnCalls$) is observed they become dependent.

A single inactive triple blocks the whole path.

*Example:* in $B\to A\leftarrow E$, $A\to J$: $B\perp E$ (the collider $A$ is unobserved), but $B\not\perp E\mid J$ ($J$ is a descendant of the collider).
