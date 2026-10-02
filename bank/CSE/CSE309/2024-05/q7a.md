---
marks: 15
topics: [switch-break]
kind: analysis
source: {page: 12}
note: "Marks printed as (10+5)."
---
Give an outline of syntax-directed translations of *switch*-statements of the following form. Accordingly, show the three-address translation of a *switch*-statement. Briefly discuss how the n-way branch in a *switch*-statement can be evaluated.

```text
switch ( E ) {
    case V1: S1
    case V2: S2
    ...
    case Vn-1: Sn-1
    default: Sn
}
```
