---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Robot soccer player: Performance: goals scored and conceded, winning, possession, no fouls or penalties. Environment: field, ball, own team, opponents, goals, referee. Actuators: legs or wheels (move, run), kicking device, head (header), communication with teammates. Sensors: cameras, ball and player detectors, odometry and IMU, contact sensors, microphone or network messages."
sources: ["AIMA 3e sec. 2.3.1 (PEAS), Exercise 2.4"]
---
**PEAS description of a robot soccer player.**

| | |
|:--|:--|
| **Performance measure** | goals scored for the team, goals conceded (against), winning the match, ball possession and successful passes, staying within the rules (no fouls, cards or penalties), energy use |
| **Environment** | the soccer field (lines, goals), the ball, teammates, opponents, the referee; lighting and noise |
| **Actuators** | legs or wheels (walking, running, turning), a kicking mechanism, head or body for blocking and heading, communication with teammates (wireless messages) |
| **Sensors** | cameras (vision of the ball, players, goals, field lines), odometry and wheel encoders, IMU and accelerometers (balance), touch or contact sensors, microphone or network receiver (referee whistle, team messages) |

The environment is partially observable, stochastic, sequential, dynamic, continuous and multi-agent: cooperative with teammates, competitive with opponents.
