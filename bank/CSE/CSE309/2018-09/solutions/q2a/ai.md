---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Need extra lookahead: Identifiers (end only at a non-letter/digit/\\_), IF/THEN/ELSE (must check the word does not continue as an identifier, e.g. iffy), PLUS (could be ++ or +++), INC (could be +++), GT (could be >= or >>). No extra: ROR >>, ROL <<, TINC +++, GE >= (no longer token begins with them)."
sources: ["MMA lexical analysis slides 37-49 (Input Buffering), 63-92 (Transition Diagrams, Reserved Words)", "Dragon book 2e sec. 3.2, 3.4.1"]
---
A token needs **extra characters** (one beyond the lexeme, then retract) when its lexeme is a **proper prefix of another possible lexeme**, so the lexer cannot know it has the longest match until it sees the next character.

| Token | Pattern | Extra character needed? | Reason |
|:--|:--|:-:|:--|
| Identifiers | `_` or letter, then `_`/letter/digit any number of times | **Yes** | An identifier can always be extended; it ends only when a character that is not `_`/letter/digit is seen (a starred, retracting state in the transition diagram) |
| IF | `if` | **Yes** | `if` is a prefix of identifiers like `iffy`; must read the next character to make sure it is not a letter/digit/`_` |
| THEN | `then` | **Yes** | Same: `thenx` is an identifier |
| ELSE | `else` | **Yes** | Same: `elsewhere` is an identifier |
| ROR | `>>` | No | No token begins with `>>` and is longer, so after the second `>` the token is complete |
| ROL | `<<` | No | No longer token begins with `<<` (and there is no `<` token) |
| PLUS | `+` | **Yes** | `+` is a prefix of `++` and `+++`; must see that the next character is not `+` |
| INC | `++` | **Yes** | `++` is a prefix of `+++`; must check the next character |
| TINC | `+++` | No | Longest operator; no token is longer |
| GT | `>` | **Yes** | `>` is a prefix of `>=` and `>>`; must see the next character |
| GE | `>=` | No | No longer token begins with `>=` |

So identifiers, IF, THEN, ELSE, PLUS, INC and GT require reading extra characters (and retracting `forward`). ROR, ROL, TINC and GE do not.

(Keywords are usually recognised as identifiers first and then looked up in a table of reserved words, which is why they inherit the identifiers' lookahead.)
