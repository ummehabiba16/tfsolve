---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "LL(k): a grammar that can be parsed by scanning the input left to right, producing a leftmost derivation, with k symbols of lookahead to choose each production. Recursive-descent parser: a set of recursive procedures, one per nonterminal, that parses top-down (with backtracking in general, predictive if the grammar is LL(1)). Lexeme: the sequence of source characters matched by the pattern of a token."
sources: ["MMA syntax analysis slides 70-123; lexical analysis slides 17-28", "Dragon book 2e sec. 3.1.2, 4.4.1, 4.4.3"]
---
**(i) LL($k$) grammar.** A grammar that can be parsed top-down by a predictive parser that reads the input **L**eft to right, builds a **L**eftmost derivation, and uses **$k$ symbols of lookahead** to decide which production to apply (Dragon book sec. 4.4.3). Formally, for any two different productions $A \to \alpha \mid \beta$ and any derivation $S \Rightarrow^* wA\gamma$, the first $k$ symbols of what $\alpha\gamma$ and $\beta\gamma$ derive must differ. For $k = 1$ (LL(1)): $\text{FIRST}(\alpha)$ and $\text{FIRST}(\beta)$ are disjoint, and if $\beta \Rightarrow^* \epsilon$, then $\text{FIRST}(\alpha) \cap \text{FOLLOW}(A) = \emptyset$. An LL($k$) grammar is neither ambiguous nor left recursive. Example: $S \to aS \mid b$ is LL(1).

**(ii) Recursive-descent parser.** A top-down parser consisting of a set of **(mutually) recursive procedures, one for each nonterminal**; the procedure for $A$ chooses a production, and for the symbols of its body calls the procedure of each nonterminal and matches each terminal with the input (Dragon book sec. 4.4.1). The general form may need **backtracking** (try one production, undo and try another on failure); if the grammar is LL(1), the lookahead symbol selects the production and the parser is **predictive** (no backtracking).

```c
void S() {                      /* S -> a S | b */
    if (lookahead == 'a') { match('a'); S(); }
    else if (lookahead == 'b') match('b');
    else error();
}
```

**(iii) Lexeme.** A **lexeme** is a sequence of characters in the source program that matches the *pattern* for a token and is identified by the lexical analyzer as an instance of that token (Dragon book sec. 3.1.2). Example: in `count = rate * 60;` the characters `count` and `rate` are lexemes of the token `id`, `=` is a lexeme of the assignment token, `60` a lexeme of the token `number`.
