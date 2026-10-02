---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Universal methods (CYK, Earley) parse any CFG but take O(n^3) time (CYK also needs Chomsky normal form), far too slow for programs of thousands of tokens; production compilers use linear-time LL or LR parsers on restricted but sufficient grammars."
sources: ["MMA syntax analysis slides 2-8 (The Role of the Parser)", "Dragon book 2e sec. 4.1.1"]
---
Universal parsing methods, such as the **Cocke-Younger-Kasami (CYK)** algorithm and **Earley's** algorithm, can parse *any* context-free grammar, including ambiguous ones. They are not used in production compilers because:

1. **Too slow.** They take $O(n^3)$ time in general (and CYK needs the grammar in Chomsky normal form). Source programs have tens of thousands of tokens, so cubic time is unacceptable. Top-down (LL) and bottom-up (LR) parsers run in **linear** time.
2. **Not needed.** Programming-language grammars can be written (or adjusted) to be LL(1) or LALR(1), which covers practically all language constructs.
3. **Ambiguity is undesirable.** A compiler needs exactly one parse tree per program; deterministic LL/LR parsers report ambiguity as table conflicts at construction time, which helps the language designer.
4. **Error handling and tools.** LL/LR parsers detect errors at the earliest possible point (viable-prefix property) and are supported by generators like Yacc.
