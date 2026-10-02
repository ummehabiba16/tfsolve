---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'With 12 flags of each colour, every sequence of 12 colours is possible: $4^{12}$ signals, of which $\binom{12}{w}3^{12-w}$ have exactly $w$ white flags. Signals with at least three or no white flags $=4^{12}-12\cdot3^{11}-\binom{12}{2}3^{10}=16{,}777{,}216-2{,}125{,}764-3{,}897{,}234=10{,}754{,}218$.'
sources: ['Brualdi, Introductory Combinatorics, Ch. 3 (permutations of multisets)']
---
**Signals.** A signal is the sequence of colours of the 12 flags on the pole, read from top to bottom (flags of the same colour are identical). Since 12 flags of **each** colour are available, any sequence of 12 colours can be made, even 12 of a single colour. So there are

$$4^{12}=16{,}777{,}216$$

possible signals.

**Exactly $w$ white flags.** Choose the $w$ positions of the white flags ($\binom{12}{w}$ ways) and colour each of the other $12-w$ positions red, blue or black ($3^{12-w}$ ways):

$$N_w=\binom{12}{w}3^{12-w}$$

**At least three white flags or none.** These are all signals except those with exactly 1 or exactly 2 white flags:

$$4^{12}-N_1-N_2=4^{12}-12\cdot3^{11}-\binom{12}{2}3^{10}$$

$$=16{,}777{,}216-2{,}125{,}764-3{,}897{,}234=\mathbf{10{,}754{,}218}$$

(Directly: $N_0=3^{12}=531{,}441$ signals have no white flag, and $\sum_{w\ge3}N_w=10{,}222{,}777$ have at least three; together $10{,}754{,}218$.)
