---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Four components: initial state, actions (successor function), goal test, path cost. Abstraction removes detail irrelevant to the goal from the state and action descriptions (e.g. In(Arad) instead of weather, scenery or exact position; drive between cities instead of steering commands); a good abstraction is valid (every abstract solution can be refined into a real one) and useful (abstract actions are easy to carry out)."
sources: ["AIMA 3e sec. 3.1.1-3.1.2 (well-defined problems, abstraction)"]
---
**Four components of a formal problem.**

1. **Initial state:** where the agent starts, e.g. $In(Arad)$.
2. **Actions / successor function:** the actions applicable in each state and their results (the transition model), e.g. from $In(Arad)$: $\{Go(Sibiu), Go(Timisoara), Go(Zerind)\}$.
3. **Goal test:** whether a state is a goal, e.g. $In(Bucharest)$, or an abstract property such as "checkmate".
4. **Path cost:** a function assigning a numeric cost to each path (the sum of step costs $c(s,a,s')$, e.g. kilometres).

A solution is a path from the initial state to a goal state; an optimal solution has the lowest path cost.

**Abstraction.** The process of **removing detail** from a representation. The real world is extremely complex: a real state of a car trip includes the companions, the radio, the weather, the exact position on the road. We abstract both:

- **states**, keeping only what matters for the goal: $In(Arad)$;
- **actions**, e.g. "drive from Arad to Sibiu" instead of steering, braking and accelerating commands.

**How abstraction helps.** The abstract state space is small enough to search. A good abstraction must be:

- **valid:** any abstract solution can be expanded into a solution in the detailed world (every real way of being "in Arad" can get "to Sibiu");
- **useful:** the abstract actions are easy enough to carry out without further search or planning by the agent.

Choosing a good abstraction keeps as much detail out as possible while remaining valid.
