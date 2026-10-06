---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Static scoping binds a name to the declaration in the nearest enclosing block of the program text (decided at compile time); dynamic scoping binds it to the most recently executed active declaration, found by searching the call stack. In the example program f prints 1 under static scoping and 2 under dynamic scoping."
sources: ["Dragon book 2e sec. 1.6.3 (Static Scope and Block Structure), 1.6.5 (Dynamic Scope)"]
---
**Static (lexical) scoping.** The binding of a use of a name is determined from the **program text**: it refers to the declaration in the closest enclosing block, procedure or class that declares the name. It can be determined at **compile time**, whatever the call sequence at run time (C, Java, Pascal, Python; Dragon book sec. 1.6.3).

**Dynamic scoping.** The binding is determined at **run time**: a use of $x$ refers to the declaration of $x$ in the **most recently called procedure that is still active** (searching down the call stack). The same use can refer to different declarations in different runs (early Lisp, APL, shell variables; Dragon book sec. 1.6.5).

| | Static | Dynamic |
|:--|:--|:--|
| Decided | at compile time, from the nesting of the text | at run time, from the call chain |
| Nonlocal lookup | enclosing blocks (access links) | callers (search the stack) |
| Type checking | possible at compile time | not possible in general |

**Program with different output.**

```c
int x = 1;

void f()  { printf("%d\n", x); }

void g()  { int x = 2; f(); }

int main() { g(); return 0; }
```

- **Static scoping:** the `x` in `f` is the one in the enclosing (global) scope of `f` in the text, so `f` prints **1**.
- **Dynamic scoping:** `f` is called by `g`; the most recent active declaration of `x` is `g`'s `x = 2`, so `f` prints **2**.

(Each of the two answers is correct for its own rule; C itself uses static scoping and prints 1.)
