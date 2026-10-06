---
marks: 25
topics: [sdd-attributes, sdt-schemes]
kind: analysis
source: {page: 61}
note: "Marks printed beside (i)-(iv) as (5), (7), (8) and (5)."
---
Consider the following context free grammar (CFG) for arithmetic expressions involving addition (+) operations

$$E \to TE'$$

$$E' \to +TE' \mid \epsilon$$

$$T \to \textbf{digit}$$

(i) Extend the above CFG so that it can handle expressions having subtraction ($-$) and multiplication ($*$) operations.

(ii) Convert the extended CFG of 5(a).(i) into a Syntax Directed Definition (SDD) to evaluate the expressions.

(iii) Depict an **annotated** parse tree for expression $3 * 5 - 4$ based on the SDD of 5(a)(ii).

(iv) Convert the SDD of 5(a)(ii) into a corresponding Syntax Directed Translation (SDT).

(Assume that all the operations ($+$, $-$, $*$) follow their usual precedence and associative rules.)
