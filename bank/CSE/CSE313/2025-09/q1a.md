---
marks: 15
topics: [bankers-safety-check, safe-vs-unsafe]
kind: numerical
mandatory: true
source: {page: 1}
params:
  type: bankers_safety
  resource_names: [A, B, C]
  total: [9, 3, 6]
  allocation:
    P1: [4, 2, 3]
    P2: [2, 0, 1]
    P3: [1, 0, 1]
    P4: [2, 1, 0]
  max:
    P1: [6, 2, 5]
    P2: [2, 0, 2]
    P3: [6, 3, 3]
    P4: [7, 1, 6]
  available: [0, 0, 1]
  available_derived: true
  assumptions: [non-preemptive resources, process releases everything on completion, all processes may request their maximum at once]
---
Consider a system with 4 processes: P1 through P4 and 3 resource types: A (9 units), B (3 units), and C (6 units). Current allocation of resources and maximum requirement of a process for each resource are given in Figure for Question 1(a). Evaluate whether the current state of this system is safe or unsafe. Note that the resources are non-preemptive and a process releases all its acquired resources when it runs to completion. Also note that all of the four processes may suddenly request their maximum number of resources immediately.

**Current allocation**

| Process | A | B | C |
|:--|:-:|:-:|:-:|
| P1 | 4 | 2 | 3 |
| P2 | 2 | 0 | 1 |
| P3 | 1 | 0 | 1 |
| P4 | 2 | 1 | 0 |

**Maximum requirement**

| Process | A | B | C |
|:--|:-:|:-:|:-:|
| P1 | 6 | 2 | 5 |
| P2 | 2 | 0 | 2 |
| P3 | 6 | 3 | 3 |
| P4 | 7 | 1 | 6 |

Total: A = 9, B = 3, C = 6.
