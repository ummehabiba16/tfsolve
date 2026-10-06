---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Declare %union { int bit; struct { int n; unsigned long v; } num; }, %token <bit> BIT, %type <num> bin; rules: bin : bin BIT { \\$\\$.n = \\$1.n + 1; \\$\\$.v = (\\$1.v << 1) | \\$2; } | BIT {...}; line : bin newline prints the n-bit value (~v + 1) & mask. Tested: 1010 -> 0110."
sources: ["MMA syntax analysis slides 565-592 (Yacc / Bison)", "Dragon book 2e sec. 4.9.1, 4.9.3"]
---
**Idea.** The input is a binary string (any length, terminated by a newline). The 2's complement of an $n$-bit number $v$ is $(\sim v + 1) \bmod 2^n$, so the parser must compute both **the value** and **the length** $n$ of the string. We keep them in one semantic value, a structure.

**Data types of the semantic values.**

- token `BIT`: an `int` (0 or 1), the value set by the Lex program in `yylval.bit`;
- nonterminal `bin`: a structure `{ int n; unsigned long v; }` where `n` is the number of bits read and `v` their value.

**Middle portion (declarations and rules) of the YACC program:**

```c
%union {
    int bit;                                  /* value of a BIT token */
    struct { int n; unsigned long v; } num;   /* number of bits and value */
}
%token <bit> BIT
%type  <num> bin
%%
line : bin '\n'  { int i;
                   unsigned long mask = (1UL << $1.n) - 1;
                   unsigned long c = (~$1.v + 1) & mask;   /* 2's complement in n bits */
                   for (i = $1.n - 1; i >= 0; i--)
                       putchar(((c >> i) & 1) ? '1' : '0');
                   putchar('\n'); }
     ;
bin  : bin BIT   { $$.n = $1.n + 1;
                   $$.v = ($1.v << 1) | $2; }
     | BIT       { $$.n = 1;
                   $$.v = $1; }
     ;
%%
```

(The Lex program only returns `BIT` with `yylval.bit = yytext[0] - '0'` for `0`/`1` and `'\n'` for the newline.)

**Working.** The left-recursive rule `bin : bin BIT` appends one bit at a time: for `1010`, $v$ takes the values $1, 2, 5, 10$ and $n$ the values $1, 2, 3, 4$. At the newline: mask $= 2^4 - 1 = 15$, $\sim 10 + 1 \;\&\; 15 = 6 = 0110$. **Output: `0110`.**

*Check:* the program was compiled with `bison` and `flex` and tested: `1010` $\to$ `0110`, `0110` $\to$ `1010`, `1000` $\to$ `1000`, `0001` $\to$ `1111`, `11111` $\to$ `00001`, `101100` $\to$ `010100`, all equal to $(-v) \bmod 2^n$.
