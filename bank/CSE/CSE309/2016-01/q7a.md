---
marks: 10
topics: [type-checking]
kind: analysis
source: {page: 50}
---
What is type inference? Find out the type inference rule for the following "append" function written in ML functional language:

```text
fun append(x, y) = if null(x) then y else cons(hd(x), append(tl(x), y))
```
