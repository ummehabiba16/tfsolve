---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Rules section: copy string literals and comments unchanged (ECHO), the rule float { printf('double'); } before a general identifier rule [A-Za-z\\_][A-Za-z0-9\\_]\\* { ECHO; }, and .|newline { ECHO; }; longest match keeps identifiers such as floatval unchanged."
sources: ["MMA lexical analysis slides 111-148 (The Lexical-Analyzer Generator Lex)", "Dragon book 2e sec. 3.5, Exercise 3.5.2"]
---
Only the rules (middle) part is needed. The output is the input with every keyword `float` replaced by `double`. Identifiers that merely contain `float` (e.g. `floatval`), and `float` inside strings or comments, must not be changed.

```text
%%
\"([^"\\\n]|\\.)*\"             { ECHO; /* string literal: copy unchanged */ }
"/*"([^*]|\*+[^*/])*\*+"/"      { ECHO; /* comment: copy unchanged */ }
"//".*                          { ECHO; }
float                           { printf("double"); }
[A-Za-z_][A-Za-z0-9_]*          { ECHO; /* other identifiers/keywords */ }
.|\n                            { ECHO; /* everything else copied */ }
%%
```

How it works:

- Lex uses the **longest match**, and for equal lengths the **first** rule. For `floatval`, the identifier rule matches 8 characters versus 5 for `float`, so it is copied unchanged. For `float` alone both match 5 characters and the `float` rule comes first, so `double` is printed.
- `ECHO` copies the matched text (`yytext`) to the output.
- The string and comment rules ensure `"float"` and `/* float */` are not modified.
- `.|\n` copies all other characters one at a time.

The `main` (in the auxiliary section) calls `yylex()`; with input from stdin, `lex prog.l && cc lex.yy.c -ll` gives a filter: `./a.out < in.c > out.c`.
