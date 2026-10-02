---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "E -> E1 + T { E.node = new Node('+', E1.node, T.node) }; E -> T { E.node = T.node }; T -> T1 \\* F { T.node = new Node('\\*', T1.node, F.node) }; T -> F { T.node = F.node }; F -> ( E ) { F.node = E.node }; F -> id { F.node = new Leaf(id, id.entry) }; F -> num { F.node = new Leaf(num, num.val) }. E.g. a + 4 \\* c builds Leaf a, Leaf 4, Leaf c, Node(\\*, 4, c), Node(+, a, \\*) as the root."
sources: ["KMS Chapter 5 slides 41-47 (SDD Application: Construction of AST)", "Dragon book 2e sec. 5.3.1 (Fig. 5.10)"]
---
**Assumptions.** `Node(op, left, right)` creates an interior node of the syntax tree with operator `op` and two children. `Leaf(op, val)` creates a leaf: for `id`, `val` is the symbol-table entry; for `num`, it is the numeric value.

**S-attributed SDD** (every nonterminal has the synthesized attribute `node`):

| Production | Semantic rules |
|:--|:--|
| $E \to E_1 + T$ | $E.node = \textbf{new}\ Node('+', E_1.node, T.node)$ |
| $E \to T$ | $E.node = T.node$ |
| $T \to T_1 * F$ | $T.node = \textbf{new}\ Node('*', T_1.node, F.node)$ |
| $T \to F$ | $T.node = F.node$ |
| $F \to (E)$ | $F.node = E.node$ |
| $F \to \textbf{id}$ | $F.node = \textbf{new}\ Leaf(\textbf{id}, \textbf{id}.entry)$ |
| $F \to \textbf{num}$ | $F.node = \textbf{new}\ Leaf(\textbf{num}, \textbf{num}.val)$ |

The unit productions ($E \to T$, $T \to F$) and the parentheses create **no** nodes; they just pass the pointer up. So the syntax tree contains only operators and operands, unlike the parse tree.

**Example:** `a + 4 * c`. Bottom-up, the rules execute:

1. $p_1$ = new Leaf(id, entry-a)
2. $p_2$ = new Leaf(num, 4)
3. $p_3$ = new Leaf(id, entry-c)
4. $p_4$ = new Node('\*', $p_2$, $p_3$)
5. $p_5$ = new Node('+', $p_1$, $p_4$), which is $E.node$ (the root)

```text
        +
       / \
      a   *
         / \
        4   c
```

Since the SDD is S-attributed, it can be evaluated during LR parsing as a postfix SDT.
