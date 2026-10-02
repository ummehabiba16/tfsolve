---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-02
status: unverified
summary: "Pass the base type in globals t, w: V -> T { t = T.type; w = T.width; } D ;  T -> int { T.type = integer; T.width = 4; } | float { T.type = float; T.width = 8; };  D -> D1 , id C { top.put(id.lexeme, C.type, C.width); } | id C { same };  C -> [ num ] C1 { C.type = array(num.value, C1.type); C.width = num.value \\* C1.width; } | eps { C.type = t; C.width = w; }. For int i, k[2], j[2][3]: i integer (4), k array(2, integer) (8), j array(2, array(3, integer)) (24)."
sources: ["KMS Chapter 6 slides 37-50 (Type Expressions, Computing Types and Their Widths)", "Dragon book 2e sec. 6.3.3 (Fig. 6.15)"]
---
**Assumptions.**

- As in the textbook (Fig. 6.15), the base type and width are passed from $T$ to the array suffixes through two global variables `t` and `w`. (In an LR implementation, the first action becomes a marker $M \to \epsilon$ placed after $T$.)
- `top.put(lexeme, type, width)` stores the information in the current symbol table.
- Type expressions use the constructor `array(n, type)`.

**SDT:**

```text
V -> T            { t = T.type;  w = T.width; }
     D ;

T -> int          { T.type = integer;  T.width = 4; }
T -> float        { T.type = float;    T.width = 8; }

D -> D1 , id C    { top.put(id.lexeme, C.type, C.width); }
D -> id C         { top.put(id.lexeme, C.type, C.width); }

C -> [ num ] C1   { C.type  = array(num.value, C1.type);
                    C.width = num.value * C1.width; }
C -> eps          { C.type = t;  C.width = w; }
```

$C$ builds the type from the innermost dimension outwards. At $\epsilon$ it starts with the base type in `t` and `w`; each `[ num ]` wraps the type of the rest ($C_1$) in an `array`, and multiplies the width.

**Check with `int i, k[2], j[2][3];`:**

| Identifier | Derivation of $C$ | Type expression | Width |
|:-:|:--|:--|:-:|
| `i` | $C \to \epsilon$ | integer | 4 |
| `k` | `[2]` then $\epsilon$ | array(2, integer) | $2 \times 4 = 8$ |
| `j` | `[2]` `[3]` then $\epsilon$ | array(2, array(3, integer)) | $2 \times 3 \times 4 = 24$ |

For `j`: the innermost $C$ ($\epsilon$) gives (integer, 4); `[3]` gives (array(3, integer), 12); `[2]` gives (array(2, array(3, integer)), 24). This is the row-major layout of the textbook.
