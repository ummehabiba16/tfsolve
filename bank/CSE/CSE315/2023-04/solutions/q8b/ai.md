---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-04
status: unverified
summary: "Yes: JG (signed 'greater', = JNLE) jumps exactly when ZF = 0 and SF = OF; CMP examples show it is correct even when the subtraction overflows, which is why OF is included."
sources: ["MHE 8086-Architecture slides 26-27, 32 (ZF, SF, OF)", "Brey, The Intel Microprocessors, Sec. 6-1 (conditional jumps, Table 6-1)"]
---
**Yes, I agree.** JG (= JNLE) is the **signed** "greater than" test used after `CMP A, B`, which computes $A - B$ (without storing it) and sets the flags.

- **ZF = 0** means $A - B \neq 0$, so $A \neq B$.
- **SF = OF** means the true sign of $A - B$ is positive:
  - If there is **no overflow** (OF = 0), the sign bit of the result is correct, so SF = 0 means positive.
  - If there **is overflow** (OF = 1), the result's sign bit is wrong (inverted), so SF = 1 actually means the true result is positive.
  - In both cases SF = OF $\iff A - B \ge 0$ (signed).

Together: ZF = 0 and SF = OF $\iff A - B > 0 \iff A > B$ (signed). If ZF = 1 (equal) or SF $\neq$ OF (less), the jump is not taken. So the condition is both **necessary and sufficient**.

**Examples (8-bit, `CMP AL, BL`)**

| AL | BL | AL - BL | ZF | SF | OF | SF = OF? | JG taken? | Correct? |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 05H (+5) | 02H (+2) | 03H | 0 | 0 | 0 | yes | yes | +5 > +2 |
| 7FH (+127) | FFH (-1) | 80H | 0 | 1 | 1 | yes | yes | +127 > -1 (overflow, still right) |
| 80H (-128) | 01H (+1) | 7FH | 0 | 0 | 1 | no | no | -128 < +1 |
| FEH (-2) | 03H (+3) | FBH | 0 | 1 | 0 | no | no | -2 < +3 |
| 05H | 05H | 00H | 1 | 0 | 0 | yes | no (ZF = 1) | equal |

Rows 2 and 3 show why OF is needed: testing SF alone would give the wrong answer whenever the subtraction overflows. Also, JG is not the same as JA (unsigned "above", CF = 0 and ZF = 0): for 7FH vs FFH, JA is not taken because 127 < 255 unsigned.
