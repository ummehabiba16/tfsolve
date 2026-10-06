---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Three methods for evaluating semantic rules to decorate a parse tree: (1) parse-tree methods (build the tree and dependency graph at compile time and evaluate in a topological order), (2) rule-based methods (the order is fixed at compiler-construction time by analysing the grammar and semantic rules), (3) oblivious methods (a fixed order of evaluation, e.g. one left-to-right pass or bottom-up, chosen without looking at the semantic rules)."
sources: ["KMS Chapter 5 slides 23-40 (evaluation order)", "Dragon book 2e sec. 5.2.1-5.2.4"]
---
To decorate a parse tree (compute all attribute values) the semantic rules must be evaluated in an order that respects the dependencies. Three methods have been proposed:

1. **Parse-tree methods.** At **compile time** the compiler builds the parse tree, constructs the **dependency graph** of the attribute instances, and finds a **topological order** of the graph; the rules are evaluated in this order. It works for every SDD whose dependency graphs have no cycles, but it is the most expensive (the graph is built for every input) and needs the whole tree in memory.

2. **Rule-based methods.** The order of evaluation of the attributes for each production is determined **when the compiler is built**, by analysing the grammar and the semantic rules (static analysis of the dependencies between attributes of each production); the compiler then evaluates the rules in that order, using no dependency graph at run time. It is faster than parse-tree methods but needs a more complex generator (e.g. for ordered attribute grammars).

3. **Oblivious methods.** The order is chosen **without looking at the semantic rules**: a fixed traversal such as one left-to-right depth-first pass, or bottom-up during LR parsing. It is simple and fast, and suits **S-attributed** (bottom-up) and **L-attributed** (left-to-right depth-first) definitions, but cannot evaluate arbitrary dependencies; the grammar designer has to make the rules fit the order.

| Method | Order determined | Generality | Cost |
|:--|:--|:--|:--|
| Parse-tree | at compile time, per input | any acyclic SDD | highest |
| Rule-based | when the compiler is constructed | wide | medium |
| Oblivious | fixed in advance | S- and L-attributed only | lowest |
