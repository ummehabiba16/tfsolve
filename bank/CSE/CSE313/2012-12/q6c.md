---
marks: 10
topics: [bankers-safety-check]
kind: numerical
source: {page: 68}
---
Given the following state for the Banker's Algorithm. There are 6 processes P0 through P5 and 4 resource types: A (15 instances); B (6 instances), C( 9 instances); D (10 instances). For the following current allocation and maximum need, should a new request (3, 2, 3, 3) from P5 be granted?

**Current Allocation**

| Process | A | B | C | D |
|:-:|:-:|:-:|:-:|:-:|
| P0 | 2 | 0 | 2 | 1 |
| P1 | 0 | 1 | 1 | 1 |
| P2 | 4 | 1 | 0 | 2 |
| P3 | 1 | 0 | 0 | 1 |
| P4 | 1 | 1 | 0 | 0 |
| P5 | 1 | 0 | 1 | 1 |

**Maximum Need**

| Process | A | B | C | D |
|:-:|:-:|:-:|:-:|:-:|
| P0 | 9 | 5 | 5 | 5 |
| P1 | 2 | 2 | 3 | 3 |
| P2 | 7 | 5 | 4 | 4 |
| P3 | 3 | 3 | 3 | 2 |
| P4 | 5 | 2 | 2 | 1 |
| P5 | 4 | 4 | 4 | 4 |
