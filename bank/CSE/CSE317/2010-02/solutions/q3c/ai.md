---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "With a discontinuous (step or sign) activation, the error is a step function of the weights: the gradient is zero almost everywhere and undefined at the jump, so gradient descent / backpropagation cannot tell how to change the hidden weights. Solution: use a smooth, differentiable activation (sigmoid, tanh, or ReLU in practice), or for a single layer the perceptron rule."
sources: ["AIMA 3e sec. 18.6.4 and 18.7.4 (logistic regression, back-propagation)"]
---
**Problem.** A discontinuous activation such as the hard threshold (step or sign function) has derivative **zero everywhere except at the jump, where it is undefined**. The network's output, and hence its error, is then piecewise constant in the weights.

- Gradient-based learning (gradient descent, **back-propagation**) needs $\partial\text{Error}/\partial w$. With a step function this is 0 almost everywhere, so the gradient gives no information on how to change the weights, especially those of hidden units, whose effect reaches the output only through other step units.
- Small weight changes usually do not change the output at all, then suddenly flip it: learning cannot make gradual progress.
- (Also, outputs are 0/1 only, with no measure of confidence.)

**Solution.** Replace the step with a **smooth, differentiable** activation:

- **sigmoid (logistic)** $g(x)=\frac{1}{1+e^{-x}}$, with $g'(x)=g(x)(1-g(x))$;
- **tanh**;
- in modern networks **ReLU** $\max(0,x)$, which is differentiable almost everywhere with a non-zero gradient for positive inputs.

The error then becomes a differentiable function of all the weights, and back-propagation can compute the gradients layer by layer. (For a single layer of threshold units, the perceptron learning rule can be used instead of gradients.)
