---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Given an aircraft is present, each radar misses it with probability $0.02$, independently: $P(\text{neither detects})=0.02^2=0.0004$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 2 (independence)']
---
An aircraft has entered the area, so we condition on $A$. Each radar misses a present aircraft with probability

$$P(D^c\mid A)=1-0.98=0.02$$

The two radar systems operate independently (given that the aircraft is present), so

$$P(\text{neither detects}\mid A)=P(D_1^c\mid A)\,P(D_2^c\mid A)=0.02\times0.02=\mathbf{0.0004}$$

(Using two radars cuts the miss probability from 2% to 0.04%.)
