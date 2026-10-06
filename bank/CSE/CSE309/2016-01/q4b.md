---
marks: 20
topics: [table-driven-ll, ll1]
kind: conceptual
source: {page: 48}
note: "Marks printed as (8+3+4+5)."
---
Answer the following questions for predictive parsing.

(i) During construction of a parsing table $M$, for each production rule $A \to \alpha$ of the grammar, if $\epsilon$ is in FIRST($\alpha$), we add $A \to \alpha$ to $M[A, b]$, for each terminal $b$ in FOLLOW($A$). Why? Explain clearly in light of the parsing mechanism.

(ii) What does multiple entries in a parsing table mean? Is the corresponding grammar LL(1)?

(iii) During a parsing, if $w$ is the input that has been matched so far, and $S$ is the start symbol for the corresponding grammar, with, $S \overset{*}{\Rightarrow} w\alpha\beta\gamma$, what will be the stack contents? Also, comment on the nature of symbols in $w$ and stack contents regarding being terminals/non-terminals.

(iv) During parsing, if the input pointer is pointing to the symbol $a$, and top stack symbol in $X$, with the entry $M[X, a]$ being $X \to UVW$, explain how stack contents will be altered. Why?
