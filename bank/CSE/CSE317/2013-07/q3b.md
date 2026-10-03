---
marks: 18
topics: [propositional-logic]
kind: analysis
source: {page: 56}
set_by: [UNKNOWN]
---
Consider the problem of "wumpus world". Wumpus world is represented by a $4\times4$ grid. Initially the agent is at [1, 1]. There is one wumpus in one of the 16 squares except [1, 1]. Three of the squares except [1, 1] contain three pits. The positions of wumpus and pits are randomly distributed, however wumpus does not live in a square where there is a pit. Squares adjacent to wumpus are smelly and adjacent to pits are breezy.

At [1, 1], the agent perceives neither stench nor breeze. Agent moves to [2, 1] where it perceives both stench and breeze. When it returns to [1, 1] and thereafter moves to [1, 2], it perceives both stench and breeze.

From the initial knowledge base entail the following conclusions with the help of propositional logic.

(i) whether [2, 2] labelled square contains the wumpus.

(ii) whether [1, 3], [2, 2] and [3, 1] labeled squares contain pit.

(The grid of the problem is given as follows)

| | | | |
|:-:|:-:|:-:|:-:|
| 1,4 | 2,4 | 3,4 | 4,4 |
| 1,3 | 2,3 | 3,3 | 4,3 |
| 1,2 | 2,2 | 3,2 | 4,2 |
| 1,1 | 2,1 | 3,1 | 4,1 |
