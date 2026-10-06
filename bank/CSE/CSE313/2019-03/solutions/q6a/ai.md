---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "Five-state model: New, Ready, Running, Blocked, Exit with admit, dispatch, timeout, event wait, event occurs and release."
sources: ["Tanenbaum MOS 4e, sec. 2.1.5 (process states)", "Stallings OS, five-state model"]
---
![Five-state process model](figures/five.png)

**States.** *New* (being created), *Ready* (waiting for the CPU), *Running* (executing), *Blocked* (waiting for I/O or an event), *Exit* (terminated).

**Transitions**

- **New $\to$ Ready (admit):** the OS has set up the PCB and admits the process to the ready queue.
- **Ready $\to$ Running (dispatch):** the scheduler selects the process and gives it the CPU.
- **Running $\to$ Ready (timeout):** the time slice expires (or a higher-priority process becomes ready).
- **Running $\to$ Blocked (event wait):** the process asks for I/O or waits for an event.
- **Blocked $\to$ Ready (event occurs):** the I/O finishes or the event happens.
- **Running $\to$ Exit (release):** the process finishes or is aborted.
