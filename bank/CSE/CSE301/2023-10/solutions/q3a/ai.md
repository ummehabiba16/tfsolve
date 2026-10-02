---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: 'State = results of the last two shots (HH, HM, MH, MM); stationary probabilities $\pi_{HH}=\frac12$, $\pi_{HM}=\pi_{MH}=\frac{3}{16}$, $\pi_{MM}=\frac18$; limiting fraction of hits $=\pi_{HH}+\pi_{MH}=\frac{11}{16}$.'
sources: ['CSE301 Markov_Chain slides 3-6 (Markov chain modelling) and 19-22 (limiting probabilities)', 'Ross, Introduction to Probability Models, Ch. 4 (transforming a process into a Markov chain)']
---
**Markov chain.** The probability of a hit depends on the last **two** shots, so the result of the last shot alone is not a Markov chain. Use the pair (second-to-last shot, last shot) as the state, with H = hit and M = miss:

$$\text{states: }HH,\ HM,\ MH,\ MM$$

After the next shot, the state $(a,b)$ becomes $(b,c)$, where $c$ is the new result. The hit probability is $\frac34$ after $HH$, $\frac23$ after $HM$ or $MH$, and $\frac12$ after $MM$:

| From \ To | $HH$ | $HM$ | $MH$ | $MM$ |
|:-:|:-:|:-:|:-:|:-:|
| $HH$ | 3/4 | 1/4 | 0 | 0 |
| $HM$ | 0 | 0 | 2/3 | 1/3 |
| $MH$ | 2/3 | 1/3 | 0 | 0 |
| $MM$ | 0 | 0 | 1/2 | 1/2 |

The chain is irreducible and aperiodic.

**Limiting probabilities.**

$$\pi_{HH}=\tfrac34\pi_{HH}+\tfrac23\pi_{MH}\ \Rightarrow\ \pi_{HH}=\tfrac83\pi_{MH}$$

$$\pi_{MM}=\tfrac13\pi_{HM}+\tfrac12\pi_{MM}\ \Rightarrow\ \pi_{MM}=\tfrac23\pi_{HM}$$

$$\pi_{HM}=\tfrac14\pi_{HH}+\tfrac13\pi_{MH}=\tfrac23\pi_{MH}+\tfrac13\pi_{MH}=\pi_{MH}$$

Put $\pi_{MH}=x$. Then $\pi_{HH}=\frac83x$, $\pi_{HM}=x$, $\pi_{MM}=\frac23x$, and

$$\left(\tfrac83+1+1+\tfrac23\right)x=\tfrac{16}{3}x=1\ \Rightarrow\ x=\tfrac{3}{16}$$

$$\pi_{HH}=\tfrac12,\qquad\pi_{HM}=\tfrac{3}{16},\qquad\pi_{MH}=\tfrac{3}{16},\qquad\pi_{MM}=\tfrac18$$

**Fraction of shots that are hits.** A shot is a hit when the state it produces ends in H:

$$\pi_{HH}+\pi_{MH}=\frac12+\frac{3}{16}=\frac{11}{16}$$

(Check: $\frac34\cdot\frac12+\frac23\left(\frac3{16}+\frac3{16}\right)+\frac12\cdot\frac18=\frac38+\frac14+\frac1{16}=\frac{11}{16}$.)

**Answer:** in the long run he hits $\mathbf{11/16\approx68.75\%}$ of his shots.
