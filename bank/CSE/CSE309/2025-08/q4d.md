---
marks: 10
topics: [slr, shift-reduce]
kind: numerical
source: {page: 4}
note: "Printed as given. The grammar has only S, yet the GOTO part has columns S, A, B and the entries for states 2, 4, 6 sit under B and state 5's under A; the table also uses r4 and r5 although only three productions are listed. The table appears to have been taken from a different grammar."
---
For the grammar:

1. $S \to SS+$
2. $S \to SS*$
3. $S \to a$

Here is the SLR (1) parse table:

| State | a | + | * | \$ | GOTO S | GOTO A | GOTO B |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 0 | s2 | | | | 1 | | |
| 1 | | | | acc | | | |
| 2 | s4 | r3 | r3 | r3 | | | 3 |
| 3 | | | | r1 | | | |
| 4 | s4 | r3 | r3 | r3 | | | 5 |
| 5 | | s7 | s8 | | | 6 | |
| 6 | s4 | r3 | r3 | r3 | | | 9 |
| 7 | r4 | | | r4 | | | |
| 8 | r5 | | | r5 | | | |
| 9 | | r2 | r2 | r2 | | | |

*Table for Question 4(d). Columns a, +, \*, \$ are ACTION.*

Show the parsing steps in a table on the input aa\*a+.
