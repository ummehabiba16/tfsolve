---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "CPU-bound processes use long CPU bursts, I/O-bound ones short bursts between I/O; giving I/O-bound processes priority keeps the I/O devices busy and responsive."
sources: ["Tanenbaum MOS 4e, sec. 2.4.1 (CPU-bound and I/O-bound processes); sec. 2.4.4 (priority scheduling)"]
---
- **CPU-bound (compute-bound) process:** spends most of its time computing; long CPU bursts, rare I/O requests.
- **I/O-bound process:** spends most of its time waiting for I/O; very short CPU bursts between I/O requests (it computes only briefly to issue the next request).

**Why I/O-bound processes get higher priority.** An I/O-bound process needs the CPU only for a short moment, after which it issues an I/O request and blocks. If it is given the CPU at once, it quickly starts its next I/O operation, so the **I/O devices stay busy in parallel** with the CPU (overlap), which raises the overall utilisation of the system. It also gives good **response time** to interactive processes. Giving it the CPU first costs the CPU-bound process almost nothing, because the I/O-bound process uses the CPU only briefly. If a CPU-bound process ran first, the I/O-bound processes would wait for its whole long burst and the devices would sit idle.
