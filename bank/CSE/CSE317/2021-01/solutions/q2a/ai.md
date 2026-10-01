---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Auction bidding: P = win items at low price within budget; E = auctioneer, bidders, items; A = bids; S = prices, bids, time; partially observable, multi-agent, stochastic/strategic, sequential, dynamic, discrete. Taxi: P = safe, fast, legal, comfortable, profitable; E = roads, traffic, pedestrians, customers; A = steering, accelerator, brake, signal, horn, display; S = cameras, sonar, speedometer, GPS, odometer, engine sensors, keyboard; partially observable, multi-agent, stochastic, sequential, dynamic, continuous."
sources: ["AIMA 3e sec. 2.3 (Figures 2.4, 2.6) and Exercise 2.4"]
---
**(i) Bidding on an item at an auction**

| PEAS | |
|:--|:--|
| Performance | Win the wanted item(s); pay as little as possible; stay within budget; maximise profit/value |
| Environment | Auctioneer, other bidders, items, auction rules, time |
| Actuators | Bid / raise bid / stop bidding (raise paddle, speak, click) |
| Sensors | Auctioneer's announcements, current highest bid, other bids, item details, clock |

Properties: **partially observable** (others' valuations unknown), **multi-agent, competitive**, **stochastic / strategic** (outcome depends on others' bids), **sequential** (each bid affects later ones), **dynamic** (price changes while deciding), **discrete** (bid increments), known rules.

**(ii) Automated taxi driving**

| PEAS | |
|:--|:--|
| Performance | Safe, fast, legal, comfortable trip; maximise profit; minimise fuel and wear |
| Environment | Roads, other traffic, pedestrians, customers, weather, police |
| Actuators | Steering, accelerator, brake, gear, signal, horn, display/speech to passenger |
| Sensors | Cameras, radar/LIDAR/sonar, speedometer, GPS, odometer, accelerometer, engine sensors, keyboard/microphone |

Properties: **partially observable**, **multi-agent** (partly cooperative, partly competitive), **stochastic**, **sequential**, **dynamic**, **continuous** (states, time and actions), and largely **known** physics but unknown other drivers. It is one of the hardest task environments.
