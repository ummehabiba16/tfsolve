---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "The grammar is unambiguous (it is SLR(1) with no conflicts, so each string has a unique parse tree); it generates a (single a) or parenthesised, non-empty, comma-separated lists whose elements are again such strings. The leftmost and rightmost derivations of ((a,a),a,(a)) are given step by step."
sources: ["MMA syntax analysis slides on derivations and ambiguity", "Dragon book 2e sec. 4.2.2-4.2.5"]
---
Grammar: $S \to (L) \mid a$, $L \to L, S \mid S$. String: $((a, a), a, (a))$.

**(i) Leftmost derivation** (always expand the leftmost nonterminal):

```text
S => ( L )
  => ( L , S )
  => ( L , S , S )
  => ( S , S , S )
  => ( ( L ) , S , S )
  => ( ( L , S ) , S , S )
  => ( ( S , S ) , S , S )
  => ( ( a , S ) , S , S )
  => ( ( a , a ) , S , S )
  => ( ( a , a ) , a , S )
  => ( ( a , a ) , a , ( L ) )
  => ( ( a , a ) , a , ( S ) )
  => ( ( a , a ) , a , ( a ) )
```

**(ii) Rightmost derivation** (always expand the rightmost nonterminal):

```text
S => ( L )
  => ( L , S )
  => ( L , ( L ) )
  => ( L , ( S ) )
  => ( L , ( a ) )
  => ( L , S , ( a ) )
  => ( L , a , ( a ) )
  => ( S , a , ( a ) )
  => ( ( L ) , a , ( a ) )
  => ( ( L , S ) , a , ( a ) )
  => ( ( L , a ) , a , ( a ) )
  => ( ( S , a ) , a , ( a ) )
  => ( ( a , a ) , a , ( a ) )
```

**(iii) Ambiguous or unambiguous? Unambiguous.** A grammar is ambiguous if some string has two different parse trees (equivalently two leftmost derivations). Here:

- Each $S$ is either `a` or a parenthesised $L$; the first symbol of the string, `a` or `(`, decides.
- The list $L \to L, S \mid S$ is **left recursive in the only possible way**: a list of $n$ elements $S_1, \ldots, S_n$ has exactly one tree, $((S_1, S_2), S_3)\ldots$ ; the last comma of a list is always the one that belongs to the topmost $L$, and the elements between commas are separated unambiguously because nested lists are enclosed in matching parentheses.
- Formally, the grammar is **SLR(1)** (the SLR table has no conflicts), and every LR grammar is unambiguous.

Both derivations above correspond to the same unique parse tree, as they must.

**(iv) The language.** $L(G)$ consists of the string `a` and all strings `(` $x_1, x_2, \ldots, x_n$ `)` with $n \ge 1$ in which every $x_i$ is again a string of $L(G)$: **nested, parenthesised, comma-separated lists whose atoms are `a`** (like Lisp S-expressions without the empty list). Examples: `a`, `(a)`, `(a, a)`, `((a), a)`, `((a, a), a, (a))`. Parentheses are balanced, lists are never empty, and commas appear only between two elements of a list.

*Check:* an SLR(1) table for the grammar has no conflicts and accepts the string; the derivations were generated from its parse tree by a script.
