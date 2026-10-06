---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "SDD: S -> id := E {S.type = (id.type == E.type) ? void : type_error}; S -> S1 ; S2 {S.type = (S1.type == void && S2.type == void) ? void : type_error}; S -> while E do S1 {S.type = (E.type == boolean && S1.type == void) ? void : type_error}. Post-system rules: rho |- id : t and rho |- E : t give rho |- id := E : void; rho |- S1 : void and rho |- S2 : void give rho |- S1 ; S2 : void; rho |- E : boolean and rho |- S1 : void give rho |- while E do S1 : void."
sources: ["KMS Chapter 6 slides 37-51 (type checking)", "Dragon book 2e sec. 6.5.1"]
---
Notation: $\rho \vdash e : \tau$ means "in the environment $\rho$ (a set of $\langle name, type\rangle$ pairs), $e$ has type $\tau$". Statements have type $void$ when they are correct and $type\_error$ otherwise (Dragon book sec. 6.5.1).

**(a) $S \to \textbf{id} := E$**

Syntax-directed definition:

| Production | Semantic rule |
|:--|:--|
| $S \to \textbf{id} := E$ | $S.type = (\textbf{id}.type == E.type)\ ?\ void : type\_error$ |

where $\textbf{id}.type$ is found by looking the name up in the symbol table. Post-system rule (a statement is correct if the variable and the expression have the same type):

$$\frac{\rho \vdash \textbf{id} : \tau \qquad \rho \vdash E : \tau}{\rho \vdash \textbf{id} := E : void}$$

**(b) $S \to S_1 ; S_2$**

| Production | Semantic rule |
|:--|:--|
| $S \to S_1\ ;\ S_2$ | $S.type = (S_1.type == void\ \&\&\ S_2.type == void)\ ?\ void : type\_error$ |

$$\frac{\rho \vdash S_1 : void \qquad \rho \vdash S_2 : void}{\rho \vdash S_1 ; S_2 : void}$$

**(c) $S \to \textbf{while}\ E\ \textbf{do}\ S_1$**

| Production | Semantic rule |
|:--|:--|
| $S \to \textbf{while}\ E\ \textbf{do}\ S_1$ | $S.type = (E.type == boolean\ \&\&\ S_1.type == void)\ ?\ void : type\_error$ |

$$\frac{\rho \vdash E : boolean \qquad \rho \vdash S_1 : void}{\rho \vdash \textbf{while}\ E\ \textbf{do}\ S_1 : void}$$

The expressions inside are typed by their own rules, for instance: $\langle x, \tau\rangle \in \rho$ gives $\rho \vdash x : \tau$; $\rho \vdash e_1 : integer$ and $\rho \vdash e_2 : integer$ give $\rho \vdash e_1 + e_2 : integer$ and $\rho \vdash e_1 < e_2 : boolean$.

**Proof for an example program** `while x < 10 do x := x + 1; y := x` with $\rho = \{\langle x, integer\rangle, \langle y, integer\rangle, \langle 1, integer\rangle, \langle 10, integer\rangle\}$:

1. $\rho \vdash x : integer$ and $\rho \vdash 10 : integer$ (names and constants in $\rho$).
2. $\rho \vdash x < 10 : boolean$ (relational rule, from 1).
3. $\rho \vdash x + 1 : integer$ (plus, with $x$ and $1$), so $\rho \vdash x := x + 1 : void$ (rule (a)).
4. $\rho \vdash \textbf{while}\ x < 10\ \textbf{do}\ x := x + 1 : void$ (rule (c), from 2 and 3).
5. $\rho \vdash y := x : void$ (rule (a), both are $integer$).
6. $\rho \vdash (\textbf{while}\ \ldots) ; (y := x) : void$ (rule (b), from 4 and 5).

The program is correctly typed. If the condition were `x + 1` (type $integer$), rule (c) could not be applied and the statement would be a type error.
