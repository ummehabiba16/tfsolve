---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-05
status: unverified
summary: "JMP: new busy set (must be clear before), old busy cleared, new NT cleared, old NT unchanged. CALL/interrupt/exception: new busy set (must be clear), old busy stays set, new NT set and back link = old TSS, old NT unchanged. IRET: new (returned-to) busy unchanged (must be set), old busy cleared, new NT unchanged, old NT cleared."
sources: ["Intel 80386 Programmer's Reference Manual, Table 7-2 (effect of a task switch on busy, NT and link fields)", "Brey, The Intel Microprocessors, Sec. 17-6"]
---
| Field | JMP | CALL / Interrupt / Exception | IRET |
|:--|:--|:--|:--|
| **Busy bit of new TSS** | **set** (must be clear before) | **set** (must be clear before) | **unchanged** (must already be set) |
| **Busy bit of old TSS** | **cleared** | **unchanged** (stays set) | **cleared** |
| **NT bit of new task** | **cleared** | **set** | **unchanged** |
| **NT bit of old task** | unchanged | unchanged | **cleared** |
| Back link of new TSS | unchanged | **set to the old TSS selector** | unchanged |
| Back link of old TSS | unchanged | unchanged | unchanged |

**Why:**

- **JMP** is a one-way switch: the old task is no longer active, so its busy bit is cleared, and the new task is not nested (NT = 0).
- **CALL / interrupt / exception** nests the new task inside the old one: the old task stays busy (it cannot be re-entered, which prevents recursion), the new task gets NT = 1 and a back link to the old TSS.
- **IRET** with NT = 1 returns to the task in the back link: the returning (old) task's busy bit and NT are cleared, and the task returned to keeps its busy bit (it was already set).
