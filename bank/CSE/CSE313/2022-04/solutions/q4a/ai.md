---
author: ai
via: chat
status: unverified
summary: 'Compute-bound: long CPU bursts, rare I/O (timeline mostly CPU). I/O-bound: short CPU bursts with frequent long I/O waits (timeline mostly waiting).'
sources: [Scheduling slides 5-7, 'Tanenbaum, MOS 4e, sec. 2.4.1 (Fig 2-39)']
imported_from: tfsolve-questions/data/solutions/2019-20.json
---
- Compute-bound (CPU-bound): a long CPU burst then a short I/O, repeatedly, the timeline is mostly CPU activity. Limited by CPU speed.
- I/O-bound: a short CPU burst then a long I/O wait, repeatedly, the timeline is mostly device waiting. Limited by device speed.

Figure: two horizontal burst timelines, the compute-bound one as long CPU blocks with brief I/O gaps, the I/O-bound one as short CPU blocks with long I/O gaps. As memory grows and processes get more CPU, they tend to become more I/O-bound.
