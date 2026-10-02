---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Keywords match the identifier pattern, so either (1) all keywords are installed in the symbol table before scanning, marked as reserved with their token; the identifier diagram's action looks the lexeme up and returns the keyword token if it is reserved, else id (installing it); or (2) each keyword gets its own transition diagram, tried before the identifier diagram, with a test that the next character cannot continue an identifier; in Lex, keyword patterns are listed before the id pattern (first rule wins for equal-length matches)."
sources: ["MMA lexical analysis slides 77-83 (Recognition of Reserved Words and Identifiers), 146-148 (Conflict Resolution in Lex)", "Dragon book 2e sec. 3.4.2, 3.5.3"]
---
Keywords such as `if`, `while` and `int` have the same form as identifiers (a letter followed by letters and digits), so the transition diagram (or regular expression) for identifiers also matches them. The lexer distinguishes them in one of the following ways.

**1. Install the reserved words in the symbol table initially.**

- Before lexical analysis begins, each keyword is entered in the symbol table, with a field marking it as a **reserved word** and giving the token it represents (e.g. `if` $\to$ IF).
- Keywords and identifiers are recognised with the **same** transition diagram: letter (letter | digit)\*. When it accepts, the lexer calls `installID()`:
- if the lexeme is already in the table as a keyword, that entry is found;
- otherwise the lexeme is entered as a new identifier.
- `getToken()` then returns the keyword's own token for reserved words, and **id** (with a pointer to the entry) for all other names.

Example: `while` is found as a keyword and returned as WHILE. `whilex` is not in the table as a keyword, so it is returned as id.

**2. Separate transition diagrams for each keyword.**

- For example, the diagram for `then` recognises `t`, `h`, `e`, `n`, followed by a test that the next character is not a letter or digit (so `thenextvalue` is not split).
- The keyword diagrams are tried **before** the identifier diagram. When both match, the keyword is preferred.

**In Lex**, this follows from the conflict-resolution rules: the **longest match** wins (`ifx` is an identifier), and when several patterns match the same longest lexeme, the **pattern listed first** wins. So the keyword rules are placed before the identifier rule.
