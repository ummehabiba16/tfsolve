---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Common Yacc actions compute the value of the head from the values of the body symbols (evaluate, build tree nodes, print, update the symbol table); an action is C code in braces after a production body, using 43888 for the head's value and , , ... for the body symbols' values (e.g. expr : expr '+' term { 43888 =  + ; }); the default action is 43888 = ."
sources: ["MMA syntax analysis slides 565-592 (The Parser Generator Yacc)", "Dragon book 2e sec. 4.9.1"]
---
**Common semantic actions** in Yacc are pieces of C code executed when the parser **reduces** by a production. Typically they:

- compute the attribute (value) of the head from the values of the body symbols (e.g. evaluate an expression in a desk calculator);
- build syntax-tree nodes or emit intermediate code;
- print output (translation) or messages;
- enter or look up information in the symbol table.

**How an action is formed.** In the translation-rules section, an action is a sequence of C statements in braces after the body:

```text
head : body1   { semantic action 1 }
     | body2   { semantic action 2 }
     ;
```

Inside the action:

- \$\$ is the attribute value of the **head** (left side).
- \$i is the value of the $i$-th grammar symbol of the **body** (\$1, \$2, ...). For tokens, this is the value set by the lexer in `yylval`.

**Example (desk calculator, textbook):**

```c
%token DIGIT
%%
line   : expr '\n'        { printf("%d\n", $1); }
       ;
expr   : expr '+' term    { $$ = $1 + $3; }
       | term
       ;
term   : term '*' factor  { $$ = $1 * $3; }
       | factor
       ;
factor : '(' expr ')'     { $$ = $2; }
       | DIGIT
       ;
%%
int yylex() {
    int c = getchar();
    if (isdigit(c)) { yylval = c - '0'; return DIGIT; }
    return c;
}
```

In `expr : expr '+' term`, \$1 is the value of `expr`, \$2 is `'+'` and \$3 is `term`, so the sum is assigned to \$\$. The actions run in the order the reductions happen (bottom-up), so values flow from the leaves up.

**Default semantic action.** If a production has no action, Yacc uses **{ \$\$ = \$1; }**: the value of the head is the value of the first body symbol. That is why `expr : term` and `factor : DIGIT` above need no explicit action.
