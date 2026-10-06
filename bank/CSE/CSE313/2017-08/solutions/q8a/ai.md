---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Priority scheduling runs the highest-priority ready process (risk of starvation, fixed by aging); guaranteed scheduling gives each of n users 1/n of the CPU; lottery scheduling gives random tickets so the CPU share is proportional to tickets."
sources: ["Tanenbaum MOS 4e, sec. 2.4.4-2.4.5 (priority, guaranteed, lottery scheduling)"]
---
**(i) Priority scheduling.** Each process has a priority; the scheduler always runs the **highest-priority ready process**. Priorities can be static (assigned by importance) or dynamic (e.g. I/O-bound processes get a boost, priority $=1/f$ where $f$ is the fraction of the last quantum used). Variants: preemptive, or non-preemptive; processes with equal priority are served round robin in **priority classes**. *Problems:* **starvation** of low-priority processes (solved by **aging**: raising the priority of waiting processes) and **priority inversion**.

**(ii) Guaranteed scheduling.** Makes a real promise: with $n$ processes each gets $1/n$ of the CPU. The system tracks each process's CPU time consumed versus the time it is entitled to (time since creation$/n$); the ratio actual/entitled (0.5 means half of what it should have) is computed and the process with the **lowest ratio** is run until its ratio overtakes its closest competitor. *Drawback:* bookkeeping, ignores priorities, and a process that slept for long builds up a huge claim.

**(iii) Lottery scheduling.** Each process holds **lottery tickets** for system resources such as CPU time; at every scheduling decision a ticket is drawn at random and its owner runs. A process with a fraction $f$ of the tickets gets about $f$ of the CPU in the long run. It is simple, **highly responsive** (a new process gets tickets at once and is quickly in the draw), allows **priorities** by giving important processes more tickets, and cooperating processes may **exchange tickets** (e.g. a client gives its tickets to the server it waits for).
