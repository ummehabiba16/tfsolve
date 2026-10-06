---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "FCFS 146 cylinders = 876 ms; SSTF 60 cylinders = 360 ms; elevator 58 cylinders = 348 ms."
sources: ["Tanenbaum MOS 4e, sec. 5.4.3 (disk arm scheduling)"]
---
Requests (in arrival order): 10, 22, 20, 2, 40, 6, 38. The arm starts at cylinder 20; one cylinder costs 6 ms.

**(i) FCFS** (serve in arrival order): $20\to10\to22\to20\to2\to40\to6\to38$.

$$10+12+2+18+38+34+32=146\text{ cylinders}\ \Rightarrow\ 146\times6=\mathbf{876\ ms}$$

**(ii) SSTF** (nearest request next): $20\to20\to22\to10\to6\to2\to38\to40$.

$$0+2+12+4+4+36+2=60\text{ cylinders}\ \Rightarrow\ 60\times6=\mathbf{360\ ms}$$

**(iii) Elevator** (moving up first, reverse at the last request in that direction): $20\to22\to38\to40$ (up), then $10\to6\to2$ (down).

$$(22-20)+(38-22)+(40-38)+(40-10)+(10-6)+(6-2)=2+16+2+30+4+4=58\text{ cylinders}$$

$$58\times6=\mathbf{348\ ms}$$

(The request at cylinder 20 is served at once, with no movement.)
