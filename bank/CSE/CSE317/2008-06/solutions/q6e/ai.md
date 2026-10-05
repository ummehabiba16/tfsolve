---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "AIMA 2e section 7.7: (1) Locality: a circuit-based agent scales only if each proposition can be determined from a constant number of other propositions (true in the Wumpus world, false in Minesweeper); nonlocal domains need huge circuits. (2) Acyclicity: every feedback path from a register's output to its input must pass through a delay element, because cyclic circuits can oscillate; this forbids interlocking dependencies (breeze depends on pits, pits on breeze), so the acyclic agent is incomplete (it cannot conclude a breeze in [2,2] from a breeze in [1,1])."
sources: ["AIMA 2e sec. 7.7.2 (circuit-based agents: locality, acyclicity, comparison with inference-based agents)"]
---
A **circuit-based agent** (AIMA 2e §7.7) is a reflex agent with state, implemented as a **sequential Boolean circuit**. Gates compute propositions directly from the percepts, and **registers with delay lines** store state (e.g. $K(P_{x,y})$, "it is known that there is a pit in $[x,y]$"). There is no explicit inference. Its design is subject to two restrictions:

**1. Locality.** For the circuit to stay reasonably small, with a constant number of gates per proposition, the environment must exhibit **locality**: the truth of each proposition of interest must be determinable by looking at **only a constant number of other propositions**.

- The Wumpus world is local: whether a square has a pit depends only on the breezes in adjacent squares.
- **Minesweeper is non-local**: deciding whether a square has a mine can depend on squares arbitrarily far away.

For non-local domains, circuit-based agents are not practical, because the circuit becomes too large.

**2. Acyclicity.** The circuit must be **acyclic**: every path from a register's output back to its input must pass through a **delay** element. Cyclic circuits are physically unstable: they can go into oscillation, producing undefined values.

- This forbids interlocking dependencies such as "breeziness depends on known adjacent pits, and pits depend on adjacent breeziness" (AIMA's Equation 7.9).
- As a result, the acyclic agent is **incomplete**: it can know less than an inference-based agent. For example, from a breeze in $[1,1]$, an inference-based agent can conclude that there is a breeze in $[2,2]$; the acyclic circuit cannot.

(Beyond these restrictions, a circuit that is complete for every determinable proposition may have to be exponentially large, and circuits remember only individual propositions, not disjunctive knowledge such as "$P_{1,2}\lor P_{2,1}$".)
