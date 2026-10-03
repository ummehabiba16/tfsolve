---
marks: 15
topics: [propositional-logic]
kind: numerical
source: {page: 44}
set_by: [UNKNOWN]
---
Suppose, the current Knowledge Base (KB) of a logical agent contains the following sentences:

$A \land B \Rightarrow C$, $A \land D \Rightarrow C$, $B \land C \Rightarrow E$, $C \land E \Rightarrow D$, $A \land C \Rightarrow P$, $D \Rightarrow E$, $D \land P \Rightarrow Q$, $P \land Q \Rightarrow R$, $A \land D \land R \Rightarrow S$, A, and B

Use Forward Chaining algorithm (PL-FC-Entails?) to determine whether the KB entails "S" or not. Clearly show the states of the associated data structures at each iteration of the algorithm.
