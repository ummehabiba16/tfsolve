---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Binary perceptron on bag-of-words features [BIAS, like, love, travel, rhymes, play, read], Adult = +1, Kid = -1, predict Adult if w.f >= 0. Updates: after 'love rhymes' w = [0,0,-1,0,-1,0,0]; after 'love to read' [1,0,0,0,-1,0,1]; after 'love rhymes' again [0,0,-1,0,-2,0,1]. Epoch 3 has no mistakes, so the final w = [0,0,-1,0,-2,0,1]."
sources: ["AIMA 4e sec. 19.6.3 (perceptron learning rule)", "Berkeley CS188 Perceptron lecture (binary perceptron on word features)"]
---
**Set-up.**

- *Features:* the bag of words over the vocabulary $[\text{BIAS},\ like,\ love,\ travel,\ rhymes,\ play,\ read]$, with BIAS $=1$ always. "to" is not a feature and is ignored.
- *Labels:* Adult $=+1$, Kid $=-1$.
- *Decision rule:* predict Adult if $\mathbf{w}\cdot\mathbf{f}\ge0$, otherwise Kid.
- *Update on a mistake:* $\mathbf{w}\leftarrow\mathbf{w}+y^*\,\mathbf{f}$ (add $\mathbf{f}$ if the true class is Adult, subtract it if Kid).
- *Initial weights:* $\mathbf{w}=[1,0,0,0,0,0,0]$.

| Sentence | $\mathbf{f}$ | Label |
|:--|:--|:-:|
| like to travel | [1,1,0,1,0,0,0] | Adult |
| love rhymes | [1,0,1,0,1,0,0] | Kid |
| love to play | [1,0,1,0,0,1,0] | Kid |
| love to read | [1,0,1,0,0,0,1] | Adult |

**Training passes.**

| Pass | Sentence | $\mathbf{w}\cdot\mathbf{f}$ | Predicted | True | New $\mathbf{w}$ |
|:-:|:--|:-:|:-:|:-:|:--|
| 1 | like to travel | 1 | Adult | Adult | unchanged |
| 1 | love rhymes | 1 | Adult | Kid | $\mathbf{w}-\mathbf{f}=[0,0,-1,0,-1,0,0]$ |
| 1 | love to play | $-1$ | Kid | Kid | unchanged |
| 1 | love to read | $-1$ | Kid | Adult | $\mathbf{w}+\mathbf{f}=[1,0,0,0,-1,0,1]$ |
| 2 | like to travel | 1 | Adult | Adult | unchanged |
| 2 | love rhymes | 0 | Adult | Kid | $\mathbf{w}-\mathbf{f}=[0,0,-1,0,-2,0,1]$ |
| 2 | love to play | $-1$ | Kid | Kid | unchanged |
| 2 | love to read | 0 | Adult | Adult | unchanged |
| 3 | like to travel | 0 | Adult | Adult | unchanged |
| 3 | love rhymes | $-3$ | Kid | Kid | unchanged |
| 3 | love to play | $-1$ | Kid | Kid | unchanged |
| 3 | love to read | 0 | Adult | Adult | unchanged |

Pass 3 makes no mistakes, so the perceptron has converged:

$$\mathbf{w}=[\text{BIAS}=0,\ like=0,\ love=-1,\ travel=0,\ rhymes=-2,\ play=0,\ read=1].$$

Interpretation: "rhymes" and "love" point to a kid, and "read" points to an adult.

*Notes:*

- *Assumptions:* Adult is the positive class and a score of exactly 0 is classified as Adult. The question's "multilevel" is read as the standard (single-layer) perceptron.
- A multiclass perceptron (one weight vector per class, predict the arg max) gives an equivalent result for two classes. With the opposite tie rule, the sequence of updates changes.
