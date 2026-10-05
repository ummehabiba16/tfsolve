---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Sound: in every model where (J and H) => P and not P are both true, P is false, so J and H must be false, so not J or not H is true. Truth table: the premises hold only in rows with P false and not both J and H, and in all of them not J or not H is true. (It is modus tollens followed by De Morgan.)"
sources: ["AIMA 3e sec. 7.4-7.5 (soundness, model checking)"]
---
**Rule.** From $(J\land H)\Rightarrow P$ and $\neg P$, infer $\neg J\lor\neg H$. It is sound iff **every model of the premises is a model of the conclusion**.

**Truth table** (rows where both premises are true are marked):

| $J$ | $H$ | $P$ | $(J\land H)\Rightarrow P$ | $\neg P$ | Both premises | $\neg J\lor\neg H$ |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| T | T | T | T | F | | F |
| T | T | F | F | T | | F |
| T | F | T | T | F | | T |
| T | F | F | T | T | **yes** | **T** |
| F | T | T | T | F | | T |
| F | T | F | T | T | **yes** | **T** |
| F | F | T | T | F | | T |
| F | F | F | T | T | **yes** | **T** |

In every row where both premises are true, the conclusion $\neg J\lor\neg H$ is true. So $\{(J\land H)\Rightarrow P,\ \neg P\}\models\neg J\lor\neg H$, and **the rule is sound**.

(It is **modus tollens**, which gives $\neg(J\land H)$, followed by **De Morgan's law**.)
