---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Hidden states = English words (or alignment positions), observations = Bangla words; transition P(e_t | e_{t-1}) = English language model, emission P(b_t | e_t) = translation table, both learned from a parallel corpus (Baum-Welch/EM). For a query, the Bangla words are the evidence and Viterbi finds the most likely English sequence."
sources: ["MNM slides Lecture 6 - Hidden Markov Model", "AIMA 4e sec. 14.3 (HMMs); AIMA 3e sec. 23.4 (statistical machine translation)", "Vogel, Ney & Tillmann 1996, HMM-based word alignment"]
---
**Noisy-channel view.** Think of the Bangla sentence $b_{1:T}$ as an English sentence $e_{1:T}$ "corrupted" into Bangla. We want

$$\hat e=\arg\max_eP(e\mid b)=\arg\max_eP(e)\,P(b\mid e).$$

An HMM provides both factors.

**HMM design** (word-by-word, simplified):

- *Hidden state* $X_t$: the English word at position $t$ (the vocabulary of English words).
- *Observation* $E_t$: the Bangla word at position $t$.
- *Transition model* $P(X_t\mid X_{t-1})$: a bigram **English language model**, so that the output is fluent English.
- *Emission model* $P(E_t\mid X_t)$: the **translation (dictionary) model**, the probability that English word $e$ is expressed by Bangla word $b$.
- *Initial* $P(X_1)$: the probability that a sentence starts with $e$.

```text
English (hidden):   e1 ---> e2 ---> e3 ---> ... ---> eT     P(e_t | e_t-1)  language model
                     |       |       |                |
                     v       v       v                v     P(b_t | e_t)    translation model
Bangla (observed):  b1      b2      b3      ...      bT
```

(Bangla is SOV and English is SVO. A better HMM uses **alignment positions** as hidden states, with jump probabilities $P(a_t\mid a_{t-1})$ that model reordering, and the emission $P(b_t\mid e_{a_t})$.)

**Training.** From a sentence-aligned Bangla-English parallel corpus, estimate the transition and emission tables by counting, or by **Baum-Welch (EM)** when the word alignments are unknown. Use smoothing for unseen pairs.

**Answering a query.** Given a new Bangla sentence $b_1\dots b_T$:

1. Treat the Bangla words as the evidence sequence.
2. Run the **Viterbi algorithm** (dynamic programming over the HMM trellis) to find the most likely hidden sequence:

$$\hat e_{1:T}=\arg\max_{e_{1:T}}P(e_1)P(b_1\mid e_1)\prod_{t=2}^{T}P(e_t\mid e_{t-1})P(b_t\mid e_t),$$

in $O(T\,|V|^2)$ time, instead of enumerating $|V|^T$ sentences.
3. Output $\hat e_{1:T}$ (followed by back-pointers) as the English translation. In the alignment version, reorder the words according to the decoded alignment.

*Limitation:* one hidden state per Bangla word assumes a one-to-one, nearly monotone correspondence. Modern systems use phrase-based or neural (sequence-to-sequence) models.
