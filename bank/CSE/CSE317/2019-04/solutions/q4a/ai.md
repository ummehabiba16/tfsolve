---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Temporal constraints: each action has a duration and ordering constraints; a schedule assigns start times with ES/LS. Resource constraints: actions declare Use (reusable, e.g. EngineHoists(1)) or Consume (e.g. LugNuts(20)) of numeric resources, never exceeding capacity. Aggregation groups identical objects into a quantity (Inspectors(2), LugNuts(500)), avoiding a huge number of symmetric assignments."
sources: ["AIMA 3e sec. 11.1 (time, schedules and resources), Fig. 11.1 / AIMA 4e sec. 11.6"]
---
**Representation (job-shop scheduling).** The problem is a set of *jobs*. Each job is a partially ordered collection of *actions*, each with a **duration** and **resource requirements**. Plans are made first and scheduled afterwards.

**Temporal constraints.**

- Each action has a duration: $Action(AddEngine1,\ \textsc{Duration}:30)$.
- Ordering constraints inside a job, e.g. $AddEngine1\prec AddWheels1$ and $AddWheels1\prec Inspect1$.
- A schedule assigns start times $ES(A)\le start(A)\le LS(A)$ with $start(B)\ge start(A)+Duration(A)$ for $A\prec B$. The objective is to minimize the makespan (total time). Without resources, ES and LS come from the **critical path method**.

**Resource constraints.** Declare the resources, e.g. $EngineHoists(1)$, $WheelStations(1)$, $Inspectors(2)$, $LugNuts(500)$. Actions state what they need:

- **reusable** resources are *used* (occupied during the action, then released): $\textsc{Use}:EngineHoists(1)$;
- **consumable** resources are *consumed*: $\textsc{Consume}:LugNuts(20)$.

At no time may the amount in use exceed the capacity, and consumables must not run out.

**Aggregation.** Objects that are indistinguishable for the problem are grouped into a **quantity** instead of being named individually. For example, $Inspectors(2)$ instead of two named inspectors $I_1,I_2$, and $LugNuts(500)$ instead of 500 nut objects. This keeps the representation compact. It also avoids the combinatorial explosion of symmetric choices: the planner does not have to try "inspector $I_1$ or $I_2$", or which of 500 nuts to use. It only checks that the numeric quantity in use stays within the limit, which makes reasoning about resource conflicts far more efficient.
