---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "After assigning X, forward checking deletes from each unassigned neighbour's domain the values inconsistent with X; if a domain becomes empty it backtracks immediately. Example: Australia map colouring, WA = red, Q = green leaves NT and SA only blue; V = blue empties SA, so the failure is found at once."
sources: ["AIMA 3e sec. 6.3.2 (Figure 6.7)"]
---
**Forward checking.** Whenever a variable $X$ is assigned a value during backtracking search, for each **unassigned** variable $Y$ connected to $X$ by a constraint, delete from $D_Y$ every value inconsistent with the value of $X$. If some domain becomes **empty**, the current partial assignment cannot be completed: backtrack immediately (undo the deletions).

**Example: Australia map colouring** (colours R, G, B; neighbours must differ; WA-NT, WA-SA, NT-SA, NT-Q, SA-Q, SA-NSW, SA-V, Q-NSW, NSW-V; T isolated).

| Step | WA | NT | Q | NSW | V | SA | T |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| Initial | RGB | RGB | RGB | RGB | RGB | RGB | RGB |
| WA = R | **R** | GB | RGB | RGB | RGB | GB | RGB |
| Q = G | **R** | B | **G** | RB | RGB | B | RGB |
| V = B | **R** | B | **G** | R | **B** | (empty) | RGB |

After WA = R, red is removed from NT and SA. After Q = G, green is removed from NT, NSW and SA, leaving NT = {B}, SA = {B}. After V = B, blue is removed from NSW and SA, so SA's domain is empty: forward checking detects the failure **now**, without ever trying to assign NT, NSW, SA; the search backtracks and tries another value for V (V = R).

**Benefits.** It detects failures earlier than plain backtracking, combines naturally with the MRV heuristic (the reduced domain sizes are exactly what MRV needs), and is cheap. Limitation: it only checks constraints between the assigned variable and its neighbours, so it does not notice that NT and SA both having only {B} is already inconsistent; arc consistency (MAC) would.
