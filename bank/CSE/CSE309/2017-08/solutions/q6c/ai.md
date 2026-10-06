---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Static (lexical) scoping binds a name to the declaration in the closest enclosing block of the program text, decided at compile time; dynamic scoping binds it to the most recent active declaration found by looking down the run-time call stack. In the example f() returns 1 under static and 2 under dynamic scoping."
sources: ["Dragon book 2e sec. 1.6.3 (Static Scope and Block Structure), 1.6.5 (Dynamic Scope)"]
---
**Static (lexical) scope.** The scope of a declaration is determined by the **program text** alone, so the binding of every use of a name can be found **at compile time**: the use refers to the declaration in the closest enclosing block (or function / class) that declares the name. Most languages (C, C++, Java, Python, Pascal) use static scope.

**Dynamic scope.** The binding is determined by the **run-time behaviour**: a use of $x$ refers to the declaration of $x$ in the most recently called, still active procedure, found by looking down the call stack. So the same use may refer to different declarations in different executions. Dynamic scope appears in early Lisp, APL, some shell and macro languages (Dragon book sec. 1.6.5).

**Example.**

```c
int x = 1;
int f()  { return x; }
int g()  { int x = 2; return f(); }
int main() { printf("%d", g()); }
```

- Static scope: in `f`, `x` is the global `x` (the enclosing block of `f`'s text), so the output is **1**.
- Dynamic scope: `f` is called from `g`, so `x` refers to the most recent active declaration, the `x` in `g`, and the output is **2**.

| | Static | Dynamic |
|:--|:--|:--|
| Binding decided | at compile time, from the text | at run time, from the call stack |
| Implementation | symbol tables per block / access links | search the stack (or deep/shallow binding) |
| Predictability, type checking | easy, can be checked statically | hard |
