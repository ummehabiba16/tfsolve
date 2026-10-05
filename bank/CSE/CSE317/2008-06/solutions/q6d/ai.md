---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Information gain is biased towards attributes with many values: an attribute like Date or ID splits the examples into tiny pure subsets, gets the maximum gain, but does not generalize. The gain ratio divides the gain by SplitInfo = -sum_v (|S_v|/|S|) log2 (|S_v|/|S|), which is large for many-valued splits, so such attributes are penalized. Example: with 1000 examples, ID has gain 1.0 but SplitInfo about 10 (ratio 0.1), while a binary attribute with gain 0.5 has ratio 0.5."
sources: ["AIMA 3e sec. 18.3.6 (multivalued attributes, gain ratio)", "Quinlan 1993 (C4.5)"]
---
**Problem with information gain for multi-valued attributes.**

$$\text{Gain}(S,A)=H(S)-\sum_v\frac{|S_v|}{|S|}H(S_v)$$

This favours attributes with **many values**. An attribute such as *Date*, *CustomerID* or *ExactTime* splits the training set into many tiny subsets, often singletons, which are trivially pure. Its remainder is about 0, so its gain is about the maximum $H(S)$, and it would be chosen as the root. But it is useless for predicting new examples (new dates never seen before): **overfitting**.

**Gain ratio** (Quinlan's C4.5) corrects this by dividing by the **split information**, the entropy of the partition itself:

$$\text{SplitInfo}(S,A)=-\sum_v\frac{|S_v|}{|S|}\log_2\frac{|S_v|}{|S|},\qquad\text{GainRatio}(S,A)=\frac{\text{Gain}(S,A)}{\text{SplitInfo}(S,A)}.$$

SplitInfo is large when $A$ splits the data into many small parts ($\log_2n$ for $n$ singletons), so such attributes are penalized, while attributes that split the data into a few large, informative groups are favoured.

**Example.** 1000 training examples, half positive.

| Attribute | Split | Gain | SplitInfo | Gain ratio |
|:--|:--|:-:|:-:|:-:|
| $ID$ (unique per example) | 1000 singletons | 1.0 (all pure) | $\log_21000\approx9.97$ | **0.10** |
| $A$ (Boolean, informative) | 500 / 500 | 0.5 | 1.0 | **0.50** |

Information gain would choose $ID$. The gain ratio correctly chooses $A$. (C4.5 also applies the ratio only to attributes with at least average gain, to avoid favouring attributes whose SplitInfo is close to 0.)
