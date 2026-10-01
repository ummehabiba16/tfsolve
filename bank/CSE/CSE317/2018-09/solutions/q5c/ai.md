---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "PEAS = Performance measure, Environment, Actuators, Sensors, the specification of the task environment. Examples: automated taxi driver (safe, fast, legal, comfortable, profitable; roads, traffic, pedestrians, customers; steering, accelerator, brake, signal, horn; cameras, sonar, speedometer, GPS) and medical diagnosis system (healthy patient, low cost; patient, hospital, staff; display of questions, tests, diagnoses, treatments; keyboard entry of symptoms and findings)."
sources: ["AIMA 3e sec. 2.3.1 (Figures 2.4, 2.5)"]
---
**PEAS description.** The first step in designing an agent is to specify its **task environment** as completely as possible:

- **P**erformance measure: the criterion of success;

- **E**nvironment: what the agent operates in;

- **A**ctuators: how it acts;

- **S**ensors: how it perceives.

**Example 1: automated taxi driver**

| | |
|:--|:--|
| Performance | Safe, fast, legal, comfortable trip, maximise profits |
| Environment | Roads, other traffic, pedestrians, customers |
| Actuators | Steering, accelerator, brake, signal, horn, display |
| Sensors | Cameras, sonar, speedometer, GPS, odometer, accelerometer, engine sensors, keyboard |

**Example 2: medical diagnosis system**

| | |
|:--|:--|
| Performance | Healthy patient, reduced costs |
| Environment | Patient, hospital, staff |
| Actuators | Display of questions, tests, diagnoses, treatments, referrals |
| Sensors | Keyboard entry of symptoms, findings, patient's answers |

(Other valid examples: part-picking robot, satellite image analyser, interactive English tutor.)
