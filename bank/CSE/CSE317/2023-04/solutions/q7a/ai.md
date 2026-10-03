---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Skip-gram: input layer of 10 neurons (one-hot target word), a linear hidden (projection) layer of 3 neurons (the word vector), output layer of 10 softmax neurons (one per vocabulary word) for each context position. Input = target, hidden = meaning (embedding), output = context."
sources: ["Mikolov et al. 2013, 'Efficient Estimation of Word Representations in Vector Space' (word2vec skip-gram)", "AIMA 4e sec. 24.1 (word embeddings)", "CS50 AI Lecture 6 (word2vec)"]
---
**Skip-gram.** Given a *target* word $w_t$, predict the words around it in a window, $w_{t-c},\dots,w_{t+c}$. Training on all (target, context) pairs from the document makes words that occur in similar contexts get similar hidden vectors. Those hidden vectors are the learned "meaning".

**Architecture** (vocabulary $V=10$ words, embedding size $N=3$):

```text
 INPUT layer            HIDDEN layer           OUTPUT layer(s)
 (target word)          (word vector)          (context words)
 10 neurons, one-hot    3 linear neurons       10 softmax neurons per context position

  x1  o \                                     / o  P(word 1 | target)
  x2  o  \      W_in (10 x 3)    h1 o        /  o  P(word 2 | target)
  ..  o   >-------------------->  h2 o  ----<   ..
  ..  o  /                       h3 o  W_out \  ..
  x10 o /                          (3 x 10)   \ o  P(word 10 | target)
```

- **Input layer: 10 neurons.** A one-hot vector for the target word: 1 at the word's index, 0 elsewhere.
- **Hidden (projection) layer: 3 neurons**, linear (no activation). $\mathbf{h}=W_{in}^{\top}\mathbf{x}$ simply picks the target word's row of $W_{in}$ ($10\times3$). That row is the word's 3-D vector.
- **Output layer: 10 neurons**, with $\mathbf{y}=\text{softmax}(W_{out}^{\top}\mathbf{h})$ ($W_{out}$ is $3\times10$). It gives the probability of each vocabulary word appearing in the context. For a window of $C$ context words there are $C$ such output blocks, all **sharing** $W_{out}$ (often drawn as one block).
- **Training:** maximize $\sum\log P(w_{t+j}\mid w_t)$ (cross-entropy loss) by backpropagation, usually with negative sampling.

**Which layer represents what.**

| Layer | Represents |
|:--|:--|
| Input (10, one-hot) | the **target** word |
| Hidden (3) | the **meaning**: the learned 3-D word embedding (row of $W_{in}$) |
| Output (10, softmax) | the **context**: the predicted surrounding words |

*Note:* to keep the vector components in $[-1,1]$ as the question asks, the embeddings can be scaled to unit length (cosine-normalized) after training, or a $\tanh$ applied to the hidden layer. Standard word2vec uses a linear hidden layer.
