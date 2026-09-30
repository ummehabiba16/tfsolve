---
marks: 10
topics: [bankers-safety-check, safe-vs-unsafe]
kind: numerical
source: {page: 26}
note: Process names are A-D (not P1-P4); resource names R1-R5 are added for convenience.
params:
  type: bankers_safety
  resource_names: [R1, R2, R3, R4, R5]
  total: null
  allocation:
    A: [1, 0, 2, 1, 1]
    B: [2, 0, 1, 1, 0]
    C: [1, 1, 0, 1, 0]
    D: [1, 1, 1, 1, 0]
  max:
    A: [1, 1, 2, 1, 3]
    B: [2, 2, 2, 1, 0]
    C: [2, 1, 3, 1, 0]
    D: [1, 1, 2, 2, 1]
  available: [0, 0, x, 1, 1]
  available_derived: false
  unknown: x
  ask: min_x_for_safe_state
---
A system has four processes and five allocatable resources. The current allocation and maximum needs are as follows. What is the smallest value of x for which this is a safe state? Show the intermediate steps.

**Current allocation**

| Process | R1 | R2 | R3 | R4 | R5 |
|:--|:-:|:-:|:-:|:-:|:-:|
| A | 1 | 0 | 2 | 1 | 1 |
| B | 2 | 0 | 1 | 1 | 0 |
| C | 1 | 1 | 0 | 1 | 0 |
| D | 1 | 1 | 1 | 1 | 0 |

**Maximum requirement**

| Process | R1 | R2 | R3 | R4 | R5 |
|:--|:-:|:-:|:-:|:-:|:-:|
| A | 1 | 1 | 2 | 1 | 3 |
| B | 2 | 2 | 2 | 1 | 0 |
| C | 2 | 1 | 3 | 1 | 0 |
| D | 1 | 1 | 2 | 2 | 1 |

Available: (0, 0, x, 1, 1).
