---
marks: 20
topics: [first-order-logic]
kind: analysis
source: {page: 17}
note: "'eigth' is printed so."
---
Consider the knowledge base (KB) comprising eigth First-Order Logic sentences each converted into Conjunctive Normal Form shown in Figure for Q.6(a). Here

- A, B, C, D, E, F, G, H are predicates
- x, y, z, are variables
- $M_1, M_2, M_3, M_4$, are constants

Using Resolution, prove that $KB \models E(M_2)$.

1. $\neg F(M_1, x) \lor \neg G(x) \lor D(M_2, x, M_1)$
2. $\neg H(x, M_3) \lor C(x)$
3. $\neg G(x) \lor B(x)$
4. $F(M_1, M_4)$
5. $\neg A(x) \lor \neg B(y) \lor \neg C(z) \lor \neg D(x, y, z) \lor E(x)$
6. $G(M_4)$
7. $A(M_2)$
8. $H(M_1, M_3)$

*Figure for Q.6(a)*
