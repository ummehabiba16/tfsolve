---
marks: 15
topics: [propositional-logic]
kind: code
source: {page: 16}
note: "'the proportion that we are interested in' is printed so (probably 'proposition')."
---
Consider the function named *check_all*, shown in Figure for Q.5(a), used for implementing the Model Checking inference algorithm for propositional logic. Its parameters are

- knowledge: knowledge base used to draw inferences
- query: a query, or the proportion that we are interested in whether it is entailed by the knowledge base
- symbols: a list of all the symbols (or atomic propositions) used
- model: an assignment of truth and false values to symbols

Can this *check_all* function correctly implement the Model Checking algorithm? If not, explain why this function fails to correctly implement the Model Checking algorithm by referring to the relevant lines of code.

```text
 1  def check_all(knowledge, query, symbols, model):
 2      """Checks if knowledge base entails query, given a particular model."""
 3
 4      # If model has an assignment for each symbol
 5      if not symbols:
 6
 7      # If knowledge base is true in model, then query must also be true
 8          if knowledge.evaluate(model):
 9              return query.evaluate(model)
10          return True
11      else:
12
13          # Choose one of the remaining unused symbols
14          remaining = symbols.copy()
15          p = remaining.pop()
16
17          # Create a model where the symbol is true
18          model_true = model.copy()
19          model_true[p] = True
20
21          # Create a model where the symbol is false
22          model_false = model.copy()
23          model_false[p] = False
24
25          # Ensure entailment holds in both models
26          return (check_all(knowledge, query, remaining, model_true) or
27                  check_all(knowledge, query, remaining, model_false))
28
```

*Figure for Q.5(a)*
