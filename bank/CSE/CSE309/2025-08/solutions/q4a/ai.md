---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "LR(0): LR(0) automaton, fewest states, weakest; SLR(1): same LR(0) automaton + FOLLOW sets, same states, more grammars; CLR(1): LR(1) automaton, many more states (often 10x), most powerful; LALR(1): LR(1) automaton with same-core states merged, same states as SLR, power between SLR and CLR (used by Yacc). LR(0) < SLR < LALR < CLR."
sources: ["MMA syntax analysis slides 227-238, 354, 404-406, 490-494", "Dragon book 2e sec. 4.6-4.7"]
---
| Parser | Automaton used | Number of states | Parsing capability |
|:--|:--|:--|:--|
| LR(0) | LR(0) items (canonical LR(0) collection) | $n$ (fewest) | Weakest: any state with a complete item must reduce on every input; no lookahead |
| SLR(1) | LR(0) automaton; reduce $A \to \alpha$ on FOLLOW($A$) | $n$ (same as LR(0)) | More than LR(0); fails when FOLLOW is too coarse (e.g. $S \to L = R \mid R$) |
| LALR(1) | LR(1) automaton with states of the same core merged (or LR(0) automaton with propagated lookaheads) | $n$ (same as SLR) | Between SLR and CLR; may get reduce/reduce conflicts after merging; used by Yacc/Bison |
| CLR(1) (canonical LR) | LR(1) items $[A \to \alpha \cdot \beta, a]$ | Often 5-10 times $n$ (thousands for a real language) | Most powerful: every LR(1) grammar |

*Here $n$ is the number of LR(0) item sets.*

Grammar classes: LR(0) $\subset$ SLR(1) $\subset$ LALR(1) $\subset$ LR(1). All four parsers use the same driver algorithm (stack of states with ACTION and GOTO tables); they differ only in how the tables are built. For a language like C, SLR and LALR tables have a few hundred states, while canonical LR(1) has several thousand.
