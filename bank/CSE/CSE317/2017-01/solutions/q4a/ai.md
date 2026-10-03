---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Simple model checking (TT-ENTAILS) enumerates all 2^n models. DPLL (a backtracking search on CNF) adds early termination (a clause is true if any literal is true; the sentence is false if any clause is false), the pure-symbol heuristic and the unit-clause heuristic (unit propagation). Scale-up tricks: component analysis, variable and value ordering (degree heuristic), intelligent backtracking (conflict-clause learning), random restarts, and clever indexing (watched literals)."
sources: ["AIMA 3e sec. 7.6.1 (DPLL algorithm and its improvements)"]
---
**Simple model checking** (TT-ENTAILS / TT-CHECK-ALL) enumerates all $2^n$ complete truth assignments and evaluates the sentence in each. It is exponential, even when the answer could be found early.

**DPLL** (Davis-Putnam-Logemann-Loveland) is a recursive, depth-first enumeration of **partial** models of a CNF sentence, with three improvements:

1. **Early termination:** a clause is true as soon as **any** of its literals is true, and the whole sentence is false as soon as **any** clause is false, even when other symbols are unassigned. Large subtrees are skipped.
2. **Pure symbol heuristic:** a symbol that appears with the same sign in all remaining clauses (e.g. only positive) can be set to make those literals true. This never hurts satisfiability.
3. **Unit clause heuristic:** a clause with only one unassigned literal (and the others false) forces that literal's value. Assigning it can create new unit clauses, a cascade called **unit propagation**, which is like forward chaining.

**Scaling up to large problems** (SAT solvers handling millions of variables):

- **Component analysis:** split the clauses into disjoint components with no shared unassigned variables, and solve each separately.
- **Variable and value ordering:** choose the variable that appears most often (degree heuristic), and try the value that satisfies the most clauses first.
- **Intelligent backtracking:** on a conflict, analyse the cause, **learn a conflict clause** to avoid repeating it, and backjump directly to the relevant decision (CDCL).
- **Random restarts:** restart the search with different random choices (keeping the learned clauses) when progress stalls.
- **Clever indexing:** data structures such as *watched literals* find unit clauses quickly without scanning every clause.
