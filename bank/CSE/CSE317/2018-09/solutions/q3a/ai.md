---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Score each result with w . f(query, doc). From the user's feedback (a clicked result ranked below an unclicked one), form pairs (preferred d+, other d-); if w . f(d+) <= w . f(d-), update w <- w + alpha (f(d+) - f(d-)) (ranking perceptron); re-rank by the new scores."
sources: ["AIMA 4e sec. 19.6.3 (perceptron rule)", "Collins 2002 / Joachims 2002 (perceptron and SVM ranking from clickthrough data)", "Berkeley CS188 Perceptron lecture (ranking)"]
---
**Ranking function.** For a query $q$, represent each search result $d$ by a feature vector $\mathbf{f}(q,d)$: for example Google's rank position, query-term matches in the title and URL, PageRank, freshness, whether you clicked this site before. Score it with

$$\text{score}(d)=\mathbf{w}\cdot\mathbf{f}(q,d)$$

and re-rank the results by decreasing score.

**Training data: pairwise preferences.** From feedback, take pairs where result $d^+$ should be ranked above $d^-$. A typical source: you clicked $d^+$ but skipped $d^-$, which was shown above it.

**Perceptron update (ranking perceptron).** For each preference pair:

- if $\mathbf{w}\cdot\mathbf{f}(d^+)>\mathbf{w}\cdot\mathbf{f}(d^-)$, the order is correct: do nothing;
- otherwise (wrong order):

$$\mathbf{w}\leftarrow\mathbf{w}+\alpha\,\big(\mathbf{f}(d^+)-\mathbf{f}(d^-)\big).$$

This is the ordinary perceptron rule applied to the difference vector $\mathbf{x}=\mathbf{f}(d^+)-\mathbf{f}(d^-)$ with label $+1$: it raises the score of the preferred document and lowers the other's. Features where the preferred document is higher gain weight.

Alternatively, with a list of results and a single target $d^\ast$, update against the current top result $\hat d$: $\mathbf{w}\leftarrow\mathbf{w}+\mathbf{f}(d^\ast)-\mathbf{f}(\hat d)$, as in the structured or multiclass perceptron.

Repeat over all pairs (several passes, or online as new clicks arrive) until the pairs are ordered correctly. Averaging the weights (averaged perceptron) gives more stable rankings.
