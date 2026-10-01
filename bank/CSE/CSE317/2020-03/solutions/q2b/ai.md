---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Goal-based agent: update state with a model, if the goal is not achieved plan a sequence of actions to the goal and execute it. Utility-based agent: same structure but chooses the action (or plan) with maximum expected utility instead of a goal test."
sources: ["AIMA 3e sec. 2.4.4-2.4.5"]
---
Both agents are model-based: they keep an internal state updated with a world model. They differ in how they choose actions.

**Goal-based agent.** Uses goal information: it searches/plans for a sequence of actions whose result satisfies the goal, and then follows it.

```text
function GOAL-BASED-AGENT(percept) returns an action
    persistent: state   // current conception of the world state
                model   // how the next state depends on state and action
                goal    // description of the desired goal states
                plan    // sequence of actions, initially empty
                action  // most recent action, initially none

    state <- UPDATE-STATE(state, action, percept, model)
    if GOAL-ACHIEVED(state, goal) then return NoOp
    if plan is empty then
        plan <- PLAN(state, goal, model)     // e.g. search for a path to the goal
        if plan = failure then return NoOp
    action <- FIRST(plan)
    plan   <- REST(plan)
    return action
```

**Utility-based agent.** Goals only distinguish "happy" from "unhappy" states. A utility function $U(s)$ measures how desirable a state is, so the agent can trade off conflicting goals and uncertainty: it chooses the action with the **maximum expected utility**.

```text
function UTILITY-BASED-AGENT(percept) returns an action
    persistent: state, model, action
                U       // utility function on states

    state <- UPDATE-STATE(state, action, percept, model)
    best, bestEU <- none, -infinity
    for each action a in ACTIONS(state):
        EU <- sum over outcomes s' of  P(s' | state, a, model) * U(s')
        if EU > bestEU then best, bestEU <- a, EU
    action <- best
    return action
```

(A planning version computes a plan maximising expected utility and replans when needed; the structure is the same as the goal-based agent, with PLAN optimising $U$ instead of reaching a goal.)
