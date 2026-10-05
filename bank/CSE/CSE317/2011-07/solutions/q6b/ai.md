---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Material value: a numeric weight for each piece, summed in a linear evaluation function, as with chess material (pawn 1, queen 9). For Ludo: a piece at home is worth 0; an active piece is worth its progress along the track; a paka guti (allowed to enter home) gets a bonus over a kacha one; pieces on safe cells get a bonus and pieces within reach of an opponent a risk penalty; finished pieces get the highest value. Eval = sum of own values - sum of the opponent's."
sources: ["AIMA 3e sec. 5.4.1 (evaluation functions, material value)", "Ludo rules (kacha/paka guti, safe squares)"]
---
**Material value.** In game playing, the material value is a numeric weight given to each piece. The **evaluation function** is then a weighted linear sum of features, as in chess, where pawn = 1, knight or bishop = 3, rook = 5 and queen = 9:

$$Eval(s)=\sum_{\text{my pieces}}MV(p)-\sum_{\text{opponent's pieces}}MV(p).$$

It estimates how good a non-terminal position is when search has to stop.

**Scheme for 2-player Ludo** (each player has 4 pieces; track length $L$, about 57 steps to home). For each piece $p$ with progress $d(p)$ steps:

| Situation of the piece | Material value $MV(p)$ |
|:--|:--|
| Still in the yard (not opened) | 0 |
| Opened, **kacha guti** (unripe: cannot yet enter the home column) | $10+\dfrac{d(p)}{L}\times40$ |
| **paka guti** (ripe: has made a capture, may enter the home column) | $25+\dfrac{d(p)}{L}\times60$ |
| Inside the home column (cannot be captured) | 80 |
| Reached home (finished) | 100 |

**Safety adjustments:**

- $+10$ if the piece is on a **safe cell** (star or starting squares, where it cannot be captured), or forms a block with another own piece;
- $-k\cdot P(\text{capture})$ if an opponent piece is 1-6 cells behind it. For example, subtract $\frac{\#\text{dice values that hit it}}{6}\times MV(p)$: the expected loss if it is captured.
- (Optionally) $+5$ for each opponent piece within striking distance ahead (a capture threat).

The weights reflect that a piece's worth grows with progress and maturity (paka > kacha). Pieces close to home and safe are hardest for the opponent to undo. The evaluation is the difference between the two players' total material values, used at the cut-off of an expectiminimax search over dice outcomes.

*Note:* "kacha guti" is taken as a piece that has not yet captured (and so cannot go home), and "paka guti" as one that has, following the common Bangladeshi rules. The exact numbers are design choices.
