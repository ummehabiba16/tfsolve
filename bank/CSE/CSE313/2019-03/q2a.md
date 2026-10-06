---
marks: 10
topics: [page-replacement]
kind: numerical
source: {page: 33}
---
Suppose that the WSClock page replacement algorithm uses at $\tau$ of 2 ticks, and the system state is the following:

| Page# | Time stamp | V | R | M |
|:-:|:-:|:-:|:-:|:-:|
| 0 | 9 | 1 | 1 | 0 |
| 1 | 9 | 1 | 1 | 1 |
| 2 | 7 | 1 | 0 | 0 |
| 3 | 4 | 0 | 0 | 0 |
| 4 | 6 | 1 | 0 | 1 |

Here, the three flag bits V, R, and M stand for Valid, Referenced, and Modified, respectively.

(i) If a clock interrupt occurs at tick 10, show the contents of the new table entries with explanation.

(ii) Suppose that instead of a clock interrupt, a page fault occurs at tick 10 due to a read request to page 3. Show the contents of the new table entries with explanation.
