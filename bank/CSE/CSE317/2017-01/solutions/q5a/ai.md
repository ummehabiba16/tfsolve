---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "The latter is true only at a trivial level: a computer executes its program, but programs can learn, search and adapt, so programmers do not specify (and cannot foresee) the behaviour; and the same argument applied to brains (neurons only do what physics and genes tell them) would deny that humans are intelligent. So it does not imply the former."
sources: ["AIMA 3e Exercise 1.11 and sec. 26.1 (weak AI: can machines act intelligently?)", "Lady Lovelace objection (Turing 1950)"]
---
**Is the latter statement true?** Only in a narrow, literal sense.

- A computer does execute exactly the instructions of its program. But the program can tell it to **learn** (from data or experience), **search** huge spaces, or **reason** from general knowledge. The programmer specifies *how to learn and decide*, not *what* to do in each situation.
- A learning system's behaviour depends on its experience and is often unknown to, and better than, its programmer's own abilities. Samuel's checkers program learned to beat Samuel; AlphaGo found moves its designers could not have predicted. So in the ordinary sense, the computer does more than it was "told".

**Does it imply the former?** **No.**

1. The same argument proves too much. Human brains "only do what their neurons, physics and genes tell them", yet we call humans intelligent. Being determined by a mechanism does not exclude intelligence.
2. Intelligence is about **behaviour**: perceiving, reasoning, learning and acting well in new situations (rational action). It is not about the absence of a program. If a programmed system shows that behaviour, it is intelligent in the sense that matters (the Turing test and rational-agent views).
3. This is the "Lady Lovelace objection" ("the Analytical Engine has no pretensions to originate anything"). Turing answered that machines can surprise us, and can learn.

So the conclusion does not follow: computers can be intelligent even though they follow programs.
