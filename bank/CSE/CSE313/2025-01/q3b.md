---
marks: 10
topics: [safe-vs-unsafe, bankers-safety-check]
kind: numerical
source: {page: 9}
params:
  type: bankers_safety_single
  resource_names: [R]
  total: [20]
  allocation:
    P1: [5]
    P2: [6]
    P3: [2]
    P4: [0]
  max:
    P1: [9]
    P2: [12]
    P3: [8]
    P4: [15]
  available: [7]
  available_derived: false
---
Distinguish between a safe state and an unsafe state. Consider a system with 4 processes: P1 through P4 and 1 resource type with 20 instances: Current allocation of resources and maximum requirement of each process are given in Figure for Question 3(b). Determine whether the current state of this system is safe or not. Show the intermediate steps.

**Current allocation**

| Process | R |
|:--|:-:|
| P1 | 5 |
| P2 | 6 |
| P3 | 2 |
| P4 | 0 |

**Maximum requirement**

| Process | R |
|:--|:-:|
| P1 | 9 |
| P2 | 12 |
| P3 | 8 |
| P4 | 15 |

Total: R = 20; Available: (7).
