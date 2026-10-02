---
marks: 10
topics: [input-buffering]
kind: analysis
source: {page: 31}
---
Let's a consider a language like C++ where both + and ++ constitute valid tokens. In some code of this language there are three consecutive + characters followed by a newline character. During lexical analysis with a buffer pair, both the pointers are on the leftmost + character. Describe clearly, with necessary figures, the activities that will happen starting from the present moment to the moment when the newline character will be found.
