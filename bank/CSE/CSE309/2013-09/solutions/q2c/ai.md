---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Recursive-descent parsing is top-down parsing with a set of (mutually recursive) procedures, one for each nonterminal, that executes the productions by calling procedures and matching terminals. It does not work for left-recursive grammars (infinite recursion), and for grammars that are not left-factored or need more lookahead it needs backtracking (and may be exponential or give wrong results without it)."
sources: ["MMA syntax analysis slides 70-75 (recursive-descent parsing)", "Dragon book 2e sec. 4.4.1"]
---
**Recursive-descent parsing.** A top-down method in which the parser consists of a set of **procedures, one for each nonterminal**. The procedure for $A$ chooses a production $A \to X_1 X_2 \cdots X_k$ and executes its body from left to right: for a nonterminal $X_i$ it **calls the procedure** of $X_i$, for a terminal $X_i$ it checks that it equals the current input symbol and advances (Dragon book sec. 4.4.1). The call sequence traces out a leftmost derivation and the parse tree. If the choice of production is made by lookahead and never undone, the parser is *predictive*; otherwise it uses **backtracking**.

```c
void E() { T(); while (lookahead == '+') { match('+'); T(); } }
```

**When does it not work?**

1. **Left-recursive grammars.** For $E \to E + T \mid T$ the procedure `E` would call `E` first, without consuming any input, so it **recurses forever** (stack overflow). The left recursion (immediate or indirect) must be eliminated first.

```c
void E() { E(); match('+'); T(); }     /* never terminates */
```

2. **Grammars that are not left-factored / need more than one lookahead symbol.** For $S \to ab\,c \mid ab\,d$ (or $A \to \alpha\beta_1 \mid \alpha\beta_2$) the parser cannot know which alternative to use. With backtracking it tries the first, and on failure it **undoes** the input consumed and tries the next, which can take **exponential time**; without backtracking it may pick the wrong production and reject a valid string.
3. **Ambiguous grammars** give more than one parse and a deterministic choice cannot represent both.
4. Productions with $\epsilon$ alternatives need $\text{FOLLOW}$ information to decide when to use them; otherwise the parser may wrongly succeed or fail.

For LL(1) grammars (no left recursion, left-factored, with disjoint predictions) recursive descent works without backtracking.
