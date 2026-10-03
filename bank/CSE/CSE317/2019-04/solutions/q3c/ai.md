---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Goal Have(Cake) and Eaten(Cake). Level cost: Have = 0 (S0), Eaten = 1 (S1); in S1 the two are mutex, in S2 they are not. Max-level = 1, level-sum = 1, set-level = 2 (the true plan Eat, Bake has length 2). A serial planning graph allows only one non-persistence action per level (all pairs mutex), so levels equal time steps."
sources: ["AIMA 3e sec. 10.3, Fig. 10.7-10.8 (have cake and eat cake too) / AIMA 4e sec. 11.3"]
---
**Problem** (AIMA):

- $Init(Have(Cake))$; $Goal(Have(Cake)\land Eaten(Cake))$
- $Eat(Cake)$: Pre $Have(Cake)$; Eff $\neg Have(Cake)\land Eaten(Cake)$
- $Bake(Cake)$: Pre $\neg Have(Cake)$; Eff $Have(Cake)$

**Planning graph** (P = persistence):

| Level | Contents | Mutexes |
|:--|:--|:--|
| $S_0$ | $Have$, $\neg Eaten$ | |
| $A_0$ | $Eat$, P($Have$), P($\neg Eaten$) | $Eat$ vs P($Have$) and P($\neg Eaten$) (inconsistent effects / interference) |
| $S_1$ | $Have$, $\neg Have$, $Eaten$, $\neg Eaten$ | $Have$ - $\neg Have$, $Eaten$ - $\neg Eaten$, **$Have$ - $Eaten$** (only reachable by mutex actions), $\neg Have$ - $\neg Eaten$ |
| $A_1$ | $Eat$, $Bake$, persistences | e.g. $Bake$ vs $Eat$ (competing needs) |
| $S_2$ | all four literals | $Have$ - $Eaten$ **no longer mutex** ($Bake$ + P($Eaten$) are compatible) |

**Level costs.** $level(Have)=0$ (in $S_0$) and $level(Eaten)=1$ (first appears in $S_1$).

- **Max-level** $=\max(0,1)=$ **1**.
- **Level-sum** $=0+1=$ **1**. (Admissible here, though not in general.)
- **Set-level** = the first level where *all* goals appear with no pair mutex. At $S_1$, $Have$ and $Eaten$ are mutex; at $S_2$ they are not. So set-level = **2**.

The real optimal plan is $[Eat(Cake),\ Bake(Cake)]$, of length 2, so set-level is exact here, while max-level and level-sum underestimate.

**Serial planning graph.** A planning graph in which **only one action can occur per time step** (besides persistence actions). Mutex links are added between **every pair** of non-persistence actions at each level. Level numbers then correspond to the number of actions (time steps), so level costs are tighter estimates for totally ordered, sequential plans.
