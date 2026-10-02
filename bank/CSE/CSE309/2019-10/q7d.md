---
marks: 15
topics: [garbage-collection]
kind: numerical
source: {page: 34}
note: "Marks printed as (2+8+5). Edges as read from the figure: X->A, Y->B, A->D, A->E, B->C, B->E, C->I, D->F, D->G, D->H, E->H, F->I, G->H, H->I, I->E."
---
Each garbage collection algorithm starts with a root set. Which objects constitute the root set? Consider the network of objects in Figure 7(d). Show the steps of a mark-and-sweep garbage collector on this network with the pointer $A \to D$ deleted. Assume X and Y are members of the root set. What is the primary difference between basic mark-and-compact and Cheney's copying collector algorithms?

![Figure for Question 7(d)](figures/q7d-1.png)
