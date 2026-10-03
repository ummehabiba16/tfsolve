---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Bag of words: an email is a multiset of words W_1..W_n, assumed independent given the class; P(spam | words) is proportional to P(spam) prod_i P(w_i | spam), with each P(w | class) estimated by word counts; predict the larger posterior (computed with logs). Zero counts would make the product 0, so use Laplace (add-k) smoothing: P(w | c) = (count(w, c) + k) / (N_c + k|V|)."
sources: ["AIMA 4e sec. 12.6.1 (text classification with naive Bayes) and 20.2.2 (Laplace smoothing)", "Berkeley CS188 Naive Bayes lecture (spam filter)"]
---
**Bag-of-words naive Bayes** (5 marks).

- *Model:* class $Y\in\{\text{spam},\text{ham}\}$. The email is the sequence of its words $W_1,\dots,W_n$. Word order is ignored ("bag"), and each word is assumed independent of the others given the class, with the same distribution $P(W\mid Y)$ at every position:

$$P(Y,W_1,\dots,W_n)=P(Y)\prod_{i=1}^{n}P(W_i\mid Y).$$

- *Training* (maximum likelihood) on labeled emails: $P(\text{spam})=\frac{\#\text{spam emails}}{\#\text{emails}}$, and

$$P(w\mid\text{spam})=\frac{\text{count of word }w\text{ in spam emails}}{\text{total words in spam emails}}$$

(and similarly for ham).

- *Classification:* compare

$$\log P(\text{spam})+\sum_i\log P(w_i\mid\text{spam})\quad\text{and}\quad\log P(\text{ham})+\sum_i\log P(w_i\mid\text{ham}).$$

Choose the larger (or threshold the posterior; a high threshold avoids losing real mail). Logs prevent underflow.

**Words with zero probability** (5 marks). If a word, say "free", never occurs in the ham training emails, then $P(\text{free}\mid\text{ham})=0$. Any email containing "free" then gets $P(\text{ham}\mid\text{email})=0$, however strong the other evidence: one unseen word vetoes the class (overfitting to the training counts). Words never seen in training at all make both classes 0.

**Fix: Laplace (add-$k$) smoothing.** Pretend every word was seen $k$ extra times in each class:

$$P(w\mid c)=\frac{\text{count}(w,c)+k}{N_c+k\,|V|},$$

where $N_c$ is the total word count of class $c$ and $|V|$ is the vocabulary size. Choose $k$ (often 1) on held-out validation data. Words never seen in any class (outside the vocabulary) can simply be ignored, or mapped to an "unknown" token.
