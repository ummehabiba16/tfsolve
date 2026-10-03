---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "The statement gives P(not cr | cc) = 0.9 directly, so P(cr | cc) = 0.1. Check: P(cc) = P(cc|cr)P(cr)/P(cr|cc) = 0.4 x 0.05/0.1 = 0.2, and P(cc | not cr) = 0.18/0.95 = 0.19, consistent."
sources: ["MNM slides Uncertainty-1-(quantifying) (Bayes rule)", "AIMA 4e sec. 12.5"]
---
**Given.** $P(cr)=0.05$, $P(cc\mid cr)=0.40$, and "among all chronic-cough patients, 9 out of 10 are non-cancerous": $P(\neg cr\mid cc)=0.9$.

**Answer.**

$$P(cr\mid cc)=1-P(\neg cr\mid cc)=1-0.9=\mathbf{0.1}\ (10\%).$$

**Check with Bayes' rule.**

$$P(cr\mid cc)=\frac{P(cc\mid cr)P(cr)}{P(cc)}\ \Rightarrow\ P(cc)=\frac{0.4\times0.05}{0.1}=0.2.$$

$$P(cc,\neg cr)=0.2-0.02=0.18\ \Rightarrow\ P(cc\mid\neg cr)=\frac{0.18}{0.95}=0.189.$$

All the numbers are consistent. A chronic cough doubles the probability of cancer, from the prior 5% to **10%**, but cancer is still unlikely.

*Note:* reading the statement instead as $P(cc\mid\neg cr)=0.9$ would give $P(cr\mid cc)=\frac{0.02}{0.02+0.855}=0.023$. The wording "among all chronic cough patients" supports the reading used above.
