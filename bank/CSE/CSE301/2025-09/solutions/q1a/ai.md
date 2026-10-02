---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'All five cards aces is impossible: probability $0$ (only 4 aces exist; if "all four aces" is meant, $48/\binom{52}{5}=1/54145$). Same suit: $4\binom{13}{5}/\binom{52}{5}=33/16660\approx0.00198$.'
sources: ['Blitzstein & Hwang, Introduction to Probability, Ch. 1 (naive definition of probability, counting)']
---
**Naive definition.** If all outcomes of an experiment are equally likely, then for an event $A$

$$P_{\text{naive}}(A)=\frac{\text{number of outcomes favourable to }A}{\text{total number of outcomes}}$$

Every 5-card hand is equally likely, so the sample space is the set of all 5-card subsets of the deck:

$$|S|=\binom{52}{5}=2{,}598{,}960$$

**(i) All five cards are aces.** A standard deck has only 4 aces, so no 5-card hand can consist of aces only:

$$P(\text{all aces})=\frac{\binom{4}{5}}{\binom{52}{5}}=\frac{0}{2{,}598{,}960}=0$$

The event is impossible, so its probability is **0**.

*If the question means "the hand contains all four aces":* the fifth card can be any of the other 48 cards, so

$$P=\frac{\binom{4}{4}\binom{48}{1}}{\binom{52}{5}}=\frac{48}{2{,}598{,}960}=\frac{1}{54{,}145}\approx1.85\times10^{-5}$$

**(ii) All five cards from the same suit.** Choose the suit (4 ways), then choose 5 of its 13 cards:

$$\#\text{favourable}=4\binom{13}{5}=4\times1287=5148$$

$$P(\text{same suit})=\frac{5148}{2{,}598{,}960}=\frac{33}{16{,}660}\approx0.00198$$

This count includes the 40 straight flushes; excluding them (a poker "flush") gives $5108/2{,}598{,}960\approx0.00197$.
