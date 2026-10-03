---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Fit h_w(x) = w0 + w1 x by minimizing the squared loss Loss(w) = sum_j (y_j - h_w(x_j))^2: start from any w, repeat w_i <- w_i - alpha dLoss/dw_i (simultaneously for w0, w1) until convergence. The step size alpha matters: too small converges very slowly; too large overshoots and oscillates or diverges; a decaying alpha or line search helps."
sources: ["AIMA 4e sec. 19.6.1-19.6.2 (univariate linear regression, gradient descent)"]
---
**Problem.** Univariate linear regression fits $h_{\mathbf{w}}(x)=w_1x+w_0$ to the data $\{(x_j,y_j)\}_{j=1}^N$ by minimizing the squared-error loss

$$Loss(\mathbf{w})=\sum_{j=1}^{N}\big(y_j-(w_1x_j+w_0)\big)^2.$$

**Gradient descent.** The loss is a convex bowl over the weight space. Start anywhere and repeatedly step downhill, against the gradient:

```text
w <- any point in the parameter space (e.g. w0 = w1 = 0)
loop until convergence (the change in w or in the loss is tiny):
    for each w_i in w (updated simultaneously):
        w_i <- w_i - alpha * dLoss(w) / dw_i
```

Here $\alpha$ is the **step size (learning rate)**. Each step moves the line slightly so that the total error decreases. *Batch* gradient descent uses all $N$ examples per step; *stochastic* gradient descent uses one random example (or a mini-batch) per step, which is faster for large data.

**Effect of the step size $\alpha$.**

- **Too small:** each step barely changes $\mathbf{w}$, so convergence is very slow (many iterations).
- **Too large:** the step **overshoots** the minimum. The weights oscillate from one side of the bowl to the other, or **diverge** (the loss grows without bound).
- **Well chosen:** fast, steady decrease to the minimum.

In practice, $\alpha$ is tuned (for example on a validation set), decreased over time (e.g. $\alpha=1000/(1000+t)$, which also guarantees convergence for SGD), or chosen by line search at each step.
