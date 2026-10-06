---
marks: 15
topics: [gantt-avg-turnaround]
kind: numerical
source: {page: 20}
note: "Printed as 'run job B for time units' (the number of units is missing); the example graph shows 5 units of B."
---
Scheduling policies can be easily depicted with some graphs. For example, let's say we run scheduler **S** for 1 time unit, job **A** for 5 time units, run scheduler **S** again for 1 time unit, and then run job **B** for time units. Our graph of this policy will look like this:

```text
CPU | S A A A A A S B B B B B
    +-------------------------
      0           6          12
```

i. Draw a similar graph of **ROUND-ROBIN** scheduling for jobs **A** (arriving at **T=0**), **B** (arriving at **T = 5**), and **C** (arriving at **T = 10**), each running for **6 time-units**. Assume a **2 time unit** time slice; also assume that the scheduler (**S**) takes 1 time unit to make a scheduling decision. Make sure to label the x-axis appropriately.

ii. What is the average **RESPONSE TIME** for jobs A, B and C?

iii. What is the average **TURNAROUND TIME** for jobs A, B and C?
