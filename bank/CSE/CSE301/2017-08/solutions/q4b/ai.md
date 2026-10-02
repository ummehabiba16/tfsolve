---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'With cards of length 2, the centre of gravity of the top $k$ cards lies $d_k$ from the top card''s edge, $d_1=1$, $d_{k+1}=d_k+\frac{1}{k+1}$; the largest overhang of $n$ cards is $H_n=1+\frac12+\cdots+\frac1n$ (unbounded as $n\to\infty$).'
sources: ['Graham, Knuth & Patashnik, Concrete Mathematics, Ch. 6 (harmonic numbers: the overhang problem)']
---
**Set-up.** Number the cards $1,2,\dots,n$ from the top. Each card has length 2, so its centre of gravity is 1 unit from either end. Let $d_k$ be the horizontal distance from the right edge of the top card (the extreme point of the overhang) to the centre of gravity of the top $k$ cards.

**Stability.** The top $k$ cards are stable on card $k+1$ (or on the table, for $k=n$) as long as their common centre of gravity lies over card $k+1$. For the largest overhang, place each card so that the right edge of the card below is exactly under the centre of gravity of the cards above it.

**Recurrence.** $d_1=1$ (the centre of the top card). The right edge of card $k+1$ is at distance $d_k$, so its centre is at distance $d_k+1$. The centre of gravity of the top $k+1$ cards (all of equal weight) is therefore

$$d_{k+1}=\frac{k\,d_k+(d_k+1)}{k+1}=d_k+\frac{1}{k+1}$$

Unfolding, $d_k=1+\frac12+\cdots+\frac1k=H_k$, the $k$-th harmonic number.

**Maximum overhang.** The table edge is placed under the centre of gravity of all $n$ cards, so the top card reaches beyond the table by

$$d_n=H_n=1+\frac12+\frac13+\cdots+\frac1n$$

(card $k$ from the top sticks out $d_k-d_{k-1}=\frac1k$ beyond the card below it, and the bottom card sticks out $\frac1n$ beyond the table). Since $H_n\approx\ln n+0.5772$ grows without bound, the overhang can be made as large as we like with enough cards. For example $H_4=\frac{25}{12}>2$: with only 4 cards the top card lies completely beyond the edge of the table.

(If the cards have length 1 instead of 2, every distance halves and the maximum overhang is $\frac12H_n$.)
