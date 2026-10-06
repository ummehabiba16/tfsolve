---
marks: 10
topics: [bankers-safety-check]
kind: numerical
source: {page: 31}
---
Consider the following snapshot of a system. There are three processes, P1, P2 and P3 competing for three resources R1, R2, and R3. (8+2)

**Total Resource Instances**

| R1 | R2 | R3 |
|:-:|:-:|:-:|
| 3 | 2 | 5 |

**Available**

| R1 | R2 | R3 |
|:-:|:-:|:-:|
| 1 | 1 | 1 |

**Allocated**

| Process ID | R1 | R2 | R3 |
|:-:|:-:|:-:|:-:|
| P1 | 0 | 0 | 2 |
| P2 | 1 | 0 | 2 |
| P3 | 1 | 1 | 0 |

**Maximum Required**

| Process ID | R1 | R2 | R3 |
|:-:|:-:|:-:|:-:|
| P1 | 3 | 1 | 3 |
| P2 | 1 | 2 | 3 |
| P3 | 2 | 2 | 1 |

Now, answer the following questions using the banker's algorithm:

(i) Illustrate that the system is in a safe state by demonstrating an order in which the threads may complete.

(ii) If a request from process P1 arrives for (1, 1, 1), can the request be granted immediately?
