---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'Inclusion-exclusion over the events "no card of suit $i$": $P=\big[4\binom{39}{13}-6\binom{26}{13}+4\binom{13}{13}\big]/\binom{52}{13}\approx0.0511$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 1 (inclusion-exclusion)']
---
Let $A_i$ be the event that the hand has **no** card of suit $i$ ($i=1,2,3,4$). We want $P(A_1\cup A_2\cup A_3\cup A_4)$. All $\binom{52}{13}$ hands are equally likely.

- $P(A_i)=\binom{39}{13}\big/\binom{52}{13}$: all 13 cards come from the other 39 cards.
- $P(A_i\cap A_j)=\binom{26}{13}\big/\binom{52}{13}$: all 13 cards come from the other two suits.
- $P(A_i\cap A_j\cap A_k)=\binom{13}{13}\big/\binom{52}{13}=1\big/\binom{52}{13}$: all 13 cards come from the one remaining suit.
- $P(A_1\cap A_2\cap A_3\cap A_4)=0$: a hand cannot miss all four suits.

By symmetry there are $\binom41=4$, $\binom42=6$ and $\binom43=4$ terms of each kind, so inclusion-exclusion gives

$$P(\text{void in at least one suit})=\frac{4\binom{39}{13}-6\binom{26}{13}+4\binom{13}{13}}{\binom{52}{13}}$$

With $\binom{52}{13}=635{,}013{,}559{,}600$, $\binom{39}{13}=8{,}122{,}425{,}444$ and $\binom{26}{13}=10{,}400{,}600$:

$$\text{numerator}=32{,}489{,}701{,}776-62{,}403{,}600+4=32{,}427{,}298{,}180$$

$$P=\frac{32{,}427{,}298{,}180}{635{,}013{,}559{,}600}\approx0.0511$$

So about **5.1%** of 13-card hands are void in at least one suit.
