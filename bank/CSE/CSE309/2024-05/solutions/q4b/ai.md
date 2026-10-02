---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Taking the alternative as the terminal a: right-sentential forms and handles: aaa\\*a++ (a at 1), Saa\\*a++ (a at 2), SSa\\*a++ (a at 3), SSS\\*a++ (SS\\* at 2-4), SSa++ (a at 3), SSS++ (SS+ at 2-4), SS+ (SS+ at 1-3), S."
sources: ["MMA syntax analysis slides 152-200 (Reductions, Handle Pruning, Shift-Reduce Parsing)", "Dragon book 2e sec. 4.5.2-4.5.3, Exercise 4.5.2"]
---
The last alternative is printed as $\alpha$; the input string uses `a`, so take the grammar as $S \to SS+ \mid SS* \mid a$.

A **handle** is a substring that matches a production body and whose reduction is one step backwards in a **rightmost** derivation. Rightmost derivation of `aaa*a++`:

$$S \underset{rm}{\Rightarrow} SS+ \underset{rm}{\Rightarrow} SSS++ \underset{rm}{\Rightarrow} SSa++ \underset{rm}{\Rightarrow} SSS*a++$$

$$\underset{rm}{\Rightarrow} SSa*a++ \underset{rm}{\Rightarrow} Saa*a++ \underset{rm}{\Rightarrow} aaa*a++$$

Handle pruning (reading the derivation backwards):

| Right-sentential form | Handle (position) | Reduce by |
|:--|:--|:--|
| a a a \* a + + | first a (1) | $S \to a$ |
| S a a \* a + + | a (2) | $S \to a$ |
| S S a \* a + + | a (3) | $S \to a$ |
| S S S \* a + + | S S \* (2-4) | $S \to SS*$ |
| S S a + + | a (3) | $S \to a$ |
| S S S + + | S S + (2-4) | $S \to SS+$ |
| S S + | S S + (1-3) | $S \to SS+$ |
| S | | accept |

**Computation (shift-reduce parser):**

| Stack | Input | Action |
|:--|--:|:--|
| \$ | aaa\*a++\$ | shift |
| \$a | aa\*a++\$ | reduce $S \to a$ |
| \$S | aa\*a++\$ | shift |
| \$Sa | a\*a++\$ | reduce $S \to a$ |
| \$SS | a\*a++\$ | shift |
| \$SSa | \*a++\$ | reduce $S \to a$ |
| \$SSS | \*a++\$ | shift |
| \$SSS\* | a++\$ | reduce $S \to SS*$ |
| \$SS | a++\$ | shift |
| \$SSa | ++\$ | reduce $S \to a$ |
| \$SSS | ++\$ | shift |
| \$SSS+ | +\$ | reduce $S \to SS+$ |
| \$SS | +\$ | shift |
| \$SS+ | \$ | reduce $S \to SS+$ |
| \$S | \$ | accept |

The handle is always on top of the stack when it is reduced.
