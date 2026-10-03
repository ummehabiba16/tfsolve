---
author: ai
via: claude-code
model: claude-opus-5-5
prompt: solve-v1
created: 2026-10-03
status: unverified
summary: "Root GPA (gain 0.206; Attendance 0.091, Preparation 0.002). High -> Yes; Medium -> Preparation (Good -> Yes, Bad -> No); Low -> Attendance (>=80% -> Yes, <80% -> No)."
sources: ["MNM slides Lecture 10 - Machine Learning - Decision Tree (entropy, information gain)", "AIMA 4e sec. 19.3"]
---
**Entropy** $H(p,n)=-\frac{p}{p+n}\log_2\frac{p}{p+n}-\frac{n}{p+n}\log_2\frac{n}{p+n}$, and $\text{Gain}(A)=H(S)-\sum_v\frac{|S_v|}{|S|}H(S_v)$.

Values used: $H(7,3)=0.881$, $H(5,1)=0.650$, $H(5,2)=0.863$, $H(2,1)=0.918$, $H(k,k)=1$, $H(k,0)=0$.

**Root: all 10 students** (7 Yes, 3 No). $H(S)=-0.7\log_20.7-0.3\log_20.3=0.881$.

| Attribute | Value: (Yes, No) | Remainder | Gain |
|:--|:--|:-:|:-:|
| GPA | High (3,0), Medium (2,1), Low (2,2) | $0+0.3(0.918)+0.4(1)=0.675$ | **0.206** |
| Attendance | $\ge 80\%$ (5,1), $<80\%$ (2,2) | $0.6(0.650)+0.4(1)=0.790$ | 0.091 |
| Exam Preparation | Good (5,2), Bad (2,1) | $0.7(0.863)+0.3(0.918)=0.880$ | 0.002 |

Split on **GPA**. GPA = High (students 1, 4, 10) is all Yes, so it is a leaf **Yes**.

**GPA = Medium** (students 2, 7, 8: Yes, Yes, No; $H=0.918$).

| Attribute | Value: (Yes, No) | Remainder | Gain |
|:--|:--|:-:|:-:|
| Attendance | $\ge 80\%$ (1,1), $<80\%$ (1,0) | $\frac23(1)=0.667$ | 0.252 |
| Exam Preparation | Good (2,0), Bad (0,1) | 0 | **0.918** |

Split on **Exam Preparation**: Good $\to$ Yes, Bad $\to$ No.

**GPA = Low** (students 3, 5, 6, 9: Yes, No, No, Yes; $H=1$).

| Attribute | Value: (Yes, No) | Remainder | Gain |
|:--|:--|:-:|:-:|
| Attendance | $\ge 80\%$ (2,0), $<80\%$ (0,2) | 0 | **1.000** |
| Exam Preparation | Good (1,2), Bad (1,0) | $\frac34(0.918)=0.689$ | 0.311 |

Split on **Attendance**: $\ge 80\%$ $\to$ Yes, $<80\%$ $\to$ No.

**Final decision tree.**

```text
GPA ?
|-- High   -> Grade A or above = Yes
|-- Medium -> Exam Preparation ?
|              |-- Good -> Yes
|              |-- Bad  -> No
|-- Low    -> Attendance Score ?
               |-- >= 80% -> Yes
               |-- <  80% -> No
```

All 10 examples are classified correctly.
