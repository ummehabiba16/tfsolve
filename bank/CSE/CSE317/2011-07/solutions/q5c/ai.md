---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "PEAS = Performance measure, Environment, Actuators, Sensors. FIFA 2011, for the agent controlling one player: P = win, goal difference, possession; E = virtual pitch, ball, 22 players, referee rules; A = move, pass, shoot, tackle, switch player; S = game state or screen view of positions. Properties: partially observable (fully, if the game state is read directly), stochastic, sequential, dynamic, continuous, multi-agent, competitive against the opponents and cooperative with teammates."
sources: ["AIMA 3e sec. 2.3 (PEAS, properties of task environments)"]
---
**PEAS description.** A specification of a task environment through its **Performance measure, Environment, Actuators** and **Sensors**. It is the first step in designing an agent.

**PEAS for the FIFA 2011 player-controlling agent:**

- *Performance:* winning the match, goals scored minus goals conceded, possession, few fouls.
- *Environment:* the virtual pitch, the ball, 11 teammates and 11 opponents (controlled by the PC), the referee and the game rules, the clock.
- *Actuators:* move the controlled player, run, pass, shoot, tackle, switch to another player.
- *Sensors:* the game screen (camera view) or game-state information: positions of the ball and players, score, time.

**Task-environment characteristics.**

| Property | FIFA 2011 | Reason |
|:--|:--|:--|
| Observable | **partially** observable | the camera shows only part of the pitch, and opponents' intentions are hidden (fully observable only if the agent reads the whole game state) |
| Deterministic / stochastic | **stochastic** | the other 21 players' actions are not known in advance, and shots and passes have random outcomes |
| Episodic / strategic / sequential | **sequential** (and *strategic*, since opponents are agents) | current actions (positioning, passes) affect future situations |
| Static / dynamic | **dynamic** | the game continues in real time while the agent decides |
| Discrete / continuous | **continuous** | positions, velocities and time are continuous |
| Agents | **multi-agent** | 22 agents |
| Competitive / cooperative | **both** | competitive against the opposing team, cooperative with own teammates |
