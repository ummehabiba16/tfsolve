---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Variables Q1..Q8 (queen in column i); domain {1..8} = row; constraints for i != j: Qi != Qj (different rows) and |Qi - Qj| != |i - j| (different diagonals); columns differ by construction. Solve with backtracking + MRV/forward checking or min-conflicts."
sources: ["AIMA 3e sec. 6.1 and 6.4"]
---
**Formulation.** Since each column must contain exactly one queen, use one variable per column:

- **Variables**: $Q_1,\dots,Q_8$, where $Q_i$ is the row of the queen in column $i$.

- **Domains**: $D_i=\{1,2,\dots,8\}$.

- **Constraints** (binary, for every pair $i<j$):

- not in the same row: $Q_i\ne Q_j$;

- not on the same diagonal: $|Q_i-Q_j|\ne|i-j|$.

(Columns are different by construction.) The constraint graph is complete: 28 binary constraints.

**Solving.** Backtracking search assigns $Q_1,Q_2,\dots$ in turn, using forward checking to delete attacked rows from the domains of later columns and MRV to choose the most constrained column; or **min-conflicts** local search: start with all 8 queens placed, repeatedly move a queen that is attacked to the row in its column with the fewest attacks. One solution: $(Q_1,\dots,Q_8)=(1,5,8,6,3,7,2,4)$.
