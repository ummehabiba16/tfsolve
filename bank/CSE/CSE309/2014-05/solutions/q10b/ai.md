---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "F -> 0.B {F.val = B.val}; B0 -> 0 B1 {B0.val = B1.val / 2}; B0 -> 1 B1 {B0.val = B1.val / 2 + 1/2}; B -> 0 {B.val = 0}; B -> 1 {B.val = 1/2}. For 0.101 this gives 0.625."
sources: ["KMS Chapter 5 slides 48-69 (postfix SDT)", "Dragon book 2e sec. 5.1, 5.4.1"]
---
The value of the fraction $0.b_1b_2\ldots b_n$ is $\sum_{i=1}^{n} b_i\,2^{-i}$. Let $B$ derive the digit string $b_1 b_2 \ldots b_n$ and let $B.val$ be its value as the fraction $0.b_1b_2\ldots b_n$ (so the first digit $b_1$ has weight $1/2$). Then:

- A single digit $b$ has value $b/2$: $B \to 0$ gives $0$ and $B \to 1$ gives $1/2$.
- For $B_0 \to b\,B_1$, the leading digit $b$ has weight $1/2$ and the digits of $B_1$ are all shifted one place to the right, so their value is halved: $B_0.val = b/2 + B_1.val/2$.

**Completed translation scheme** (postfix SDT, since all actions are at the right ends):

$$F \to 0.B\ \{F.val = B.val\}$$

$$B_0 \to 0\,B_1\ \{B_0.val = B_1.val / 2\}$$

$$B_0 \to 1\,B_1\ \{B_0.val = B_1.val / 2 + 1/2\}$$

$$B \to 0\ \{B.val = 0\}$$

$$B \to 1\ \{B.val = 1/2\}$$

All attributes are synthesized, so the actions can be executed as each production is reduced by a bottom-up parser.

**Check on `0.101`.** Reductions, innermost first: $B \to 1$ gives $1/2$; $B \to 0B_1$ gives $1/4$; $B \to 1B_1$ gives $1/8 + 1/2 = 5/8$; $F.val = 5/8 = 0.625 = 1/2 + 1/8$. Correct.

(The question's text, "is calculated as each non-terminal has a synthesized attribute", is missing the summation formula; the formula above is the standard one.)
