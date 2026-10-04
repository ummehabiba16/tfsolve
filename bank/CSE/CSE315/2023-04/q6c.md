---
marks: 15
topics: [interrupt-hardware]
kind: analysis
source: {page: 29}
note: "The figure is labelled '80286 with the 82288' although the question says 8086."
---
Figure 6(c) expands the interrupt structure of 8086 µP. (5+10=15)

i) What are the vector numbers for IR2 and IR5?

ii) Suppose the vector addresses for IR2 and IR5 are 4C215h and 13D2Bh respectively. If IR2 has higher priority than IR5 and both the interrupts are activated simultaneously, explain the priority resolution protocol.

![Figure 6(c): 74ALS244 (U1) puts the vector on D0-D7 when INTA is low; IR0-IR6 inputs (active low, with 10K pull-ups) go to the buffer inputs and to a 74ALS30 NAND (U2) that drives INTR](figures/q6c-1.png)
