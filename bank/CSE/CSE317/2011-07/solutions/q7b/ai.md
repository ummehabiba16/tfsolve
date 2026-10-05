---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "In a sensorless problem the agent cannot observe its state, so it searches over belief states: sets of physical states it might be in. Any subset of the S physical states could be the agent's current belief, and a set of S elements has 2^S subsets, so the belief-state space has up to 2^S belief states (though usually only a small fraction is reachable from the initial belief)."
sources: ["AIMA 3e sec. 4.4.1 (searching with no observation)"]
---
**Belief states.** In a **sensorless (conformant)** problem the agent has no percepts, so it does not know which physical state it is in. It reasons about a **belief state**: the **set of physical states it might currently be in**. Initially that is every possible state. Each action maps the belief state $b$ to $b'=\{\text{Result}(s,a):s\in b\}$, and the goal is reached when **every** state in the belief state is a goal state. Search (BFS, A\*) runs in this belief-state space, where the solution is a sequence of actions that works whatever the true state is.

**Why $2^S$.** If the physical problem has $S$ states, a belief state can be **any subset** of those $S$ states. Each physical state is either in the set or not, so there are $2^S$ subsets (including the empty set, which never arises in practice). So the belief-state space has up to $2^S$ belief states.

*Example:* the two-cell vacuum world has $S=8$ physical states, so up to $2^8=256$ belief states, of which only 12 are reachable from the initial belief state.
