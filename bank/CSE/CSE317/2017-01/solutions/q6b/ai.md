---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "PEAS for: (i) used AI books on the Internet (performance: price, quality, cost, speed; environment: web sites, sellers, shippers; actuators: browse, fill forms, pay; sensors: web pages); (ii) bidding at an auction (performance: item won at low price; environment: auctioneer, other bidders, items; actuators: place bids; sensors: current price, bids, item description); (iii) playing soccer (performance: goals scored and conceded, winning; environment: field, ball, teammates, opponents; actuators: legs, kicking, running; sensors: cameras, touch, odometry)."
sources: ["AIMA 3e sec. 2.3.1 (PEAS), Exercise 2.4"]
---
| Activity | Performance measure | Environment | Actuators | Sensors |
|:--|:--|:--|:--|:--|
| **(i) Shopping for used AI books on the Internet** | low price, right books, condition or quality, quick delivery, low shipping cost, secure transaction | Internet web sites, online bookstores and sellers, payment and shipping services, the user | follow links, fill in search forms, display results, place orders, pay | web pages (HTML text, images), user requests, order confirmations |
| **(ii) Bidding on an item at an auction** | wins the desired item, at the lowest price, within budget; time spent | auctioneer, other bidders, items, auction rules (live or online) | place a bid (amount), raise paddle or click, withdraw | current price, bids from others, auctioneer's calls, item description, time left |
| **(iii) Playing soccer** | goals scored minus goals conceded, winning the match, fair play (no fouls) | soccer field, ball, own team, opponents, referee, weather | legs and feet (run, dribble, kick, pass), body and head | cameras or vision, ball and player positions, touch or contact sensors, odometry, hearing (whistle) |

Brief environment properties: (i) partially observable, deterministic, sequential, static, discrete, single-agent (but strategic sellers); (ii) partially observable, strategic, sequential, dynamic, multi-agent competitive; (iii) partially observable, stochastic, sequential, dynamic, continuous, multi-agent (cooperative and competitive).
