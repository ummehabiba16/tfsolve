---
marks: 10
topics: [planning]
kind: analysis
source: {page: 52}
---
Suppose following predicates describe the environment of blocks completely having two agents in that environment. These two agents are Agent1 and Agent2.

- ON(A,B) -- Block A is on block B.
- ONTABLE(A) -- Block A is on the table.
- CLEAR(A) -- There is nothing on top of block A.
- HOLDING(A, 1) -- The Agent1's arm is holding block A.
- HOLDING(A, 2) -- The Agent2's arm is holding block A.
- ARMEMPTY(1) -- The Agent1's arm is holding nothing.
- ARMEMPTY(2) -- The Agent2's arm is holding nothing.

Now define the precondition, add-list and delete-list for the following action as a precursor to goal stack planning:-

i) STACK(X, Y, 1) and STACK(X, Y, 2).

ii) UNSTACK (X, Y, 1) and UNSTACK (X, Y, 2).

iii) PICKUP (X, 1) and PICKUP (X, 2).

iv) PUTDOWN (X, 1) and PUTDOWN (X, 2).
