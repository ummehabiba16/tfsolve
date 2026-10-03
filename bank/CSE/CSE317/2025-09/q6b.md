---
marks: 20
topics: [decision-tree]
kind: numerical
source: {page: 3}
note: "The table is captioned 'Figure for Question 6(a)' on the scan, but the text belongs to 6(b)."
---
Consider the following tabular dataset, where **O**, **T**, **H**, and **W** are attributes of every input and **Play** is the target variable we want to predict. Now, build a decision tree considering 'entropy' as the criterion to select the best attribute at each step. You need to show every step with proper calculations.

| # | O | T | H | W | Play |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | S | H | H | W | - |
| 2 | S | H | H | S | - |
| 3 | O | H | H | W | + |
| 4 | R | M | H | W | + |
| 5 | R | C | N | W | + |
| 6 | R | C | N | S | - |
| 7 | O | C | N | S | + |
| 8 | S | M | H | W | - |
| 9 | S | C | N | W | + |
| 10 | R | M | N | W | + |
| 11 | S | M | N | S | + |
| 12 | O | M | H | S | + |
| 13 | O | H | N | W | + |
| 14 | R | M | H | S | - |
