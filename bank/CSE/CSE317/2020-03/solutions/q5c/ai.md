---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Rejection sampling generates samples from the prior and throws away those that disagree with the evidence; with unlikely evidence almost all are wasted, and evidence is used only to reject, never to guide sampling. Likelihood weighting fixes the evidence and samples only the other variables, weighting each sample by the product of P(e_i | parents); no sample is rejected."
sources: ["MNM slides Uncertainty-5-BN-Sampling (rejection sampling, likelihood weighting)", "AIMA 4e sec. 13.4.1"]
---
**Rejection sampling.** Generate full samples from the network by prior sampling (topological order). Discard every sample that does not match the evidence $\mathbf{e}$, and estimate $P(X\mid\mathbf{e})$ by counting $X$ in the samples that remain.

**Problems.**

1. **Wasted samples.** The fraction kept is $P(\mathbf{e})$, which falls exponentially with the number of evidence variables. With rare evidence almost every sample is rejected. For example, with $P(\mathbf{e})=0.001$, about 999 of 1000 samples are thrown away, so the estimate is very noisy for a given amount of work.
2. **Evidence does not guide sampling.** Upstream variables are sampled without considering the evidence, so most samples describe situations that contradict what we observed.

**Likelihood weighting (LW).** Fix the evidence variables to their observed values and sample only the non-evidence variables, in topological order, from $P(X_i\mid\text{parents}(X_i))$. Give each sample the weight

$$w=\prod_{\text{evidence }E_j}P(e_j\mid\text{parents}(E_j)),$$

and estimate $P(x\mid\mathbf{e})=\dfrac{\sum_{\text{samples with }x}w}{\sum_{\text{all samples}}w}$.

- Every sample is consistent with the evidence, so **none is rejected**.
- The weight corrects for having forced the evidence: samples in which the evidence is likely count more. The estimate is consistent.
- *Remaining weakness:* evidence affects only its descendants, not its ancestors. With evidence near the leaves, a few samples carry nearly all the weight; Gibbs sampling addresses this.

**Example** (Cloudy $\to$ Sprinkler, Rain $\to$ WetGrass; query $P(Rain\mid Sprinkler=t, WetGrass=t)$).

- *Rejection:* sample $C,S,R,W$. With $P(s)\approx0.3$, about 70% of samples have $S=f$ and are thrown away.
- *LW:* sample $C$ (say $c$). Set $S=s$, so $w\leftarrow P(s\mid c)=0.1$. Sample $R$ (say $r$). Set $W=w$, so $w\leftarrow0.1\times P(w\mid s,r)=0.1\times0.99=0.099$. The sample $(c,s,r,w)$ is kept with weight 0.099, and the weighted counts of $r$ versus $\neg r$ give the answer.
