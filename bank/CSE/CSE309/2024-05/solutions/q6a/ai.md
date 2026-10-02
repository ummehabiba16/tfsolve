---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Postfix SDT: E -> E1 + T { E.node = Node('+', E1.node, T.node) }; E -> T { E.node = T.node }; T -> T1 \\* F { T.node = Node('\\*', T1.node, F.node) }; T -> F; F -> ( E ) { F.node = E.node }; F -> id { F.node = Leaf(id, id.entry) }; F -> num { F.node = Leaf(num, num.val) }. Node and Leaf first look up a hash table keyed by <op, left, right> (value-number method) and return an existing node if one matches, so a repeated subexpression gets the same node (common subexpression detected)."
sources: ["KMS Chapter 6 slides 12-19 (DAG, SDD for Constructing DAG, Value Number Method)", "KMS Chapter 5 slides 55-57 (Postfix SDT, Parser-Stack Implementation)", "Dragon book 2e sec. 6.1.1-6.1.2"]
---
**Assumptions.** `id` has the attribute `entry` (symbol-table pointer) and `num` has `val`. The SDT is implemented by an LR parser (the grammar is left recursive).

**Postfix SDT** (every action at the right end of its production, so it runs at the reduction):

```text
E -> E1 + T    { E.node = Node('+', E1.node, T.node); }
E -> T         { E.node = T.node; }
T -> T1 * F    { T.node = Node('*', T1.node, F.node); }
T -> F         { T.node = F.node; }
F -> ( E )     { F.node = E.node; }
F -> id        { F.node = Leaf(id, id.entry); }
F -> num       { F.node = Leaf(num, num.val); }
```

On an LR parser stack, the action for $E \to E_1 + T$ is `stack[top-2].node = Node('+', stack[top-2].node, stack[top].node); top = top - 2;`. The others are similar.

**How common subexpressions are detected.** `Node` and `Leaf` do not blindly create nodes. They use the **value-number method**:

- The nodes are kept in an array/hash table. Each interior node is a record `<op, left, right>`, where left and right are the value numbers (indices) of the children; a leaf is `<label, value>`.
- `Node(op, l, r)` first searches the table (hashing on `<op, l, r>`). If such a node already exists, it **returns the existing node**; otherwise it creates a new one, enters it, and returns it. `Leaf` works the same way, so each `id`/`num` has exactly one leaf.

So a subexpression that occurs twice is built once, and both occurrences point to the same node: in the DAG that node has two parents. This is exactly a common subexpression.

**Example:** `a + a * (b + c) + (b + c) * d`:

| Step | Call | Result |
|:-:|:--|:--|
| 1 | `Leaf(id, a)` | new node 1 |
| 2 | `Leaf(id, a)` | **existing** node 1 |
| 3 | `Leaf(id, b)`, `Leaf(id, c)` | nodes 2, 3 |
| 4 | `Node('+', 2, 3)` | node 4 (`b+c`) |
| 5 | `Node('*', 1, 4)` | node 5 |
| 6 | `Node('+', 1, 5)` | node 6 |
| 7 | `Leaf(id, b)`, `Leaf(id, c)` | existing 2, 3 |
| 8 | `Node('+', 2, 3)` | **existing** node 4: `b+c` recognised as common |
| 9 | `Leaf(id, d)`; `Node('*', 4, 7)` | nodes 7, 8 |
| 10 | `Node('+', 6, 8)` | node 9 (root) |

For the paper's example `2*(3+4)*5`, the leaves 2, 3, 4, 5 and the nodes for `3+4`, `2*(3+4)` and `...*5` are created. A number that appears twice would also be shared.
