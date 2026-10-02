---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Using the LL(1) table (M[E,id] = M[E,(] = E -> TE'; M[E',+] = E' -> +TE'; M[E',)] = M[E',END] = E' -> eps; M[T,id] = M[T,(] = T -> FT'; M[T',\\*] = T' -> \\*FT'; M[T',+] = M[T',)] = M[T',END] = T' -> eps; M[F,id] = F -> id; M[F,(] = F -> (E)), the parser makes 17 moves: E -> TE', T -> FT', F -> id, match id, T' -> eps, E' -> +TE', match +, T -> FT', F -> id, match id, T' -> \\*FT', match \\*, F -> id, match id, T' -> eps, E' -> eps, accept."
sources: ["MMA syntax analysis slides 112-151 (Predictive Parsing Table, Nonrecursive Predictive Parsing)", "Dragon book 2e sec. 4.4.4 (Example 4.35, Fig. 4.21)"]
---
**FIRST and FOLLOW:**

| Nonterminal | FIRST | FOLLOW |
|:-:|:--|:--|
| $E$ | (, id | ), \$ |
| $E'$ | +, $\epsilon$ | ), \$ |
| $T$ | (, id | +, ), \$ |
| $T'$ | \*, $\epsilon$ | +, ), \$ |
| $F$ | (, id | +, \*, ), \$ |

**Predictive parsing table $M$:**

| | id | + | \* | ( | ) | \$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| $E$ | $E \to TE'$ | | | $E \to TE'$ | | |
| $E'$ | | $E' \to +TE'$ | | | $E' \to \epsilon$ | $E' \to \epsilon$ |
| $T$ | $T \to FT'$ | | | $T \to FT'$ | | |
| $T'$ | | $T' \to \epsilon$ | $T' \to *FT'$ | | $T' \to \epsilon$ | $T' \to \epsilon$ |
| $F$ | $F \to \textbf{id}$ | | | $F \to (E)$ | | |

**Moves on `id + id * id`** (stack shown with its top at the left):

| Matched | Stack | Input | Action |
|:--|:--|--:|:--|
| | $E$\$ | id + id \* id \$ | output $E \to TE'$ |
| | $TE'$\$ | id + id \* id \$ | output $T \to FT'$ |
| | $FT'E'$\$ | id + id \* id \$ | output $F \to \textbf{id}$ |
| | id $T'E'$\$ | id + id \* id \$ | match id |
| id | $T'E'$\$ | + id \* id \$ | output $T' \to \epsilon$ |
| id | $E'$\$ | + id \* id \$ | output $E' \to +TE'$ |
| id | $+TE'$\$ | + id \* id \$ | match + |
| id + | $TE'$\$ | id \* id \$ | output $T \to FT'$ |
| id + | $FT'E'$\$ | id \* id \$ | output $F \to \textbf{id}$ |
| id + | id $T'E'$\$ | id \* id \$ | match id |
| id + id | $T'E'$\$ | \* id \$ | output $T' \to *FT'$ |
| id + id | $*FT'E'$\$ | \* id \$ | match \* |
| id + id \* | $FT'E'$\$ | id \$ | output $F \to \textbf{id}$ |
| id + id \* | id $T'E'$\$ | id \$ | match id |
| id + id \* id | $T'E'$\$ | \$ | output $T' \to \epsilon$ |
| id + id \* id | $E'$\$ | \$ | output $E' \to \epsilon$ |
| id + id \* id | \$ | \$ | **accept** |

The productions output, in order, form the leftmost derivation of `id + id * id`.
