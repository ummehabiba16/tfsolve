---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Taking the last row as P(dry | rain) = 0.25: P(sun, dry) = 0.85(0.9) = 0.765, P(rain, dry) = 0.15(0.25) = 0.0375; P(W | dry) = (sun 0.953, rain 0.047)."
sources: ["MNM slides Uncertainty-1-(quantifying) (Bayes' rule, normalization)", "Berkeley CS188 probability lecture (same W, D tables)"]
---
**Data.** $P(W)$: sun 0.85, rain 0.15. $P(D\mid W)$: $P(\text{wet}\mid\text{sun})=0.1$, $P(\text{dry}\mid\text{sun})=0.9$, $P(\text{wet}\mid\text{rain})=0.75$, $P(\text{dry}\mid\text{rain})=0.25$.

**Bayes' rule with normalization.**

$$P(W\mid\text{dry})=\alpha\,P(\text{dry}\mid W)\,P(W)$$

$$P(\text{sun},\text{dry})=0.9\times0.85=0.765$$

$$P(\text{rain},\text{dry})=0.25\times0.15=0.0375$$

$$P(\text{dry})=0.765+0.0375=0.8025$$

$$P(\text{sun}\mid\text{dry})=\frac{0.765}{0.8025}=\mathbf{0.953},\qquad P(\text{rain}\mid\text{dry})=\frac{0.0375}{0.8025}=\mathbf{0.047}$$

*Note:* the paper prints the last row of $P(D\mid W)$ as "wet, rain, 0.25". The conditional probabilities given rain must sum to 1 ($0.75+0.25$), so that row is taken to be **dry**, rain, 0.25.
