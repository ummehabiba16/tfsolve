---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "S -> while ( {begin=newlabel(); B.true=newlabel(); B.false=S.next} B ) {S1.next=begin} S1 {S.code = label(begin) || B.code || label(B.true) || S1.code || gen('goto' begin)}: inherited attributes are computed by actions just before the symbol that uses them, the synthesized attribute S.code at the end."
sources: ["KMS Chapter 5 slides 48-80 (SDT schemes, L-attributed SDDs)", "Dragon book 2e sec. 5.4.5, Fig. 6.36"]
---
The SDD is **L-attributed**, so it can be turned into an SDT with the rules of Dragon book sec. 5.4.5:

1. Embed the action that computes an **inherited attribute** of a nonterminal $A$ in the body *immediately before* $A$.
2. Place the action that computes a **synthesized attribute** of the head at the **end** of the production.

Here $B.true$ and $B.false$ are inherited by $B$, and $S_1.next$ is inherited by $S_1$; $S.code$ is synthesized. Note that $B.true$, $B.false$ and $begin$ must be computed before $B$ is parsed, and $S_1.next = begin$ before $S_1$.

$$S \to \textbf{while}\ (\ \{\,begin = newlabel();\ B.true = newlabel();\ B.false = S.next;\,\}\ B\ )\ \{\,S_1.next = begin;\,\}\ S_1$$

$$\{\,S.code = label(begin)\ /\!/\ B.code\ /\!/\ label(B.true)\ /\!/\ S_1.code\ /\!/\ gen(\text{'goto'}\ begin);\,\}$$

(the second line is the last action of the same production, written on its own line for space; $/\!/$ is the concatenation operator printed as `//` in the question).

The order of the actions is: first the three assignments, then the parse of $B$, then $S_1.next = begin$, then the parse of $S_1$, and finally the construction of $S.code$ from $B.code$ and $S_1.code$, which only exist after $B$ and $S_1$ have been translated. Because every inherited attribute is defined only from attributes of the head or of symbols to the left, the actions can be executed in one left-to-right pass.
