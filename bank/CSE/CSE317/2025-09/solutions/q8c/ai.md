---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "KB: forall x [Roman(x) and Know(x,Marcus)] => [Hate(x,Caesar) or forall y ((exists z Hate(y,z)) => ThinkCrazy(x,y))]; Roman(Hulk). CNF: one clause plus Roman(Hulk). Adding Hate(Hulk,Caesar) gives no empty clause, so 'Hulk does not hate Caesar' is NOT entailed."
sources: ["AIMA 4e sec. 9.5 (resolution, conversion to CNF)", "Rich & Knight, Artificial Intelligence, ch. 5 (Marcus/Caesar example)"]
---
**(i) KB in first-order logic.** Predicates: $Roman(x)$, $Know(x,y)$, $Hate(x,y)$, $ThinkCrazy(x,y)$ ("$x$ thinks $y$ is crazy"). Constants: $Marcus$, $Caesar$, $Hulk$.

1. All Romans who know Marcus either hate Caesar or think anyone who hates someone is crazy:

$$\forall x\,\big[Roman(x)\land Know(x,Marcus)\big]\Rightarrow\Big[Hate(x,Caesar)\lor\forall y\,\big(\exists z\,Hate(y,z)\Rightarrow ThinkCrazy(x,y)\big)\Big]$$

2. Hulk is Roman: $Roman(Hulk)$.

**(ii) Conversion to CNF** (sentence 1).

*Eliminate $\Rightarrow$:*

$$\forall x\,\neg[Roman(x)\land Know(x,Marcus)]\lor Hate(x,Caesar)\lor\forall y\,\big(\neg\exists z\,Hate(y,z)\lor ThinkCrazy(x,y)\big)$$

*Move $\neg$ inwards* (De Morgan, $\neg\exists z\equiv\forall z\,\neg$):

$$\forall x\,\neg Roman(x)\lor\neg Know(x,Marcus)\lor Hate(x,Caesar)\lor\forall y\,\big(\forall z\,\neg Hate(y,z)\lor ThinkCrazy(x,y)\big)$$

*Standardize variables / Skolemize:* the variables are already distinct and there are no existential quantifiers, so no Skolem functions are needed.

*Drop the universal quantifiers* (all variables are universal):

$$C_1:\ \neg Roman(x)\lor\neg Know(x,Marcus)\lor Hate(x,Caesar)\lor\neg Hate(y,z)\lor ThinkCrazy(x,y)$$

$$C_2:\ Roman(Hulk)$$

**(iii) Is "Hulk does not hate Caesar" entailed?** The goal is $\alpha=\neg Hate(Hulk,Caesar)$. Resolution refutation: add $\neg\alpha$,

$$C_3:\ Hate(Hulk,Caesar)$$

and try to derive the empty clause.

- $C_3$ with $C_1$ on $\neg Hate(y,z)$, $\theta=\{y/Hulk,\ z/Caesar\}$:
$C_4:\ \neg Roman(x)\lor\neg Know(x,Marcus)\lor Hate(x,Caesar)\lor ThinkCrazy(x,Hulk)$
- $C_4$ with $C_2$, $\theta=\{x/Hulk\}$:
$C_5:\ \neg Know(Hulk,Marcus)\lor Hate(Hulk,Caesar)\lor ThinkCrazy(Hulk,Hulk)$
- $C_1$ with $C_2$, $\{x/Hulk\}$, gives $\neg Know(Hulk,Marcus)\lor Hate(Hulk,Caesar)\lor\neg Hate(y,z)\lor ThinkCrazy(Hulk,y)$, and with $C_3$ again $C_5$.

No further progress is possible. $Know$ occurs only negatively and $ThinkCrazy$ only positively in the whole clause set (they are *pure literals*). Every clause derived from $C_1$ keeps $\neg Know(\cdot,Marcus)$, and nothing can resolve it away. The process saturates **without the empty clause**.

Since resolution is refutation-complete, $KB\land\neg\alpha$ is satisfiable. Indeed, a model is: Hulk is Roman, Hulk hates Caesar, and nobody knows Marcus. It satisfies $C_1$, $C_2$ and $C_3$.

**Answer:** $KB\not\models\neg Hate(Hulk,Caesar)$. **"Hulk does not hate Caesar" cannot be proved** from the KB. (Neither can "Hulk hates Caesar": we do not know whether Hulk knows Marcus.)

*Note:* the paper writes "Ceaser" in (iii); it is taken to be the same constant $Caesar$.
