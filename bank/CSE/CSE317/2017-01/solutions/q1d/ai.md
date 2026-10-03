---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Industrial robots work in structured, fully known, static environments, repeating preprogrammed motions (welding, painting) without perception or reasoning; AI robots must perceive, reason, plan and learn under uncertainty in unstructured, dynamic environments. Example domain, robotic cars: autonomous vehicles (DARPA challenges, Waymo, Tesla) using LIDAR, cameras, SLAM and planning for self-driving and driver assistance."
sources: ["AIMA 3e sec. 25.1 and 25.8 (application domains)"]
---
**AI robotics versus industrial robotics.**

| Industrial robotics | AI robotics |
|:--|:--|
| Highly **structured**, engineered workcell; every part is placed where expected | **Unstructured**, partially observable, dynamic real world |
| Repeats **pre-programmed** trajectories (welding, painting, pick-and-place) | **Perceives**, **reasons and plans** online, **learns** from experience |
| Little or no sensing; position control | Rich sensing (vision, LIDAR, touch), handling sensor noise and uncertainty (probabilistic localization, SLAM) |
| Fails if the environment changes | Adapts to new situations, obstacles and people |

The key difference is **autonomy under uncertainty**: AI robots must decide what to do based on what they perceive.

**Recent applications: (i) robotic cars.** Autonomous vehicles (the DARPA Grand and Urban Challenges, Waymo, Tesla Autopilot, Baidu Apollo) combine LIDAR, radar and cameras with deep-learning perception, probabilistic localization and mapping (SLAM) and motion planning. They do lane keeping, adaptive cruise control, automatic emergency braking, self-parking and full self-driving in limited areas (robotaxis). The aims are fewer accidents (about 90% are caused by human error) and mobility for people who cannot drive.

(Alternatives: *health care*, with surgical robots such as da Vinci assisting surgeons with precise minimally invasive operations, plus rehabilitation and elder-care robots. *Human augmentation*, with powered exoskeletons and intelligent prosthetic limbs controlled by muscle or brain signals.)
