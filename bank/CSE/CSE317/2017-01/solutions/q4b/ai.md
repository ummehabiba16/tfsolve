---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "SATPlan: encode the planning problem as a propositional sentence with time-indexed fluents and actions (initial state, goal at time T, successor-state axioms, precondition axioms, action-exclusion axioms); a SAT solver's model gives the plan (the actions true at each time step), trying T = 0, 1, 2, ... Precondition axioms stop the solver from choosing actions whose preconditions are false; action-exclusion axioms stop it from choosing two incompatible actions at the same time step."
sources: ["AIMA 3e sec. 7.7.4 (making plans by propositional inference, SATPlan)"]
---
**Planning by propositional inference (SATPlan).**

1. Make time-indexed copies of every fluent ($HaveArrow^t$, $L_{1,1}^t$) and every action ($Shoot^t$, $Forward^t$) for $t=0..T$.
2. Build a sentence: **initial state** at $t=0$, plus **successor-state axioms** for every fluent and step, plus **precondition axioms**, plus **action-exclusion axioms**, plus the **goal** asserted at time $T$.
3. Give it to a SAT solver (DPLL or WalkSAT). If it finds a model, the plan is the sequence of action symbols assigned true. If it is unsatisfiable, increase $T$ and repeat, up to some limit.

**Why precondition axioms?** The successor-state axioms say what happens *if* an action is done, but not *when* it can be done. Without precondition axioms, the solver could satisfy the goal by assigning true to an action whose preconditions do not hold. For example, it could make $Shoot^t$ true even though the agent has no arrow, because the axioms only describe the effects. Precondition axioms state, for each action $A$: $A^t\Rightarrow PRE(A)^t$. For example, $Shoot^t\Rightarrow HaveArrow^t$. This rules out such illegal plans.

**Why action-exclusion axioms?** Without them, the solver may set **several actions true at the same time step**, for example $Forward^t$ and $Shoot^t$, or moving to two different squares, producing a "plan" no single agent can execute. Action-exclusion axioms $\neg A_i^t\lor\neg A_j^t$ for every pair of actions (or only for pairs that interfere, to allow partial order) ensure the plan is a valid sequence: one action, or only compatible actions, per step.
