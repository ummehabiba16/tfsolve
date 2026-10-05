---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Tiling (Mezard & Nadal 1989) builds layers one by one: each layer has a master unit trained (pocket algorithm) to classify, plus ancillary units added until the layer is faithful (patterns of different classes never get the same internal representation). Each new master unit can at least copy the previous master and is trained to correct at least one more error, so the number of errors strictly decreases; after finitely many layers it is 0, and the last master classifies every training sample correctly."
sources: ["Mezard & Nadal 1989, Learning in feedforward layered networks: the tiling algorithm", "AIMA 3e sec. 18.7 (bibliographical notes: constructive algorithms)"]
---
**Tiling algorithm** (a constructive algorithm for networks of threshold units). Layers are added one at a time:

1. **Master unit.** In each new layer $L$, first train a single unit, the master, to classify the training samples as well as possible from the previous layer's outputs (with the pocket perceptron algorithm). Its output is the network's current answer.
2. **Ancillary units.** If the master still makes errors, add ancillary units to layer $L$ until the layer's representation is **faithful**: no two training samples of **different classes** produce the **same** output vector (internal representation) in that layer. Each new ancillary unit is trained on a subset of samples that share a representation but have mixed classes, splitting that subset.
3. Use layer $L$'s outputs as the input of layer $L+1$, and repeat.

**Why the final network classifies all training samples correctly.**

- **Faithfulness:** each layer maps samples of different classes to different representations, so the class is still a *function* of the layer's output. No information needed for classification is lost.
- **Errors strictly decrease:** the master unit of layer $L+1$ can always reproduce the previous master's output: copy that input with a large weight, threshold 0, which gives $e_L$ errors. Because the representation is faithful, there is a weight change that also fixes at least one misclassified sample (Mezard and Nadal prove such weights exist), so $e_{L+1}\le e_L-1$.
- The number of errors is a non-negative integer that decreases with every layer, so after a finite number of layers it reaches **0**. The master unit of the last layer then classifies **every training sample correctly**.

Convergence is guaranteed for any consistent (Boolean or binarized) training set. Generalization to new samples is not guaranteed.
