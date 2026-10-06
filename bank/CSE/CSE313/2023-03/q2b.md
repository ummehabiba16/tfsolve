---
marks: 5
topics: [deadlock-four-conditions]
kind: analysis
source: {page: 19}
---
You wrote a piece of code with four threads (1-4) and four locks (A-D).

Thread 1 grabs Locks A and B (in some order); Thread 2 grabs Locks B and C (in some order);

Thread 3 grabs Locks C and D (in some order); Thread 4 grabs Locks D and A (in some order);

Is it possible that this code might result in deadlock? Briefly explain.
