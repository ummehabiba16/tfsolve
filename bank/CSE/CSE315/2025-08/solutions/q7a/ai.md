---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-01
status: unverified
summary: "Yes: JG (signed 'greater') jumps exactly when ZF = 0 and SF = OF; examples with CMP show it is right even when overflow occurs."
sources: ["MHE 8086-Architecture slides 26-27, 32 (ZF, SF, OF)"]
---
**Yes, I agree.** JG (= JNLE) is the **signed** "greater than" test after `CMP A, B` (which computes $A-B$ and sets the flags):

- **ZF = 0** means $A-B\neq0$, so $A\neq B$.
- **SF = OF** means the true sign of $A-B$ is positive. If there is no overflow (OF = 0), the sign bit is correct, so SF = 0. If there is overflow (OF = 1), the sign bit is wrong, so SF = 1 actually means positive. In both cases SF = OF means $A-B>0$ in signed arithmetic.

So $A>B$ (signed) $\iff$ ZF = 0 and SF = OF. If ZF = 1 (equal) or SF $\neq$ OF (less), the jump is not taken.

**Examples (8-bit, CMP AL, BL):**

| AL | BL | AL - BL | ZF | SF | OF | SF = OF? | JG taken? | Correct? |
|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| 05H (+5) | 02H (+2) | 03H | 0 | 0 | 0 | yes | yes | +5 > +2 |
| 7FH (+127) | FFH (-1) | 80H | 0 | 1 | 1 | yes | yes | +127 > -1 (overflow, but still right) |
| 80H (-128) | 01H (+1) | 7FH | 0 | 0 | 1 | no | no | -128 < +1 |
| 05H | 05H | 00H | 1 | 0 | 0 | yes | no (ZF = 1) | equal |

The second and third rows show why OF must be included: checking SF alone would give the wrong answer when the subtraction overflows.
