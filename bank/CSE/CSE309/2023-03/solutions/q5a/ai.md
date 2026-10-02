---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "A dependency graph shows the flow of information among the attribute instances of a parse tree: one node per attribute instance, and an edge X.b -> Y.c when the semantic rule defining Y.c uses X.b. Construction: for each parse-tree node and each of its attributes create a node; for each production used and each semantic rule c = f(..., b, ...) add an edge from b to c (for synthesized attributes the edge goes from children to parent, for inherited ones from parent/siblings to the child). Application: any topological sort of the graph is a valid evaluation order for the SDD; a cycle means no order exists."
sources: ["KMS Chapter 5 slides 23-29 (Evaluation Order of SDD, Dependency Graph)", "Dragon book 2e sec. 5.2.1-5.2.2"]
---
**What it is (4 marks).** A *dependency graph* depicts the flow of information among the **attribute instances** in a particular parse tree. It has one node for every attribute of every node of the parse tree, and an edge from attribute instance $X.b$ to $Y.c$ if the value of $Y.c$ is computed using $X.b$ ($Y.c$ depends on $X.b$).

**How it is constructed (4 marks).**

1. For each node $X$ of the parse tree and each attribute $a$ of $X$, create a graph node $X.a$.
2. For each node where production $p$ is used, and each semantic rule of $p$ of the form $c = f(b_1, \ldots, b_k)$:
- if $c$ is a **synthesized** attribute of the head $A$, add an edge from each $b_i$ (attributes of the children, or of $A$ itself) to $A.c$;
- if $c$ is an **inherited** attribute of a body symbol $B$, add an edge from each $b_i$ (attributes of the head or of siblings) to $B.c$.
3. A rule with a side effect (e.g. `print(E.val)`) is treated as defining a dummy attribute, which gets a node of its own.

**Example** (textbook): $T \to F T'$ with $T'.inh = F.val$ and $T.val = T'.syn$; $T' \to * F T_1'$ with $T_1'.inh = T'.inh \times F.val$ and $T'.syn = T_1'.syn$; $T' \to \epsilon$ with $T'.syn = T'.inh$. For `3 * 5`:

```text
           T.val
             ^
             |
F.val ---> T'.inh            T'.syn  (edge T'.syn -> T.val)
             |                  ^
             v                  |
 F.val -> T1'.inh            T1'.syn
             |                  ^
             +------------------+     (T1' -> eps: T1'.syn = T1'.inh)
```

The edges are: digit.lexval $\to$ F.val; F.val $\to$ T'.inh; T'.inh, F.val $\to$ T1'.inh; T1'.inh $\to$ T1'.syn; T1'.syn $\to$ T'.syn; T'.syn $\to$ T.val.

**Application (3 marks).** The dependency graph gives the **order in which the attributes can be evaluated**: an attribute can be computed only after everything it depends on. Any **topological sort** of the graph is a valid evaluation order for the SDD. If the graph has a **cycle**, there is no valid order, and the SDD cannot be evaluated on that tree. That is why we look for classes (S-attributed, L-attributed) whose dependency graphs are guaranteed acyclic.
