---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Local beam search keeps k states, generates all their successors and keeps the k best; unlike hill climbing (one state) it shares information among k searches, and unlike SA it is greedy and deterministic (stochastic beam search adds randomness)."
sources: ["AIMA 3e sec. 4.1.3 (Local beam search)"]
---
**Local beam search.** Keeps track of $k$ states instead of one:

1. Start with $k$ randomly generated states.

2. At each step generate all successors of all $k$ states.

3. If any successor is a goal, stop; otherwise select the **best $k$ successors from the complete list** and repeat.

**Difference from hill climbing.** Hill climbing keeps a single state. Local beam search is not the same as $k$ independent random-restart hill climbs: information is shared, because if one state generates many good successors, the next generation is concentrated around it, and unpromising searches are abandoned. With $k=1$ it reduces to hill climbing.

**Difference from simulated annealing.** SA keeps one state and escapes local maxima by accepting worse moves with a temperature-controlled probability. Local beam search is greedy (always keeps the best $k$) and has no temperature; it can suffer from lack of diversity, with all $k$ states crowded into one region. *Stochastic beam search* fixes this by choosing the $k$ successors at random with probability increasing with their value, which is similar in spirit to natural selection (and to GAs).

| | Hill climbing | Simulated annealing | Local beam search |
|:--|:-:|:-:|:-:|
| States kept | 1 | 1 | $k$ |
| Accepts worse moves | no | yes, probability $e^{\Delta E/T}$ | no (yes in stochastic version) |
| Escapes local maxima | no (only by restarts) | yes | partly (k parallel searches) |
