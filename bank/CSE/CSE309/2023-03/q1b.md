---
marks: 10
topics: [input-buffering, tokens]
kind: analysis
mandatory: true
source: {page: 14}
---
The partial contents of a buffer in lexical analyzer is `dhaka_+++_123.456_`, where `_` indicates a space. At the current moment, both the `lexemeBegin` and `forward` pointers are on `d` at left. From the perspective of the C programming language, describe clearly the pointer movements and recognition of tokens that will happen.
