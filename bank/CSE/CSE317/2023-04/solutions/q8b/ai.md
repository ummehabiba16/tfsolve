---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "The sentence is ambiguous and the chart parser prints 3 trees (checked by running the program): 'with dog' attaches to the VP, to 'street', or to 'street' inside an NP 'car on street with dog'."
sources: ["AIMA 4e sec. 23.2-23.3 (grammars, syntactic ambiguity, chart parsing)", "CS50 AI Lecture 6 (nltk.CFG / ChartParser)", "NLTK 3 (program run to confirm the output)"]
---
After the prompt `Sentence: ` and the input `she saw car on street with dog`, the program prints every parse tree. The grammar has two sources of ambiguity: `VP -> V NP PP` versus `VP -> V NP`, and `NP -> N PP`. So the prepositional phrases can attach in several ways. Running the program (NLTK 3) prints **three** trees, in this order.

**Tree 1:** she saw [car on street] [with dog]. "with dog" modifies the seeing (VP).

```text
(S (NP (N she))
   (VP (V saw)
       (NP (N car) (PP (P on) (NP (N street))))
       (PP (P with) (NP (N dog)))))

     S
  ___|_______
 |           VP
 |    _______|___________________
 |   |       NP                  |
 |   |    ___|___                |
 |   |   |       PP              PP
 |   |   |    ___|____       ____|___
 NP  |   |   |        NP    |        NP
 |   |   |   |        |     |        |
 N   V   N   P        N     P        N
 |   |   |   |        |     |        |
she saw car  on     street with     dog
```

**Tree 2:** she saw [car] [on street with dog]. The VP takes NP "car" and PP "on street with dog"; "with dog" modifies "street".

```text
(S (NP (N she))
   (VP (V saw)
       (NP (N car))
       (PP (P on) (NP (N street) (PP (P with) (NP (N dog)))))))

     S
  ___|_______
 |           VP
 |    _______|__________
 |   |   |              PP
 |   |   |    __________|___
 |   |   |   |              NP
 |   |   |   |     _________|____
 |   |   |   |    |              PP
 |   |   |   |    |          ____|___
 NP  |   NP  |    |         |        NP
 |   |   |   |    |         |        |
 N   V   N   P    N         P        N
 |   |   |   |    |         |        |
she saw car  on street     with     dog
```

**Tree 3:** she saw [car on [street with dog]]. Everything is inside the object NP.

```text
(S (NP (N she))
   (VP (V saw)
       (NP (N car)
           (PP (P on) (NP (N street) (PP (P with) (NP (N dog))))))))

     S
  ___|_______
 |           VP
 |    _______|____
 |   |            NP
 |   |    ________|_____
 |   |   |              PP
 |   |   |    __________|___
 |   |   |   |              NP
 |   |   |   |     _________|____
 |   |   |   |    |              PP
 |   |   |   |    |          ____|___
 NP  |   |   |    |         |        NP
 |   |   |   |    |         |        |
 N   V   N   P    N         P        N
 |   |   |   |    |         |        |
she saw car  on street     with     dog
```

The parse "[car with dog]" with "on street" attached separately is impossible: the grammar has no rule `NP -> NP PP`, so a PP can attach only directly to an N or to the VP. No `ValueError` is raised, because every word is in the grammar.
