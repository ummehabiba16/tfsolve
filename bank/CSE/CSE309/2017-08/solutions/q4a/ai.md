---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Panic mode is used when the scanner cannot proceed because no prefix of the remaining input matches any token pattern: successive characters are deleted from the remaining input until a well-formed token appears. Other repairs: delete one character, insert a missing character, replace a character by another, transpose two adjacent characters."
sources: ["MMA lexical analysis slides 29-36 (Lexical Errors, panic-mode recovery)", "Dragon book 2e sec. 3.1.4"]
---
**When panic mode is used.** A lexical analyzer reports an error when it cannot proceed because **no prefix of the remaining input matches the pattern of any token**. In *panic-mode recovery* the lexer then **deletes successive characters from the remaining input until it finds a well-formed token at the beginning of what is left**, and continues scanning. It is the simplest strategy and may delete much of the input; the parser may later report an error caused by the deletion.

**Three (four) other recovery actions** (Dragon book sec. 3.1.4) are *single-character repairs* tried on the remaining input:

1. **Delete** one character from the remaining input.
2. **Insert** a missing character into the remaining input.
3. **Replace** a character by another character.
4. **Transpose** two adjacent characters.

Any three of these are asked for. Such transformations are tried in the hope of getting a valid lexeme with the *minimum number of transformations* (the minimum-distance idea); for instance `fi` $\to$ `if` is one transposition. In practice few errors are single-character errors, and the cost of searching makes these methods less common than panic mode.
