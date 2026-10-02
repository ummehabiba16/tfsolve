---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "An SDD is a CFG with attributes and semantic rules (no evaluation order); an SDT is a CFG with program fragments (actions) embedded at positions in production bodies, which fixes when each action is executed. A postfix SDT has all its actions at the right end of the production bodies, so each action runs when the body is reduced; e.g. the desk calculator L -> E n { print(E.val) }; E -> E1 + T { E.val = E1.val + T.val }; E -> T { E.val = T.val }; T -> T1 \\* F { T.val = T1.val \\* F.val }; T -> F { T.val = F.val }; F -> ( E ) { F.val = E.val }; F -> digit { F.val = digit.lexval }, implemented on the LR parser stack."
sources: ["KMS Chapter 5 slides 9-17, 48-57 (SDD, SDT, Postfix SDT, Parser-Stack Implementation)", "Dragon book 2e sec. 5.1, 5.4.1-5.4.2"]
---
**SDD vs SDT (5 marks)**

| | SDD | SDT |
|:--|:--|:--|
| Definition | Context-free grammar + attributes + **semantic rules** for each production | Context-free grammar + **program fragments (semantic actions)** embedded in the production bodies |
| Example | $E \to E_1 + T$ $\quad E.val = E_1.val + T.val$ | $E \to E_1 + T\ \{E.val = E_1.val + T.val;\}$ |
| Order of evaluation | Not specified: any order allowed by the dependency graph | Specified: an action is executed as soon as all symbols to its left have been matched |
| Level | Specification (high level, implementation details hidden) | Implementation (closer to code) |

Every S-attributed or L-attributed SDD can be turned into an SDT.

**Postfix SDT (4 marks).** An SDT in which **all actions are at the right end** of the production bodies. Each action is executed when the body is **reduced** to the head, so it can be implemented during LR (bottom-up) parsing. An S-attributed SDD on an LR grammar is converted into a postfix SDT simply by putting each rule, as an action, at the end of its production.

**Example (desk calculator):**

```text
L -> E n         { print(E.val); }
E -> E1 + T      { E.val = E1.val + T.val; }
E -> T           { E.val = T.val; }
T -> T1 * F      { T.val = T1.val * F.val; }
T -> F           { T.val = F.val; }
F -> ( E )       { F.val = E.val; }
F -> digit       { F.val = digit.lexval; }
```

**Implementation on the parser stack:** each stack entry holds a grammar symbol (state) and its attribute value. When $E \to E_1 + T$ is reduced, $T$ is on top and $E_1$ is two places below. So the action is `stack[top-2].val = stack[top-2].val + stack[top].val; top = top - 2;`, and the parser then replaces the three entries by $E$ with that value. For `3 * 5 + 4 n`, the reductions compute 3, 15, 4, 19 and finally print 19.
