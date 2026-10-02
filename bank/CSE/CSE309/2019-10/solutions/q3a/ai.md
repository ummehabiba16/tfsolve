---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "With A -> alpha beta1 | alpha beta2 a predictive parser cannot choose until it has read past alpha, so it would guess and backtrack; left factoring A -> alpha A', A' -> beta1 | beta2 defers the decision until after alpha is consumed, when the next symbol distinguishes beta1 from beta2 (e.g. if-then vs if-then-else)."
sources: ["MMA syntax analysis slides 61-69 (Left Factoring)", "Dragon book 2e sec. 4.3.4"]
---
**Problem.** If two alternatives of $A$ begin with the same prefix,

$$A \to \alpha\beta_1 \mid \alpha\beta_2$$

then, looking at the input, a top-down parser cannot tell which one to use: both start with FIRST($\alpha$). A general recursive-descent parser must **guess** (say $\alpha\beta_1$), parse $\alpha$, and if $\beta_1$ then fails, **backtrack** (reset the input to where $\alpha$ began) and try $\alpha\beta_2$, parsing $\alpha$ again.

**Left factoring** postpones the decision until enough input has been seen:

$$A \to \alpha A'$$

$$A' \to \beta_1 \mid \beta_2$$

Now $\alpha$ is parsed once, unconditionally. When $A'$ is expanded, the parser is past $\alpha$, and the next input symbol (FIRST($\beta_1$) vs FIRST($\beta_2$)) decides. No guess, so no backtracking.

**Example 1 (if statement):**

$$stmt \to \textbf{if}\ expr\ \textbf{then}\ stmt\ \textbf{else}\ stmt \mid \textbf{if}\ expr\ \textbf{then}\ stmt$$

On seeing `if`, the parser cannot know whether an `else` will come. After left factoring:

$$stmt \to \textbf{if}\ expr\ \textbf{then}\ stmt\ S'$$

$$S' \to \textbf{else}\ stmt \mid \epsilon$$

The choice is made when the parser reaches the position of a possible `else`.

**Example 2:** $S \to abc \mid abd$. Input `abd`: without factoring, the parser tries `abc`, fails at `d`, backtracks two symbols, and tries `abd`. With $S \to abS'$, $S' \to c \mid d$, it reads `ab`, then chooses $S' \to d$ directly.
