---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "For A -> A alpha the procedure A() starts by calling A() without consuming input, so the lookahead never changes and A() recurses forever (stack overflow); also FIRST(A alpha) contains FIRST(beta) of the other alternative, so the lookahead cannot choose. Remove it first: A -> beta A', A' -> alpha A' | eps."
sources: ["MMA basic concepts of parsing slides 50-56 (Left Recursion)", "Dragon book 2e sec. 2.4.5, 4.3.3"]
---
In a procedure-based predictive parser, each nonterminal $A$ has a procedure that chooses a production by the lookahead and then, for each body symbol, calls that symbol's procedure or matches a terminal.

Take $A \to A\alpha \mid \beta$, e.g. $expr \to expr + term \mid term$:

```c
void expr() {
    if (/* choose expr -> expr + term */) {
        expr();          /* first action: call itself */
        match('+');
        term();
    } else term();
}
```

**1. Infinite recursion.** The body $A\alpha$ begins with $A$, so the first thing `expr()` does is call `expr()` again. No input has been consumed and the lookahead has not changed. The same choice is made again and again, so the procedure loops forever (until the stack overflows) and never reaches `match('+')`.

**2. No predictive choice.** Every string derived from $A$ starts with a string derived from $\beta$, so FIRST($A\alpha$) $\supseteq$ FIRST($\beta$). The lookahead therefore cannot distinguish $A \to A\alpha$ from $A \to \beta$, so a left-recursive grammar is never LL(1).

**Remedy:** rewrite $A \to A\alpha \mid \beta$ as the right-recursive

$$A \to \beta A'$$

$$A' \to \alpha A' \mid \epsilon$$

which generates the same strings $\beta\alpha^*$. Now each procedure consumes input (via $\beta$ or $\alpha$) before recursing. (Indirect left recursion, $A \Rightarrow B\ldots \Rightarrow A\ldots$, causes the same problem and is removed with Algorithm 4.19.)
