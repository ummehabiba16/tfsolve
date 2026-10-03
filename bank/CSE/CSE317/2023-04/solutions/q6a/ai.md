---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Add the negated goal 9: not E(M2). Resolve 9+5 {x/M2}, then with 7; 1+4 {x/M4}, then with 6, gives D(M2,M4,M1); resolve {y/M4, z/M1}; 3+6 gives B(M4); 2+8 gives C(M1); the empty clause follows, so KB entails E(M2)."
sources: ["AIMA 4e sec. 9.5 (resolution refutation, unification)"]
---
**Refutation.** To prove $KB\models E(M_2)$, add the negated goal and derive the empty clause $\square$.

9. $\neg E(M_2)$ (negated goal)

| Step | Resolve | Unifier | Resolvent |
|:-:|:--|:--|:--|
| 10 | 9, 5 | $\{x/M_2\}$ | $\neg A(M_2)\lor\neg B(y)\lor\neg C(z)\lor\neg D(M_2,y,z)$ |
| 11 | 10, 7 | $\{\}$ | $\neg B(y)\lor\neg C(z)\lor\neg D(M_2,y,z)$ |
| 12 | 1, 4 | $\{x/M_4\}$ | $\neg G(M_4)\lor D(M_2,M_4,M_1)$ |
| 13 | 12, 6 | $\{\}$ | $D(M_2,M_4,M_1)$ |
| 14 | 11, 13 | $\{y/M_4,\ z/M_1\}$ | $\neg B(M_4)\lor\neg C(M_1)$ |
| 15 | 3, 6 | $\{x/M_4\}$ | $B(M_4)$ |
| 16 | 14, 15 | $\{\}$ | $\neg C(M_1)$ |
| 17 | 2, 8 | $\{x/M_1\}$ | $C(M_1)$ |
| 18 | 16, 17 | $\{\}$ | $\square$ (empty clause) |

The clause variables are standardized apart before each step (each clause's $x$ is independent). For example, in step 12, $F(M_1,M_4)$ unifies with $\neg F(M_1,x)$ by $x/M_4$, which also turns $\neg G(x)$ into $\neg G(M_4)$.

The empty clause is derived, so $KB\land\neg E(M_2)$ is unsatisfiable. Hence **$KB\models E(M_2)$**.

**Proof tree** (read upwards):

```text
               []
             /    \
        ~C(M1)    C(M1) <- 2,8 {x/M1}
          /    \
~B(M4) v ~C(M1)  B(M4) <- 3,6 {x/M4}
     /       \
~B(y)v~C(z)v~D(M2,y,z)    D(M2,M4,M1) <- (1,4 {x/M4}), 6
     |
~A(M2)v~B(y)v~C(z)v~D(M2,y,z) <- 9,5 {x/M2}, then 7 removes ~A(M2)
```
