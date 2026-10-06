---
marks: 28
topics: [control-flow, sdd-attributes]
kind: analysis
source: {page: 61}
note: "Marks printed as (12) for (i) and (16) for (ii)."
---
Consider the following CFG for control flow statements.

$$P \to S$$

$$S \to \textbf{id} = \textbf{num};$$

$$S \to \textbf{if}\ (B)\ S1\ \textbf{else}\ S2$$

$$B \to B \mid\mid B \mid B\ \&\&\ B$$

$$B \to E\ \textbf{relop}\ E$$

$$E \to \textbf{id} \mid \textbf{num}$$

(i) Convert the above CFG into an SDD so that it can generate equivalent three address codes for the control flow statements.

(ii) For the statement `if (x < 100 || x > 200 && x !=y) x = 0; else x = 1;` construct an annotated parse tree based on the SDD of 6(b)(i) by showing values for all necessary attributes.
