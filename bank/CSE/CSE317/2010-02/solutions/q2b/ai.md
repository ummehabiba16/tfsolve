---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Gain(S,A) = H(S) - sum_v (|S_v|/|S|) H(S_v): the expected reduction in entropy, i.e. the information (bits) the test on A gives about the class. Problem: it favours many-valued attributes (e.g. Date or ID, which split the data into pure singletons, gain = H(S)) that do not generalize. Gain ratio = Gain / SplitInfo, SplitInfo = -sum_v (|S_v|/|S|) log2 (|S_v|/|S|), penalizing attributes that split the data into many small subsets."
sources: ["AIMA 3e sec. 18.3.4 (choosing attribute tests), 18.3.6", "Quinlan 1993 (C4.5, gain ratio)"]
---
**The gain criterion** (ID3). The entropy of a set $S$ with class proportions $p_c$ is $H(S)=-\sum_cp_c\log_2p_c$. The information gain of attribute $A$ is

$$\text{Gain}(S,A)=H(S)-\sum_{v\in\text{Values}(A)}\frac{|S_v|}{|S|}H(S_v).$$

At each node, choose the attribute with the largest gain.

**Physical meaning.** $H(S)$ is the average number of bits needed to identify the class of an example (its uncertainty). The remainder is the expected uncertainty left after testing $A$. So **Gain = the expected reduction in uncertainty (information, in bits) about the class obtained by knowing $A$**. It equals the mutual information $I(C;A)$. A high gain means the test separates the classes well, so the tree is short.

**The problem with gain.** It is **biased towards attributes with many values**. An attribute like *Date* or *CustomerID* splits $S$ into many singleton subsets, each pure, so its remainder is 0 and its gain is the maximum $H(S)$. Yet it is useless for new examples: it overfits.

**Gain ratio** (C4.5) normalizes by the information in the split itself:

$$\text{SplitInfo}(S,A)=-\sum_v\frac{|S_v|}{|S|}\log_2\frac{|S_v|}{|S|},\qquad \text{GainRatio}(S,A)=\frac{\text{Gain}(S,A)}{\text{SplitInfo}(S,A)}.$$

SplitInfo is large when $A$ splits the data into many small, equal parts ($\log_2n$ for $n$ singletons), so such attributes are **penalized**.

*Example:* with 1000 training examples (half positive), an *ID* attribute has the maximal Gain $=H(S)=1.0$. But it splits the data into 1000 singletons, so $\text{SplitInfo}=\log_21000\approx9.97$ and $\text{GainRatio}\approx0.10$. A genuinely useful binary attribute with Gain $=0.5$ and an even split has $\text{SplitInfo}=1$ and $\text{GainRatio}=0.5$, so it is now preferred. (On very small data sets the penalty may not be enough. C4.5 therefore also considers only attributes whose gain is at least average.)
