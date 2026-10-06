---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Separating lexical from syntax analysis gives a simpler design (white space and comments handled outside the grammar), a more efficient scanner (buffering, DFA) and portability; using only the parser for both would need a huge grammar, be slow, and make keyword/identifier decisions awkward."
sources: ["MMA lexical analysis slides 2-16 (Role of the lexical analyzer)", "Dragon book 2e sec. 3.1.1"]
---
**Reasons for the separation** (Dragon book sec. 3.1.1):

1. **Simplicity of design.** Removing white space and comments in a separate scanner keeps the grammar for the parser small. A parser that had to handle white space and comments itself would be much more complex; the two phases can be designed, written and tested independently.
2. **Efficiency.** Reading and grouping every character is a large part of the compile time. A separate scanner can use specialised techniques (buffer pairs, sentinels, DFAs) that are much faster than the general parsing method.
3. **Portability.** Character-set and input-device peculiarities are confined to the scanner.

**What is wrong with the parser alone doing both tasks?**

- The grammar would have to describe every identifier, number, keyword and comment character by character, which makes it **very large and hard to maintain**, with parse-tree nodes for individual characters.
- White space and comments could appear between any two tokens, so every production would need to allow them.
- A stack-based parser (LL or LR) performs table lookups and stack operations for each character, so compilation becomes **slow**; regular constructs need no stack, and a finite automaton is both simpler and faster.
- Decisions such as "keyword or identifier" (`if` versus `iffy`) and longest-match would create grammar conflicts and ambiguity that the scanner resolves trivially with its longest-match rule.
