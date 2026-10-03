---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Actions are stochastic, so a fixed path is not a solution; we need a policy (an action for every state) that maximizes expected utility. Value iteration: repeat U'[s] <- R(s) + gamma max_a sum P(s'|s,a)U[s'] until delta < eps(1-gamma)/gamma."
sources: ["MNM slides MDP-1-SB (sequential decision problems, value iteration pseudocode)", "AIMA 3e sec. 17.1-17.2, Fig. 17.4"]
---
**Why BFS/DFS are not suitable for an MDP.**

- *Stochastic actions:* in an MDP an action leads to several possible states, with probabilities $P(s'\mid s,a)$. BFS and DFS assume deterministic actions and return a fixed **sequence** of actions (a path). Under uncertainty the agent may end up somewhere the path did not plan for, so a fixed path is not a usable solution.
- *The solution is a policy:* we need an action for **every** state the agent might reach, $\pi(s)$, not just a path to the goal.
- *Optimality is expected utility:* the objective is the expected (discounted) sum of rewards, $E\big[\sum_t\gamma^tR(S_t)\big]$, averaged over outcomes. It is not the cost of one path. Search algorithms compare path costs, not expectations.
- *No single goal, possibly infinite horizon:* rewards come at every step. The process may never terminate, and states can be revisited forever, which BFS/DFS cannot handle (they loop or explore an infinite tree).

These are solved by dynamic programming on the Bellman equation (value or policy iteration), not by search.

**Bellman equation.**

$$U(s)=R(s)+\gamma\max_{a\in A(s)}\sum_{s'}P(s'\mid s,a)\,U(s')$$

**Value iteration (pseudocode).**

```text
function VALUE-ITERATION(mdp, eps) returns a utility function
  inputs: mdp, an MDP with states S, actions A(s), transition model P(s'|s,a),
          rewards R(s), discount gamma
          eps, the maximum error allowed in the utility of any state
  local variables: U, U', vectors of utilities for states in S, initially zero
                   delta, the maximum change in the utility of any state in an iteration
  repeat
      U <- U';  delta <- 0
      for each state s in S do
          U'[s] <- R(s) + gamma * max over a in A(s) of  sum over s' of P(s'|s,a) * U[s']
          if |U'[s] - U[s]| > delta then delta <- |U'[s] - U[s]|
  until delta < eps * (1 - gamma) / gamma
  return U
```

When the loop ends, the policy is extracted with $\pi^*(s)=\arg\max_a\sum_{s'}P(s'\mid s,a)\,U(s')$.
