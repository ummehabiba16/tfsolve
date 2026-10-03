---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Predict y' = +1 if w . f(x) >= 0, else -1. On a mistake, w <- w + y* f(x) (add the features for a missed positive, subtract them for a false positive); w <- w + alpha (y - h_w(x)) x in the 0/1 form. No change when correct."
sources: ["AIMA 4e sec. 19.6.3 (perceptron learning rule)", "Berkeley CS188 Perceptron lecture"]
---
**Classifier.** Feature vector $\mathbf{f}(x)$, including a constant BIAS feature $=1$, and weights $\mathbf{w}$. Then

$$y'=\begin{cases}+1 & \text{if }\mathbf{w}\cdot\mathbf{f}(x)\ge0\\-1 & \text{otherwise.}\end{cases}$$

**Weight update** (online, one example at a time):

1. Start with $\mathbf{w}=0$ (or small values).
2. For each training example $(x,y^*)$, compute the prediction $y'$.
3. If $y'=y^*$: no change.
4. If $y'\neq y^*$:

$$\mathbf{w}\leftarrow\mathbf{w}+y^*\,\mathbf{f}(x),$$

i.e. **add** $\mathbf{f}(x)$ when a positive example was predicted negative, and **subtract** it when a negative was predicted positive. After the update, $\mathbf{w}\cdot\mathbf{f}(x)$ moves by $\|\mathbf{f}(x)\|^2$ towards the correct side.

Equivalently, with outputs 0/1 and learning rate $\alpha$: $w_i\leftarrow w_i+\alpha\,(y-h_{\mathbf{w}}(\mathbf{x}))\,x_i$.

5. Repeat passes over the data until no mistakes are made (or for a fixed number of epochs).

If the data are linearly separable, the perceptron convergence theorem guarantees a separating $\mathbf{w}$ after finitely many mistakes. Otherwise use a decaying $\alpha$ or the averaged perceptron.
