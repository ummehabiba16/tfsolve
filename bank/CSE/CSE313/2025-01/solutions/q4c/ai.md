---
author: ai
via: chat
status: unverified
summary: Multi-user OS shares one machine among concurrent users with protection; multi-processor OS runs one machine with several CPUs; lottery scheduling gives each process tickets and draws one to pick who runs, so CPU share is proportional to tickets.
sources: [Introduction slides 35-36, Scheduling slides 46-47, 'Tanenbaum, MOS 4e, sec. 1.4 and 2.4.4']
imported_from: tfsolve-questions/data/solutions/2022-23.json
---
- Multi-user OS: lets several users share one machine concurrently, isolating and time-sharing CPU, memory and files with protection and accounting (e.g. a UNIX server).
- Multi-processor OS: manages a machine with two or more CPUs sharing memory, scheduling threads across CPUs and handling synchronisation and cache coherence to exploit true parallelism.
- Lottery scheduling: each process holds some lottery tickets; at each scheduling decision a ticket is drawn at random and its holder runs, so CPU share is proportional to ticket fraction. Cooperating processes can trade tickets and the scheme is naturally fair and responsive.
