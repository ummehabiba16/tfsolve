---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "SIMPLE-PROBLEM-SOLVING-AGENT keeps an action sequence; when it is empty it updates the state, formulates a goal and a problem, calls SEARCH to get a solution sequence, then returns the first action and keeps the rest (formulate-search-execute, open loop)."
sources: ["AIMA 3e sec. 3.1 (Figure 3.1)"]
---
The agent follows the **formulate, search, execute** design: when it has no plan, it formulates a goal and a problem, searches for a solution, and then executes the solution one action at a time, ignoring percepts while executing (open-loop).

```text
function SIMPLE-PROBLEM-SOLVING-AGENT(percept) returns an action
    persistent: seq      // an action sequence, initially empty
                state    // description of the current world state
                goal     // a goal, initially null
                problem  // a problem formulation

    state <- UPDATE-STATE(state, percept)
    if seq is empty then
        goal    <- FORMULATE-GOAL(state)
        problem <- FORMULATE-PROBLEM(state, goal)
        seq     <- SEARCH(problem)
        if seq = failure then return a null action
    action <- FIRST(seq)
    seq    <- REST(seq)
    return action
```

**Explanation.**

- `UPDATE-STATE` interprets the percept to update the agent's view of the world.

- `FORMULATE-GOAL` decides what to achieve (e.g. be in Bucharest).

- `FORMULATE-PROBLEM` defines initial state, actions, transition model, goal test and path cost for that goal.

- `SEARCH` (BFS, UCS, A*, ...) returns an action sequence leading to the goal, or failure.

- On each call while `seq` is non-empty, the agent returns the next action without searching again. When the sequence is finished, it formulates a new goal.

This works when the environment is fully observable, deterministic, discrete and known, so the plan can be executed without checking percepts.
