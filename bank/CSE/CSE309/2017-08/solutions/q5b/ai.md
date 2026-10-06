---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "A parse tree shows every grammar symbol of the derivation, an AST only the operators and operands. Postfix SDT run on reduction: S -> id = E {assign node}, S -> id [E] = E {assign(index(id,E1),E2)}, E -> E+T {node('+')}, T -> T*F {node('*')}, F -> id | id[E] | num build leaf/node objects kept in the parser stack."
sources: ["KMS Chapter 5 slides 41-47 (syntax tree construction), 48-69 (postfix SDT)", "Dragon book 2e sec. 2.5.1, 5.3.1, 5.4.1-5.4.2"]
---
**Parse tree versus abstract syntax tree.** A **parse tree** is the concrete syntax: each interior node is a nonterminal and the leaves are the terminals of the input, so it contains every grammar symbol, including chain nodes such as $E \to T \to F$ and punctuation like `[`, `]`, `=`. An **abstract syntax tree** (AST, syntax tree) keeps only the **meaningful constructs**: interior nodes are operators (`+`, `*`, assign, index) and their children are the operands; helper nonterminals and punctuation disappear. For `a[i] = b + 2`, the AST is `assign(index(a, i), +(b, 2))`.

**Postfix SDT (all actions at the right end of the body)**, using `Node(op, child...)` and `Leaf(token, value)` to create tree nodes, with each node pointer stored as the attribute `node` of the grammar symbol:

```text
S -> id = E          { S.node = new Node('assign', new Leaf(id, id.entry), E.node) }
S -> id [ E1 ] = E2  { S.node = new Node('assign',
                          new Node('index', new Leaf(id, id.entry), E1.node), E2.node) }
E -> E1 + T          { E.node = new Node('+', E1.node, T.node) }
E -> T               { E.node = T.node }
T -> T1 * F          { T.node = new Node('*', T1.node, F.node) }
T -> F               { T.node = F.node }
F -> id              { F.node = new Leaf(id, id.entry) }
F -> id [ E ]        { F.node = new Node('index', new Leaf(id, id.entry), E.node) }
F -> num             { F.node = new Leaf(num, num.val) }
```

**Implementation with the parser stack** (Dragon book sec. 5.4.2). An LR parser keeps the attributes next to the symbols in its stack; when it reduces by a production, the symbols of the body are on top of the stack, so the action refers to them as `stack[top]`, `stack[top-1]`, ..., and the result is stored where the head will be after the reduction:

```text
S -> id = E          stack[top-2].node = new Node('assign', new Leaf(id, stack[top-2].entry),
                                                  stack[top].node);
                     top = top - 2;
S -> id [ E1 ] = E2  stack[top-5].node = new Node('assign',
                         new Node('index', new Leaf(id, stack[top-5].entry), stack[top-3].node),
                         stack[top].node);
                     top = top - 5;
E -> E1 + T          stack[top-2].node = new Node('+', stack[top-2].node, stack[top].node);
                     top = top - 2;
T -> T1 * F          stack[top-2].node = new Node('*', stack[top-2].node, stack[top].node);
                     top = top - 2;
F -> id              stack[top].node = new Leaf(id, stack[top].entry);
F -> id [ E ]        stack[top-3].node = new Node('index', new Leaf(id, stack[top-3].entry),
                                                   stack[top-1].node);
                     top = top - 3;
F -> num             stack[top].node = new Leaf(num, stack[top].val);
E -> T,  T -> F      (no action: the node attribute is already in the right stack position)
```

For example, for the input `a[i] = b + 2`, the reductions build `Leaf(a)`, `Leaf(i)`, `index(a, i)`, `Leaf(b)`, `Leaf(2)`, `+(b, 2)` and finally `assign(index(a, i), +(b, 2))`; this is the AST.
