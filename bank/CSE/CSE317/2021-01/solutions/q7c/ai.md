---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Accuracy misleads on imbalanced data (always predicting the majority class gets high accuracy). Precision = TP/(TP+FP), the cost of false alarms; recall = TP/(TP+FN), the cost of misses. Email auto-reply: precision matters most. Airport watch-list face recognition: recall matters most."
sources: ["AIMA 4e sec. 19.4 (model selection and evaluation)", "Google ML crash course: precision and recall"]
---
**Why accuracy is not always good.** Accuracy $=\frac{TP+TN}{TP+TN+FP+FN}$ treats all errors equally and is dominated by the majority class. With imbalanced classes it is misleading: if 1 passenger in 10,000 is on a watch list, a system that always says "not on the list" is 99.99% accurate and completely useless. Different errors also have different costs, which accuracy ignores.

**Precision and recall** (for the positive class):

$$\text{Precision}=\frac{TP}{TP+FP},\qquad \text{Recall}=\frac{TP}{TP+FN}.$$

- *Precision* asks: of everything flagged positive, how much really is positive? It matters when **false positives are costly**.
- *Recall* asks: of all real positives, how many did we catch? It matters when **false negatives (misses) are costly**.
- There is a trade-off: raising the decision threshold increases precision and lowers recall. The $F_1$ score $=\frac{2PR}{P+R}$ combines both.

**Customer-support email automation: precision.** The system classifies an email (for example "refund request") and sends an automatic reply or action. A wrong automatic reply (false positive) annoys the customer and can do damage. A missed email (false negative) is simply passed to a human agent, so little is lost. The system should automate only when it is confident, i.e. high precision.

**Airport face recognition (matching travellers against a watch list): recall.** Missing a wanted person (false negative) is a serious security failure. A false alarm (false positive) only costs a manual check by an officer. So the system must catch almost every true match, i.e. high recall.

*Note:* if airport face recognition is used instead to *grant* access (e-gates matching a passport photo), a false accept is the dangerous error, and precision for "match" is then more important.
