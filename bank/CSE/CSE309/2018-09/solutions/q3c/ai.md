---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "For S -> Sa the procedure S() first calls S() without consuming input, so the lookahead never changes and it recurses forever (and FIRST(Sa) contains FIRST of the other alternatives, so no predictive choice). S -> aSa is fine: the a is matched first, so every recursive call consumes input and terminates, and FIRST(aSa) = {a} (it is right/centre recursion, not left recursion)."
sources: ["MMA basic concepts of parsing slides 50-56 (Left Recursion)", "Dragon book 2e sec. 2.4.5"]
---
**Why $S \to Sa$ is unsuitable (6 marks).** The recursive-descent procedure for $S$ follows the body from left to right:

```c
void S() {
    S();          /* S -> S a : first symbol is S itself */
    match('a');
}
```

1. The first action of `S()` is to call `S()` again, **without consuming any input**. The lookahead is unchanged, so the same decision is made again, and again. The recursion never ends (stack overflow), and `match('a')` is never reached.
2. With other alternatives, e.g. $S \to Sa \mid b$, every string from $S$ starts with $b$. So FIRST($Sa$) = FIRST($b$) = {b}, and the lookahead cannot choose. A left-recursive grammar is never LL(1).

The fix is to rewrite it as $S \to bS'$, $S' \to aS' \mid \epsilon$.

**What about $S \to aSa$? (4 marks)** This is **not** left recursive; the recursion is in the middle.

```c
void S() {
    if (lookahead == 'a') {
        match('a');   /* consumes one input symbol first */
        S();
        match('a');
    } else ...        /* other alternative(s) of S */
}
```

- Before the recursive call, an `a` is **matched**, so each nested call starts further along the input. The depth of recursion is bounded by the input length, and the parser terminates.
- FIRST($aSa$) = {a}. As long as the other alternatives of $S$ do not start with `a`, the choice is predictive.

So $S \to aSa$ works well with recursive descent. Only recursion as the *first* symbol of a body (left recursion) causes the problem.
