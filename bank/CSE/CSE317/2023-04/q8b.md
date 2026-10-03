---
marks: 20
topics: [nlp]
kind: code
source: {page: 19}
note: "'Contest-Free Grammar' is printed so."
---
Consider the program (Figure for Q.8(b)) that parses a given English sentence using the syntax defined by a Contest-Free Grammar, Show the output of this program for the input 'she saw car on street with dog'.

```python
import nltk

grammar = nltk.CFG.fromstring("""
    S -> NP VP

    AP -> A | A AP
    NP -> N | D NP | AP NP | N PP
    PP -> P NP
    VP -> V | V NP | V NP PP

    A -> "big" | "blue" | "small" | "dry" | "wide"
    D -> "the" | "a" | "an"
    N -> "she" | "city" | "car" | "street" | "dog" | "binoculars"
    P -> "on" | "over" | "before" | "below" | "with"
    V -> "saw" | "walked"
""")

parser = nltk.ChartParser(grammar)

sentence = input("Sentence: ").split()
try:
    for tree in parser.parse(sentence):
        tree.pretty_print()
except ValueError:
    print("No parse tree possible.")
```

*Figure for Q.8(b)*
