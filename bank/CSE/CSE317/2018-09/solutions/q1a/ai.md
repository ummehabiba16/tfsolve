---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "P(Q | e_1..e_k) = alpha sum_{h_1..h_r} P(Q, e_1..e_k, h_1..h_r), where each joint entry is the product of CPT entries (BN factorization); evaluate the nested sums depth-first, normalize over the values of Q. Cost O(n d^r) time, O(n) space."
sources: ["MNM slides Uncertainty-4-BN-INF and part_b_uncertainty (inference by enumeration)", "AIMA 4e sec. 13.3.1, Fig. 13.11 (ENUMERATION-ASK)"]
---
**Variables.** Query $Q$; evidence $E_1=e_1,\dots,E_k=e_k$; hidden variables $H_1,\dots,H_r$ (all the others).

**Step 1: write the query as a sum over the hidden variables** (marginalization):

$$P(Q\mid e_1,\dots,e_k)=\alpha\,P(Q,e_1,\dots,e_k)=\alpha\sum_{h_1}\sum_{h_2}\cdots\sum_{h_r}P(Q,e_1,\dots,e_k,h_1,\dots,h_r).$$

**Step 2: expand each joint entry with the chain rule of the Bayes net:**

$$P(x_1,\dots,x_n)=\prod_{i=1}^{n}P(x_i\mid\text{parents}(X_i)),$$

so every term is a product of CPT entries. Push each sum inside as far as possible: a factor that does not mention $h_j$ moves outside $\sum_{h_j}$.

**Step 3: evaluate for each value $q$ of $Q$.** Enumerate the hidden values depth-first (ENUMERATION-ASK), multiply the CPT entries and add.

**Step 4: normalize.** $\alpha=1/\sum_qP(q,e_1,\dots,e_k)$, so the results sum to 1.

**Example** (burglary network):

$$P(B\mid j,m)=\alpha\,P(B)\sum_eP(e)\sum_aP(a\mid B,e)\,P(j\mid a)\,P(m\mid a)=\langle0.284,\ 0.716\rangle.$$

**Complexity.** With $n$ variables and domain size $d$, the time is $O(n\,d^{\,r})$, exponential in the number of hidden variables, and the space is $O(n)$. The same sub-expressions are recomputed many times; variable elimination avoids this.
