---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "The data say 9 of 10 chronic-cough patients are non-cancerous, so P(cr | cc) = 1 - 0.9 = 0.1. Bayes check: P(cc) = 0.4 x 0.1 / 0.1 = 0.4 and P(cc | not cr) = 0.4, so the cough carries no information here: P(cr | cc) = P(cr) = 10%."
sources: ["MNM slides Uncertainty-1-(quantifying) (Bayes' rule)", "AIMA 4e sec. 12.5"]
---
**Given.** $P(cr)=0.10$, $P(cc\mid cr)=0.40$, and "among all chronic-cough patients, 9 out of 10 are non-cancerous", i.e. $P(\neg cr\mid cc)=0.9$.

**Answer.**

$$P(cr\mid cc)=1-P(\neg cr\mid cc)=1-0.9=\mathbf{0.1}\ (10\%).$$

**Consistency check with Bayes' rule.**

$$P(cr\mid cc)=\frac{P(cc\mid cr)\,P(cr)}{P(cc)}\ \Rightarrow\ P(cc)=\frac{0.4\times0.1}{0.1}=0.4$$

Then $P(cc,\neg cr)=P(cc)-P(cc,cr)=0.4-0.04=0.36$, so

$$P(cc\mid\neg cr)=\frac{0.36}{0.9}=0.4=P(cc\mid cr).$$

The data are consistent. They also show that, in these numbers, chronic cough is **independent** of cancer: the posterior $P(cr\mid cc)=0.1$ equals the prior $P(cr)=0.1$. Having the symptom does not change the probability.

*Note:* if the statement is read as "90% of *non-cancerous* people have chronic cough", i.e. $P(cc\mid\neg cr)=0.9$, then $P(cr\mid cc)=\frac{0.4(0.1)}{0.4(0.1)+0.9(0.9)}=\frac{0.04}{0.85}=0.047$. The wording "among all chronic cough patients" supports the first reading.
