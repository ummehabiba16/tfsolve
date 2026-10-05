---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "Heuristics for the hostile agents: start at the gunshot's source (the last known position) and search outward within the radius reachable since the shot (speed x elapsed time); score candidate positions by the distance from the last shot, the cover and hiding spots available, and the escape routes; split the agents to cover different sectors and to block exits; update a probability map after each new shot."
sources: ["AIMA 3e sec. 3.6 (inventing heuristics), sec. 4.4 (belief-state search)", "game-AI pursuit-evasion practice"]
---
The protagonist is invisible between shots, so the hostile agents search over a **belief state**: the set of places the player could be. Every gunshot reveals the exact source. Useful heuristics:

1. **Last-known position:** start the search at the location of the most recent gunshot.
2. **Reachability radius:** since the shot, the player can have moved at most $d=v_{max}\cdot\Delta t$ (stealth speed times elapsed time). Only search inside this circle (a reachable-region heuristic, like a Manhattan or Euclidean distance bound). Prefer positions closer to the last shot: estimated cost $h=$ distance from the agent to the candidate position, and probability decreasing with distance from the shot.
3. **Likely hiding spots first:** rank candidate positions by cover (walls, buildings, bushes), proximity to escape routes, and line of sight to where the agents were (the player tends to hide where it can shoot again).
4. **Divide and conquer:** split the agents to cover different sectors of the reachable region and **block exits and chokepoints**, so the region shrinks over time.
5. **Probability (heat) map:** keep a probability over grid cells. It diffuses outward each time step and is reset to a peak at each new gunshot. Search the highest-probability cells first.
6. **Avoid predictability:** agents keep distance from each other and do not all converge on the shot point, to avoid being picked off one by one.
