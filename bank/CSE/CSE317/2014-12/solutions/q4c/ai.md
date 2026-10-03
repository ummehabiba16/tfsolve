---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "PEAS: soccer (goals, winning / field, ball, players / legs, kick / cameras, touch); Titan ocean explorer (data gathered, survival, energy / subsurface ocean, currents, ice / thrusters, sampling arm, transmitter / sonar, cameras, chemical and pressure sensors); tennis (points or match won / court, ball, net, opponent / arm, racket, legs / cameras, ball tracking, joint sensors); high jump (bar height cleared, no knock-off / track, bar, mat / legs, body / cameras, joint angle, IMU)."
sources: ["AIMA 3e sec. 2.3.1, Exercise 2.4"]
---
| Activity | Performance measure | Environment | Actuators | Sensors |
|:--|:--|:--|:--|:--|
| **(i) Playing soccer** | goals scored minus conceded, winning, possession, no fouls | field, ball, teammates, opponents, referee | legs or wheels, kicker, head, communication | cameras, contact sensors, odometry, IMU, microphone (whistle) |
| **(ii) Exploring the subsurface oceans of Titan** | scientific data collected (maps, samples, signs of life), survival time, energy efficiency, successful transmission | liquid hydrocarbon or water ocean under ice, currents, low temperature and high pressure, seabed, ice crust | thrusters or propellers, rudders, sampling arm or drill, ballast, radio transmitter | sonar, cameras and lights, chemical analysers, pressure and temperature sensors, IMU, depth gauge |
| **(iii) Playing a tennis match** | points, games and sets won, winning the match, few unforced errors | court, net, ball, opponent, umpire, weather | arms with racket, legs (running), body | cameras or vision (ball tracking), ball-speed estimate, joint and force sensors, hearing |
| **(iv) Performing a high jump** | height of the bar cleared without knocking it off, number of attempts | runway, bar and standards, landing mat | legs (run-up, take-off), arms and body (arching over the bar) | vision (bar position, run-up marks), joint angle and force sensors, IMU (balance) |

Environment properties, briefly: soccer and tennis are multi-agent, dynamic, continuous and partially observable; the Titan explorer is single-agent, partially observable, stochastic and dynamic, with very limited communication; high jump is single-agent, episodic per attempt, continuous and dynamic.
