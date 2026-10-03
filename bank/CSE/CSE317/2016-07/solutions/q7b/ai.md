---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "ID3 chooses, at each node, the attribute with the highest information gain, Gain(A) = H(S) - sum_v (|S_v|/|S|) H(S_v) with H(S) = -sum_c p_c log2 p_c, i.e. the largest expected reduction in entropy (most important attribute first); it partitions the examples by its values and recurses (C4.5 uses the gain ratio to avoid favouring many-valued attributes)."
sources: ["AIMA 4e sec. 19.3.3 (choosing attribute tests)", "Quinlan 1986 (ID3)", "MNM slides Lecture 10 - Machine Learning - Decision Tree"]
---
**Principle.** ID3 builds the tree top-down and greedily. At each node it picks the **most important** attribute: the one that best separates the classes, so that the remaining subsets are as pure as possible. Importance is measured by **information gain**, the expected reduction in entropy.

**Entropy** of a set $S$ with class proportions $p_c$:

$$H(S)=-\sum_cp_c\log_2p_c.$$

It is 0 for a pure set and 1 bit for a 50/50 Boolean split.

**Information gain** of attribute $A$, whose values $v$ split $S$ into subsets $S_v$:

$$\text{Gain}(S,A)=H(S)-\underbrace{\sum_{v\in\text{values}(A)}\frac{|S_v|}{|S|}H(S_v)}_{\text{Remainder}(A)}.$$

**Procedure.**

1. Compute $\text{Gain}(S,A)$ for every remaining attribute.
2. Choose $A^*=\arg\max_A\text{Gain}(S,A)$ as the test at this node.
3. Partition the training set by the values of $A^*$, and create one branch per value.
4. Recurse on each subset with the remaining attributes. Stop when a subset is pure (a leaf with that class), when no attributes are left (plurality class), or when no examples are left (plurality class of the parent).

*Example:* in PlayTennis, $\text{Gain}(\text{Outlook})=0.247$ beats Humidity (0.152), Wind (0.048) and Temperature (0.029), so Outlook becomes the root.

*Note:* information gain favours attributes with many values (e.g. a Date attribute splits the data into singletons). C4.5 uses the **gain ratio** $\text{Gain}/\text{SplitInfo}$ to correct for this.
