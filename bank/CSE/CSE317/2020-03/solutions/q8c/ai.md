---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "(i) Supervised learning: learn h approximating f from labeled pairs (x, y); classification or regression; judged on unseen test data. (ii) Overfitting: the model fits noise or accidental patterns in the training data (low training error, high test error); caused by too complex a model or too little data; cured by regularization, pruning, validation and more data."
sources: ["AIMA 4e sec. 19.1-19.2 and 19.4", "MNM slides Learning Theory (ERM)-1 (supervised learning, ERM: overfitting)"]
---
**(i) Supervised learning.** The agent is given a training set of **labeled** examples $(x_1,y_1),\dots,(x_N,y_N)$, where each $y_j=f(x_j)$ is produced by an unknown function $f$. The task is to find a hypothesis $h$ from a hypothesis space $H$ that approximates $f$ well, so that it predicts the correct $y$ for **new, unseen** $x$.

- *Classification:* the output is one of a finite set of classes (spam / not spam, digit 0-9).
- *Regression:* the output is a number (house price, temperature).
- *Examples of methods:* decision trees, linear and logistic regression, naive Bayes, neural networks, $k$-NN.
- Learning usually minimizes the empirical loss on the training set (ERM). Quality is measured on a separate **test set**: generalization is what counts.
- Contrast: in *unsupervised* learning there are no labels (clustering); in *reinforcement* learning the agent only gets rewards.

**(ii) Overfitting.** A hypothesis **overfits** when it fits the training data very closely, including noise and accidental regularities, but performs poorly on new data. Its training error is low and its test error is high.

- *Causes:* a hypothesis space that is too expressive for the amount of data (a high-degree polynomial through every point, a fully grown decision tree), noisy labels, irrelevant attributes, too little data.
- *Symptom:* as model complexity grows, training error keeps falling while validation error starts to rise.
- *Remedies:* simpler models (Ockham's razor), regularization (penalize complexity), decision-tree pruning or early stopping, cross-validation for model selection, more training data, ensembles.
