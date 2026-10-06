---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A left-recursive production lets the shift-reduce parser reduce after each operand, so the stack stays small (constant depth) and operators are left associative; a right-recursive production forces it to shift the whole list onto the stack before the first reduction, so the stack grows with the input length."
sources: ["MMA syntax analysis slides 152-226 (shift-reduce parsing)", "Dragon book 2e sec. 4.5"]
---
For a **shift-reduce (bottom-up) parser**, left recursion is the natural choice (unlike top-down parsing, which cannot handle it).

Compare the two grammars for a list of `id`s separated by `+`:

$$E \to E + \textbf{id} \mid \textbf{id} \qquad \text{(left recursive)}$$

$$E \to \textbf{id} + E \mid \textbf{id} \qquad \text{(right recursive)}$$

Input: `id + id + id + id`.

**Left recursive.** The parser shifts `id`, reduces it to $E$, shifts `+`, shifts `id` and immediately reduces $E + \textbf{id}$ to $E$. After every operand the stack is back to `E`:

```text
STACK        INPUT                 ACTION
$ id         + id + id + id $      shift
$ E          + id + id + id $      reduce E -> id
$ E +        id + id + id $        shift
$ E + id     + id + id $           shift
$ E          + id + id $           reduce E -> E + id
$ E + id     + id $                ... (same pattern: the stack never exceeds E + id)
```

The stack depth is **bounded by a constant** (3 symbols) however long the list is.

**Right recursive.** The first reduction can only happen at the right end, after the last `id` has been seen (the handle is the last `id`). So the parser must **shift every operand and operator** on the stack first:

```text
$ id + id + id + id        all shifted ... then reduce E -> id, E -> id + E, E -> id + E, ...
```

The stack grows to about $2n$ symbols for $n$ operands, which costs memory and can overflow for long lists.

**Other reasons.**

- A left-recursive production gives the usual **left associativity** of `+`, `-`, `*`, `/` directly: $a - b - c$ is $(a - b) - c$. A right-recursive production would group $a - (b - c)$, which is wrong for these operators.
- LR parsers handle left recursion without any grammar change, so there is no need to eliminate it; the grammar stays smaller and the parse tree (and the semantic actions) stay simple.
