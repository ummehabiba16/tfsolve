---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Most constrained variable (MRV) = fail-first: assign the variable most likely to cause failure first, so dead ends are found early and the tree is pruned. Least constraining value = fail-last: since only one solution is needed, try the value that leaves the most options for other variables."
sources: ["AIMA 3e sec. 6.3.1"]
---
**Variable ordering: most constrained (MRV).** Every variable must be assigned eventually, so the variable order does not affect which solutions exist, only the size of the search tree. Choosing the variable with the fewest legal values first is **fail-first**: if the current partial assignment cannot be completed, this variable is the most likely to reveal it. Failures are detected at shallow depth, so large subtrees are pruned. If a variable has no legal values left, it is chosen immediately and the search backtracks at once.

**Value ordering: least constraining.** For a chosen variable, the order of values matters only for how fast we find **one** solution. Trying first the value that rules out the fewest values in the neighbours' domains is **fail-last**: it leaves maximum flexibility for the remaining variables, so the first value tried is the one most likely to lead to a solution, and backtracking is minimised.

Example (Australia map colouring, WA = red, NT = green): MRV picks SA (only blue remains) before V (three colours). For Q, red leaves SA with blue, while blue leaves SA with nothing; LCV tries red first.
