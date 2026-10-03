---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Parameters: the prior P(Y) (P(spam), P(ham)) and, for every vocabulary word w, P(w | spam) and P(w | ham), estimated by (smoothed) counts. Query: P(Y | w_1..w_n) is proportional to P(Y) prod_i P(w_i | Y); compute in logs for both classes, normalize, and answer spam if P(spam | email) > 0.5 (or a higher threshold)."
sources: ["AIMA 4e sec. 12.6.1 (text classification with naive Bayes)", "Berkeley CS188 Naive Bayes lecture (spam filter)"]
---
**Model.** Class $Y\in\{\text{spam},\text{ham}\}$; words $W_1,\dots,W_n$ of the email, treated as a bag (order ignored) and conditionally independent given $Y$, all sharing one distribution $P(W\mid Y)$ over the vocabulary $V$:

$$P(Y,W_1,\dots,W_n)=P(Y)\prod_{i=1}^nP(W_i\mid Y).$$

**Parameters to learn** from labeled training emails:

- the **prior** $P(Y)$: $P(\text{spam})=\frac{\#\text{spam emails}}{\#\text{emails}}$, and $P(\text{ham})=1-P(\text{spam})$;
- the **word likelihoods** $P(w\mid\text{spam})$ and $P(w\mid\text{ham})$ for every $w\in V$, that is $2|V|$ numbers (minus normalization):

$$P(w\mid\text{spam})=\frac{\text{count}(w\text{ in spam})+k}{\text{total words in spam}+k|V|}$$

(Laplace-smoothed; similarly for ham).

**Answering the query** for a new email $w_1,\dots,w_n$:

$$P(\text{spam}\mid w_{1:n})=\frac{P(\text{spam})\prod_iP(w_i\mid\text{spam})}{P(\text{spam})\prod_iP(w_i\mid\text{spam})+P(\text{ham})\prod_iP(w_i\mid\text{ham})}$$

In practice, compare the sums of logs. Classify as spam if the posterior is above 0.5, or above a higher threshold, so that legitimate mail is rarely lost.
