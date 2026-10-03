---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Subsumption architecture (Brooks): reactive controllers built bottom-up from layers of augmented finite state machines (AFSMs) wired directly from sensors to actuators; higher layers subsume (suppress or override) lower ones, with no central world model. An AFSM is an FSM extended with timers and inputs/outputs on wires (signals). A hexapod leg AFSM: lift leg, swing forward, set down, push back, with sensor feedback (e.g. a collision or a stuck leg triggers a higher lift)."
sources: ["AIMA 3e sec. 25.7.1 (subsumption architecture, Fig. 25.24)"]
---
**Working principle of the subsumption architecture** (Brooks, 1986). A framework for building **reactive** robot controllers bottom-up, without symbolic planning or a central world model.

- The controller is a set of **layers**, each a simple behaviour (avoid obstacles, walk, explore). Layers run **in parallel** and connect sensors almost directly to actuators.
- Higher layers implement more complex goals and can **subsume** lower ones: they *suppress* a lower layer's input or *inhibit* its output. For example, "walk to light" overrides plain "walk".
- Behaviour emerges from the interaction of the layers with the environment. Design is incremental: get the lowest layer working, then add layers on top.
- It is fast and robust to sensor noise, but hard to extend to complex tasks requiring memory or deliberation.

**Augmented finite state machine (AFSM).** A finite state machine augmented with **timers** (clocks that trigger state changes after a delay) and with input and output **wires** carrying sensor signals and actuator commands. AFSMs communicate by sending signals over these wires. Subsumption controllers are networks of AFSMs.

**AFSM for one leg of a hexapod robot.** A cyclic walking gait, with sensor feedback for obstacles:

```text
          +-----------+   timer   +-------------+   timer   +------------+
  start ->| S1: lift  |---------->| S2: swing   |---------->| S3: set    |
          | leg up    |           | leg forward |           | leg down   |
          +-----------+           +-------------+           +------------+
                ^                       |                         |
                |               collision sensor                  | ground contact
                |               (leg hits obstacle)               v
                |                       |                  +-------------+
                |                       v                  | S4: push    |
                |               +---------------+          | leg back    |
                +---------------| S5: retract & |          | (propel)    |
                    timer       | lift higher   |          +-------------+
                                +---------------+                 |
                ^                                                 |
                +------------------------- timer -----------------+
```

Signals: *up/down* and *forward/back* commands to the leg's two motors. The coordination between legs (alternating tripod gait: legs 1-4-5 move while 2-3-6 support) is handled by a higher layer that triggers the AFSMs of the appropriate legs.
