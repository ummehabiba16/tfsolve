---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Variables F, O, R, T, Y, E, N, S, I, X (digits 0-9, all different, so a permutation of 0-9), F, T, S != 0, and carries C1-C4 in {0, 1, 2}. Column constraints: Y + 2N = Y + 10 C1; T + 2E + C1 = T + 10 C2; R + 2T + C2 = X + 10 C3; O + C3 = I + 10 C4; F + C4 = S. The constraint hypergraph joins each column constraint (a square node) to its letters and carries, plus one Alldiff hyperedge over all ten letters."
sources: ["AIMA 3e sec. 6.1.3 (cryptarithmetic, constraint hypergraph, Fig. 6.2)"]
---
**Variables.** The letters $F,O,R,T,Y,E,N,S,I,X$ (10 distinct letters), with domains $\{0,\dots,9\}$; leading letters are non-zero, $F,T,S\neq0$. Auxiliary **carry** variables $C_1,C_2,C_3,C_4$ (adding three numbers, a carry can be 0, 1 or 2).

```text
    F O R T Y
        T E N
  +     T E N
  -----------
    S I X T Y
```

**Addition (column) constraints**, from right to left:

1. $Y+N+N=Y+10\,C_1$, i.e. $2N=10\,C_1$
2. $T+E+E+C_1=T+10\,C_2$, i.e. $2E+C_1=10\,C_2$
3. $R+T+T+C_2=X+10\,C_3$
4. $O+C_3=I+10\,C_4$
5. $F+C_4=S$

**All-different constraint.** $Alldiff(F,O,R,T,Y,E,N,S,I,X)$: there are 10 letters, so they use each digit exactly once.

**Constraint hypergraph.** Variables are circles, constraints are squares, and each square is joined to the variables it constrains:

```text
   (N)   (Y)       (E)          (R)  (T)   (X)        (O)  (I)        (F)  (S)
     \   /          |  \          \   |   /             \   /            \   /
      [1]---(C1)---[2]--(C2)--------[3]-----(C3)---------[4]----(C4)-------[5]
             (T also links to [2])

   [Alldiff] = one hyperedge joining all 10 letters F,O,R,T,Y,E,N,S,I,X
```

- [1] links $N$, $Y$, $C_1$.
- [2] links $E$, $T$, $C_1$, $C_2$.
- [3] links $R$, $T$, $X$, $C_2$, $C_3$.
- [4] links $O$, $I$, $C_3$, $C_4$.
- [5] links $F$, $S$, $C_4$.
- The Alldiff hyperedge links all ten letters.

(The solution, not required, is $29786+850+850=31486$.)
