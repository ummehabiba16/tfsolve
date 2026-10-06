---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Context-sensitive analysis is the semantic analysis that checks properties a context-free grammar cannot (declaration before use, types, scope), done with syntax-directed definitions. An S-attributed definition uses only synthesized attributes (E -> E1 + T { E.val = E1.val + T.val }); an L-attributed one also allows inherited attributes that depend only on the parent and left siblings (D -> T L { L.inh = T.type })."
sources: ["KMS Chapter 5 slides 6-40 (SDDs, S-attributed and L-attributed)", "Dragon book 2e sec. 1.2.3, 5.1, 5.2.3-5.2.4"]
---
**Context-sensitive analysis.** Syntax analysis uses a **context-free** grammar, which says whether the tokens are arranged correctly but cannot express rules that depend on the *context* of a construct: a variable must be declared before it is used, an identifier cannot be declared twice in a scope, operands must have compatible types, a function call must have the right number and types of arguments. These checks need information from other parts of the program (the symbol table, types), so they are called **context-sensitive analysis**, i.e. **semantic analysis** (Dragon book sec. 1.2.3).

**Purpose.** (1) To check the program for semantic consistency with the language definition (declarations, types, scope, return types) and report errors; (2) to **gather type information** (and perform coercions) and save it in the syntax tree or symbol table for the intermediate-code and code generation phases. It is specified and implemented with **syntax-directed definitions**: a context-free grammar with attributes attached to the grammar symbols and semantic rules.

**S-attributed definition.** An SDD in which **every attribute is synthesized**: each attribute of the head is computed from attributes of the body symbols. It can be evaluated in one **bottom-up** pass, e.g. during LR parsing (Dragon book sec. 5.2.3).

| Production | Semantic rule |
|:--|:--|
| $L \to E\ \textbf{n}$ | $L.val = E.val$ |
| $E \to E_1 + T$ | $E.val = E_1.val + T.val$ |
| $E \to T$ | $E.val = T.val$ |
| $T \to T_1 * F$ | $T.val = T_1.val \times F.val$ |
| $F \to \textbf{digit}$ | $F.val = \textbf{digit}.lexval$ |

**L-attributed definition.** An SDD in which each attribute is either synthesized or **inherited** such that an inherited attribute of $X_i$ in $A \to X_1 \cdots X_n$ depends only on (a) inherited attributes of $A$, (b) attributes of $X_1, \ldots, X_{i-1}$ (the symbols to the left), (c) attributes of $X_i$ itself without cycles. It can be evaluated in one **left-to-right depth-first** pass (Dragon book sec. 5.2.4). Every S-attributed SDD is also L-attributed.

| Production | Semantic rule |
|:--|:--|
| $D \to T\ L$ | $L.inh = T.type$ |
| $T \to \textbf{int}$ | $T.type = integer$ |
| $T \to \textbf{float}$ | $T.type = float$ |
| $L \to L_1\ ,\ \textbf{id}$ | $L_1.inh = L.inh;\ addType(\textbf{id}.entry, L.inh)$ |
| $L \to \textbf{id}$ | $addType(\textbf{id}.entry, L.inh)$ |

Here the inherited attribute $L.inh$ carries the type from $T$ (a left sibling) to the identifiers, so the SDD is L-attributed but **not** S-attributed.
