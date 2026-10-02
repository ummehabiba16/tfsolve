---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "On a syntax error the parser discards input symbols one at a time until it finds a token from a designated synchronizing set (e.g. ; or }, often FOLLOW(A) of the nonterminal being parsed); it pops the stack to a state/nonterminal that can continue with that token and resumes; simple, never loops, but may skip a lot of input."
sources: ["MMA syntax analysis slides 15-24 (Syntax Error Handling)", "Dragon book 2e sec. 4.1.4, 4.4.5, 4.8.3"]
---
**Idea.** When the parser detects an error, it does not try to repair the input. Instead it **skips input symbols** until it finds a **synchronizing token** from which parsing can safely continue. Synchronizing tokens are usually delimiters whose role is clear: `;`, `}`, `end`.

**Top-down (predictive) parser:**

1. An error occurs when the terminal on top of the stack does not match the input, or $M[A, a]$ is empty.
2. If $M[A, a]$ is empty, skip input symbols until one in the synchronizing set of $A$ appears.

- The synchronizing set of $A$ contains FOLLOW($A$). On such a token, pop $A$, as if $A$ had been parsed, and continue.
- Add FIRST($A$): on such a token, resume parsing $A$ itself.
- Add tokens that start higher-level constructs (keywords beginning statements), so an error in an expression does not skip a whole statement.

3. If the terminal on top of the stack does not match, pop it (as if it had been inserted).

The table entries `synch` mark where to pop.

**Bottom-up (LR) parser:** scan down the stack until a state $s$ with a GOTO on a particular nonterminal $A$ is found (e.g. a statement or expression). Discard input symbols until a symbol $a$ that can legitimately follow $A$ is found. Push GOTO$(s, A)$ and resume. This amounts to pretending a whole $A$ was parsed (Yacc's `error` token works this way).

**Example:** `x = a + * b ; y = c ;`. The error is detected at `*`. The parser skips `* b` up to `;` (in FOLLOW(stmt)), finishes the statement, and parses `y = c ;` normally.

**Properties:** simple to implement, and it **cannot go into an infinite loop** (input is always consumed or the stack popped). However, it may skip a considerable amount of input without checking it for further errors.
