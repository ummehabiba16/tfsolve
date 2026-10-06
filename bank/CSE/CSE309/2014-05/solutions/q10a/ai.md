---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "append : list(a) x list(a) -> list(a) for every type a, obtained by unifying x : list(a1) (from null(x)), y : list(a1) (the then-branch and the type of cons(...)) and the result list(a1)."
sources: ["KMS Chapter 6 slides 37-51", "Dragon book 2e sec. 6.5.4-6.5.5 (type inference, unification)"]
---
**Type inference** finds the type of an expression or function from the way its parts are used, without declarations; the checker writes equations between type expressions (containing type variables) and solves them by **unification** (Dragon book sec. 6.5.4-6.5.5). A function that works for any element type has a **polymorphic** type, $\forall\alpha.\ \ldots$

The function:

```text
fun append(x, y) = if null(x) then y
                   else cons(hd(x), append(tl(x), y))
```

Types of the built-ins (for any $\alpha$): $null : list(\alpha) \to boolean$; $hd : list(\alpha) \to \alpha$; $tl : list(\alpha) \to list(\alpha)$; $cons : \alpha \times list(\alpha) \to list(\alpha)$ (concatenates the element $src$ in front of the list $dest$); `if` $: boolean \times \gamma \times \gamma \to \gamma$.

**Inference.** Let $x : \beta$, $y : \gamma$, $append : \beta \times \gamma \to \delta$.

1. $null(x)$ must be applied to a list: unify $\beta = list(\alpha_1)$.
2. The `then` branch is $y$, so the type of the whole `if` is $\gamma$ and $\delta = \gamma$.
3. In the `else` branch, $hd(x) : \alpha_1$ and $tl(x) : list(\alpha_1)$.
4. The call $append(tl(x), y)$ requires arguments of types $\beta \times \gamma$: $list(\alpha_1) = \beta$ (already known); its result has type $\delta$.
5. $cons(hd(x), append(tl(x), y))$: $cons$ is used at $\alpha = \alpha_1$, and its second argument has type $\delta$, which must be $list(\alpha_1)$. The `else` branch has type $list(\alpha_1)$.
6. Both branches must have the same type: $\gamma = list(\alpha_1)$, and $\delta = list(\alpha_1)$.

**Result:**

$$append : \forall \alpha.\ list(\alpha) \times list(\alpha) \to list(\alpha)$$

Both arguments are lists with elements of the same type and the result is a list of that type.
