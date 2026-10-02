---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Augment with E' -> E. I0 = closure([E' -> .E, end]) = {[E'->.E, end], [E->.E+T, end/+], [E->.T, end/+], [T->.T\\*F, end/+/\\*], [T->.F, end/+/\\*], [F->.id, end/+/\\*]}."
sources: ["MMA syntax analysis slides 441-478 (Constructing LR(1) Sets of Items)", "Dragon book 2e sec. 4.7.2 (Fig. 4.40 CLOSURE)"]
---
**Augmented grammar:**

$$E' \to E$$

$$E \to E + T \mid T$$

$$T \to T * F \mid F$$

$$F \to \textbf{id}$$

**Closure rule for LR(1) items:** for each item $[A \to \alpha \cdot B\beta, a]$ in the set, each production $B \to \gamma$, and each terminal $b \in$ FIRST($\beta a$), add $[B \to \cdot\gamma, b]$.

$I_0$ = CLOSURE($\{[E' \to \cdot E, \$]\}$):

1. $[E' \to \cdot E, \$]$: $\beta = \epsilon$, so FIRST(\$) = {\$}. Add $[E \to \cdot E + T, \$]$ and $[E \to \cdot T, \$]$.
2. $[E \to \cdot E + T, \$]$: $\beta = +T$, so FIRST($+T$ \$) = {+}. Add $[E \to \cdot E + T, +]$ and $[E \to \cdot T, +]$. (Repeating with lookahead + adds nothing new.)
3. $[E \to \cdot T, \$/+]$: $\beta = \epsilon$, so the lookaheads are \$ and +. Add $[T \to \cdot T * F, \$/+]$ and $[T \to \cdot F, \$/+]$.
4. $[T \to \cdot T * F, \ldots]$: FIRST($*F\ldots$) = {\*}. Add $[T \to \cdot T * F, *]$ and $[T \to \cdot F, *]$.
5. $[T \to \cdot F, \$/+/*]$: add $[F \to \cdot\textbf{id}, \$/+/*]$.
6. Nothing more can be added.

$$I_0:\ [E' \to \cdot E,\ \$]$$

$$[E \to \cdot E + T,\ \$/+] \qquad [E \to \cdot T,\ \$/+]$$

$$[T \to \cdot T * F,\ \$/+/*] \qquad [T \to \cdot F,\ \$/+/*]$$

$$[F \to \cdot \textbf{id},\ \$/+/*]$$

Written out in full, that is 1 + 2 + 2 + 3 + 3 + 3 = **14 items** ($a/b$ is shorthand for two items with the same core).
