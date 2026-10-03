---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "A car moving on a plane has 3 DOF (x, y, heading) but only 2 controllable ones (non-holonomic: it cannot move sideways). Robots with many DOF are hard because the configuration space grows exponentially in the DOF (planning becomes intractable), and there are more joints and actuators to sense, coordinate and control, and more weight, cost and failure points."
sources: ["AIMA 4e sec. 26.2 and 26.6 (robot configuration space, degrees of freedom)"]
---
**DOF of a car.** A car on the ground has **3 degrees of freedom**: position $(x,y)$ and orientation $\theta$. Its configuration is $(x,y,\theta)$. It has only **2 controls** (forward speed and steering angle) and cannot move sideways, so it is **non-holonomic**: it has fewer controllable DOF than total DOF and must manoeuvre (as in parallel parking) to reach some configurations.

**Why high-DOF robots are difficult to build** (3 marks):

- **Planning:** the configuration space has one dimension per DOF. Motion-planning methods (cell decomposition, roadmaps) scale exponentially with the dimension, so planning for a 7+ DOF arm or a humanoid (30+ DOF) is computationally very hard.
- **Control and sensing:** every joint needs an actuator, sensors and a coordinated controller. Dynamics couple the joints, and errors accumulate along long kinematic chains, which affects accuracy and stability.
- **Hardware:** more motors mean more weight, power, cost and points of failure, and a more complex mechanical design.
