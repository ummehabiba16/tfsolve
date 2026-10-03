---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "DOF = the number of independent parameters needed to specify the robot's configuration (a rigid body in 3-D has 6; a car has 3). Tasks are specified in workspace (Cartesian) coordinates, but planning is easier in configuration space, where the robot is a point and obstacles become C-space obstacles; the planner switches by forward and inverse kinematics."
sources: ["AIMA 4e sec. 26.5-26.6 (configuration space, motion planning)"]
---
**Degree of freedom (DOF).** The number of independent parameters (coordinates) needed to specify the complete configuration of the robot. Each actuated joint usually adds one.

- A free rigid body in 3-D has 6 DOF (3 position + 3 orientation).
- A car on the ground has 3 DOF $(x,y,\theta)$.
- A typical arm has 6-7 DOF (one per revolute joint).

**Why switch between configuration space and coordinate (work) space?**

- The **task** is stated in **workspace / Cartesian coordinates**: "put the gripper at position $(x,y,z)$", and obstacles are described there.
- **Planning** is much easier in **configuration space (C-space)**, the space of joint values. There the whole robot is a **single point**, the obstacles become C-space obstacles, and motion planning becomes finding a path for a point through free C-space (with cell decomposition or roadmaps). In the workspace, the robot is a complex linked shape, and checking collisions along a motion is hard.
- The robot also moves by commanding its **joints**, i.e. in C-space.

So the planner maps the goal from workspace to C-space (**inverse kinematics**), plans in C-space, and maps configurations back to the workspace (**forward kinematics**) to check collisions and verify the task.
