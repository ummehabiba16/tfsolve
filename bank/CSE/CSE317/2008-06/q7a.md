---
marks: 18
topics: [propositional-logic]
kind: analysis
source: {page: 76}
---
Consider the following description of wumpus world problem:

Wumpus world is a $4\times4$ grid. Initially the Agent is at [1, 1]. There is one wumpus in one of the 16 squares except [1, 1]. Three of the squares except [1, 1] contain three pits. The positions of wumpus and pits are randomly distributed, however wumpus doesn't live in a square where there is a pit. Squares adjacent to wumpus are smelly and adjacent to pits are breezy.

At [1, 1] the Agent perceives neither Stench nor Breeze perception. Now the Agent moves to [2, 1] where it perceives both Stench and Breeze perceptions. Then it returns to [1, 1], and thereafter moves to [1, 2] where it perceives both Stench and Breeze perceptions.

From the initial Knowledge Base and observed perceptions, entail the following conclusions with the help of propositional logic:

(i) whether [2, 2] labelled square contains the wumpus.

(ii) whether [1, 3], [2, 2] and [3, 1] labeled squares contain pit.

(The labelling of the square is shown in figure 7(a)).

| | | | |
|:-:|:-:|:-:|:-:|
| 1,4 | 2,4 | 3,4 | 4,4 |
| 1,3 | 2,3 | 3,3 | 4,3 |
| 1,2 | 2,2 | 3,2 | 4,2 |
| 1,1 | 2,1 | 3,1 | 4,1 |
