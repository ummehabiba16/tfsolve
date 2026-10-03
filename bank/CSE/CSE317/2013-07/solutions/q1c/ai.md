---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Partial-order planning starts with Start (effects: At(Flat, Axle), At(Spare, Trunk)) and Finish (precondition At(Spare, Axle)); adds PutOn(Spare, Axle) for the goal, Remove(Spare, Trunk) for At(Spare, Ground), and Remove(Flat, Axle) for not At(Flat, Axle), with causal links and ordering constraints; LeaveOvernight would threaten the links, so it is not used; the result is a partial order in which the two Remove steps can occur in either order, before PutOn."
sources: ["AIMA 3e sec. 10.4.4 (partial-order planning), Fig. 10.2 (spare tire problem)"]
---
**Actions** (AIMA's spare-tire problem):

- $Remove(obj,loc)$: precondition $At(obj,loc)$; effect $\neg At(obj,loc)\land At(obj,Ground)$.
- $PutOn(Spare,Axle)$: precondition $At(Spare,Ground)\land\neg At(Flat,Axle)$; effect $\neg At(Spare,Ground)\land At(Spare,Axle)$.
- $LeaveOvernight$: effect: no tire is at Ground, Axle or Trunk (everything is stolen).

**Partial-order planning (POP)** searches in the space of **partial plans**: a set of steps, ordering constraints $A\prec B$, causal links $A\xrightarrow{p}B$, and open preconditions. It commits to an order only when necessary (least commitment).

1. **Initial plan:** $Start$ (effects $At(Flat,Axle)$, $At(Spare,Trunk)$) and $Finish$ (precondition $At(Spare,Axle)$), with $Start\prec Finish$.
2. **Open precondition $At(Spare,Axle)$** of Finish: add the step $PutOn(Spare,Axle)$ and the causal link $PutOn\xrightarrow{At(Spare,Axle)}Finish$.
3. **Open preconditions of PutOn.** For $At(Spare,Ground)$: add $Remove(Spare,Trunk)$ with the link $Remove(Spare,Trunk)\xrightarrow{At(Spare,Ground)}PutOn$. Its own precondition $At(Spare,Trunk)$ is supplied by $Start$. For $\neg At(Flat,Axle)$: add $Remove(Flat,Axle)$ with the link $\xrightarrow{\neg At(Flat,Axle)}PutOn$. Its precondition $At(Flat,Axle)$ is supplied by $Start$.
4. **Threats:** $LeaveOvernight$ could achieve $\neg At(Flat,Axle)$, but it also deletes $At(Spare,Ground)$ and $At(Spare,Trunk)$, so it would **clobber** the causal links. If chosen, the conflict cannot be resolved by ordering (promotion or demotion). The planner backtracks and uses $Remove(Flat,Axle)$ instead.
5. **No open preconditions or unresolved threats remain**, so the plan is complete.

```text
              Start
             /     \
Remove(Spare,Trunk)  Remove(Flat,Axle)      (unordered with respect to each other)
             \     /
        PutOn(Spare,Axle)
               |
             Finish
```

**Solution:** the two $Remove$ steps can be done in **either order** (or in parallel), followed by $PutOn(Spare,Axle)$. Any linearization works, e.g. Remove(Flat, Axle), Remove(Spare, Trunk), PutOn(Spare, Axle). The advantage of POP is that it does not commit to that order unnecessarily.
