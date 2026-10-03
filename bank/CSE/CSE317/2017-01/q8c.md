---
marks: 15
topics: [arc-consistency]
kind: analysis
source: {page: 41}
note: "(i) is printed as 'a directed arc x_i x_i -> x_j'; the domain is printed as '{v_1i,...,v_ni)'."
---
A binary CSP has a set $X = \{x_1, \ldots, x_n\}$ of variables, each having a domain $D_i = \{v_{1i}, \ldots, v_{ni})$ of values. In addition, a CSP has a set $C = \{C1, \ldots, Cm\}$ of constraints, each relating to a subset of $X$ and specifying the allowable combinations of assignments to the variables in that subset.

(i) Given a binary CSP, define what it means for a directed arc $x_i$ $x_i \to x_j$ between variables $x_i$ and $x_j$ to be arc consistent. Discuss how $x_i \to x_j$ can fail to be arc consistent. Explain how this can be solved.

(ii) Describe the AC-3 algorithm for enforcing arc consistency.

(iii) Prove that the time complexity of the AC-3 algorithm is $O(n^2 d^3)$, where $d$ is the size of the largest domain.
