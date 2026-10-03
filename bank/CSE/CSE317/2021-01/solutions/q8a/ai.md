---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Class C = character; features F_i = binarized pixels of a size-normalized image; predict argmax_c P(c) prod_i P(f_i | c), using logs; train by counting. Against overfitting: Laplace smoothing (k tuned on validation), fewer or better features (down-sampling, zoning, HOG/PCA), more and augmented data."
sources: ["AIMA 4e sec. 12.6 and 20.2.2 (naive Bayes, Laplace smoothing)", "Berkeley CS188 Naive Bayes lecture (digit recognition)"]
---
**Model.** Class $C\in\{\text{the Bangla characters}\}$ (about 50 basic characters, more with compound letters). Input: a scanned character image.

**Pre-processing and features.** Binarize the image, crop it to the bounding box and resize it to a fixed grid, for example $28\times28$. Each pixel gives a feature $F_{ij}\in\{0,1\}$ (ink or no ink): $784$ features. Better features can be added: zoning densities, matra (head-line) and stroke features, HOG.

**Naive Bayes assumption.** Given the class, the features are independent:

$$P(C,F_1,\dots,F_n)=P(C)\prod_{i=1}^{n}P(F_i\mid C).$$

```text
                 C (character)
        /     /      |      \      \
      F1     F2     F3  ...  F783   F784     (pixels)
```

**Training** (maximum likelihood, by counting over the labeled training images):

$$P(c)=\frac{N_c}{N},\qquad P(F_i=1\mid c)=\frac{\text{count}(F_i=1,\ c)}{N_c}.$$

**Classification.**

$$\hat c=\arg\max_c\Big[\log P(c)+\sum_i\log P(f_i\mid c)\Big].$$

Logs avoid underflow from multiplying 784 small numbers.

**Avoiding overfitting.**

- **Laplace (add-$k$) smoothing:** $P(F_i=1\mid c)=\frac{\text{count}+k}{N_c+2k}$, so that a pixel never seen as ink for some class does not give probability 0 and veto that class. Choose $k$ on a **held-out validation set** (or by cross-validation): too small overfits, too large underfits.
- **Fewer, more robust features:** down-sample to a smaller grid, use zoning or projection features or PCA, or select informative pixels. Fewer parameters ($|C|\times n$) means less variance.
- **More data and data augmentation:** small shifts, rotations, stroke-width changes and noise, so the model learns the character's shape and not the quirks of one writer.
- Normalize size, position and slant before extracting features. Evaluate on a separate test set.
