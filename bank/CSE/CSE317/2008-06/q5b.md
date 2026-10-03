---
marks: 10
topics: [first-order-logic]
kind: analysis
source: {page: 75}
note: "'NumDigits (n, g)' is printed so in (ii) (probably 9)."
---
For each of the following sentences, is the accompanying sentence in First-Order Logic a good translation? If yes, answer "yes". If no, explain why not and then give a correct answer.

(i) No two people have the same social security number. $\neg\exists x,y,n\ (Person(x) \land Person(y)) \Rightarrow (HasSSN(x,n) \land HasSSN(y,n))$

(ii) Every one's social security number has nine digits. $\forall x,n\ Person(x) \Rightarrow (HasSSN(x,n) \land NumDigits(n,g))$
