---
marks: 15
topics: [garbage-collection]
kind: numerical
source: {page: 20}
note: "Printed as 'The baker's mark-and-sweep'. Edges as read from the figure: X->A, Y->B, A->D, A->E, B->C, B->E, C->I, D->F, D->G, D->H, E->H, F->I, G->H, H->I, I->E."
---
The baker's mark-and-sweep algorithm for garbage collection moves objects among four lists: *Free, Unreached, Unscanned,* and *Scanned*. Illustrate how Baker's mark-and-sweep algorithm garbage collector works using the example network below when the pointer $A \to D$ is deleted. Assume X and Y are members of the root set. What is the time and space complexity of the algorithm?

![Figure for Question 3(a)](figures/q3a-1.png)
