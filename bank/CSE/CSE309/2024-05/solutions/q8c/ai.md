---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Assuming b and e live on exit, liveness gives live intervals a [1,9], b [1,11], c [1,11], d [1,11], e [3,11], f [1,8] (b, c, d, f live on entry). Scanning by start point with 3 registers and spilling the interval that ends last: a -> R0, b -> R1, c -> R2; d spilled; f takes R2 and c is spilled; e spilled. Final: a R0, b R1, f R2, with c, d, e in memory. Advantage: very fast (one linear pass over the sorted intervals after liveness), so it suits JIT compilers."
sources: ["KMS Global Register Allocation slides 1-60 (Live Ranges and Live Intervals, Register Allocation with Live Intervals, Register Spilling, Linear Scan)", "Poletto and Sarkar, Linear scan register allocation (1999)"]
---
**Assumptions.**

- The question does not say which variables are live on exit. Take **`b` and `e` live on exit**, as in the flow graph of the same code in the 2021-22 paper (Q8(b)). All variables used before being defined (`b`, `c`, `d`, `f`) are live on entry.
- Program points are numbered by the line numbers 1-11. A variable's **live interval** runs from the first line where it is live (or defined) to the last line where it is live, in the linear order of the code.
- When no register is free, the variable whose interval **ends last** is spilled (the Poletto-Sarkar heuristic). Ties are broken alphabetically. Spilled variables live in memory and are loaded into a scratch register when used.

**Step 1: liveness** (backward data-flow over the flow graph 1 $\to$ 2 $\to$ 3 $\to$ 4 $\to$ {5, 8}, 5 $\to$ 6 $\to$ 11, 8 $\to$ 9 $\to$ 11):

| Line | Instruction | Live in | Live out |
|:-:|:--|:--|:--|
| 1 | `a = b + c` | b, c, d, f | a, b, c, d, f |
| 2 | `d = d - b` | a, b, c, d, f | a, c, d, f |
| 3 | `e = a + f` | a, c, d, f | a, c, d, e, f |
| 4 | `ifFalse e goto L1` | a, c, d, e, f | a, c, d, e, f |
| 5 | `f = a - d` | a, c, d, e | c, d, e |
| 6 | `goto L2` | c, d, e | c, d, e |
| 8 | `b = d + f` | a, c, d, f | a, c, d |
| 9 | `e = a - c` | a, c, d | c, d, e |
| 11 | `b = d + c` | c, d, e | b, e |

**Step 2: live intervals**

| Variable | Interval |
|:-:|:-:|
| a | [1, 9] |
| b | [1, 11] |
| c | [1, 11] |
| d | [1, 11] |
| e | [3, 11] |
| f | [1, 8] |

```text
line:  1  2  3  4  5  6  7  8  9 10 11
a      |-------------------------|
b      |--------------------------------|
c      |--------------------------------|
d      |--------------------------------|
e            |--------------------------|
f      |----------------------|
```

`b` is actually dead from line 3 to line 7 (and its definition at line 8 is never used), but an interval cannot express such holes. This is the imprecision of live intervals.

**Step 3: linear scan with R0, R1, R2.** Process the intervals in order of start point, keeping an *active* list sorted by end point. Free the registers of intervals that have ended before the current start.

| Interval | Active before (end) | Action | Registers |
|:--|:--|:--|:--|
| a [1,9] | none | assign R0 | a = R0 |
| b [1,11] | a(9) | assign R1 | b = R1 |
| c [1,11] | a(9), b(11) | assign R2 | c = R2 |
| d [1,11] | a(9), b(11), c(11) | none free; the furthest end (11) is not later than d's own end, so **spill d** | d in memory |
| f [1,8] | a(9), b(11), c(11) | none free; c ends at 11 > 8, so **spill c**, give R2 to f | f = R2, c in memory |
| e [3,11] | f(8), a(9), b(11) | nothing has ended by line 3; b ends at 11, not later than e, so **spill e** | e in memory |

**Result:** `a` $\to$ R0, `b` $\to$ R1, `f` $\to$ R2; `c`, `d`, `e` are kept in memory (loaded or stored around each use).

This is unavoidable to some extent: at lines 3-4, five variables (a, c, d, e, f) are live at once, so with three registers at least two must be in memory there. Because intervals are coarse, linear scan spills three.

**Advantage of linear scan (2 marks).** It is **very fast**: after the live intervals are computed, it allocates in a single pass over the intervals sorted by start point (linear time, apart from the sort). It produces reasonable code and can generate code during that pass. That is why it is used in JIT compilers (e.g. Java HotSpot), where compile time matters. (Disadvantage: intervals are imprecise compared with live ranges, so graph-colouring allocators often produce better code.)
