---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "A naive Bayes model assumes all features (effects) are conditionally independent given the class (cause): P(C, x_1..x_n) = P(C) prod_i P(x_i | C), so P(C | x) is proportional to P(C) prod_i P(x_i | C). Example: spam filtering with word features, or Cavity -> Toothache, Catch."
sources: ["AIMA 4e sec. 12.6 (naive Bayes models)"]
---
**Naive Bayes model.** A single "cause" (class) variable $C$ directly influences several "effect" (feature) variables $X_1,\dots,X_n$, and the effects are assumed **conditionally independent given the cause**:

$$P(C,X_1,\dots,X_n)=P(C)\prod_{i=1}^{n}P(X_i\mid C).$$

As a Bayesian network, $C$ is the only parent of every $X_i$. Classification by Bayes' rule:

$$P(C\mid x_1,\dots,x_n)=\alpha\,P(C)\prod_iP(x_i\mid C).$$

It is "naive" because the independence assumption is usually not exactly true, but the model works surprisingly well. It is compact ($O(n)$ parameters instead of $O(2^n)$) and trains easily by counting, with Laplace smoothing.

**Example (dentist).** $Cavity$ causes $Toothache$ and $Catch$ (the probe catching), and given $Cavity$ they are independent:

$$P(Cavity\mid toothache,catch)=\alpha\,P(Cavity)\,P(toothache\mid Cavity)\,P(catch\mid Cavity).$$

With $P(cavity)=0.2$, $P(toothache\mid cavity)=0.6$, $P(catch\mid cavity)=0.9$, $P(toothache\mid\neg cavity)=0.1$ and $P(catch\mid\neg cavity)=0.2$:

$$\alpha\langle0.2\times0.6\times0.9,\ 0.8\times0.1\times0.2\rangle=\alpha\langle0.108,\ 0.016\rangle=\langle0.871,\ 0.129\rangle.$$

**Another example: spam filtering.** $C\in\{\text{spam},\text{ham}\}$, $X_i$ = the words of the email, giving $P(\text{spam}\mid\text{words})\propto P(\text{spam})\prod_iP(w_i\mid\text{spam})$.
