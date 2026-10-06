---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Table-driven predictive parser: stack with the end marker and start symbol, input buffer, table M. Loop: let X be the top and a the current input; if X = a = \\$ accept; if X is a terminal equal to a, pop and advance; if X is a terminal otherwise, error; if M[X,a] is an error entry, error; if M[X,a] = X -> Y1...Yk, pop X and push Yk ... Y1, outputting the production."
sources: ["MMA syntax analysis slides 124-151 (non-recursive predictive parsing)", "Dragon book 2e sec. 4.4.3, Algorithm 4.34"]
---
A **non-recursive (table-driven) predictive parser** uses an explicit stack instead of recursive calls. It has an input buffer (the input string followed by the end marker `$`), a stack (grammar symbols, with `$` at the bottom and the start symbol $S$ above it), and a parsing table $M[A, a]$. It outputs the productions used (a leftmost derivation).

**Algorithm 4.34 (table-driven predictive parsing).** Input: a string $w$ and a parsing table $M$ for grammar $G$. Output: a leftmost derivation of $w$ if $w \in L(G)$, otherwise an error indication.

```text
set ip to point to the first symbol of w$;
push $ and then S on the stack (S on top);
repeat
    let X be the top stack symbol and a the symbol pointed to by ip;
    if ( X = $ and a = $ )  accept: parsing is complete;
    else if ( X is a terminal )
        if ( X = a )  pop X from the stack and advance ip;
        else          error();
    else  /* X is a nonterminal */
        if ( M[X, a] = X -> Y1 Y2 ... Yk ) {
            output the production X -> Y1 Y2 ... Yk;
            pop X from the stack;
            push Yk, Yk-1, ..., Y1 onto the stack, with Y1 on top;
        }
        else  error();      /* M[X, a] is an error entry */
until false
```

**Notes.** (1) The stack holds the unmatched part of the left-sentential form (top = leftmost symbol), so the matched input $w'$ and the stack contents $\alpha$ always satisfy $S \Rightarrow^*_{lm} w'\alpha$. (2) An $\epsilon$-production $X \to \epsilon$ simply pops $X$ and pushes nothing. (3) The table $M$ is built from FIRST and FOLLOW (Algorithm 4.31); the parser works in time linear in the input length for an LL(1) grammar. (4) Error recovery can be added in the error entries (panic mode with synchronizing tokens from FOLLOW sets).
