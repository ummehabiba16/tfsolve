---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "h_w(x) = 1 if w . x >= 0 else 0 (with x0 = 1 for the bias). For each example, w_i <- w_i + alpha (y - h_w(x)) x_i: no change when correct; add alpha x on a false negative, subtract on a false positive. Converges if the data are linearly separable."
sources: ["AIMA 4e sec. 19.6.3 (linear classifiers with a hard threshold, perceptron learning rule)", "CS50 AI Lecture 4"]
---
**Perceptron (linear threshold unit).** For input $\mathbf{x}=(x_1,\dots,x_n)$, add a dummy input $x_0=1$ so that $w_0$ acts as the bias (threshold):

$$h_{\mathbf{w}}(\mathbf{x})=\text{Threshold}(\mathbf{w}\cdot\mathbf{x})=\begin{cases}1 & \text{if } \sum_{i=0}^{n}w_ix_i\ge0\\ 0 & \text{otherwise}\end{cases}$$

The decision boundary $\mathbf{w}\cdot\mathbf{x}=0$ is a line (hyperplane) separating class 1 from class 0.

**Perceptron learning rule.** Start with $\mathbf{w}$ = 0 (or small random values). Take the training examples $(\mathbf{x},y)$ one at a time, and update every weight:

$$w_i\leftarrow w_i+\alpha\,\big(y-h_{\mathbf{w}}(\mathbf{x})\big)\,x_i,\qquad i=0,1,\dots,n,$$

where $\alpha$ is the learning rate. There are three cases:

| Prediction | $y-h$ | Update | Effect |
|:--|:-:|:--|:--|
| correct ($h=y$) | 0 | none | |
| false negative ($y=1$, $h=0$) | $+1$ | $w_i\leftarrow w_i+\alpha x_i$ | $\mathbf{w}\cdot\mathbf{x}$ increases, toward the output 1 |
| false positive ($y=0$, $h=1$) | $-1$ | $w_i\leftarrow w_i-\alpha x_i$ | $\mathbf{w}\cdot\mathbf{x}$ decreases, toward the output 0 |

Only inputs with $x_i\neq0$ change their weight. A weight changes more for a larger input, which is the input that contributed most to the error.

Repeat over the training set (epochs) until all examples are classified correctly or an epoch limit is reached.

**Example.** $\mathbf{w}=(0,0,0)$, $\alpha=1$, example $\mathbf{x}=(1,\,2,\,1)$ (with $x_0=1$) and $y=0$. Then $\mathbf{w}\cdot\mathbf{x}=0\ge0$, so $h=1$: a false positive. The update is $\mathbf{w}\leftarrow\mathbf{w}-\mathbf{x}=(-1,-2,-1)$, after which $\mathbf{w}\cdot\mathbf{x}=-6<0$ and the example is correct.

**Convergence (perceptron convergence theorem).** If the data are **linearly separable**, the rule finds a separating $\mathbf{w}$ after a finite number of updates. If they are not (for example XOR), it never settles. Then a decaying $\alpha$, the pocket algorithm, or a logistic (soft-threshold) unit trained by gradient descent is used.
