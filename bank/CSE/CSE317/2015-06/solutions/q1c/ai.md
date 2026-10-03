---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "No. A simple reflex agent sees only the current location and its dirt status; it cannot know whether the other square is already clean, so it must either keep moving (paying -1 per move forever) or stop moving (failing to clean the other square when it is dirty); neither is optimal for every environment. A reflex agent with state remembers which squares it has seen or cleaned, cleans each square once, and then stops (NoOp), which is rational."
sources: ["AIMA 3e sec. 2.2.1 and Exercise 2.9 (vacuum world with a movement penalty)"]
---
**Setting.** Two squares A and B. The agent gets +1 for each clean square per time step and **-1 for each movement**. Percept = [location, dirty or clean].

**Can a simple reflex agent be perfectly rational? No.** A simple reflex agent's action depends only on the **current percept**. When it is in a clean square, it cannot tell whether the **other** square is clean or dirty, because that is not in the percept. Every fixed rule for the percept [A, Clean] fails in some environment:

- *Rule "move to B":* if B is also clean, it moves back and forth forever, paying -1 each step for nothing.
- *Rule "NoOp" (stay):* if B is dirty, it never goes to clean it, and loses the points B would have earned.

So no simple reflex agent maximizes the expected score in every possible initial configuration. It cannot be perfectly rational. (A *randomized* reflex agent does better on average, but it is still not optimal.)

**Reflex agent with state (model-based).** It keeps **internal state**: which squares it has visited and whether each is known to be clean. Its rules:

- if the current square is dirty: **Suck**;
- else if the other square's status is unknown or dirty: **move** there (once);
- else (both known clean): **NoOp**, so it does not waste movement points.

This agent cleans everything with the minimum number of moves (at most one move to check the other square, plus none afterwards) and then stays still. It is **rational** for this performance measure. It can be improved further if the geography or the dirt probabilities are unknown, by learning or exploring.
