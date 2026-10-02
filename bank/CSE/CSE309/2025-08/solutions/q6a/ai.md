---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "An SDD attaches semantic rules (attribute equations) to productions, with no order of evaluation; an SDT embeds program fragments (actions) at specific positions in production bodies, so it fixes when each action runs. The SDT is suitable for implementation. Two classes implementable during parsing: S-attributed (postfix SDT, LR parsing) and L-attributed (LL or LR parsing)."
sources: ["KMS Chapter 5 slides 9-17, 30-32, 48-55", "Dragon book 2e sec. 5.1, 5.2.3-5.2.4, 5.4"]
---
| | SDD (syntax-directed definition) | SDT (syntax-directed translation scheme) |
|:--|:--|:--|
| What it is | A grammar with attributes and **semantic rules** attached to each production | A grammar with **program fragments (semantic actions)** embedded in production bodies |
| Example | $E \to E_1 + T$ $\quad E.val = E_1.val + T.val$ | $E \to E_1 + T\ \{\ E.val = E_1.val + T.val;\ \}$ |
| Order of evaluation | Not specified: any order consistent with the dependency graph | Specified: an action runs when everything to its left has been recognised |
| Nature | High-level, declarative specification | Lower-level, close to an implementation |
| Side effects | Ideally none (pure equations) | Allowed (print, insert into symbol table, emit code) |

**Which one is suitable for implementation? The SDT.** An SDD says *what* to compute but not *when*, so the implementer must build the dependency graph and find an evaluation order (a topological sort), and cycles may exist. An SDT already places each action at a definite point in the body. During parsing, the action is executed when the parser reaches that point (for a postfix action: at the reduction), so it can be implemented directly during parsing, with no separate parse tree.

**Two classes of SDDs that allow implementation during parsing:**

1. **S-attributed SDDs:** only synthesized attributes. They are converted to *postfix SDTs* (all actions at the right end) and evaluated bottom-up, during LR parsing, using the parser stack.
2. **L-attributed SDDs:** synthesized attributes, plus inherited attributes that depend only on the parent's inherited attributes and on siblings to the **left**. They are evaluated in one left-to-right depth-first pass, so they can be implemented during LL (recursive-descent) parsing, and also during LR parsing for LL grammars (using marker nonterminals).
