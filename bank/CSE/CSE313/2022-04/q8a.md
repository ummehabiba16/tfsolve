---
marks: 10
topics: [page-replacement]
kind: numerical
source: {page: 28}
---
In a hypothetical machine, there are a total of 8 physical page frames.

| Page Table Index | Time of Last Use (t) | Referenced Bit | Modified Bit |
|:-:|:-:|:-:|:-:|
| 0 | 214 | 1 | 1 |
| 1 | 381 | 0 | 1 |
| 2 | 402 | 1 | 0 |
| 3 | 289 | 1 | 1 |
| 4 | 409 | 0 | 0 |
| 5 | 160 | 1 | 1 |
| 6 | 315 | 1 | 0 |
| 7 | 387 | 0 | 1 |

At t = 430 and t = 440, two page faults occur. Using working set page replacement algorithm (with execution time approximation), identify the page frames that will be evicted. Assume the age threshold ($\tau$) to be 50. Also assume that the clock interrupt to clear referenced bit last occurred at t = 425, and this interrupt occurs at 20 units time interval.
