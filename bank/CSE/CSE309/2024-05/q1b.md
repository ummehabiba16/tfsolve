---
marks: 6
topics: [input-buffering, tokens]
kind: numerical
mandatory: true
source: {page: 8}
---
The partial contents of a buffer in a lexical analyzer is

```text
cse123--++12.45==_1_
```

Where `_` indicates a space. At the current moment, both `lexemeBegin` and `forward` pointers are on c of cse (indicated as position 0). From the perspective of C programming language, write down the positions of the pointers in the table below when this string is scanned. Also, indicate any token identified in the third row. Not all the cells in this row will get populated. There may be more columns than needed in this table.

| | | | | | | | | | | | | | | | |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| `lexemeBegin` | | | | | | | | | | | | | | | |
| `forward` | | | | | | | | | | | | | | | |
| Token | | | | | | | | | | | | | | | |

*The paper prints this table twice, with a vertical ellipsis between the two copies.*
