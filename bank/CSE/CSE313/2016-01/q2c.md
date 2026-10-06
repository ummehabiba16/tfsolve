---
marks: 15
topics: [gantt-avg-turnaround]
kind: numerical
source: {page: 51-52}
---
A particular CPU scheduling algorithm is implemented as follows:

The ready queue of processes is treated as a FIFO queue. New processes are added to the tail of the ready queue as soon as they arrive. The scheduler removes a process from the head of the ready queue, sets a timer to interrupt after Q seconds, and gives control of the CPU to the process for execution.

One of two things will then happen:

(i) The currently running process may have a CPU burst of less than Q. In this case, the process itself will release the CPU voluntarily.

(ii) If the CPU burst of the currently running process is longer than Q, the timer will go off and will cause an interrupt to the operating system. The process will be added at the tail of the ready queue.

The scheduler will then remove another process from the head of the ready queue and proceed in the similar fashion.

Apply the above described algorithm for scheduling the workload given in the following table and illustrate the resulting schedule using Gantt chart for each of the cases:

(i) Q = 1

(ii) Q = 2

(iii) Q = 4

Assume that the process switching time is 0 second.

| Process | Arrival Time (sec) | CPU Burst Time (sec) |
|:-:|:-:|:-:|
| A | 0 | 3 |
| B | 1.8 | 6 |
| C | 3.2 | 4 |
| D | 5.6 | 5 |
| E | 7.9 | 2 |

*Table for Q. No. 2(c)*
