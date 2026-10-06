---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "(i) L1: t1 = i + 1; i = t1; t2 = i * 16; t3 = b[t2]; if t3 < v goto L1. (ii) param a; param b; param c; param d; param e; t1 = call p, 5; t2 = i * 16; t3 = b[t2]; t4 = t1 + t3; y = t4."
sources: ["KMS Chapter 6 slides 52-103 (expressions, arrays, flow of control)", "Dragon book 2e sec. 6.4.3, 6.6.3, 6.9"]
---
Array element address: $b[i]$ is at $base(b) + i \times 16$, since each element takes 16 units (Dragon book sec. 6.4.3).

**(i) `do i = i + 1; while (b[i] < v)`.** The body is executed first, then the condition is tested; if it is true, control goes back to the start of the body:

```text
L1:  t1 = i + 1
     i  = t1
     t2 = i * 16
     t3 = b [ t2 ]
     if t3 < v goto L1
```

(Fall through to the next statement when the condition is false.)

**(ii) `y = p(a, b, c, d, e) + b[i];`** A function call is translated into one `param` instruction for each of the 5 arguments followed by `call p, 5` whose result is a temporary (sec. 6.9); then the array element is fetched and the sum computed:

```text
     param a
     param b
     param c
     param d
     param e
     t1 = call p, 5
     t2 = i * 16
     t3 = b [ t2 ]
     t4 = t1 + t3
     y  = t4
```

The call is evaluated first because the left operand of `+` is translated before the right one.
