---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Without resources, scheduling is the critical-path problem: ES/LS by a forward and a backward pass, polynomial (O(Nb)). With resource limits, actions that compete for a resource must be ordered, a disjunctive constraint (A before B or B before A); the number of possible orderings is exponential, and the problem is NP-hard (job-shop scheduling)."
sources: ["AIMA 3e sec. 11.1.2 (solving scheduling problems) / AIMA 4e sec. 11.6"]
---
**Critical-path problem (no resource conflicts).** The only constraints are *conjunctive* ordering constraints $start(B)\ge start(A)+d_A$. These form a DAG.

- One forward pass computes the earliest starts: $ES(B)=\max_{A\prec B}ES(A)+d_A$.
- One backward pass computes the latest starts: $LS(A)=\min_{B\succ A}LS(B)-d_A$.
- The makespan is the length of the longest (critical) path. It takes time $O(Nb)$ for $N$ actions with branching factor $b$, which is **polynomial**: a longest-path computation in a DAG.

**With resource constraints.** Two actions that need the same limited resource (one engine hoist) cannot overlap. That gives a **disjunctive** constraint:

$$start(A)+d_A\le start(B)\quad\textbf{or}\quad start(B)+d_B\le start(A).$$

- The feasible region is no longer convex. The solver must **choose an order** for every conflicting pair, and the number of combinations grows exponentially with the number of conflicting actions.
- Finding the minimum-makespan schedule is then **NP-hard** (job-shop scheduling).
- So exact methods (branch-and-bound, CSP, integer programming) or heuristics (for example the **minimum-slack** algorithm, which is greedy and not always optimal) are needed.

In short, the critical-path problem is a shortest/longest-path computation, while resource conflicts make it a combinatorial search over orderings.
