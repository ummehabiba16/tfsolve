---
marks: 13
topics: [astar, greedy-best-first]
kind: analysis
source: {page: 37}
---
The heuristic path algorithm is a best-first search in which the evaluation function is $f(n) = (2-w)g(n) + wh(n)$. For what values of w, this algorithm is guaranteed to be optimal (you may assume that h is admissible). What kind of search does this perform for the following cases:

(i) w = 0 (ii) w = 1 (iii) w = 2
