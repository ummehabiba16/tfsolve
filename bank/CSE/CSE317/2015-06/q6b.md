---
marks: 18
topics: [propositional-logic]
kind: analysis
source: {page: 47}
note: "'There is one Wumpus is one of the 16 squares', 'proof the following propositions' and '[2. 1]' are printed so."
---
Consider the problem of "Wumpus World". Wumpus world is represented by $4\times4$ grid. Initially the agent is at [1,1]. There is one Wumpus is one of the 16 squares except [1,1]. There are four pits in the squares except [1,1]. The position of Wumpus and Pits are randomly distributed, but Wumpus cannot live in a square containing pit. Squares adjacent to Wumpus are smelly and adjacent to pits are breezy. The grid is shown below.

| | | | |
|:-:|:-:|:-:|:-:|
| 1,4 | 2,4 | 3,4 | 4,4 |
| 1,3 | 2,3 | 3,3 | 4,3 |
| 1,2 | 2,2 | 3,2 | 4,2 |
| 1,1 | 2,1 | 3,1 | 4,1 |

At [1,1], the agent perceives neither breeze nor stench. Then the agent moves to [2. 1] where it perceives only breeze but no stench. Then the agent moves to [1,2] (via [1,1]) where it perceive neither breeze nor stench. Then the agent moves to [1,3] where it perceives both stench and breeze.

Now can you proof the following propositions using the resolution algorithm? You only need to incorporate the clauses that you need to proof the following proposition.

(i) [2,2] contains no pit.

(ii) [3,1] contains a pit

(iii) [1,4] contains the Wumpus.
