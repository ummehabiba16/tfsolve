---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Five-state model with an example for each transition (admit, dispatch, timeout, event wait, event occurs, release)."
sources: ["Tanenbaum MOS 4e, sec. 2.1.5", "Stallings, five-state process model"]
---
![Process states and transitions](figures/five.png)

| Transition | Example |
|:--|:--|
| **New $\to$ Ready (admit)** | the user types `./a.out`; the shell forks, the OS creates the PCB and the process is admitted to the ready queue |
| **Ready $\to$ Running (dispatch)** | the scheduler picks the process because the CPU became free |
| **Running $\to$ Ready (timeout)** | the process uses up its time slice and the timer interrupt preempts it |
| **Running $\to$ Blocked (event wait)** | the process calls `read()` on the disk or the keyboard and must wait for the data |
| **Blocked $\to$ Ready (event occurs)** | the disk interrupt signals that the data has arrived, so the process can be scheduled again |
| **Running $\to$ Exit (release)** | the process calls `exit()` or finishes `main`; the OS releases its resources |
