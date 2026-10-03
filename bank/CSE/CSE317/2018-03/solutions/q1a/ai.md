---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Noisy channel: argmax_E P(E | B) = argmax P(E) P(B | E). HMM with hidden English words (or alignment positions) and observed Bangla words; transitions = English bigram language model, emissions = word-translation table; train on a parallel corpus (counting or Baum-Welch); translate with Viterbi."
sources: ["MNM slides Lecture 6 - Hidden Markov Model", "AIMA 3e sec. 23.4 (statistical machine translation)", "Vogel, Ney & Tillmann 1996 (HMM alignment)"]
---
**Goal.** Given a Bangla sentence $b_{1:T}$, find

$$\hat e=\arg\max_eP(e\mid b)=\arg\max_eP(e)\,P(b\mid e),$$

where $P(e)$ is a language model (fluent English) and $P(b\mid e)$ is a translation model (adequacy).

**HMM model.**

- *Hidden states* $X_t$: English words (the English vocabulary). In a more realistic version, the hidden state is the alignment position $a_t$, i.e. which English word the Bangla word $b_t$ translates.
- *Observations* $E_t$: the Bangla words $b_t$.
- *Transitions* $P(X_t\mid X_{t-1})$: an English bigram language model, or alignment jump probabilities $P(a_t\mid a_{t-1})$ that model word reordering (Bangla is SOV, English SVO).
- *Emissions* $P(b_t\mid X_t)$: the word-translation table $P(\text{Bangla word}\mid\text{English word})$.
- *Initial* $P(X_1)$.

```text
English (hidden):  e1 --> e2 --> e3 --> ... --> eT
                    |      |      |              |
Bangla (observed): b1     b2     b3     ...     bT
```

**Learning.** Estimate the tables from a sentence-aligned Bangla-English parallel corpus: by relative-frequency counting when word alignments are known, otherwise by EM (Baum-Welch / IBM-style alignment training). Apply smoothing for unseen word pairs.

**Translating.** For a new Bangla sentence (the evidence), run the **Viterbi** algorithm to find the most likely hidden sequence

$$\hat e_{1:T}=\arg\max P(e_1)P(b_1\mid e_1)\prod_{t\ge2}P(e_t\mid e_{t-1})P(b_t\mid e_t)$$

in $O(T|V|^2)$ time, and output it, reordered by the decoded alignment if alignment states are used.
