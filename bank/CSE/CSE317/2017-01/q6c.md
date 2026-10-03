---
marks: 10
topics: [heuristics]
kind: analysis
source: {page: 40}
---
Assume two heuristic functions $h_1$ and $h_2$, both of which are admissible and applicable to your problem. It has been recommended that you should try to combine them to make a more general heuristic function $h$, which can be defined as

$$h(s) = \alpha_1 h_1(s) + \alpha_2 h_2(s)$$

Here $s$ denotes any state in the search problem, and the constants $\alpha_1$ and $\alpha_2$ are constrained such that they are non-negative and $\alpha_1 + \alpha_2 = 1$. Is the function $h$ always admissible? Justify your answer with a specific example.
