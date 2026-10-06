---
marks: 10
topics: [deadlock-detection-graph, safe-vs-unsafe]
kind: diagram
source: {page: 62}
---
Suppose two processes, P1 and P2 are running concurrently in a single processor system. The system contains one printer and one DVD-ROM. P1 has 500 instructions and P2 has 300 instructions. P1 requests the DVD-ROM at 100th instruction and the printer at 200th instruction. P1 releases the DVD-ROM and printer at 300th and 400th instruction, respectively. P2 requests the printer at 50th instruction and the DVD-ROM at 100th instruction. P2 releases the printer and DVD-ROM at 150th and 200th instruction, respectively. Explain the concept of unsafe region and deadlock for this system graphically. Make necessary assumptions and mention those assumptions.
