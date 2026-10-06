---
marks: 20
topics: [sdd-attributes]
kind: analysis
source: {page: 44}
---
Write an attribute grammar that recognizes strings consisting of a, b, c and produces the number of substrings that correspond to the regular expression $ab^+c$ in the input string. For example, if the input string is 'abbccabcb', then the output will be 2. You can use any arithmetic, bitwise or logical operators in the semantic rules. Show the annotated parse tree for the input string 'abbccabcb'.

$$S \to S\textbf{a} \mid S\textbf{b} \mid S\textbf{c} \mid \textbf{a} \mid \textbf{b} \mid \textbf{c}$$
