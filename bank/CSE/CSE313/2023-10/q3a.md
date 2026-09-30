---
marks: 15
topics: [bankers-safety-check, safe-vs-unsafe]
kind: numerical
source: {page: 14}
note: Same instance as the worked example in Notes_on_algorithm_simulation.pdf (safe order P2 -> P1 -> P3 -> P4).
params:
  type: bankers_safety
  resource_names: [A, B, C]
  total: [9, 3, 6]
  allocation:
    P1: [1, 0, 0]
    P2: [6, 1, 2]
    P3: [2, 1, 1]
    P4: [0, 0, 2]
  max:
    P1: [3, 2, 2]
    P2: [6, 1, 3]
    P3: [3, 1, 4]
    P4: [4, 2, 2]
  available: [0, 1, 1]
  available_derived: true
  assumptions: [all processes request their maximum at once]
---
Consider a system with 4 processes: P1 through P4 and 3 resources types: A (9 units), B (3 units), C (6 Units). Current allocation of resources and maximum requirement of a process for each resource are given in Figure for Question 3(a). Determine whether the current state of this system is safe or not.

**Current allocation**

| Process | A | B | C |
|:--|:-:|:-:|:-:|
| P1 | 1 | 0 | 0 |
| P2 | 6 | 1 | 2 |
| P3 | 2 | 1 | 1 |
| P4 | 0 | 0 | 2 |

**Maximum requirement**

| Process | A | B | C |
|:--|:-:|:-:|:-:|
| P1 | 3 | 2 | 2 |
| P2 | 6 | 1 | 3 |
| P3 | 3 | 1 | 4 |
| P4 | 4 | 2 | 2 |

Total: A = 9, B = 3, C = 6.
