---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "A state is a configuration of the world; a node is a data structure in the search tree that contains a state plus bookkeeping. The five components of a node: STATE, PARENT-NODE, ACTION (that generated it), PATH-COST g(n), DEPTH."
sources: ["AIMA 2e sec. 3.3 / AIMA 3e sec. 3.3.1 (infrastructure for search algorithms)"]
---
**Node versus state.**

- A **state** is a (representation of a) physical configuration of the world, e.g. $In(Arad)$.
- A **node** is a **data structure** in the search tree that *contains* a state plus bookkeeping about how it was reached: its parent, the action, the cost and the depth. Two different nodes can contain the same state if it is reached by different paths, and they then have different parents, path costs and depths. States have no parents, depth or cost; nodes do.

**Five components of a node.**

1. **STATE:** the state in the state space to which the node corresponds.
2. **PARENT-NODE:** the node in the search tree that generated this node.
3. **ACTION:** the action applied to the parent to generate the node.
4. **PATH-COST** $g(n)$: the cost of the path from the initial state to the node, following the parent pointers.
5. **DEPTH:** the number of steps along the path from the initial state.

(Following the parent pointers from a goal node recovers the solution path.)
