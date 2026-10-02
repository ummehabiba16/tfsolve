---
marks: 20
topics: [simple-codegen, codegen-issues]
kind: conceptual
source: {page: 20}
note: "Marks printed as (5+15=20)."
---
Explain why register allocation and assignment is a critical issue during code generation? While generating code for a basic block, a function is used to select registers for each memory location associated with a three-address instruction $I$. Assume the function is called *getReg(I)*. For an instruction of the form, $I$: $x = y + z$, what rules are used by the function *getReg(I)* while selecting registers for each of the variables, $x$, $y$, and $z$.
