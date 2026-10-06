---
marks: 10
topics: [deadlock-four-conditions]
kind: diagram
source: {page: 51}
---
Suppose two processes P1 and P2 are running concurrently in a single processor system. The system contains two dedicated resources: one printer and one DVD-ROM. These resources can be used by only one process at a time. Both P1 and P2 has 600 instructions. P1 requests the DVD-ROM at 200th instruction and the printer at 400th instruction. P1 releases the DVD-ROM and printer at 300th and 500th instruction respectively. P2 requests the printer at 200th instruction and the DVD-ROM at 300th instruction. P2 releases the printer and DVD-ROM at 400th and 500th instruction respectively.

Draw a diagram where each point depicts a joint state of the two processes where the horizontal axis represents the number of instructions executed by P1 and the vertical axis represents the number of instructions executed by P2. You must mark the regions where entry is restricted by the mutual exclusion rule.
