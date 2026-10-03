---
marks: 18
topics: [neural-networks]
kind: numerical
source: {page: 26}
---
You are given some tasks of text classification, where from the given text input you need to predict whether the text is written by a kid or an adult. Consider the following labeled text SAMPLE,

"like to travel" - Adult

"love rhymes" - Kid

"love to play" - Kid

"love to read" - Adult

Design a multilevel perceptron classification approach to learn the weight vector from the above text SAMPLE. Assume the following initial weight vector, **w** [BIAS, like, love, travel, rhymes, play, read] as [1, 0, 0, 0, 0, 0, 0].
