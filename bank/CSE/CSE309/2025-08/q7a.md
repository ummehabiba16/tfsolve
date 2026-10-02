---
marks: 12
topics: [types-declarations, sdt-schemes]
kind: numerical
source: {page: 6}
note: "Marks printed as (4+8). Printed as 'The symbol T is the above grammar' ('is' corrected to 'in' by hand on the scan); there is also a handwritten mark on the D-production."
---
Briefly describe two applications of types in a program. Consider the following grammar related to variable declarations.

$$P \to D$$

$$D \to T\ \textbf{id};\ D \mid \epsilon$$

Now, convert the above to an SDT (Syntax-Directed Translation Scheme) to save each declared variable in the symbol table along with its type and offset information. The symbol $T$ is the above grammar represents type of **id** and it has two synthesized attributes *type* and *width*. Based on your SDT, what will be the offset of each of the variables in the below declarations.

**int** a; **int** b; **float** f;

Assume that the size of **int** is 2 byte and size of **float** is 4 byte.
