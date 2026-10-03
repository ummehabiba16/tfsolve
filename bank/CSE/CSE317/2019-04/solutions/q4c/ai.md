---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Case 1 (1 hoist, 1 wheel station, 2 inspectors; J1 30-30-10, J2 60-15-10): the critical path is 85, but minimum slack schedules J2's engine first and gives a makespan of 130 min (the optimum, with J1's engine first, is 115). Case 2 (2 hoists, 1 wheel station, 1 inspector; J2 40-15-10): minimum slack gives 85 min, which is optimal."
sources: ["AIMA 3e sec. 11.1, Fig. 11.1-11.3 (car assembly; the minimum-slack algorithm gives 130, not 115)"]
---
**Actions.** $AE$ = AddEngine (uses an engine hoist), $AW$ = AddWheels (uses the wheel station, consumes 20 lug nuts), $I$ = Inspect (uses an inspector). Each job is ordered $AE\prec AW\prec I$. Lug nuts ($500\ge40$) never bind.

**Minimum-slack algorithm.** Compute ES and LS by the critical-path method. Repeatedly schedule, at its earliest feasible start (respecting resources), the unscheduled action whose predecessors are all scheduled and whose **slack** $LS-ES$ is smallest. Then update ES and LS.

**Case 1: 1 hoist, 1 wheel station, 2 inspectors, J1 = (30, 30, 10), J2 = (60, 15, 10).**

Critical-path values (resources ignored; critical path = J2 = 60 + 15 + 10 = 85):

| Action | $AE_1$ | $AW_1$ | $I_1$ | $AE_2$ | $AW_2$ | $I_2$ |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|
| ES | 0 | 30 | 60 | 0 | 60 | 75 |
| LS | 15 | 45 | 75 | 0 | 60 | 75 |
| slack | 15 | 15 | 15 | 0 | 0 | 0 |

Minimum-slack steps:

1. $AE_2$ (slack 0) runs $[0,60]$ on the hoist. $AE_1$ must now wait for the hoist (ES 60), and after the update J1's actions have slack 0.
2. $AW_2$ runs $[60,75]$; $I_2$ runs $[75,85]$.
3. $AE_1$ runs $[60,90]$ (hoist free at 60); $AW_1$ runs $[90,120]$; $I_1$ runs $[120,130]$.

```gantt
# Case 1: minimum-slack schedule (makespan 130)
AE2 0 60
AE1 60 90
AW2 60 75
AW1 90 120
I2 75 85
I1 120 130
```

**Makespan by minimum slack = 130 minutes.** It is not optimal. Giving the hoist to J1 first ($AE_1\ [0,30]$, $AE_2\ [30,90]$, $AW_1\ [30,60]$, $AW_2\ [90,105]$, $I_1\ [60,70]$, $I_2\ [105,115]$) gives the optimal **115 minutes**, checked by trying all orders.

**Case 2: 2 hoists, 1 wheel station, 1 inspector, J2 = (40, 15, 10).**

Critical path = J1 = 30 + 30 + 10 = 70. Slack: J1 actions 0, J2 actions 5.

1. $AE_1$ $[0,30]$, $AW_1$ $[30,60]$, $I_1$ $[60,70]$ (slack 0).
2. $AE_2$ $[0,40]$ on the second hoist. $AW_2$ needs the wheel station, busy until 60, so it runs $[60,75]$. $I_2$ runs $[75,85]$ (the inspector is free after 70).

```gantt
# Case 2: minimum-slack schedule (makespan 85)
AE1 0 30
AE2 0 40
AW1 30 60
AW2 60 75
I1 60 70
I2 75 85
```

**Makespan = 85 minutes**, which is optimal for this case (checked by brute force). The single wheel station is the bottleneck: the two AddWheels need $30+15=45$ minutes in sequence after $AE_1$.
