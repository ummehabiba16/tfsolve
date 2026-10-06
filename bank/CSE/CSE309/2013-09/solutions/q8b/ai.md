---
author: ai
via: claude-code
model: claude-sonnet-5-5
prompt: solve-v1
created: 2026-10-06
status: unverified
summary: "D -> T id ; {top.put(id.lexeme, T.type, offset); offset = offset + T.width}; T -> B {t = B.type; w = B.width} C {T.type = C.type; T.width = C.width}; B -> int {B.type = integer; B.width = 4}; B -> float {B.type = float; B.width = 8}; C -> [num] C1 {C.type = array(num.value, C1.type); C.width = num.value * C1.width}; C -> eps {C.type = t; C.width = w}."
sources: ["KMS Chapter 6 slides 37-51 (declarations, types and widths)", "Dragon book 2e sec. 6.3.4-6.3.5, Fig. 6.15"]
---
Grammar: $D \to T\ \textbf{id}\ ;$, $T \to B\,C$, $B \to \textbf{int} \mid \textbf{float}$, $C \to [\textbf{num}]\,C \mid \epsilon$. The type of the identifier is a basic type ($B$) followed by array dimensions ($C$); the **width** is the number of bytes (4 for `int`, 8 for `float`, times the dimensions). The standard solution (Dragon book sec. 6.3.4) uses an **inherited** basic type and width, passed through the variables $t$ and $w$, and a **synthesized** array type and width, in an SDT:

$$D \to T\ \textbf{id}\ ;\ \{\ top.put(\textbf{id}.lexeme,\ T.type,\ offset);\ offset = offset + T.width\ \}$$

$$T \to B\ \{\ t = B.type;\ w = B.width\ \}\ C\ \{\ T.type = C.type;\ T.width = C.width\ \}$$

$$B \to \textbf{int}\ \{\ B.type = integer;\ B.width = 4\ \}$$

$$B \to \textbf{float}\ \{\ B.type = float;\ B.width = 8\ \}$$

$$C \to [\ \textbf{num}\ ]\ C_1\ \{\ C.type = array(\textbf{num}.value,\ C_1.type);\ C.width = \textbf{num}.value \times C_1.width\ \}$$

$$C \to \epsilon\ \{\ C.type = t;\ C.width = w\ \}$$

- `top` is the current symbol table (`top.put` inserts the name with its type and relative address); `offset` is the next free relative address.
- The variables $t$ and $w$ carry the basic type and width from $B$ down to the empty production $C \to \epsilon$, which makes them the type and width at the innermost level; the other $C$-productions wrap them in `array` constructors and multiply the widths, on the way up.

**Example.** `float [3][5] x;` gives $B$: float, width 8; $C \to [3]\,C_1$, $C_1 \to [5]\,C_2$, $C_2 \to \epsilon$: $C_2.type = float$, width 8; $C_1.type = array(5, float)$, width $5 \times 8 = 40$; $C.type = array(3, array(5, float))$, width $3 \times 40 = 120$. The entry for `x` has this type and the width 120, and `offset` advances by 120.
