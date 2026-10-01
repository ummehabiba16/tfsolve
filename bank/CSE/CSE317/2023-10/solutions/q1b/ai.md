---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "PEAS tables for an auction bidding agent, a medical diagnosis system and an interactive English tutor."
sources: ["AIMA 3e sec. 2.3.1 (Figure 2.5) and Exercise 2.4"]
---
PEAS = Performance measure, Environment, Actuators, Sensors.

**(i) Bidding on an item at an auction**

| | |
|:--|:--|
| Performance | Win desired items, at the lowest price, within the budget; not overpaying (cost vs. value) |
| Environment | Auctioneer, other bidders, items for sale, auction rules (English/Dutch/sealed-bid), time |
| Actuators | Place a bid, raise bid, withdraw/stop bidding (speaker, raised paddle, or bid button/API) |
| Sensors | Current price, bids of others, auctioneer's announcements, item description, time remaining (camera/microphone or web feed) |

**(ii) Medical diagnosis system**

| | |
|:--|:--|
| Performance | Healthy patient, correct diagnosis, minimised costs and risk, no lawsuits |
| Environment | Patient, hospital, doctors, staff, laboratory |
| Actuators | Display of questions, tests, diagnoses, treatments, referrals |
| Sensors | Keyboard entry of symptoms, findings, patient's answers; test results; medical images |

**(iii) Interactive English tutor**

| | |
|:--|:--|
| Performance | Student's score on tests, improvement in reading/writing/speaking, engagement |
| Environment | Set of students, testing agency, course material |
| Actuators | Display of exercises, suggestions, corrections, explanations (screen, speech) |
| Sensors | Keyboard input, microphone (spoken answers), possibly camera |

Environment properties (brief): auction: partially observable, multi-agent (competitive), stochastic/strategic, sequential, dynamic, discrete. Medical diagnosis: partially observable, single-agent, stochastic, sequential, dynamic, continuous. English tutor: partially observable, multi-agent, stochastic, sequential, dynamic, discrete.
