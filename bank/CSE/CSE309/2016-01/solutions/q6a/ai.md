---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "With the rules var (<x,t> in rho gives rho |- x : t), + (both operands integer gives integer) and := (both sides same type gives void): rho |- x : integer, rho |- y : integer, rho |- x + y : integer, rho |- 2 : integer, rho |- (x + y) + 2 : integer, rho |- x := (x + y) + 2 : void, so the statement is typed correctly. For S -> S1 ; S2: S.type = void if S1.type = void and S2.type = void, else type_error."
sources: ["Dragon book 2e sec. 6.5.1 (Rules for Type Checking)", "KMS Chapter 6 slides 37-51"]
---
Notation: $\rho \vdash e : \tau$ means "in the environment $\rho$, expression $e$ has type $\tau$". A **Post system** is a set of inference rules: premises above the line, conclusion below.

$$\rho = \{\langle x, integer\rangle,\ \langle y, integer\rangle,\ \langle z, char\rangle,\ \langle 1, integer\rangle,\ \langle 2, integer\rangle\}$$

**Rules used (Post system).**

- **(var / const)** From $\langle x, \tau\rangle \in \rho$ conclude $\rho \vdash x : \tau$ (names and numeric constants are entries of $\rho$).
- **(plus)** From $\rho \vdash e_1 : integer$ and $\rho \vdash e_2 : integer$ conclude $\rho \vdash e_1 + e_2 : integer$.
- **(assign)** From $\rho \vdash x : \tau$ and $\rho \vdash e : \tau$ conclude $\rho \vdash x := e : void$.
- **(seq)** From $\rho \vdash S_1 : void$ and $\rho \vdash S_2 : void$ conclude $\rho \vdash S_1\,;\,S_2 : void$.

**(i) Proof that `x := x + y + 2` is typed correctly.** `x + y + 2` is `(x + y) + 2` (left associative):

1. $\langle x, integer\rangle \in \rho$, so $\rho \vdash x : integer$ (var).
2. $\langle y, integer\rangle \in \rho$, so $\rho \vdash y : integer$ (var).
3. From 1 and 2: $\rho \vdash x + y : integer$ (plus).
4. $\langle 2, integer\rangle \in \rho$, so $\rho \vdash 2 : integer$ (const).
5. From 3 and 4: $\rho \vdash (x + y) + 2 : integer$ (plus).
6. From 1 and 5, both of type $integer$: $\rho \vdash x := (x + y) + 2 : void$ (assign).

The statement has type $void$ (no type error), so it **is typed correctly**. (If `z`, of type `char`, appeared in the sum, the premise of (plus) would fail and the statement would be a type error.)

**(ii) Type checking for $S \to S_1\,;\,S_2$.**

Post-system expression (inference rule):

$$\frac{\rho \vdash S_1 : void \qquad \rho \vdash S_2 : void}{\rho \vdash S_1\,;\,S_2 : void}$$

Semantic rule (syntax-directed definition, with $type\_error$ for an error):

| Production | Semantic rule |
|:--|:--|
| $S \to S_1\ ;\ S_2$ | $S.type = (S_1.type == void\ \&\&\ S_2.type == void)\ ?\ void : type\_error$ |

That is, a sequence of statements is well typed (of type $void$) only if both statements are well typed; otherwise the error propagates.
