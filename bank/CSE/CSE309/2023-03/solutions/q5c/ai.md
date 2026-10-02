---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Example: D -> T { L.inh = T.type } L; T -> int { T.type = integer }; T -> float { T.type = float }; L -> L1 , id { L1.inh = L.inh; addType(id.entry, L.inh) }; L -> id { addType(id.entry, L.inh) }, which is L-attributed and left recursive (LR, not LL). Not every LR grammar with an L-attributed SDD can be handled bottom up: an inherited attribute must be computed before its nonterminal is parsed, which in a bottom-up parser needs a marker reduction, but an LR parser may not yet know which production it is in; markers can create conflicts (an LR grammar can become non-LR). It always works for L-attributed SDDs on LL grammars."
sources: ["KMS Chapter 5 slides 32-40, 76-80 (L-attributed SDD, L-Attributed SDDs and LL Parsing, L-Attributed SDDs on LR Grammars)", "Dragon book 2e sec. 5.2.4, 5.5.4"]
---
**Example of an L-attributed SDD on an LR grammar (6 marks).** The textbook's declaration SDD:

| Production | Semantic rules |
|:--|:--|
| $D \to T\ L$ | $L.inh = T.type$ |
| $T \to \textbf{int}$ | $T.type = integer$ |
| $T \to \textbf{float}$ | $T.type = float$ |
| $L \to L_1\ ,\ \textbf{id}$ | $L_1.inh = L.inh$; $addType(\textbf{id}.entry, L.inh)$ |
| $L \to \textbf{id}$ | $addType(\textbf{id}.entry, L.inh)$ |

- It is **L-attributed**: the only inherited attributes, $L.inh$ and $L_1.inh$, depend on a left sibling ($T.type$) or on the parent ($L.inh$).
- The grammar is **left recursive** ($L \to L_1 , \textbf{id}$), so it is LR (in fact SLR) but not LL.
- Here bottom-up evaluation works by a trick: when $L \to \textbf{id}$ or $L \to L_1 , \textbf{id}$ is reduced, $T$ (with $T.type$) is always just below the $L$-part on the parser stack, so the action can read it at a fixed stack position.

**Can every LR grammar with an L-attributed SDD be handled bottom up? No (8 marks).** Intuitive argument:

1. In an L-attributed SDD, the inherited attributes of a nonterminal $B$ must be computed **before** $B$ is parsed (they are needed while parsing $B$). In a bottom-up parser, the only way to run an action at that point is to insert a **marker nonterminal** $M \to \epsilon$ just before $B$ and do the action when $M$ is reduced.
2. To reduce $M$, the parser must already know **which production** it is in at that point, because the action belongs to one particular production. A top-down (LL) parser knows the production as soon as it starts it. An LR parser, however, may still be working on several productions with a common prefix and decides only at the final reduction, which is the strength of LR parsing.
3. If two productions with a common prefix need different marker actions there, the parser cannot choose which marker to reduce. The modified grammar has a reduce/reduce or shift/reduce conflict, so it is no longer LR. Example: $A \to X\ B \mid X\ C$, where $B$ needs `B.i = f(X.s)` and $C$ needs `C.i = g(X.s)`: after $X$, the markers $M_1$ (for $B$) and $M_2$ (for $C$) would both have to be reduced on the same lookahead.
4. Only when the inherited values can be found at a known place on the stack (as in the example above) can the action be postponed without markers. That does not hold in general.

Positive result (textbook): **any L-attributed SDD on an LL grammar** can be implemented bottom up, because inserting markers into an LL grammar keeps it LR. The class "L-attributed SDD on an LR grammar" as a whole cannot.
