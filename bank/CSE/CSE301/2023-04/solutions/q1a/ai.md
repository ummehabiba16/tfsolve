---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: '$P(D)=0.98(0.07)+0.05(0.93)=0.1151$; $P(\text{no aircraft}\mid D)=\frac{0.05\times0.93}{0.1151}=\frac{0.0465}{0.1151}\approx0.404$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 2 (Bayes'' rule, law of total probability)', 'Ross, Introduction to Probability Models, Ch. 1 (Bayes'' formula)']
---
Let $A$ = "an aircraft is present" and $D$ = "the radar reports (detects) an aircraft". We are given

$$P(A)=0.07,\qquad P(D\mid A)=0.98,\qquad P(D\mid A^c)=0.05$$

**Law of total probability.**

$$P(D)=P(D\mid A)P(A)+P(D\mid A^c)P(A^c)=0.98(0.07)+0.05(0.93)$$

$$=0.0686+0.0465=0.1151$$

**Bayes' rule.**

$$P(A^c\mid D)=\frac{P(D\mid A^c)P(A^c)}{P(D)}=\frac{0.0465}{0.1151}\approx\mathbf{0.404}$$

So about 40% of the radar's alarms are false alarms, even though the radar is quite accurate, because aircraft are rarely present ($P(A)=0.07$).
