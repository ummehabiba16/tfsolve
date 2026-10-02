---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "(i) Unacceptable: the bottom of the stack is just the left end of every viable prefix. (ii) Acceptable in the sense that the whole stack (bottom to top) is a viable prefix whose right end is at the top; viable prefixes are never 'inside'. (iii) Acceptable: every prefix of the stack contents is a viable prefix, so the stack holds a nested set of viable prefixes. (iv) Acceptable: that is the definition, a viable prefix never extends past the right end of the handle."
sources: ["MMA syntax analysis slides 152-226 (Handle Pruning, Shift-Reduce Parsing), 388-403 (Viable Prefixes)", "Dragon book 2e sec. 4.5, 4.6.5"]
---
**Definition.** A *viable prefix* is a prefix of a right-sentential form that does not continue past the right end of the rightmost handle of that form. In shift-reduce parsing, the stack contents (from bottom to top), followed by the unread input, form a right-sentential form. The parser only shifts while the stack remains a viable prefix, so **the stack always holds a viable prefix**.

**(i) "Only at the bottom of the stack and not inside": not acceptable.** A viable prefix always *starts* at the bottom of the stack (the left end of the sentential form), but it is the whole stack contents up to the top, not something sitting only at the bottom. For example, with $E \to E + T$ and stack \$ E + T, the viable prefix is $E + T$, which extends to the top.

**(ii) "Only at the top of the stack and not inside": acceptable, if read correctly.** Its right end is always the **top** of the stack: the parser reduces as soon as a handle appears on top, so it never needs to look inside the stack. But it is not a symbol "at the top" alone: it runs from the bottom to the top. A viable prefix never ends somewhere inside the stack with stack symbols beyond it.

**(iii) "The stack contains only a set of viable prefixes": acceptable.** Any prefix of a viable prefix is also a viable prefix. So the stack contents $X_1 X_2 \ldots X_m$ give the nested set $X_1$, $X_1X_2$, ..., $X_1 \ldots X_m$, all viable prefixes. Nothing else is ever on the stack: if shifting would make the stack a non-viable prefix, the LR parser detects an error instead. (In an LR parser each state summarises the viable prefix below it.)

**(iv) "Viable prefixes do not continue past the right end of the rightmost handle": acceptable.** This is the definition. The parser must reduce the handle as soon as its right end is on top of the stack, before shifting further. Once the handle is on top, the stack holds the longest possible viable prefix for that sentential form.
