---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Type inference infers the types of unannotated expressions from how they are used (by unification). For append: append : list(a) x list(a) -> list(a) for every type a."
sources: ["Dragon book 2e sec. 6.5.4-6.5.5 (type inference and polymorphic functions, unification)", "KMS Chapter 6 slides 37-51"]
---
**Type inference** determines the type of a language construct from the way it is used, without declarations (Dragon book sec. 6.5.4). Types may contain **type variables**; the checker generates equations from the program and solves them by **unification** (sec. 6.5.5), or reports a type error if they cannot be satisfied. A function that works for all types gets a *polymorphic* type, $\forall \alpha.\ \ldots$.

**The function.**

$$\textbf{fun}\ append(x, y) = \textbf{if}\ null(x)\ \textbf{then}\ y\ \textbf{else}\ cons(hd(x), append(tl(x), y))$$

**Types of the built-ins** (each can be used at any $\alpha$): $null : list(\alpha) \to boolean$; $hd : list(\alpha) \to \alpha$; $tl : list(\alpha) \to list(\alpha)$; $cons : \alpha \times list(\alpha) \to list(\alpha)$; `if` $: boolean \times \gamma \times \gamma \to \gamma$.

**Derivation.** Let $x : \beta$, $y : \gamma$, $append : \beta \times \gamma \to \delta$ (inside its own body, $append$ is monomorphic).

1. $null(x)$ requires $\beta = list(\alpha_1)$; the result is $boolean$, as `if` needs.
2. The `then` branch is $y$, so the type of the `if` is $\gamma$, hence $\delta = \gamma$.
3. In the `else` branch: $hd(x) : \alpha_1$ (since $x : list(\alpha_1)$), $tl(x) : list(\alpha_1)$.
4. The recursive call $append(tl(x), y)$: its arguments must match $\beta \times \gamma$, so $list(\alpha_1) = \beta$ (consistent with step 1) and the result type is $\delta$.
5. $cons(hd(x), append(tl(x), y))$: the first argument has type $\alpha_1$, so $cons$ is used at $\alpha = \alpha_1$, and its second argument $append(\ldots) : \delta$ must equal $list(\alpha_1)$. The result is $list(\alpha_1)$.
6. The `else` branch has type $list(\alpha_1)$ and the `if` has type $\gamma$ (from the `then` branch), so $\gamma = list(\alpha_1)$ and $\delta = \gamma = list(\alpha_1)$.

**Result (type inference rule).**

$$append : \forall \alpha.\ list(\alpha) \times list(\alpha) \to list(\alpha)$$

i.e. $append$ takes two lists whose elements have the same type $\alpha$ and returns a list of that type; it is polymorphic. (If $x$ had a different element type than $y$, unification would fail.)
