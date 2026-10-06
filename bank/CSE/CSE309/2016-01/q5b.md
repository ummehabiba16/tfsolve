---
marks: 10
topics: [three-address-code, control-flow]
kind: numerical
source: {page: 48}
---
Consider the following syntax directed translation rules to generate three-address code:

| Productions | Semantic rules |
|:--|:--|
| $S \to \textbf{id} := E$ | $S.code := E.code \parallel gen(\textbf{id}.place\ \text{':='}\ E.place);$ |
| | $S.begin := S.after := nil$ |
| $S \to \textbf{while}\ E\ \textbf{do}\ S_1$ | $S.begin := newlabel()$ |
| | $S.after := newlabel()$ |
| | $S.code := gen(S.begin\ \text{':'}) \parallel E.code \parallel$ |
| | $\quad gen(\text{'if'}\ E.place\ \text{'='}\ \text{'0'}\ \text{'goto'}\ S.after) \parallel$ |
| | $\quad S_1.code \parallel gen(\text{'goto'}\ S.begin) \parallel gen(S.after\ \text{':'})$ |
| $E \to E_1 + E_2$ | $E.place := newtemp();$ |
| | $E.code := E_1.code \parallel E_2.code \parallel gen(E.place\ \text{':='}\ E_1.place\ \text{'+'}\ E_2.place)$ |
| $E \to E_1 * E_2$ | $E.place := newtemp();$ |
| | $E.code := E_1.code \parallel E_2.code \parallel gen(E.place\ \text{':='}\ E_1.place\ \text{'*'}\ E_2.place)$ |
| $E \to \textbf{id}$ | $E.place := \textbf{id}.name$ |
| | $E.code := \text{''}$ |
| $E \to \textbf{num}$ | $E.place := newtemp();$ |
| | $E.code := gen(E.place\ \text{':='}\ \textbf{num}.value)$ |

Assume, the function 'newtemp()' generates the temporary variables like $t_1$, $t_2$, etc and the function 'newlabel()' generates new label consistently. Generate three address code according to the above semantic rules for the following strings:

```text
i := i + j*k
while i do
i := 2 * n + k
```
