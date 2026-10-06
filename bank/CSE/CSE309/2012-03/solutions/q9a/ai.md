---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Lex returns NUMBER (with yylval.d = atof), SIN, COS, TAN and the operator characters; Yacc has %union { double d; }, %token <d> NUMBER, precedence declarations %left '+' '-', %left '*' '/', %right UMINUS, and rules expr : expr '+' expr | ... | SIN '(' expr ')' | ... | NUMBER; line : expr newline prints the value. Tested: 1+2*3 = 7, sin(0)+cos(0) = 1."
sources: ["MMA syntax analysis slides 565-592 (Yacc / Bison)", "Dragon book 2e sec. 4.9.1-4.9.3"]
---
The program has two files. Semantic values are `double`s, so the Yacc specification declares `%union { double d; }`. The ambiguous expression grammar is resolved with **precedence and associativity declarations**: `*` `/` bind tighter than `+` `-`, all are left associative, and unary minus has the highest precedence. Trigonometric functions take radians. Input is a single line terminated by a newline.

**Lex file (`calc.l`):**

```text
%{
#include <stdlib.h>
#include "calc.tab.h"
%}
%%
[0-9]+\.?[0-9]*|\.[0-9]+   { yylval.d = atof(yytext); return NUMBER; }
"sin"                      { return SIN; }
"cos"                      { return COS; }
"tan"                      { return TAN; }
[ \t]                      ;
\n                         { return '\n'; }
.                          { return yytext[0]; }
%%
int yywrap(void) { return 1; }
```

**Yacc file (`calc.y`):**

```c
%{
#include <stdio.h>
#include <math.h>
int yylex(void);
void yyerror(const char *s) { fprintf(stderr, "error: %s\n", s); }
%}
%union { double d; }
%token <d> NUMBER
%token SIN COS TAN
%type  <d> expr
%left '+' '-'
%left '*' '/'
%right UMINUS
%%
line : expr '\n'                { printf("%g\n", $1); }
     ;
expr : expr '+' expr            { $$ = $1 + $3; }
     | expr '-' expr            { $$ = $1 - $3; }
     | expr '*' expr            { $$ = $1 * $3; }
     | expr '/' expr            { $$ = $1 / $3; }
     | '-' expr %prec UMINUS    { $$ = -$2; }
     | '(' expr ')'             { $$ = $2; }
     | SIN '(' expr ')'         { $$ = sin($3); }
     | COS '(' expr ')'         { $$ = cos($3); }
     | TAN '(' expr ')'         { $$ = tan($3); }
     | NUMBER                   { $$ = $1; }
     ;
%%
int main(void) { return yyparse(); }
```

**Build and run:** `bison -d calc.y; flex calc.l; gcc calc.tab.c lex.yy.c -lm`.

*Check:* the program was built with `bison`, `flex` and `gcc` and run: `1+2*3` gives 7, `(1.5+2.5)*2` gives 8, `sin(0)+cos(0)` gives 1, `2*tan(0.5)` gives 1.0926, `10/4-1` gives 1.5, `-3+5` gives 2, `8/2/2` gives 2, `.5+.25` gives 0.75; all agree with Python.
