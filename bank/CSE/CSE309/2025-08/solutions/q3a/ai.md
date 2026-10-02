---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "(i) S -> S(S)S | eps is left recursive, so S() would call itself forever; rewrite as S -> (S)S | eps (same balanced-parentheses language) and code S(){ if (la=='(') {match('(');S();match(')');S();} }. (ii) Left factor S -> 0 S'', S'' -> S 1 | 1 and code S(){match('0'); if(la=='0'){S();match('1');} else match('1');}."
sources: ["MMA basic concepts of parsing slides 23-56 (Predictive Parsing, Left Recursion)", "Dragon book 2e sec. 2.4.2-2.4.5, 4.4.1"]
---
A procedure-based (recursive-descent) parser has one procedure per nonterminal. It uses the lookahead token `la` to choose a production, and `match(t)` checks that `la == t` and advances.

```c
void match(int t) {
    if (la == t) la = nextToken();
    else error();
}
```

**(i) $S \to S(S)S \mid \epsilon$**

Written directly, the procedure would be

```c
void S() { S(); match('('); S(); match(')'); S(); }   /* or nothing for eps */
```

The first action is to call `S()` again **without consuming input**, so it recurses forever. The grammar is left recursive and must be transformed first.

Eliminating left recursion with $A \to A\alpha \mid \beta$, where $\alpha = (S)S$ and $\beta = \epsilon$:

$$S \to S', \qquad S' \to (S)S\,S' \mid \epsilon$$

Both generate balanced parentheses. The equivalent and simpler grammar is

$$S \to (\,S\,)\,S \mid \epsilon$$

FIRST($(S)S$) = { ( } and FOLLOW($S$) = { ), \$ }, which are disjoint, so the parser chooses on `la`:

```c
void S() {
    if (la == '(') {          /* S -> ( S ) S */
        match('('); S(); match(')'); S();
    }
    /* else S -> eps: do nothing; la must be ')' or '$' */
}
```

**(ii) $S \to 0S1 \mid 01$**

Both alternatives start with `0`, so one lookahead symbol cannot choose between them. Left factor:

$$S \to 0\,R$$

$$R \to S\,1 \mid 1$$

FIRST($S1$) = { 0 } and FIRST($1$) = { 1 }, so the grammar is LL(1):

```c
void S() {
    match('0');
    R();
}

void R() {
    if (la == '0') { S(); match('1'); }   /* R -> S 1 */
    else if (la == '1') match('1');       /* R -> 1   */
    else error();
}
```

or, inlining `R` into `S`:

```c
void S() {
    match('0');
    if (la == '0') S();
    match('1');
}
```

The main program calls `S()` and then checks that `la == '$'`. For example, on `0011`: `S` matches 0, sees 0 and calls `S`, which matches 0, sees 1 and matches 1; back in the outer `S`, it matches 1, then `$`: accepted.
