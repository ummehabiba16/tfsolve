---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Separating lexical analysis from parsing gives (1) a simpler design (white space, comments handled outside the grammar), (2) more efficient specialised scanners with buffering, (3) portability (character-set and device peculiarities confined to the lexer). A parser-only compiler would have a huge, hard-to-maintain grammar, be slow (a parse step per character) and ambiguous (keyword versus identifier)."
sources: ["MMA lexical analysis slides 2-16 (Role of the lexical analyzer)", "Dragon book 2e sec. 3.1.1"]
---
**Reasons for separating lexical analysis (scanning) from syntax analysis** (Dragon book sec. 3.1.1):

1. **Simplicity of design.** Separation lets us simplify at least one of the tasks. A parser that also had to deal with white space and comments would be considerably more complex; a lexer removes them, and the parser's grammar is written over tokens rather than characters. Each phase is easier to design, write and test.

2. **Compiler efficiency.** Lexical analysis is a very large share of the compile time because it reads every character of the source. A separate scanner can use specialised techniques (buffer pairs with sentinels, regular expressions turned into DFAs) that are much faster than general parsing, which can never be as fast on the character level.

3. **Compiler portability.** Input-device-specific peculiarities (character sets, end-of-line conventions, special symbols) are confined to the lexical analyzer, so the parser and later phases do not change.

**What is wrong with using the parser only for both tasks?**

- The grammar would have to describe every identifier, number, keyword and comment character by character, so it would be enormous, hard to read and to maintain, and the parse tree would have a node for every character.
- White space and comments could occur between *any* two tokens, so every production would have to allow them, or the grammar would become full of extra symbols.
- A character-level parser such as an LR or LL parser is much **slower** than a DFA-based scanner: it performs table lookups, pushes and pops for each character.
- Regular constructs need no stack; using a context-free machinery for them wastes power and makes conflicts likely (for example, a keyword like `if` versus an identifier `ifx` would turn into an LL/LR conflict or ambiguity which a longest-match rule in the scanner settles trivially).
