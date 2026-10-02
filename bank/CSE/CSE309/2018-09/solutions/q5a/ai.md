---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Add a level above T in the same style: E -> T E' { E'.inh = T.val; E.val = E'.syn }; E' -> + T E1' { E1'.inh = E'.inh + T.val; E'.syn = E1'.syn }; E' -> - T E1' { E1'.inh = E'.inh - T.val; E'.syn = E1'.syn }; E' -> eps { E'.syn = E'.inh }; the T, T', F rules stay unchanged. Precedence of \\* over + and -, and left associativity, are preserved."
sources: ["KMS Chapter 5 slides 18-22 (Evaluating Inherited Attributes), 32-40 (L-attributed SDD)", "Dragon book 2e sec. 5.1.2 (Fig. 5.4), 5.2.4"]
---
**Idea.** The given SDD evaluates products with an inherited attribute: `T'.inh` carries the value of the product so far, left to right. Addition and subtraction have **lower** precedence, so they are handled by a new level **above** $T$ in exactly the same style. A nonterminal $E'$ carries the running sum/difference in `E'.inh`, and its operands are whole terms $T$. The grammar is not left recursive, so the SDD remains L-attributed and works top-down.

**Extended SDD:**

| | Production | Semantic rules |
|:-:|:--|:--|
| 1) | $E \to T\ E'$ | $E'.inh = T.val$ |
| | | $E.val = E'.syn$ |
| 2) | $E' \to +\ T\ E_1'$ | $E_1'.inh = E'.inh + T.val$ |
| | | $E'.syn = E_1'.syn$ |
| 3) | $E' \to -\ T\ E_1'$ | $E_1'.inh = E'.inh - T.val$ |
| | | $E'.syn = E_1'.syn$ |
| 4) | $E' \to \epsilon$ | $E'.syn = E'.inh$ |
| 5) | $T \to F\ T'$ | $T'.inh = F.val$ |
| | | $T.val = T'.syn$ |
| 6) | $T' \to *\ F\ T_1'$ | $T_1'.inh = T'.inh \times F.val$ |
| | | $T'.syn = T_1'.syn$ |
| 7) | $T' \to \epsilon$ | $T'.syn = T'.inh$ |
| 8) | $F \to \textbf{digit}$ | $F.val = \textbf{digit}.lexval$ |

(A start rule $L \to E\ \textbf{n}$ with $L.val = E.val$ can be added to print the result.)

**Why it is correct.**

- Each $T$ computes a complete product before it is added or subtracted, so `*` has higher precedence: `2+3*4` gives $2 + 12 = 14$, not 20.
- `E'.inh` accumulates **from the left**, so `-` is left-associative: `9-3-2` gives $(9-3)-2 = 4$. In $E' \to - T E_1'$, the new running value is `E'.inh - T.val`, and the final value is passed up unchanged through `syn`.
- Any number of `+`, `-` and `*` operators can appear: $E'$ repeats for each additive operator, and $T'$ for each `*`.
