---
marks: 15
topics: [control-flow]
kind: analysis
source: {page: 33}
---
Consider the following partially completed SDD for generating three-address codes for expressions, booleans and flow-of-control statements.

| PRODUCTION | SEMANTIC RULES |
|:--|:--|
| $P \to S$ | $S.next = newlabel()$ |
| | $P.code = S.code \,\Vert\, label(S.next)$ |
| $S \to \text{if}\ (B)\ S_1$ | $B.true = newlabel()$ |
| | $B.false = S_1.next = S.next$ |
| | $S.code = B.code \,\Vert\, label(B.true) \,\Vert\, S_1.code$ |
| $B \to E_1\ \textbf{rel}\ E_2$ | $B.code = E_1.code \,\Vert\, E_2.code$ |
| | $\Vert\ gen('\text{if}'\ E_1.addr\ \textbf{rel}.op\ E_2.addr\ '\text{go to}'\ B.true)$ |
| | $\Vert\ gen('\text{go to}'\ B.false)$ |
| $E \to \textbf{id}$ | $E.addr = top.get(\textbf{id}.lexeme)$ |
| | $E.code = ''$ |

Here **rel** means relational operators (<, >, <=, >=, !=, ==), *top* denote the current symbol table, *top.get* retrieves the entry corresponding to the **id**, *newlabel()* creates a new label each time it is called, *label (L)* attaches label *L* to the next three-address instruction to be generated and *gen(.)* generates three address instruction in string format. Other symbols and attribute names have their usual meanings.

Now add rules to the SDD above for the following constructs.

(i) $S \to \text{if}\ (B)\ S_1\ \text{else}\ S_2$

(ii) **while** $(B)\ S_1$

(iii) $B \to B_1 \Vert B_2$

(iv) $B \to B_1\ \&\&\ B_2$

(v) $E \to \textbf{num}$
