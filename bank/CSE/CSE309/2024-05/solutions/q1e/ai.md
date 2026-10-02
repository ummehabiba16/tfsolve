---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Procedures E() { E(); match('+'); F(); ... } and F() { if NUM match(NUM) else { match(ID); match('('); E(); match(')'); } }; flaw: E is left recursive, so E() calls itself without consuming input and recurses forever (stack overflow); also all three E alternatives start with NUM/ID, so one lookahead cannot choose."
sources: ["MMA basic concepts of parsing slides 23-56 (Predictive Parsing, Left Recursion)", "Dragon book 2e sec. 2.4.2, 2.4.5"]
---
One procedure per nonterminal, keeping the grammar exactly as given. `lookahead` holds the current token and `match(t)` checks and advances.

```c
void match(int t) {
    if (lookahead == t) lookahead = nextToken();
    else error();
}

void E() {
    /* E -> E + F | E - F | F : FIRST of every alternative is {NUM, ID} */
    if (lookahead == NUM || lookahead == ID) {
        E();                         /* E -> E + F  (or E - F) */
        if (lookahead == '+') { match('+'); F(); }
        else if (lookahead == '-') { match('-'); F(); }
        /* E -> F would also be possible here */
    }
    else error();
}

void F() {
    if (lookahead == NUM) match(NUM);          /* F -> NUM   */
    else if (lookahead == ID) {                /* F -> ID(E) */
        match(ID); match('('); E(); match(')');
    }
    else error();
}
```

**Flaws:**

1. **Infinite recursion.** $E \to E + F$ is left recursive. `E()` calls `E()` as its first action without consuming any input, so the lookahead never changes and the parser recurses until the stack overflows. A procedure-based predictive parser cannot work with a left-recursive grammar.
2. **No unique choice.** FIRST($E + F$) = FIRST($E - F$) = FIRST($F$) = {NUM, ID}. One lookahead symbol cannot decide which alternative of $E$ to use, so the grammar is not LL(1) and the parser would have to backtrack.

`F()` itself is fine (NUM and ID distinguish its alternatives). The fix is to eliminate the left recursion: $E \to F E'$, $E' \to + F E' \mid - F E' \mid \epsilon$.
